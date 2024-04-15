import spacy

nlp = spacy.load("en_core_web_sm")

def is_int(x):
    try:
        int(x)
    except:
        return False
    else:
        return True
    
def is_float(x):
    try:
        float(x)
    except:
        return False
    else:
        return True

def get_format_specifier(x):
    if x == 'int':
        return '%d'
    elif x == 'float':
        return '%f'
    else:
        return '%c'

def process_pseudocode(pseudocode):
    important_stop_words = ["for", "while", "or", "if", "not", "and", "a", "less", "else", "i", 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

    doc = nlp(pseudocode)
    
    filtered_sentence = [token for token in doc if not token.is_stop or token.text in important_stop_words]
    
    return filtered_sentence