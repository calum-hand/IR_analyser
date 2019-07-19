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
* The image looks like it's being rotated but in actuality it's because of how the numpy arrays are being created
>1. Array is just the positions along x axis (i.e. [start, end, 1])
>2. Array is all the points but seemingly rotated
* to fix this we need to somehow combine the positional element of the first array with the actual intensity of the other in order to create a uniform, flowing array   