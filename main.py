'''
module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name,
instance_var_name, function_parameter_name, local_var_name.
'''

#TODO:
#ItemAnalyser
##Analyse sold listings.

#Class imports
import ItemCreator, ItemAnalyser

def main():

    search_term = 'Cristiano Ronaldo #AT-CR7 Atomic Material /149 Patch 2020-21 Panini Obsidian Soccer'

    item = ItemCreator.create_item_from_search_term(search_term)

    print(item.lowest_uri)
    print(item.sold_uri)

    item = ItemAnalyser.analyse_item_data(item)

    print(item.lowest_listing_value)
    print(item.average_lowest_listing_value)
    print(item.one_month_sold_average)
    print(item.three_month_sold_average)
    print(item.six_month_sold_average)
    print(item.twelve_month_sold_average)

    for listing in item.sold_listings:
        print(listing.title, listing.url)

    #for listing in item.lowest_listings:
        #print(listing.title, listing.url)

if __name__ == "__main__":
    main()