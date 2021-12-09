from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.cluster import KMeans
import os

directory = 'quora'
model = SentenceTransformer('all-MiniLM-L6-v2')

clases = {}

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    print(f)
    key = f[13:-4]
    sentences = []
    with open(f) as file:
        line = file.readline()
        while line:
            parser = line[line.index(',')+1:-1]
            sentences.append(parser)
            line = file.readline()
    clases[key] = sentences

embeddings = {}
to_cluster = []
for key in clases:
    print("---------------------------")
    print(key)
    print(len(clases[key]))
    sentence_embeddings = model.encode(clases[key])
    embeddings[key] = sentence_embeddings
    with open('quora/embeddings.csv', 'a') as file:
        for sentence, embedding in zip(clases[key], sentence_embeddings):
            file.write(key+'|'+sentence+'|')
            to_cluster.append(embedding)
            for i, value in enumerate(embedding):
                if i+1 == len(embedding):
                    file.write(str(value)+'\n')
                else:
                    file.write(str(value)+'|')

array_np = np.array(to_cluster)

kmeans = KMeans(n_clusters=3).fit(array_np)
counter = {}
for i in kmeans.labels_:
    if i in counter:
        counter[i]+=1
    else:
        counter[i] = 1
print("CLUSTERING RESULTS: ")
print(counter)
print(kmeans.labels_)
    #sentences = []
    #if os.path.isfile(f+'/data.txt'):
    #    with open(f+'/data.txt') as file:
    #        line = file.readline()
    #        while line:
    #            parser = line[line.index(',')+1:-1]
    #            sentences.append(parser)
    #            line = file.readline()
#
    #sentence_embeddings = model.encode(sentences)
    #with open(f+'/embeddings.txt', 'w') as the_file:
    #    for sentence, embedding in zip(sentences, sentence_embeddings):
    #        np.savetxt(the_file, embedding)
#
    #with open(f+'/embeddings.csv', 'w') as the_file:
    #    for sentence, embedding in zip(sentences, sentence_embeddings):
    #        the_file.write(sentence+'|')
    #        for i, value in enumerate(embedding):
    #            if i+1 == len(embedding):
    #                the_file.write(str(value)+'\n')
    #            else:
    #                the_file.write(str(value)+'|')
