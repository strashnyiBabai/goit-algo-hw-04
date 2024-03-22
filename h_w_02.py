"""return list of dictionaries with info about cats
    ID, name, age. As a parameter, requires file where info about each cat is organized in this way:

    'id','name','age'
    'id','name','age'
    ...
    
    No spaces between the info, tab must be used to dived info about cats.
    """
def get_cats_info(path) -> list:
    cats_info = []
    with open (path, 'r', encoding='UTF-8') as cats_info_file:

        # parse each line of file and sort the info
        for line in cats_info_file.readlines():

            # clear the last tab when no elements left
            line = line.strip()

            # take id, name and age from file. Put it in dictionary. than add it to the list with info about other cats
            if line != '':
                try:
                    id, name, age = line.split(',')
                    cats_info.append({'id' : id, 'name' : name, 'age' : age})
                except ValueError:
                    return "Not supported file structure"

    return cats_info


