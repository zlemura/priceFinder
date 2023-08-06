from datetime import date
from dateutil import relativedelta
from thefuzz import fuzz

import ProjectVariables


#TODO

def analyse_item_data(item):
    #Lowest listings
    item = exclude_lowest_listings_from_item(item)
    item = analyse_lowest_listing_data(item)
    #Sold listings
    item = exclude_sold_listings_from_item(item)
    item = analyse_sold_listing_data(item)

    return item

def exclude_lowest_listings_from_item(item):
    temp_lowest_listings = []
    for listing in item.lowest_listings:
        similarity_score = compare_strings_for_similarity(item.search_term, listing.title)
        if similarity_score > 90:
            for company_name in ProjectVariables.grading_company_prefixes:
                if company_name in listing.title:
                    if company_name in item.search_term:
                        temp_lowest_listings.append(listing)
                        continue
                    else:
                        continue
            temp_lowest_listings.append(listing)

    item.lowest_listings = temp_lowest_listings
    return item

def analyse_lowest_listing_data(item):
    #Find lowest listing price.
    lowest_listing_value = 0
    lowest_listing_url = ''
    total_listing_value = 0
    total_listing_count = len(item.lowest_listings)
    #Loop through all lowest listings.
    for listing in item.lowest_listings:
        total_listing_value += float(listing.price)
        if lowest_listing_value == 0:
            lowest_listing_url = listing.url
            lowest_listing_value = float(listing.price)
            continue
        if float(listing.price) < lowest_listing_value:
            if listing.list_type in ['Buy It Now', 'or Best Offer']:
                lowest_listing_url = listing.url
                lowest_listing_value = float(listing.price)
    #Print lowest listing.
    #print('Lowest price is - ' + lowest_listing_value.__str__() + ' at listing - ' + lowest_listing_url)
    #Find average value of all lowest listings.
    average_listing_value = 0
    if total_listing_count != 0:
        average_listing_value = total_listing_value/total_listing_count
    #print('The average listing value is - ' + average_listing_value.__str__())
    #Update item with new values.
    item.lowest_listing_url = lowest_listing_url
    item.lowest_listing_value = round(lowest_listing_value, 2)
    item.average_lowest_listing_value = round(average_listing_value, 2)
    return item

def analyse_sold_listing_data(item):
    #1 month average
    one_month_average_value = 0
    #3 month average
    three_month_average_value = 0
    #6 month average
    six_month_average_value = 0
    #12 month average
    twelve_month_average_value = 0

    for listing in item.sold_listings:
        delta = relativedelta.relativedelta(date.today(), listing.end_date)
        if delta.months <= 1:
            one_month_average_value += float(listing.price)
            continue
        elif delta.months <= 3:
            three_month_average_value += float(listing.price)
            continue
        elif delta.months <= 6:
            six_month_average_value += float(listing.price)
        elif delta.months <=12:
            twelve_month_average_value += float(listing.price)

    item.one_month_sold_average = round(one_month_average_value, 2)
    item.three_month_sold_average = round(three_month_average_value, 2)
    item.six_month_sold_average = round(six_month_average_value, 2)
    item.twelve_month_sold_average = round(twelve_month_average_value, 2)

    return item

def exclude_sold_listings_from_item(item):
    temp_sold_listings = []
    for listing in item.sold_listings:
        similarity_score = compare_strings_for_similarity(item.search_term, listing.title)
        if similarity_score > 90:
            for company_name in ProjectVariables.grading_company_prefixes:
                if company_name in listing.title:
                    if company_name in item.search_term:
                        temp_sold_listings.append(listing)
                        continue
                    else:
                        continue
            temp_sold_listings.append(listing)

    item.sold_listings = temp_sold_listings
    return item

def compare_strings_for_similarity(s1, s2):
    return fuzz.token_set_ratio(s1, s2)
