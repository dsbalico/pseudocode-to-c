def while_loop(tokens):
    generated_CLanguage = "while("
    condition_closed = False

    currentIndex = 0

    while(currentIndex < len(tokens)):
        token_text = tokens[currentIndex].text.lower()

        if token_text == 'while':
            currentIndex += 1
            continue
        
        elif tokens[currentIndex].pos_ == 'SPACE':
            generated_CLanguage += '_'

        elif token_text == 'not' and tokens[currentIndex+1].text.lower() ==  'equal':
            generated_CLanguage += " != "
            currentIndex += 1
            
        elif token_text == 'greater' and tokens[currentIndex+1].text.lower() != "or":
            generated_CLanguage += " > "
            
        elif token_text == 'less' and tokens[currentIndex+1].text.lower() != "or":
            generated_CLanguage += " < "
            
        elif token_text == 'greater' and tokens[currentIndex+1].text.lower() == "or" and tokens[currentIndex+2].text.lower() == 'equal':
            generated_CLanguage += " >= "
            currentIndex += 2
            
        elif token_text == 'less' and tokens[currentIndex+1].text.lower() == "or" and tokens[currentIndex+2].text.lower() == 'equal':
            generated_CLanguage += " <= "
            currentIndex += 2
        
        elif token_text == 'or' or token_text == '||':
            generated_CLanguage += " || "
        
        elif token_text == 'and':
            generated_CLanguage += " && "
            
        elif token_text == ':':
            generated_CLanguage += ") {\n"
            condition_closed = True
            
        elif token_text == 'equal' or token_text == 'equals':
            generated_CLanguage += ' == '
            
        else:
            generated_CLanguage += token_text
            
        currentIndex += 1

    if condition_closed != True:
        generated_CLanguage += ") {\n"

    return generated_CLanguage

