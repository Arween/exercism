def word_count(words):
    # words = words.match(r'^a-zA-Z_')
    # print(words)
    my_words = words.lower().split()
    # print(len(my_words))
    if len(my_words) > 1:
        my_words = my_words.filter(r'a-zA-Z_')
    my_dict = {}
    for item in my_words:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1
    print(my_dict)
    return (my_dict)

word_count('car : carpet as java : javascript!!&@$%^&')

import re

# text = 'car : carpet as java : javascript!!&@$%^&'
# new_text = ''
# for t in text:
#     print(re.match(r'/w', t))
#     if re.match(r'/W', t):
#         del(t)
#         print(333)
#     else:
#         print(779879)
#         new_text += t
# print(new_text)

result = re.match(r'/w', 'AV Analytics Vidhya AV')
print(result)