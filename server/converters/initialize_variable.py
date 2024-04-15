import re
import string

from server.utilities import is_float, is_int, process_pseudocode
from word2number import w2n


def initialize_variable(tokens, line):
    generated_CLanguage = ""

    variable_name = ""
    variable_type = ""
    variable_value = ""
    
    # constant string like 'hello world' for chars
    const_string = re.findall("'([^']*)'", line) 

    # pseudocode wants to initialize a string
    if len(const_string) > 0:
        no_const_string = line.replace(f"'{const_string[0]}'", "")
        no_const_string = re.sub(" +", ' ', no_const_string)
        no_const_string = process_pseudocode(no_const_string)
    
        variable_type = "char"
        
        # assuming that elements left in this list is 'initiallize' and variable_name
        if len(no_const_string) == 2:
            variable_name = no_const_string[1].text + "[]"
            
            # constant strings
            for i in const_string:
                variable_value += i
                
            generated_CLanguage += f'{variable_type} {variable_name} = "{variable_value}";\n'
        else:
            generated_CLanguage += "//Error: You cannot initilize two variables at once\n"
    
    else:
        for i in range(1, len(tokens)):
            
            # If it a the number then most probably it is the variable value
            if tokens[i].pos_ == 'NUM' or tokens[i].is_digit:
                
                variable_value = tokens[i].text

                # check if the value is an int or float or a numeric word
                if is_int(tokens[i].text):
                    variable_type = 'int'
                    variable_value = tokens[i].text
                else:
                    converted_numeric_word = w2n.word_to_num(tokens[i].text)
                    variable_type = 'int'
                    variable_value = converted_numeric_word
            
            elif is_float(tokens[i].text):
                    variable_type = 'float'
                    variable_value = tokens[i].text

            elif tokens[i].text not in string.punctuation or tokens[i].text != 'intialize' or tokens[i].text != 'initialize':
                if tokens[i].text == 'int' or tokens[i].text == 'char' or tokens[i].text.lower() == 'float':
                    continue
                variable_name = tokens[i].text
            else:
                generated_CLanguage += "// There's an error in this line.\n"
        
        if variable_name == "":
            variable_name = line.split(" ")[1]
        
        if variable_value == "":
            if tokens[1].text == 'int' or tokens[2].text == 'int':
                variable_type = "int"
            elif tokens[1].text == 'float'or tokens[2].text == 'float':
                variable_type = "float"
            elif tokens[1].text == 'char':
                variable_type = "char"
            else:
                return None
            
            if variable_type == 'char':
                variable_name += "[]"
                
            generated_CLanguage += f"{variable_type} {variable_name};\n"
        else:
            generated_CLanguage += f"{variable_type} {variable_name} = {variable_value};\n"

    return generated_CLanguage, {variable_name.replace('[]', ''): variable_type}