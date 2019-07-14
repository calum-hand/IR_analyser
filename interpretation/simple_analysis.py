import pandas as pd

########################################################################################################################


def user_frequencies():
    """
    Takes user frequencies and returns them in a list when user specifies is complete
    :return: list of user inputted integers
    """
    user_input = []
    while True:
        entry = input('Please enter wavenumber (cm^-1) or \'run\'  : ')
        if entry == 'run':
            break
        elif entry.isnumeric():
            user_input.append(int(entry))

    return user_input


########################################################################################################################


def ir_database_parser(user_input_list, ir_data):
    """
    Given the list of user frequencies and the whole IR database, for each frequency, find the rows of the df which
    match the frequency and save the indices to a list. The original df is then filtered by the indices and returned.
    :param user_input_list: list, integers
    :param ir_data: pd.DataFrame, the IR DataFrame to be parsed for matches
    :return: indexed version of the original database
    """
    user_df = pd.DataFrame()
    for freq in user_input_list:
        matches = [count for count, row in ir_data.iterrows() if row['min_abs(cm-1)'] <= freq <= row['max_abs(cm-1)']]
        freq_matches = ir_data.iloc[matches]
        freq_matches.insert(loc=0, column='user', value=freq)  # insert user frequency for reference in the saved file
        user_df = user_df.append(freq_matches)

    return user_df


########################################################################################################################


def main():
    """
    Loads contents of an IR reference file to pandas datframe which then indices for matches to user specified
    frequencies. The resulting dataframe is then saved to a csv file with user specified name.
    """
    df = pd.read_csv('ir_frequencies.txt', sep='|')
    frequencies = user_frequencies()
    parsed_df = ir_database_parser(frequencies, df)
    save_name = input('Please enter a filename to save to plus extension: ')
    parsed_df.to_csv(save_name, index=False)


########################################################################################################################


if __name__ == '__main__':
    main()
