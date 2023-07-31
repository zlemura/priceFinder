class Item:
    def __init__(self, search_term, lowest_uri, sold_uri, lowest_listings, sold_listings):
        self.search_term = search_term
        self.lowest_uri = lowest_uri
        self.sold_uri = sold_uri
        if lowest_listings is None:
            self.lowest_listings = []
        else:
            self.lowest_listings = lowest_listings
        if sold_listings is None:
            self.sold_listings = []
        else:
            self.sold_listings = sold_listings