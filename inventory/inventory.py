# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    menu_list = ['Show table', 'Add game to inventory',
                 'Remove game from inventory', 'Update data for game']
    file_name = '/home/wera/codecool/python-lightweight-erp-project-zrzedliwy-starszy-pan-i-dzieciaki/inventory/inventory.csv'
    error_message = 'Select number from 0 to 4, pointing the action you want to be done'
    title = 'Inventory'
    table = data_manager.get_table_from_file(file_name)

    stay = True
    while stay:
        ui.print_menu(title, menu_list, 'Back to main menu')

        task_selection = ui.get_inputs([''], 'Please enter a number')

        while not common.is_selection_proper(task_selection, len(menu_list)):
            ui.print_error_message(error_message)
            task_selection = ui.get_inputs([''], 'Please enter a number')

        if task_selection[0] == '1':

            show_table(table)

        elif task_selection[0] == '2':

            table = add(table)

        elif task_selection[0] == '3':

            id_ = ask_for_id(table, 'Please enter an id of game to remove')
            table = remove(table, id_)

        elif task_selection[0] == '4':
            id_ = ask_for_id(table, 'Please enter an id of game to be updated')
            update(table, id_)

        else:
            stay = False


def ask_for_id(table, what_for):
    '''
    asks for for id, checks if it exists in table

    Args:
        table: list of lists
        what_for: (str) exmpl; 'Please enter an id of person to remove'

    Returns:
        id_: str
    '''

    id_ = ui.get_inputs([''], what_for)[0]
    while not is_id_on_table(table, id_):
        id_ = ui.get_inputs([], what_for)[0]

    return id_


def is_id_on_table(table, id_):
    '''
    function chcecks if table contain record of given id
    
    Args:
        table: list of lists

    Returns:
        Boolean
    '''
    for i in range(len(table)):
        if table[i][0] == id_:     # IS IT PROPER?
            return True
    return False


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    title_list = ['id', 'name of game', 'company', 'year of realise', 'amount']
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    attribute_list = ['id', 'name of game', 'company', 'year of realise', 'amount']
    an_item = [common.generate_random(table)]

    an_item += ui.get_inputs(['name of game', 'company', 'year of realise', 'amount'], 'Please, provide a game information')
    table.append(an_item)

    file_name = '/home/wera/codecool/python-lightweight-erp-project-zrzedliwy-starszy-pan-i-dzieciaki/inventory/inventory.csv'
    data_manager.write_table_to_file(file_name, table)

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """

    for i in range(len(table)):
        if table[i][0] == id_:
            table.remove(table[i])
            break

    file_name = '/home/wera/codecool/python-lightweight-erp-project-zrzedliwy-starszy-pan-i-dzieciaki/inventory/inventory.csv'
    data_manager.write_table_to_file(file_name, table)

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """

    for i in range(len(table)):
        if table[i][0] == id_:
            a_game = table[i]
            removal_index = i
            break

    list_of_options = ['name of game', 'company', 'year of realise', 'amount']

    option_selection = ui.get_inputs(list_of_options, "Do you want to update (y/n) : ")
    for i in range(len(option_selection)):
        if option_selection[i] == 'y' and i == 0:
            a_game[i] = common.generate_random(table)
        elif option_selection[i] == 'y':
            a_game[i] = ui.get_inputs([list_of_options[i]], "New {} is ".format(list_of_options[i]))[0]

    table.remove(table[removal_index])
    table.append(a_game)

    file_name = '/home/wera/codecool/python-lightweight-erp-project-zrzedliwy-starszy-pan-i-dzieciaki/inventory/inventory.csv'
    data_manager.write_table_to_file(file_name, table)

    return table


# special functions:
# ------------------

# the question: Which items have not exceeded their durability yet?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_items(table):

    # your code

    pass


# the question: What are the average durability times for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):

    # your code

    pass
