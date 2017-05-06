# def hey(text):
#
#     for word in text:
#         if word == '?':
#             return ("Sure.")
#         # if word == '!':
#         #     return ("Whoa, chill out!")
#     if text.isupper():
#         return ("Whoa, chill out!")
#     elif text.isspace() | text.isdigit():
#         return ("Fine. Be that way!")
#     else:
#         return ("Whatever.")
#
# hey(text)
def hey(what):
    sentence = SentenceThinker(what)
    if sentence.is_silence():
        return "Fine. Be that way!"
    elif sentence.is_yelling():
        return "Whoa, chill out!"
    elif sentence.is_question():
        return "Sure."
    else:
        return "Whatever."


class SentenceThinker(object):

    def __init__(self, sentence):
        self.sentence = sentence

    def is_yelling(self):
        return self.sentence == self.sentence.upper()

    def is_question(self):
        return self.sentence.endswith("?")
    # endswith - It returns True if the string ends with the specified suffix,
    # otherwise return False optionally restricting the matching with the given indices start and end.

    def is_silence(self):
        return not self.sentence