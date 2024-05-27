# HID-Remapper-Macros-Writer

A python script written to work with HID ReMapper. Now there is a Javascript single string remapper.
I'm not a programmer. It isn't pretty. 

Scripts that take basic strings, without punctuation, and converts it into a JSON formatted file to then import into the HID ReMapper online tool. Basically, if you open the python file there are three variables to change:
json_in_path, json_out_path, and input_strings. I would use this mainly for short phrases, a persons name, etc. There are 8 buttons attached to GPIO10-GPIO13 and GPIO18-GPIO21 on the Pi Pico. Each GPIO maps to a Macro.

the MULTIstring_to_json_remapper.py file takes 8 strings and remaps them into 8 macros.

I worked out a Javascript file for single strings. I'm not a programmer. It isn't pretty. But it works for a single remap. You can cahnge the macro it maps to but it rewrites the entire file so, it still needs work. I'm going to try a MULTIstring_to_json_remapper.js next.
