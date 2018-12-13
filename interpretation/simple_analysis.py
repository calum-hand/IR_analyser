########################################################################################################################
# Function : Reads text file and then returns as nested array including headers


def ir_database(path_to_file='ir_frequencies.txt'):

    with open(path_to_file, 'r') as f:
        return [line.split(' ') for line in f.readlines()]


########################################################################################################################
# Function : takes user of frequencies and returns a list when user specifies is complete


def user_frequencies():
    user_input = []
    while True:
        entry = input('Please enter wavenumber (cm^-1) or \'run\'  : ')
        if entry == 'run':
            break
        elif entry.isnumeric():
            user_input.append(int(entry))

    return user_input


########################################################################################################################
# Function : Takes user input as input then parses loaded file for relevant rows, will then return relevant rows


def ir_database_parser(user_input_list, ir_data):
    parsed_frequencies = [['User_input']+ir_data[0]]  # add headers to the array that will be returned
    for user_freq in user_input_list:  # for every frequency inputted by the user
        for entry in ir_data[1:]:  # for every row in the loaded IR database (excluding the headers)
            if user_freq in range(int(entry[0]), int(entry[1])):  # builds search range from min and max wavenumbers
                parsed_frequencies.append([user_freq]+entry)  # adds user input wavenumber to start or appended list

    return parsed_frequencies  # returns nested array which is a trimmed down version of the original database


########################################################################################################################


def results_writer(filtered_ir):
    while True:
        user_file_name = input('Please enter valid file name ')
        if user_file_name.isalpha():
            print('Filename saved to :  '+user_file_name+'.txt')
            break
        else:
            print('Please enter valid filename')

    with open(user_file_name+'.txt', 'w') as f:
        for line in filtered_ir:
            for entry in line:
                f.write(str(entry)+'|')

    print('file written')

########################################################################################################################
# Main : Takes database file and user input to parse the database file, return a trimmed file and then save to new txt


def main():
    returned_analysis = ir_database_parser(user_frequencies(), ir_database())  # create filtered list of wavenumbers
    results_writer(returned_analysis)


########################################################################################################################

if __name__ == '__main__':
    main()
