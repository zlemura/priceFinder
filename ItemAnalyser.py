from datetime import date
from dateutil import relativedelta
from thefuzz import fuzz

import ProjectVariables


#TODO
#Refactor exclude logic to match exact terms from item.

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
        if determine_if_listing_title_is_similar_enough_to_item(item.database_record, listing):
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

def exclude_sold_listings_from_item(item):
    temp_sold_listings = []
    for listing in item.sold_listings:
        if determine_if_listing_title_is_similar_enough_to_item(item.database_record, listing):
            temp_sold_listings.append(listing)
    item.sold_listings = temp_sold_listings
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

def compare_strings_for_similarity(s1, s2):
    return fuzz.token_set_ratio(s1, s2)

def determine_if_listing_title_is_similar_enough_to_item(database_record, listing):
    #Determine if player_name exists in listing.title.
    if database_record.player_name not in listing.title:
        return False
    #Determine if number in listing.title
    if database_record.number.__str__() not in listing.title:
        return False
    #Determine if is_numbered in listing.title, if required.
    if database_record.numbered != "":
        if database_record.numbered not in listing.title:
            return False
    #Determine if grading_company_name and grade in listing.title.
    if database_record.grading_company != "":
        if database_record.grading_company not in listing.title:
            return False
        if database_record.grade.__str__() not in listing.title:
            return False
    else:
        for company_code in ProjectVariables.grading_company_prefixes:
            if company_code in listing.title:
                return False
    return True