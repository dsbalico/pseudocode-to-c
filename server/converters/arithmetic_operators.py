# add 10 to x

def arithmetic_operators(tokens, initialized_variables):
    generated_CLanguage = ""
    variable = []
    intent = tokens[0].text.lower()

    for i in range(1, len(tokens)):
        if tokens[i].pos_ == 'NUM' or tokens[i].is_digit:
            continue
        
        variable.append(tokens[i].text)

    for var in variable:
        if var not in initialized_variables.keys():
            generated_CLanguage += f"// Warning: {var} is not initalized.\n"

    if tokens[2].is_digit:
        generated_CLanguage = "// There's something wrong in this line"
        return generated_CLanguage

    if intent == 'add':
        generated_CLanguage += f"{tokens[2]} = {tokens[2]} + {tokens[1]};\n"
    elif intent == 'subtract':
        generated_CLanguage += f"{tokens[2]} = {tokens[2]} - {tokens[1]};\n"
    elif intent == 'multiply':
        generated_CLanguage += f"{tokens[2]} = {tokens[1]} * {tokens[2]};\n"
    elif intent == 'divide':
        generated_CLanguage += f"{tokens[2]} = {tokens[1]} / {tokens[2]};\n"
    elif intent == 'modulo':
        generated_CLanguage += f"{tokens[2]} = {tokens[2]} % {tokens[1]};\n"
    else:
        generated_CLanguage += "// I can't seem to understand this line.\n"
    
    return generated_CLanguage