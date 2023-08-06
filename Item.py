class Item:
    def __init__(self, search_term, lowest_uri, sold_uri, lowest_listings, sold_listings, lowest_listing_url, lowest_listing_value
                 ,average_lowest_listing_value, one_month_sold_average, three_month_sold_average, six_month_sold_average, twelve_month_sold_average):
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
        self.lowest_listing_url = lowest_listing_url
        self.lowest_listing_value = lowest_listing_value
        self.average_lowest_listing_value = average_lowest_listing_value
        self.one_month_sold_average = one_month_sold_average
        self.three_month_sold_average = three_month_sold_average
        self.six_month_sold_average = six_month_sold_average
        self.twelve_month_sold_average = twelve_month_sold_average