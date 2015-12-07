
def parse_instructions(instruction_string):
    """
        Parse the instruction string character by character to determine
        where Santa goes.
        @instruction_string - string listing the directions to go
    """
    floor = 0
    for instruction in instruction_string:
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1
        else:
            pass
    print floor
fh = open('puzzle1.txt','r')
parse_instructions(fh.read())
