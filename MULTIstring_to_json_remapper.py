import json
import re
from collections.abc import Iterable

json_in_path = 'base 8 input JSON.json'
json_out_path = 'base modified 8 input.json'

# The strings you put into this list correspond to the number of macro.
# So 'A' is macro 1, 'B' is macro 2, etc...
# Make sure to add additional space at end of string if you want it.
input_strings = [
                 '', # Macro 1
                 '', # Macro 2
                 '', # Macro 3
                 '', # Macro 4
                 '', # Macro 5
                 '', # Macro 6
                 '', # Macro 7
                 ''  # Macro 8
                 ]

# open the template JSON file once.
with open(json_in_path) as f:
   data = json.load(f)

usages_by_function = {
'Left button': '0x00090001',
 'Right button': '0x00090002',
 'Middle button': '0x00090003',
 'Back': '0x00090004',
 'Forward': '0x00090005',
 'Button 6': '0x00090006',
 'Button 7': '0x00090007',
 'Button 8': '0x00090008',
 'Cursor X': '0x00010030',
 'Cursor Y': '0x00010031',
 'V scroll': '0x00010038',
 'H scroll': '0x000c0238',
 'Left Control': '0x000700e0',
 'Left Shift': '0x000700e1',
 'Left Alt': '0x000700e2',
 'Left GUI': '0x000700e3',
 'Right Control': '0x000700e4',
 'Right Shift': '0x000700e5',
 'Right Alt': '0x000700e6',
 'Right GUI': '0x000700e7',
 'A': '0x00070004',
 'B': '0x00070005',
 'C': '0x00070006',
 'D': '0x00070007',
 'E': '0x00070008',
 'F': '0x00070009',
 'G': '0x0007000a',
 'H': '0x0007000b',
 'I': '0x0007000c',
 'J': '0x0007000d',
 'K': '0x0007000e',
 'L': '0x0007000f',
 'M': '0x00070010',
 'N': '0x00070011',
 'O': '0x00070012',
 'P': '0x00070013',
 'Q': '0x00070014',
 'R': '0x00070015',
 'S': '0x00070016',
 'T': '0x00070017',
 'U': '0x00070018',
 'V': '0x00070019',
 'W': '0x0007001a',
 'X': '0x0007001b',
 'Y': '0x0007001c',
 'Z': '0x0007001d',
 '1': '0x0007001e',
 '2': '0x0007001f',
 '3': '0x00070020',
 '4': '0x00070021',
 '5': '0x00070022',
 '6': '0x00070023',
 '7': '0x00070024',
 '8': '0x00070025',
 '9': '0x00070026',
 '0': '0x00070027',
 'Enter': '0x00070028',
 'Escape': '0x00070029',
 'Backspace': '0x0007002a',
 'Tab': '0x0007002b',
 'Space': '0x0007002c',
 'Caps Lock': '0x00070039',
 'PrintScreen': '0x00070046',
 'Scroll Lock': '0x00070047',
 'Pause': '0x00070048',
 'Insert': '0x00070049',
 'Home': '0x0007004a',
 'PageUp': '0x0007004b',
 'Delete': '0x0007004c',
 'End': '0x0007004d',
 'PageDown': '0x0007004e',
 'Right arrow': '0x0007004f',
 'Left arrow': '0x00070050',
 'Down arrow': '0x00070051',
 'Up arrow': '0x00070052',
 'Num Lock': '0x00070053',
 '- _': '0x0007002d',
 '= +': '0x0007002e',
 '[ {': '0x0007002f',
 '] }': '0x00070030',
 '\\ |': '0x00070031',
 '; :': '0x00070033',
 '‘ “': '0x00070034',
 '` ~': '0x00070035',
 ', <': '0x00070036',
 '. >': '0x00070037',
 '/ ?': '0x00070038',
 '!': ['0x000700e1', '0x0007001e'],
 'F1': '0x0007003a',
 'F2': '0x0007003b',
 'F3': '0x0007003c',
 'F4': '0x0007003d',
 'F5': '0x0007003e',
 'F6': '0x0007003f',
 'F7': '0x00070040',
 'F8': '0x00070041',
 'F9': '0x00070042',
 'F10': '0x00070043',
 'F11': '0x00070044',
 'F12': '0x00070045',
 'F13': '0x00070068',
 'F14': '0x00070069',
 'F15': '0x0007006a',
 'F16': '0x0007006b',
 'F17': '0x0007006c',
 'F18': '0x0007006d',
 'F19': '0x0007006e',
 'F20': '0x0007006f',
 'F21': '0x00070070',
 'F22': '0x00070071',
 'F23': '0x00070072',
 'F24': '0x00070073',
 'Keypad /': '0x00070054',
 'Keypad *': '0x00070055',
 'Keypad -': '0x00070056',
 'Keypad +': '0x00070057',
 'Keypad Enter': '0x00070058',
 'Keypad 1': '0x00070059',
 'Keypad 2': '0x0007005a',
 'Keypad 3': '0x0007005b',
 'Keypad 4': '0x0007005c',
 'Keypad 5': '0x0007005d',
 'Keypad 6': '0x0007005e',
 'Keypad 7': '0x0007005f',
 'Keypad 8': '0x00070060',
 'Keypad 9': '0x00070061',
 'Keypad 0': '0x00070062',
 'Keypad .': '0x00070063',
 'Keypad =': '0x00070067',
 'Non-US \\ |': '0x00070064',
 'Non-US # ~': '0x00070032',
 'Application': '0x00070065',
 'Power': '0x00070066',
 '\\ _': '0x00070087',
 '¥ |': '0x00070089',
 'Henkan': '0x0007008a',
 'Muhenkan': '0x0007008b',
 'Kana': '0x00070088',
 'Kana (Mac)': '0x00070090',
 'Eisū (Mac)': '0x00070091',
 'Num Lock LED': '0x00080001',
 'Caps Lock LED': '0x00080002',
 'Scroll Lock LED': '0x00080003',
 'Compose LED': '0x00080004',
 'Kana LED': '0x00080005',
 'Volume up': '0x000c00e9',
 'Volume down': '0x000c00ea',
 'Mute': '0x000c00e2',
 'Mic mute': '0x000b002f',
 'Play/pause': '0x000c00cd',
 'Stop': '0x000c00b7',
 'Next track': '0x000c00b5',
 'Previous track': '0x000c00b6',
 'Nothing': '0x00000000',
 'Expression 1': '0xfff30001',
 'Expression 2': '0xfff30002',
 'Expression 3': '0xfff30003',
 'Expression 4': '0xfff30004',
 'Expression 5': '0xfff30005',
 'Expression 6': '0xfff30006',
 'Expression 7': '0xfff30007',
 'Expression 8': '0xfff30008',
 'Register 1': '0xfff50001',
 'Register 2': '0xfff50002',
 'Register 3': '0xfff50003',
 'Register 4': '0xfff50004',
 'Register 5': '0xfff50005',
 'Register 6': '0xfff50006',
 'Register 7': '0xfff50007',
 'Register 8': '0xfff50008',
 'Register 9': '0xfff50009',
 'Register 10': '0xfff5000a',
 'Register 11': '0xfff5000b',
 'Register 12': '0xfff5000c',
 'Register 13': '0xfff5000d',
 'Register 14': '0xfff5000e',
 'Register 15': '0xfff5000f',
 'Register 16': '0xfff50010',
 'Register 17': '0xfff50011',
 'Register 18': '0xfff50012',
 'Register 19': '0xfff50013',
 'Register 20': '0xfff50014',
 'Register 21': '0xfff50015',
 'Register 22': '0xfff50016',
 'Register 23': '0xfff50017',
 'Register 24': '0xfff50018',
 'Register 25': '0xfff50019',
 'Register 26': '0xfff5001a',
 'Register 27': '0xfff5001b',
 'Register 28': '0xfff5001c',
 'Register 29': '0xfff5001d',
 'Register 30': '0xfff5001e',
 'Register 31': '0xfff5001f',
 'Register 32': '0xfff50020',
 'GPIO 0': '0xfff40000',
 'GPIO 1': '0xfff40001',
 'GPIO 2': '0xfff40002',
 'GPIO 3': '0xfff40003',
 'GPIO 4': '0xfff40004',
 'GPIO 5': '0xfff40005',
 'GPIO 6': '0xfff40006',
 'GPIO 7': '0xfff40007',
 'GPIO 8': '0xfff40008',
 'GPIO 9': '0xfff40009',
 'GPIO 10': '0xfff4000a',
 'GPIO 11': '0xfff4000b',
 'GPIO 12': '0xfff4000c',
 'GPIO 13': '0xfff4000d',
 'GPIO 14': '0xfff4000e',
 'GPIO 15': '0xfff4000f',
 'GPIO 16': '0xfff40010',
 'GPIO 17': '0xfff40011',
 'GPIO 18': '0xfff40012',
 'GPIO 19': '0xfff40013',
 'GPIO 20': '0xfff40014',
 'GPIO 21': '0xfff40015',
 'GPIO 22': '0xfff40016',
 'GPIO 23': '0xfff40017',
 'GPIO 24': '0xfff40018',
 'GPIO 25': '0xfff40019',
 'GPIO 26': '0xfff4001a',
 'GPIO 27': '0xfff4001b',
 'GPIO 28': '0xfff4001c',
 'GPIO 29': '0xfff4001d',
 'Macro 1': '0xfff20001',
 'Macro 2': '0xfff20002',
 'Macro 3': '0xfff20003',
 'Macro 4': '0xfff20004',
 'Macro 5': '0xfff20005',
 'Macro 6': '0xfff20006',
 'Macro 7': '0xfff20007',
 'Macro 8': '0xfff20008',
 'Macro 9': '0xfff20009',
 'Macro 10': '0xfff2000a',
 'Macro 11': '0xfff2000b',
 'Macro 12': '0xfff2000c',
 'Macro 13': '0xfff2000d',
 'Macro 14': '0xfff2000e',
 'Macro 15': '0xfff2000f',
 'Macro 16': '0xfff20010',
 'Macro 17': '0xfff20011',
 'Macro 18': '0xfff20012',
 'Macro 19': '0xfff20013',
 'Macro 20': '0xfff20014',
 'Macro 21': '0xfff20015',
 'Macro 22': '0xfff20016',
 'Macro 23': '0xfff20017',
 'Macro 24': '0xfff20018',
 'Macro 25': '0xfff20019',
 'Macro 26': '0xfff2001a',
 'Macro 27': '0xfff2001b',
 'Macro 28': '0xfff2001c',
 'Macro 29': '0xfff2001d',
 'Macro 30': '0xfff2001e',
 'Macro 31': '0xfff2001f',
 'Macro 32': '0xfff20020'
 }

