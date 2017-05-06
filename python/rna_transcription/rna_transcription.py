# G -> C
# C -> G
# T -> A
# A -> U

def to_rna(dna):
    rna = ''
    for letter in dna:
        if letter != 'G' and letter != 'C' and letter != 'T' and letter != 'T':
            return ('')
        elif letter == 'G':
            letter = 'C'
        elif letter == 'C':
            letter = 'G'
        elif letter == 'T':
            letter = 'A'
        elif letter == 'A':
            letter = 'U'
        rna += letter
    return (rna)

