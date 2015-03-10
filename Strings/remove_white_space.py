#!/usr/bin/env python

from array import *

string1 = "Quick brown fox    jumped over the lazy    dog.\0"

s_array = array('u',['Q','u','i','c','k',' ','b','r','\t','o','w','n',' ','f','o','x','\0'])

print(s_array)

def remove_white_spaces(s):
    if s == None or len(s) == 0 or s[0]== '\0':
        return
    
    read_ptr = 0
    write_ptr = 0
    
    while read_ptr < len(s) and s[read_ptr] != '\0':
        if s[read_ptr] != ' ' and s[read_ptr] != '\t':
            s[write_ptr] = s[read_ptr]
            write_ptr += 1
        read_ptr += 1
    
    s[write_ptr]='\0'
    
remove_white_spaces(s_array)
print(s_array)