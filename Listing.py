'''
Sold
- Title - s-item__wrapper clearfix.s-item__info clearfix.s-item__link.s-item__title
- Price - s-item__wrapper clearfix.s-item__info clearfix.s-item__details clearfix.s-item__detail s-item__detail--primary.s-item__price
- End date - s-item__wrapper clearfix.s-item__info clearfix.s-item__caption-section.s-item__title--tag.class

Lowest
- Title - s-item__wrapper clearfix.s-item__info clearfix.s-item__link.s-item__title
- Price - s-item__wrapper clearfix.s-item__info clearfix.s-item__details clearfix.s-item__detail s-item__detail--primary.s-item__price
- List type - s-item__wrapper clearfix.s-item__info clearfix.s-item__details clearfix.s-item__detail s-item__detail--primary.s-item__purchase-options s-item__purchaseOptions
'''

class Listing:
    def __init__(self, title, price, endDate, listType, url):
        self.title = title
        self.price = price
        self.endDate = endDate
        self.listType = listType
        self.url = url