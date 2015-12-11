import re
import pdb

def requirement_3(input_string):
    """
    Passwords must contain at least two different, non-overlapping pairs of 
    letters, like aa, bb, or zz.
    input_string - Input value
    @returns - True/False depending on pass ability
    """
    return 2 <= len(re.findall('([a-z])\\1', input_string))

def requirement_2(input_string):
    """
    Passwords may not contain the letters i, o, or l, as these letters can be 
    mistaken for other characters and are therefore confusing.
    input_string - Input value
    @returns - True/False depending on pass ability
    """
    return 0 == len(re.findall('[iol]', input_string))
def requirement_1(input_string):
    """
    Passwords must include one increasing straight of at least three letters,
    like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd 
    doesn't count.
    input_string - Input value
    @returns - True/False depending on pass ability
    """
    for i in range(len(input_string)-2):
        sub_unit = input_string[i:i+3]
        if ord(sub_unit[0]) == ord(sub_unit[1]) - 1 == ord(sub_unit[2]) - 2:
            return True
    return False
def increment_password(input_string):
    """
    To help him remember his new password after the old one expires, Santa 
    has devised a method of coming up with a password based on the previous 
    one. Corporate policy dictates that passwords must be exactly eight 
    lowercase letters (for security reasons), so he finds his new password by 
    incrementing his old password string repeatedly until it is valid.

    Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so
    on. Increase the rightmost letter one step; if it was z, it wraps around to
    a, and repeat with the next letter to the left until one doesn't wrap 
    around.
    """
    if input_string[-1] != 'z':
        input_string = input_string[:-1] + \
            chr(ord(input_string[-1])+1)
    else:
        back_index = 1
        while input_string.endswith('z'*back_index):
            back_index += 1
        pre_partition = -1*(back_index)
        partition = pre_partition
        post_count = back_index - 1
        input_string = input_string[:pre_partition] + \
            chr(ord(input_string[partition])+1) + \
            'a'*(post_count)
    return input_string
def compute_next(input_string):
    """
        Compute Santa's next password
        input_string - input
        @returns - Result
    """
    input_string = increment_password(input_string)
    while not(
            requirement_3(input_string) and
            requirement_2(input_string) and
            requirement_1(input_string)
        ):
        input_string = increment_password(input_string)
    return input_string
seed_string = 'hxbxwxba'
print compute_next(seed_string)
print compute_next(compute_next(seed_string)

