import jellyfish
from thefuzz import fuzz

import ProjectVariables


#TODO
#Remove listings that aren't a match in set threshold.
#Summarise lowest listing data.
##Current lowest listing (excluding auctions), average listing value (of all listings for search_term)
#Summarise sold listing data.

def analyse_item_data(item):
    #Lowest listings
    item = exclude_listings_from_item(item)
    item = analyse_lowest_listing_data(item)




def exclude_listings_from_item(item):
    temp_lowest_listings = item.lowest_listings
    #Loop through all lowest listings.
    for listing in temp_lowest_listings:
        print('Processing listing - ' + listing.title + ' - ' + listing.url)
        similarity_score = compare_strings_for_similarity(item.search_term, listing.title)
        print('The similairty score is - ' + similarity_score.__str__())
        if similarity_score < 50:
            item.lowest_listings.remove(listing)
            continue
        if item.search_term not in ProjectVariables.grading_company_prefixes:
            item.lowest_listings.remove(listing)
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
            if listing.listType in ['Buy It Now', 'or Best Offer']:
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



def compare_strings_for_similarity(s1, s2):
    return fuzz.token_set_ratio(s1, s2)
