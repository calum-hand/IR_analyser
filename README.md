# PyR Analysis

## Project Function
Using Python, the aim is to allow for quicker analysis of standard Infrared (IR) Spectra.

### Current Status
The program currently works on a command line input as per the below example:
* `-r` specifies the reference lookup file for peak comparison
* `-w` space separated peak positions (integers only)
* `-s` filename to save the output file to (including csv extension)


    python main.py -r ref_pyr.txt -w "3501 1678 2345" -s example_pyr.csv

___