'''
module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name,
instance_var_name, function_parameter_name, local_var_name.
'''

#TODO:
#Perform string match between search term (player details) and ebay listing. If above set confidence, consider.
#Perform string match between search term (player details) and sold listing. If above set confidence, consider.\

#Class imports
import URICreator, URIFetcher, URIResultsExtractor

def main():
    search_term = 'Andres Iniesta 398 2003-04 Panini La Liga Megapromesas'

    #Create URI's
    uri_data = URICreator.create_uri(search_term, "L")
    #uri_data = URICreator.create_uri(search_term, "S")

    #Fetch webpage for lowest_uri
    uri_data = URIFetcher.fetch_uri_content(uri_data)

    #Extract listing results from page
    listing_list = URIResultsExtractor.extract_results_from_data(uri_data, "L")

    for item in listing_list:
        print(item.title)
        print(item.price)
        print(item.endDate)
        print(item.listType)
        print(item.url)

if __name__ == "__main__":
    main()