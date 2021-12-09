import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

directory = 'clases'

embeddings_map = {}

dataset = []
inertia_original = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    
    if os.path.isfile(f+'/embeddings.txt'):
        print(f)
        embeddings = np.loadtxt(f+'/embeddings.txt').reshape(10,384)
        embeddings_map[f] = embeddings
        centroid = np.mean(embeddings, axis = 0)
        inertia_original += np.sum(np.sqrt(np.sum((embeddings-centroid)**2, axis = 1)))


for key in embeddings_map:
    print(key)
    print(embeddings_map[key].shape)
    for i in embeddings_map[key]:
        dataset.append(i)
dataset_to = np.array(dataset)

#print(dataset_to[:10, :].shape)
#print(np.mean(dataset_to[:10, :], axis = 0).shape)



kmeans = KMeans(n_clusters=5).fit(dataset_to)
print(kmeans.labels_)
clustered_sentences = [[] for i in range(5)]
for sentence_id, cluster_id in enumerate(kmeans.labels_):
    #print(category[sentence_id])
    #print(sentence_id)
    clustered_sentences[cluster_id].append(sentence_id)
    #if 
print(kmeans.inertia_)
print(inertia_original)
    #for i, cluster in enumerate(clustered_sentences):
    #    print("Cluster ", i)
    #    print(cluster)
    #    print("")