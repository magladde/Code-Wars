def DNA_strand(dna):
    complimentary_strand = ''
    for i in range(len(dna)):
        if dna[i] == 'T':
            complimentary_strand += 'A'
        elif dna[i] == 'A':
            complimentary_strand += 'T'
        elif dna[i] == 'G':
            complimentary_strand += 'C'
        elif dna[i] == 'C':
            complimentary_strand += 'G'
    return complimentary_strand

result = DNA_strand("ATTGC")
print(result)