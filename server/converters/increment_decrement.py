def increment_decrement(tokens, initialized_variable):
    generated_CLanguage = ""

    if len(tokens) > 2:
        generated_CLanguage += "// You cannot increment or decrement two or more variables in one line!\n"

    if tokens[1].text not in initialized_variable.keys():
        generated_CLanguage += "// Warning: this variable is not initialized\n"

    if tokens[0].text == 'increment' or tokens[0].text == 'increase':
        generated_CLanguage += f"{tokens[1].text}++;\n"
    
    elif tokens[0].text == 'decrement' or tokens[0].text == 'decrease':
        generated_CLanguage += f"{tokens[1].text}--;\n"

    else:
        generated_CLanguage += "// I don't seem to understand this line...\n"

    return generated_CLanguage
