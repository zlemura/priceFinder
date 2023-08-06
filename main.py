'''
module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name,
instance_var_name, function_parameter_name, local_var_name.
'''
import random
import time

#TODO:
#Handle list of items.
#Handle output - for all listing results and summarised.

#Class imports
import ItemAnalyser, ItemCreator, SearchTermsExtract

def main():
    search_term_limit = 10
    #search_term_limit = None
    search_terms = SearchTermsExtract.extract_search_terms(search_term_limit)
    items = []
    i = 0
    for search_term in search_terms:
        print("Processing item " + (i + 1).__str__() + " of " + len(search_terms).__str__())
        item = ItemCreator.create_item_from_search_term(search_term)
        item = ItemAnalyser.analyse_item_data(item)
        sleep_value = (random.randint(1,7))
        print("Sleeping for " + sleep_value.__str__() + " seconds.")
        items.append(item)
        print("Processed item " + (i + 1).__str__() + " of " + len(search_terms).__str__())
        i += 1
    for item in items:
        print(item.__dict__)

if __name__ == "__main__":
    main()