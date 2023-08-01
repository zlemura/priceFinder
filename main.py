'''
module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name,
instance_var_name, function_parameter_name, local_var_name.
'''

#TODO:
#Use Item object to perform data analysis.
#Perform string match between search term (player details) and ebay listing. If above set confidence, consider.
#Perform string match between search term (player details) and sold listing. If above set confidence, consider.

#Class imports
import ItemCreator, ItemAnalyser

def main():

    search_term = 'Andres Iniesta 398 2003-04 Panini La Liga Megapromesas'

    item = ItemCreator.create_item_from_search_term(search_term)

    ItemAnalyser.analyse_item_data(item)

if __name__ == "__main__":
    main()