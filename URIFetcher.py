import urllib.request

def fetch_uri_content(uri):
    #open connection to uri.
    webUrl = urllib.request.urlopen(uri)

    #read the data from the uri and print
    data = webUrl.read()

    return data