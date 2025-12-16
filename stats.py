def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(items):
    return items["num"]

def get_char_count(text):
    #lowercase string
    chars = text.strip().lower()
    # Get dictionary of character counts
    char_count = {}
    for char in chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorted_list_of_dicts(dict):
    dict = [{"char": k, "num": v} for k, v in dict.items()]
    dict.sort(reverse=True, key=sort_on)
    return dict
