def word_count(words):
    my_words = words.lower().split()
    result_words = my_words.match(r'^a-zA-Z_')
    my_dict = {}
    for item in result_words:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1
    return (my_dict)
