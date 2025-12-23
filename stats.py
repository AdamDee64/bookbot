def text_to_string(path):
    with open(path) as f:
        return f.read()

def count_words(str):
    return len(str.split())
    
def count_characters(str):
    dict = {}
    for char in str:
        c = char.lower()
        if c not in dict:
            dict[c] = 0
        dict[c] += 1
    return dict
        
def sort_on(items):
    return items["num"]

def sort_high_to_low(dict):
    sorted_list_of_dict = []
    for key, val in dict.items():
        if key.isalpha():
            char_dict = {"char":key, "num":val}
            sorted_list_of_dict.append(char_dict)
    
    sorted_list_of_dict.sort(reverse=True, key=sort_on)
    return sorted_list_of_dict
    
