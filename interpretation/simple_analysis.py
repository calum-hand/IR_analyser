import pandas as pd

########################################################################################################################


def user_frequencies():
    """Takes user frequencies and returns them in a list when user specifies is complete"""
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
    user_df = pd.DataFrame()
    for freq in user_input_list:
        matches = [count for count, row in ir_data.iterrows() if row['min_abs(cm-1)'] <= freq <= row['max_abs(cm-1)']]
        freq_matches = ir_data.iloc[matches]
        freq_matches.insert(loc=0, column='user', value=freq)
        user_df = user_df.append(freq_matches)

    return user_df


########################################################################################################################


def main():
    df = pd.read_csv('ir_frequencies.txt', sep='|')
    frequencies = user_frequencies()
    parsed_df = ir_database_parser(frequencies, df)
    save_name = input('Please enter a filename to save to plus extension: ')
    parsed_df.to_csv(save_name, index=False)


if __name__ == '__main__':
    main()
