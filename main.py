import random
import time

#TODO

#Class imports
import ItemAnalyser, ItemCreator, ResultsFileGenerator, SearchTermsExtract

#TODO

def main():
    search_term_limit = None
    #search_term_limit = None
    search_terms = SearchTermsExtract.extract_search_terms(search_term_limit)
    #items = []
    search_terms_file_name, listings_file_name = ResultsFileGenerator.create_new_results_file_names()
    i = 0
    listing_count = 0
    for search_term in search_terms:
        print("Processing item " + (i + 1).__str__() + " of " + len(search_terms).__str__())
        #Determine if search term has been processed.
        if ResultsFileGenerator.determine_if_results_file_exists(search_terms_file_name) == True:
            if ResultsFileGenerator.search_results_file_for_value(search_terms_file_name, search_term) == True:
                print(search_term + " has already been processed! Skipping this term.")
                i += 1
                continue
        item = ItemCreator.create_item_from_search_term(search_term)
        item = ItemAnalyser.analyse_item_data(item)
        sleep_value = (random.randint(1,7))
        print("Sleeping for " + sleep_value.__str__() + " seconds.")
        #items.append(item)
        #Add rows to files
        ResultsFileGenerator.add_search_term_result_to_results_file(search_terms_file_name, item.search_term, item.lowest_listing_value, item.average_lowest_listing_value,
                                    item.one_month_sold_average, item.three_month_sold_average, item.six_month_sold_average,
                                    item.twelve_month_sold_average)
        for lowest_listing in item.lowest_listings:
            ResultsFileGenerator.add_search_term_listing_result_to_results_file(
                listings_file_name, item.search_term, "Lowest", lowest_listing.title, lowest_listing.price, lowest_listing.end_date,
                 lowest_listing.list_type, lowest_listing.url, lowest_listing.sold_type)
        for sold_listing in item.sold_listings:
            ResultsFileGenerator.add_search_term_listing_result_to_results_file(
                listings_file_name, item.search_term, "Sold", sold_listing.title, sold_listing.price, sold_listing.end_date,
                 sold_listing.list_type, sold_listing.url, sold_listing.sold_type)
        print("Processed item " + (i + 1).__str__() + " of " + len(search_terms).__str__())
        listing_count += len(item.lowest_listings)
        listing_count += len(item.sold_listings)
        i += 1

if __name__ == "__main__":
    main()