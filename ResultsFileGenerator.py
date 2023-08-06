import csv
from datetime import date

def generate_output_file(items):
    #Initialise result output file names.
    today = date.today()
    search_term_file_name = today.year.__str__() + '_' + today.month.__str__() + '_' + today.day.__str__() + '_summary.csv'
    search_term_listings_file_name = today.year.__str__() + '_' + today.month.__str__() + '_' + today.day.__str__() + '_listings.csv'
    #Initialise output lists
    search_term_rowlist = []
    listing_rowlist = []
    listing_count = 0
    #Loop through items and process.
    for item in items:
        listing_count += len(item.lowest_listings)
        listing_count += len(item.sold_listings)
        search_term_rowlist.append([item.search_term, item.lowest_listing_value, item.average_lowest_listing_value,
                                    item.one_month_sold_average, item.three_month_sold_average, item.six_month_sold_average,
                                    item.twelve_month_sold_average])
        #title, price, end_date, list_type, url, sold_type
        for lowest_listing in item.lowest_listings:
            listing_rowlist.append([item.search_term, "Lowest", lowest_listing.title, lowest_listing.price, lowest_listing.end_date,
                                    lowest_listing.list_type, lowest_listing.url, lowest_listing.sold_type])
        for sold_listing in item.sold_listings:
            listing_rowlist.append([item.search_term, "Sold", sold_listing.title, sold_listing.price, sold_listing.end_date,
                                    sold_listing.list_type, sold_listing.url, sold_listing.sold_type])
        with(open("results/" + search_term_file_name, 'w')) as file:
            writer = csv.writer(file)
            writer.writerows(search_term_rowlist)
            file.close()

        with(open("results/" + search_term_listings_file_name, 'w')) as file:
            writer = csv.writer(file)
            writer.writerows(listing_rowlist)
            file.close()
    #print("There should be " + listing_count.__str__() + " listings across " + len(items).__str__() + " items.")
    #print("There are " + len(listing_rowlist).__str__() + " listing rows and " + len(search_term_rowlist).__str__() + " search terms.")