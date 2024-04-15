
from server.converters.arithmetic_operators import arithmetic_operators
from server.converters.for_loop import for_loop
from server.converters.if_statement import if_statement
from server.converters.increment_decrement import increment_decrement
from server.converters.initialize_variable import initialize_variable
from server.converters.print_statement import print_statement
from server.converters.set_variable import set_variable
from server.converters.while_loop import while_loop
from flask import request
from flask_restful import Resource
from server.utilities import process_pseudocode


class PseudocodeToC(Resource):
    def post(self):
        # get the request body
        data = request.get_json()
        pseudocode = data['pseudocode']

        # pseudocode is splitted by \n (line break)
        pseudocode_lines = [p for p in pseudocode.split('\n') if p]

        generated_CLanguage = ""
        # dictionary of initialized variables and their type
        initialized_variables = {}

        # is inside a for loop?
        inside_for = False
        for_variable = ""

        # for every pseudocode line
        for line in pseudocode_lines:
            tokens = process_pseudocode(line) # process the pseudocode
            
            intent = tokens[0].text.lower() # the first token should always be the keyword 

            # line want to end if, while, for, and dowhile
            if intent == "endif" or intent == "endfor" or intent == "endwhile" or intent == "end" or intent == 'endloop':
                generated_CLanguage += "}\n"

                if intent == 'endfor' or intent == 'endloop':
                    inside_for = False
                    for_variable = ""

            elif intent == 'add' or  intent == 'subtract' or intent == 'multiply' or intent == 'divide':
                generated_CLanguage += arithmetic_operators(tokens, initialized_variables)

            # line wants to initialize a variable
            elif intent == 'initialize' or intent == 'intialize' or intent == 'declare':
                try:
                    generated = initialize_variable(tokens, line)
                    generated_CLanguage += generated[0]

                    # Add the variable to the list of initialized variables
                    initialized_variables[next(iter(generated[1]))] = generated[1][next(iter(generated[1]))]
                except:
                    generated_CLanguage += "// I can't seem to understand this line"

            # line wants to do an if statement (includes 'else if')
            elif intent == 'if' or intent == 'elif' or intent == 'elseif' or intent == 'elsif':
                generated_CLanguage += if_statement(tokens)
            
            # line wants to do an else statment
            elif intent == 'else':
                generated_CLanguage += "}\nelse {\n"

            # line wants to increment or decrement a variable
            elif intent == 'increment' or intent == 'decrement' or intent == 'increase' or intent == 'decrease':
                generated_CLanguage += increment_decrement(tokens, initialized_variables)
            
            # line wants to set a variable to a new value
            elif intent == 'set':
                generated_CLanguage += set_variable(tokens, initialized_variables)

            # line wants to do a for loop
            elif intent == 'for' or intent == 'loop':
                for_response = for_loop(tokens, initialized_variables, line)
                generated_CLanguage += for_response[0]
                inside_for = True
                for_variable = for_response[1]
            
            # line wants to do a while loop
            elif intent == 'while':
                generated_CLanguage += while_loop(tokens)

            # line want to print something
            elif intent == 'print' or intent == 'display' or intent == 'show' or intent == 'log':
                generated_CLanguage += print_statement(tokens, line, initialized_variables, inside_for, for_variable)
            
            # line wants to comment
            elif intent == 'comment' or intent == '//' or intent == '#':
                generated_CLanguage += '// '
                generated_CLanguage += " ".join(line.split(" ")[1:])
                generated_CLanguage += "\n"

            else:
                generated_CLanguage += "// I can't seem to understand this line.\n"

        # Add generated code to base code
        generated_CLanguage = f"#include <stdio.h>\n\nint main(void) {{\n{generated_CLanguage}\nreturn 0;\n}}"

        return generated_CLanguage



        