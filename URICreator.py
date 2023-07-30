from urllib.parse import urlencode, urljoin, urlparse

def create_uri(search_term,uri_type):
    if uri_type == "L":
        return create_lowest_uri(search_term)
    elif uri_type == "S":
        return create_sold_uri(search_term)
    elif uri_type == "B":
        return create_best_uri(search_term)

def create_lowest_uri(search_term):
    #https://www.ebay.com.au/sch/i.html?_from=R40&_nkw=Andres+Iniesta+398+2003-04+Panini+La+Liga+Megapromesas&_sacat=0&_sop=2
    uri_base = "https://www.ebay.com/sch/i.html?{}"
    uri_params = {'_from': 'R40', '_nkw': search_term, '_sacat': 0, '_sop': 2}
    uri = uri_base.format(urlencode(uri_params))
    return uri

def create_sold_uri(search_term):
    #https://www.ebay.com.au/sch/i.html?_from=R40&_nkw=Andres+Iniesta+398+2003-04+Panini+La+Liga+Megapromesas&_sacat=0&_sop=12&rt=nc&LH_Sold=1&LH_Complete=1
    uri_base = "https://www.ebay.com/sch/i.html?{}"
    uri_params = {'_from': 'R40', '_nkw': search_term, '_sacat': 0, '_sop': 12,'rt': 'nc', 'LH_Sold': 1, 'LH_Complete': 1}
    uri = uri_base.format(urlencode(uri_params))
    return uri

def create_best_uri(search_term):
    #https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=Andres+Iniesta+398+2003-04+Panini+La+Liga+Megapromesas&_sacat=0
    uri_base = "https://www.ebay.com/sch/i.html?{}"
    uri_params = {'_from': 'R40', '_trksid': 'p4432023.m570.l1313', '_nkw': search_term, '_sacat': 0}
    uri = uri_base.format(urlencode(uri_params))
    return uri

