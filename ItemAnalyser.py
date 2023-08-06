from datetime import date
from dateutil import relativedelta
from thefuzz import fuzz

import ProjectVariables


#TODO
#Properly exclude results of listings based on similarity score.

def analyse_item_data(item):
    #Lowest listings
    item = exclude_lowest_listings_from_item(item)
    item = analyse_lowest_listing_data(item)
    #Sold listings
    item = exclude_sold_listings_from_item(item)
    item = analyse_sold_listing_data(item)

    return item

def exclude_lowest_listings_from_item(item):
    temp_lowest_listings = item.lowest_listings
    #print(len(item.lowest_listings))
    #Loop through all lowest listings.
    for listing in temp_lowest_listings:
        #print('Processing listing - ' + listing.title + ' - ' + listing.url)
        similarity_score = compare_strings_for_similarity(item.search_term, listing.title)
        #print('The similairty score is - ' + similarity_score.__str__())
        if similarity_score < 95:
            #print("removing " + listing.title + " " + listing.url + " from lowest listings")
            item.lowest_listings.remove(listing)
            continue
        if item.search_term not in ProjectVariables.grading_company_prefixes:
            item.lowest_listings.remove(listing)
    #print(len(item.lowest_listings))
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
    average_listing_value = total_listing_value/total_listing_count
    #print('The average listing value is - ' + average_listing_value.__str__())
    #Update item with new values.
    item.lowest_listing_url = lowest_listing_url
    item.lowest_listing_value = lowest_listing_value
    item.average_lowest_listing_value = average_listing_value
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

    item.one_month_sold_average = one_month_average_value
    item.three_month_sold_average = three_month_average_value
    item.six_month_sold_average = six_month_average_value
    item.twelve_month_sold_average = twelve_month_average_value

    return item

def exclude_sold_listings_from_item(item):
    print(len(item.sold_listings))
    temp_sold_listings = item.sold_listings
    # Loop through all lowest listings.
    for listing in temp_sold_listings:
        print('Processing listing - ' + listing.title + ' - ' + listing.url)
        similarity_score = compare_strings_for_similarity(item.search_term, listing.title)
        print('The similairty score is - ' + similarity_score.__str__())
        if similarity_score < 95:
            print("removing " + listing.title + " " + listing.url + " from sold listings")
            item.sold_listings.remove(listing)
            continue
        if item.search_term not in ProjectVariables.grading_company_prefixes:
            item.sold_listings.remove(listing)
    print(len(item.sold_listings))
    return item

def compare_strings_for_similarity(s1, s2):
    return fuzz.token_set_ratio(s1, s2)
