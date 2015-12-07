
def parse_instructions(instruction_string):
    """
        Parse the instruction string character by character to determine
        where Santa goes.
        @instruction_string - string listing the directions to go
    """
    floor = 0
    basement_instruction = 0
    base_trigger = False
    for instruction in instruction_string:
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1
        else:
            pass
        if base_trigger == False:
            basement_instruction += 1
            if floor < 0:
                base_trigger = True

    print "Ending Floor: %i" % floor 
    print "Basement Instruction: %i" %basement_instruction
fh = open('puzzle1.txt','r')
parse_instructions(fh.read())
