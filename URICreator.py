from urllib.parse import urlencode, urljoin, urlparse

def create_uri(search_term,uri_type):
    if uri_type == "L":
        return create_lowest_uri(search_term)
    elif uri_type == "S":
        return create_sold_uri(search_term)
    elif uri_type == "B":
        return create_best_uri(search_term)

def create_lowest_uri(search_term):
    uri_base = "https://www.ebay.com/sch/i.html?{}"
    uri_params = {'_from': 'R40', '_nkw': search_term, '_sacat': 0, '_sop': 2, 'ipg_': 240}
    uri = uri_base.format(urlencode(uri_params))
    return uri

def create_sold_uri(search_term):
    uri_base = "https://www.ebay.com/sch/i.html?{}"
    uri_params = {'_from': 'R40', '_nkw': search_term, '_sacat': 0, 'rt': 'nc', 'LH_Sold': 1, 'LH_Complete': 1, 'ipg_': 240}
    uri = uri_base.format(urlencode(uri_params))
    return uri

def create_best_uri(search_term):
    uri_base = "https://www.ebay.com/sch/i.html?{}"
    uri_params = {'_from': 'R40', '_trksid': 'p4432023.m570.l1313', '_nkw': search_term, '_sacat': 0, 'ipg_': 240}
    uri = uri_base.format(urlencode(uri_params))
    return uri

