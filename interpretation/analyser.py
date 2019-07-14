import pandas as pd
import click

########################################################################################################################


def user_frequencies(cli_string):
    """
    Takes user frequencies as space separated string and returns them as a list of integers
    :param cli_string: str, space separated integers
    :return: list of user inputted integers
    """
    user_input = [int(i) for i in cli_string.split(' ')]
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
        freq_matches.insert(loc=0, column='User', value=freq)  # insert user frequency for reference in the saved file
        user_df = user_df.append(freq_matches)

    return user_df


########################################################################################################################

@click.command()
@click.option('--ref_file', '-r')
@click.option('--wavenumbers', '-w')
@click.option('--save_name', '-s')
def main(ref_file, wavenumbers, save_name):
    """
    Loads contents of an IR reference file to pandas datframe which then indices for matches to user specified
    wavenumbers. The resulting dataframe is then saved to a csv file with user specified name.
    :param ref_file: location of reference IR file, pipe delimited as commas present in chemical nomenclature
    :param wavenumbers: str, space separated user inputs corresponding to peaks in their IR spectrum
    :param save_name: str, the filename (including extension) of the results to be saved to
    :return: none
    """
    df = pd.read_csv(ref_file, sep='|')
    frequencies = user_frequencies(wavenumbers)
    parsed_df = ir_database_parser(frequencies, df)
    parsed_df.to_csv(save_name, index=False)


########################################################################################################################


if __name__ == '__main__':
    main()
