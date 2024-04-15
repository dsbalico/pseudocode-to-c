import re
from server.utilities import get_format_specifier, process_pseudocode

def print_statement(tokens, line, initialized_variables, inside_for, for_variable):
    generated_CLanguage = ""
    arithmetic_list = ['plus', 'minus', 'times', 'divided', 'modulo']

    # find strings that are enclose with apostrophes
    const_string = re.findall("'([^']*)'", line)

    for string in const_string:
        line = line.replace(f"'{string}'", "") # remove all const string in the line   

    no_const_string = re.sub(" +", ' ', line) # remove extra spaces
    no_const_string = process_pseudocode(no_const_string) # tokenize the pseudocode without const strings

    # constant string only
    if len(const_string) > 0 and len(no_const_string) <= 1:
        generated_CLanguage += 'printf("'

        for string in const_string:
            generated_CLanguage += string

        generated_CLanguage += '");\n'
    
    # There's a constant string and a variable
    elif len(const_string) > 0 and len(no_const_string) > 0:
        generated_CLanguage +=  'printf("'

        # Add all const strings
        for string in const_string:
            generated_CLanguage += string
        
        # Add all format specifiers of the indicated variables
        for i in range(1, len(no_const_string)):
            try:
                if no_const_string[i-1].text in arithmetic_list:
                    continue
                generated_CLanguage += f"{get_format_specifier(initialized_variables[no_const_string[i].text])} "
            except:
                if no_const_string[i].text == arithmetic_list[0] or no_const_string[i].text == arithmetic_list[1] or no_const_string[i].text == arithmetic_list[2] or no_const_string[i].text == arithmetic_list[3] or no_const_string[i].text == arithmetic_list[4] or no_const_string[i].is_digit:
                    continue

                generated_CLanguage += no_const_string[i].text
            
        generated_CLanguage +=  '"'
        
        # Add all the variables
        for i in range(1, len(no_const_string)):
            if no_const_string[i].text in initialized_variables.keys() and no_const_string[i-1].text not in arithmetic_list:
                generated_CLanguage += ','

                if i == len(no_const_string)-1: # if last element don't include space
                    generated_CLanguage += no_const_string[i].text
                else:
                    if no_const_string[i+1].text in arithmetic_list:
                        generated_CLanguage += no_const_string[i].text
                    else:
                        generated_CLanguage += no_const_string[i].text + ', '
            elif no_const_string[i].text == arithmetic_list[0]:
                generated_CLanguage += "+"
            elif no_const_string[i].text == arithmetic_list[1]:
                generated_CLanguage += "-"
            elif no_const_string[i].text == arithmetic_list[2]:
                generated_CLanguage += "*"
            elif no_const_string[i].text == arithmetic_list[3]:
                generated_CLanguage += "/"
            elif no_const_string[i].text == arithmetic_list[4]:
                generated_CLanguage += "%"
            elif no_const_string[i].is_digit:
                generated_CLanguage += no_const_string[i].text
            else:
                generated_CLanguage += no_const_string[i].text
                        
        generated_CLanguage += '); \n'

    # Variable only
    else:
        generated_CLanguage += f'printf("'

        # Format
        for i in range(1, len(tokens)):
            if tokens[i].text in initialized_variables.keys() or (inside_for == True and tokens[i].text == for_variable):
                if i == len(tokens)-1: # if last element don't include space
                    try:
                        if no_const_string[i-1].text in arithmetic_list:
                            continue

                        generated_CLanguage += get_format_specifier(initialized_variables[tokens[i].text])
                    except:
                        generated_CLanguage += "%d"
                else:
                    try:
                        generated_CLanguage += get_format_specifier(initialized_variables[tokens[i].text]) + " "
                    except:
                        generated_CLanguage += "%d "
            else:
                if tokens[i].text in arithmetic_list or tokens[i].is_digit:
                    continue
                else:
                    if i == len(tokens)-1: # if last element don't include space
                        generated_CLanguage += tokens[i].text
                    else:
                        generated_CLanguage += tokens[i].text + " "
            
        generated_CLanguage += '"'     

        # Variables
        for i in range(1, len(tokens)):
            try:
                if tokens[i].text in initialized_variables.keys() or (inside_for == True and tokens[i].text == for_variable):
                    generated_CLanguage += ','
                    if tokens[i].text in initialized_variables.keys() or (inside_for == True and tokens[i].text == for_variable) and tokens[i+1].text not in arithmetic_list:
                        if i == len(tokens)-1: # if last element don't include space
                            generated_CLanguage += tokens[i].text
                        else:
                            if tokens[i+1].text in arithmetic_list or tokens[i+1].text not in initialized_variables.keys(): 
                                generated_CLanguage += tokens[i].text
                            else:
                                generated_CLanguage += tokens[i].text + ', '
                    elif tokens[i].text == arithmetic_list[0]:
                        generated_CLanguage += "+"
                    elif tokens[i].text == arithmetic_list[1]:
                        generated_CLanguage += "-"
                    elif tokens[i].text == arithmetic_list[2]:
                        generated_CLanguage += "*"
                    elif tokens[i].text == arithmetic_list[3]:
                        generated_CLanguage += "/"
                    elif tokens[i].text == arithmetic_list[4]:
                        generated_CLanguage += "%"
                    elif tokens[i].is_digit:
                        generated_CLanguage += tokens[i].text
                    else:
                        generated_CLanguage += tokens[i].text
                else:
                    continue
            except:
                generated_CLanguage += tokens[i].text

        generated_CLanguage += ');\n'

    return generated_CLanguage