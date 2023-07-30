class Item:
    def __init__(self, search_term, lowest_uri, sold_uri, lowest_listings=None, sold_listings=None):
        self.search_term = search_term
        self.lowest_uri = lowest_uri
        self.sold_uri = sold_uri
        if lowest_listings is None:
            self.lowest_listings = []
        if sold_listings is None:
            self.sold_listings = []