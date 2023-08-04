'''
module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name,
instance_var_name, function_parameter_name, local_var_name.
'''

#TODO:
#Include logic for best offer accepted for sold listings.

#Class imports
import ItemCreator, ItemAnalyser

def main():

    search_term = '2020 PANINI CHRONICLES PRIZM BUKAYO SAKA SEALED SILVER AUTO'

    item = ItemCreator.create_item_from_search_term(search_term)

    ItemAnalyser.analyse_item_data(item)

if __name__ == "__main__":
    main()