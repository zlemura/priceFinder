# TODO
# Determine fetching for key fields for both lowest and sold.

# Create Class for listing - aiming for one for both types of listings.

from bs4 import BeautifulSoup
from datetime import datetime

#Class imports
from Listing import Listing

def extract_results_from_data(data, uri_type):
    # extract srp-results srp-list clearfix.
    uri_soup = BeautifulSoup(data, "html.parser")
    srp_results_srp_list_clearfix_soup = uri_soup.find('ul', class_='srp-results srp-list clearfix')

    # extract li items of class
    li_s_item_list = []
    for item in srp_results_srp_list_clearfix_soup.find_all('li', class_='s-item s-item__pl-on-bottom'):
        li_s_item_list.append(item)

    for item in srp_results_srp_list_clearfix_soup.find_all('li',
                                                            class_='s-item s-item__before-answer s-item__pl-on-bottom'):
        li_s_item_list.append(item)

    listing_list = []

    for item in li_s_item_list:
        title = extract_listing_title(item)
        price = extract_listing_price(item)
        if uri_type == "S":
            end_date = extract_listing_end_date(item)
        else:
            end_date = 'N/A'
        if uri_type == "L":
            listing_type = extract_listing_type(item)
        else:
            listing_type = 'N/A'
        url = extract_listing_url(item)
        if uri_type == 'S':
            sold_type = extract_sold_type(item)
        else:
            sold_type = 'N/A'
        listing_list.append(Listing(title,price,end_date,listing_type,url, sold_type))

    return listing_list

def extract_listing_title(listing_soup):
    title = listing_soup.find('div', class_='s-item__title').find('span', role='heading').getText().strip()
    return title

def extract_listing_price(listing_soup):
    price = listing_soup.find('span', class_='s-item__price').getText().replace("$","").replace(",","")
    if 'to' in price:
        split_price = price.split('to')
        price = float(split_price[0])
    return price

def extract_listing_end_date(listing_soup):
    end_date = listing_soup.find('div', class_='s-item__title--tag').find('span', class_='POSITIVE').getText()
    end_date = end_date.replace('Sold ','').strip()
    end_date_object = datetime.strptime(end_date, "%b %d, %Y").date()
    return end_date_object

def extract_listing_type(listing_soup):
    try:
        listing_type = listing_soup.find('span', class_='s-item__purchase-options s-item__purchaseOptions').getText().strip()
    except:
        listing_type = 'Auction'
    return listing_type

def extract_listing_url(listing_soup):
    url = str(listing_soup.find('div', class_='s-item__image')).split('href="')[1].split('"')[0]
    return url

def extract_sold_type(listing_soup):
    try:
        listing_type = listing_soup.find('span', class_='s-item__purchase-options s-item__purchaseOptions').getText().strip()
        if listing_type != 'Best offer accepted':
            listing_type = 'Sale'
    except:
        listing_type = 'Sale'
    return listing_type