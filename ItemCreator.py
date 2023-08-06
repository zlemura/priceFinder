#Class imports
import URICreator, URIFetcher, URIResultsExtractor
from Item import Item

def create_item_from_search_term(search_term):
    # Create lowest_uri
    lowest_uri = URICreator.create_uri(search_term, "L")

    # Fetch webpage for lowest_uri
    lowest_uri_data = URIFetcher.fetch_uri_content(lowest_uri)

    # Extract listing results from page for lowest uri
    lowest_listing_list = URIResultsExtractor.extract_results_from_data(lowest_uri_data, "L")

    # Create sold_uri
    sold_uri = URICreator.create_uri(search_term, "S")

    # Fetch webpage for sold_uri
    sold_uri_data = URIFetcher.fetch_uri_content(sold_uri)

    # Extract listing results from page for sold uri
    sold_listing_list = URIResultsExtractor.extract_results_from_data(sold_uri_data, "S")

    # Create new Item object
    item = Item(search_term, lowest_uri, sold_uri, lowest_listing_list, sold_listing_list, '', 0, 0, 0, 0, 0, 0)

    return item