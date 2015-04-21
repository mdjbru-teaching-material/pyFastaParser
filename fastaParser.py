### * Description

# Functions to parse fasta sequences from a file
#
# Example:
# f = "test-seqs.fasta"
# seqParser = parseFasta(f)
# for seq in seqParser :
#     print(seq)
#     print(countATGC(seq))

### * Functions

### ** seqParser(fileName)

def seqParser(fileName) :

    with open(fileName, "r") as fi :
        seqName = ""
        seqSeq = ""
        for line in fi :
            line = line.strip()
            if line != "" :
                if line.startswith(">") :
                    seqName = line[1:]
                else :
                    seqSeq = line
                    yield([seqName, seqSeq])
                    seqName = ""
                    seqSeq = ""

### ** countATGC(seq)

def countATGC(seq) :

    sequence = seq[1]
    nA = sequence.count("A")
    nG = sequence.count("G")
    nT = sequence.count("T")
    nC = seqeunce.count("C")
    return(nA, nT, nG, nC)

