from classes.Vocabulary import Vocabulary
import sys
voc_path = sys.argv[1]
voc = Vocabulary()
with open(voc_path,"r") as f:
    for line in f:
        line=line[:-1]
        voc.append(line)
voc.create_binary_representation()
voc.save(sys.argv[2])
