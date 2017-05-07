# class Hamming(object):
#
#     def __init__(self, list_dna, list_mistake_dna):
#         self.list_dna = list_dna
#         self.list_mistake_dna = list_mistake_dna
#
#     def distance(self):
#         count = 0
#         for dna in self.list_dna:
#             for mistake_dna in self.list_mistake_dna:
#                 if dna != mistake_dna:
#                     count += 1
#         return count
#
# hamming = Hamming()
# hamming.distance()

def distance(list_dna, list_mistake_dna):
    count = 0
    for dna in list_dna:
        for mistake_dna in list_mistake_dna:
            if dna == mistake_dna:
                count += 0
            else:
                count +=1
    return count

