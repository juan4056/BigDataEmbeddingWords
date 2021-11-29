from sentence_transformers import SentenceTransformer
import numpy as np
import time
model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = []
line = "sadasdada"
with open('clean.txt') as file:
    while line:
        line = file.readline()
        if len(line) > 1:
            parser = line[line.index(',')+1:-1]
            if len(parser) > 2:
                sentences.append(parser)



time_ = time.time()
sentence_embeddings = model.encode(sentences)
time_ = time.time() - time_
maxlen = 0
print(len(sentences))
with open('1Msentences_embeddings.txt', 'a') as the_file:

    for sentence, embedding in zip(sentences, sentence_embeddings):
        #print("Sentence:", sentence)
        #print("Embedding:", embedding)
        #print("size-embedding:", len(embedding))
        #print("")
        if(maxlen < len(embedding)):
            maxlen = len(embedding)
        np.savetxt(the_file, embedding)

print(time_)