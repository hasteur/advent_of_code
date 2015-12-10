start_string = '1321131112'

def split_string(input_string):
    """ 
        Calculate output string
        @input_string - Input to function
    """
    result_string = ''
    prev_char = input_string[0]
    char_ct = 0
    for char_pos in xrange(0,len(input_string)):

        if input_string[char_pos] == prev_char:
            char_ct += 1
        else:
            result_string += str(char_ct) + prev_char
            prev_char = input_string[char_pos]
            char_ct = 1
    return result_string + str(char_ct) + prev_char

result_string = split_string(start_string)
for i in xrange(0, 49):
    result_string = split_string(result_string)

print len(result_string)
