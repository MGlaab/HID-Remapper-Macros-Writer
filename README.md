# HID-Remapper-Macros-Writer

A python script written to work with HID ReMapper. 
I'm not a programmer. It isn't pretty. 

It take a basic string, without punctuation, and converts it into a JSON formatted file to then import into the HID ReMapper online tool. Basically, if you open the python file there are three variables to change:
json_in_path, json_out_path, and input_string. I would use this mainly for short phrases, a persons name, etc. There are two buttons attached to GPIO18 and GPIO21. GPIO18 maps to an led on GPIO13, and GPIO21 maps to Macro32. Macro32 is whatever you put as the input_string.
To Do:
Make a variable to decide what Macro to program. (so you oculd have two inputs with different macros i.e. different strings)
