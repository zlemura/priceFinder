import csv
from datetime import date
import os
#Method to read which includes opening reader.

def add_search_term_result_to_results_file(search_term_file_name, search_term, lowest_listing_value, average_lowest_listing_value
                                   ,one_month_sold_average, three_month_sold_average, six_month_sold_average, twelve_month_sold_average):
    with(open("results/" + search_term_file_name, 'a')) as file:
        search_terms_file_writer = csv.writer(file)
        search_terms_file_writer.writerow([search_term, lowest_listing_value, average_lowest_listing_value
                                   ,one_month_sold_average, three_month_sold_average, six_month_sold_average,
                                      twelve_month_sold_average])
    file.close()

def add_search_term_listing_result_to_results_file(search_term_listings_file_name, search_term, listing_type, title, price, end_date,
                                           list_type, url, sold_type):
    with(open("results/" + search_term_listings_file_name, 'a')) as file:
        listings_writer = csv.writer(file)
        listings_writer.writerow([search_term, listing_type, title, price, end_date,
                                           list_type, url, sold_type])
    file.close()

def search_results_file_for_value(file_name, search_value):
    value_found = False
    with(open("results/" + file_name, 'r')) as file:
        file_reader = csv.reader(file)
        for row in file_reader:
            if search_value in row:
                value_found = True
                break
        file.close()
    return value_found

def determine_if_results_file_exists(file_name):
    return os.path.isfile("results/" + file_name)
def create_new_results_file_names():
    # Initialise result output file names.
    today = date.today()
    search_term_file_name = today.year.__str__() + '_' + today.month.__str__() + '_' + today.day.__str__() + '_summary.csv'
    search_term_listings_file_name = today.year.__str__() + '_' + today.month.__str__() + '_' + today.day.__str__() + '_listings.csv'
    return search_term_file_name, search_term_listings_file_name
