# IR_analyser

## Project Function
Using Python, the aim is to allow for quicker analysis of standard, chemical Infrared (IR) Spectra.

### Current Status
The program currently works on a command line input as per the below example:
* `-r` specifies the reference lookup file for peak comparison
* `-w` space separated peak positions (integers only)
* `-s` filename to save the oupt file to (including csv extension)


    python analyser.py -r ir_frequencies.txt -w "3501 1678 2345" -s example_output.csv

### TODO:
* Somehow fix the rotation when reading images in !!! 