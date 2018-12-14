# IR_analyser

## Project Function
> Using Python, the aim is to allow for quicker analysis of standard, chemical Infrared (IR) Spectra. 

### Current Status
> The program currently works as described below:
>>* Using a simple entry system, the user specifies the wavenumber of the peaks observed in the spectra until told to 'run'
>>* The script then takes the usre input (stored as a list) and then loops through the [database file](https://www.sigmaaldrich.com/technical-documents/articles/biology/ir-spectrum-table.html)
>>* If the user input matches a value in the range of the peaks, then that user input and peak information is written to new list
>>* Once the wavenumbers have been passed through the database, the loop stops
>>* The user is then prompted to enter a filename for the sorted peaks to be written to and saved 


### TODO based on [r/learnpython](https://www.reddit.com/r/learnpython/comments/a5yriu/anyone_willing_to_help_review_an_beginners_code/) feedback:
>* Read database IR file with CSV module based on pipe delimiter
>* convert wavenumbers to integers while creating the database rather than convert later on during analysis
>* add kwargs in the main to allow custom file name inputs (when run as python simple_analysis.py some_file.txt) or some other way of not hardcoding the input name.
>* Instead of if 2 in range(1,5), do 1<=x<5, that way you do not need to expand the range for each entry.
>* unpack things like these to variables with informative names, eg : 
>> `for entry in data:`
        `abs_min, abs_max = entry[:2]`
        `if user_freq in range(abs_min, abs_max)`


### Future works
> While this project currently functions at a basic level the below updates are required or would like to be incorporated:
>>* To be able to take an image of an IR spectra as input rather than user inputting the numbers


 
