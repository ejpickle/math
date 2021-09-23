#!/usr/bin/env python3

# Default read comes in as strings and must be converted if you want a number

import sys

# read first value input after the script name
num = sys.argv[1]

print('Read value: {}'.format(num))

print('Read value *4: {}'.format(num*4))

print('Read value type: {}'.format(type(num)))

# Convert to a number
num_as_number = int(num)
print('Converted to number: {}'.format(num_as_number))

print('Converted value type: {}'.format(type(num_as_number)))

print('Converted value *4: {}'.format(num_as_number*4))
