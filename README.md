# IR_analyser

## Project Function
> Using Python, the aim is to allow for quicker analysis of standard, chemical Infrared (IR) Spectra.

### Current Status
The program currently works as described below:
>* Using a simple entry system, the user specifies the wavenumber of the peaks observed in the spectra until told to 'run'
>* The script then takes the usre input (stored as a list) and then loops through the [database file](https://www.sigmaaldrich.com/technical-documents/articles/biology/ir-spectrum-table.html)
>* If the user input matches a value in the range of the peaks, then that user input and peak information is written to new list
>* Once the wavenumbers have been passed through the database, the loop stops


### TODO based on [r/learnpython](https://www.reddit.com/r/learnpython/comments/a5yriu/anyone_willing_to_help_review_an_beginners_code/) feedback:
* Updated all todos and can now accept command line inputs for
>* Reference file location
>* User frequencies
>* File name for output results as below

    python analyser.py -r ir_frequencies.txt -w "3501 1678 2345" -s example_output.csv


### Future work
While this project currently functions at a basic level the below updates are required or would like to be incorporated:
>* To be able to take an image of an IR spectra as input rather than user inputting the numbers
