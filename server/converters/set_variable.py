def set_variable(tokens, initialized_variable):
    variable_not_initialized = False

    variable_name = tokens[1].text
    generated_CLanguage = ""

    if variable_name not in initialized_variable.keys():
        variable_not_initialized = True

    for token in tokens[2:]:
        if token.text == 'set' or token.text == 'equal' or token.text == 'equals':
            continue
        if token.text == 'plus' or token.text == '+':
            generated_CLanguage += " + "
        elif token.text == 'minus' or token.text == '-' or token.text == 'subtract' or token.text == 'subtracted':
            generated_CLanguage += " - "
        elif token.text == 'divided' or token.text == '/' or token.text == 'divide':
            generated_CLanguage += " / "
        elif token.text == 'times' or token.text == '*' or token.text == 'multiply' or token.text == 'multiplied':
            generated_CLanguage += " * "
        elif token.text == 'modulo' or token.text == '%':
            generated_CLanguage += " % "
        else:
            generated_CLanguage += token.text

    if variable_not_initialized:
        generated_CLanguage = f"// Warning: this variable is not initialized\n{variable_name} = {generated_CLanguage};\n"
    else:
        generated_CLanguage = f"{variable_name} = {generated_CLanguage};\n"

    return generated_CLanguage