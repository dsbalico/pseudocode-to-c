# for i equals 10 to 100
# loop i from 1 to 10

def for_loop(tokens, initialized_variables, line):
    numbers = []
    variable_name = []
    condition = "<="

    for token in tokens:
        if token.text == 'for' or token.text == 'loop' or token.text == 'equals' or token.text == 'equal' or token.text == '=' or token.text == ':':
            continue

        if token.pos_ == 'NUM' or token.is_digit:
            numbers.append(token.text)

        else:
            variable_name.append(token.text)

    if len(variable_name) <= 0:
        variable_name.append(line.split(" ")[1])

    if len(numbers) > 2:
        generated_CLanguage = "// You can't enter three or more numbers!\n"

    if len(numbers) == 2 and len(variable_name) == 1:
        if numbers[0] < numbers[1]:
            condition = "<="
        else:
            condition = ">="

        if variable_name[0] not in initialized_variables.keys():
            generated_CLanguage = f"for(int {variable_name[0]} = {numbers[0]} ; {variable_name[0]} {condition} {numbers[1]} ; {variable_name[0]}++) " + "{\n"
        else:
            generated_CLanguage = f"for({variable_name[0]} = {numbers[0]} ; {variable_name[0]} {condition} {numbers[1]} ; {variable_name[0]}++) " + "{\n"
    else:
        if len(variable_name) == 2:
            if variable_name[0] not in initialized_variables.keys():
                generated_CLanguage = f"for(int {variable_name[0]} = {numbers[0]} ; {variable_name[0]} {condition} {variable_name[1]} ; {variable_name[0]}++) " + "{\n"
            else:
                generated_CLanguage = f"for({variable_name[0]} = {numbers[0]} ; {variable_name[0]} {condition} {variable_name[1]} ; {variable_name[0]}++) " + "{\n"


    return generated_CLanguage, variable_name[0]