def magic(input_string, macro_number):
    string_list = []
    usages_list =[]

    repeats_string = re.sub(r"(.)\1", r"\1+\1", input_string)
    caps_string = re.sub(r'([A-Z])', r'_\1', repeats_string)

    caps_string = caps_string.upper()

    # print(caps_string)

    for i in caps_string:
        string_list.append(i)

    for i, n in enumerate(string_list):
        if n == '_':
            string_list[i] = 'Left Shift'
        if n == '+':
            string_list[i] = 'Nothing'
        if n == ' ':
            string_list[i] = 'Space'
    # print(string_list)

    for i in string_list:
        c = usages_by_function[i]
        usages_list.append(c)
    # print(usages_list)

    # You need to reflatten the list because of any two key characters like '!'
    def flatten(lis):
         for item in lis:
             if isinstance(item, Iterable) and not isinstance(item, str):
                 for x in flatten(item):
                     yield x
             else:
                 yield item

    flat_list = list(flatten(usages_list))

    # print(flat_list)

    # result takes the flat_list and finds instances of shift and makes a nested
    # list with it and the next adjoining value. So you can have Capitol letters.

    result = []
    temp_list = []
    for i in flat_list:
        if i == '0x000700e1':
            temp_list.append(i)
        else:
            temp_list.append(i)
            result.append(temp_list)
            temp_list = []
    # result.append(temp_list)
    # result.pop()
    # print(result)
    # insert the data we just created into the template JSON file at the certain
    # macro number.
    data['macros'].insert(macro_number, result)

    # turn the python dictionary back into a JSON object with some formatting
    modified_json = json.dumps(data, indent=4)

    # write the JSON object to a file
    with open(json_out_path, "w") as outfile:
        outfile.write(modified_json)

for i in range(0, len(input_strings)):
    magic(input_strings[i], i)
