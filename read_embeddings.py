import numpy as np
#from PIL import Image as im
import matplotlib.pyplot as plt

embeddings = np.loadtxt("sentences_embeddings.txt").reshape(1000,384)


#16 * 24 = 384
embedding1 = embeddings[762] #Fédération Internationale de Football Association
embedding1 = np.reshape(embedding1, (16,24))

# Normalised [0,255] as integer: don't forget the parenthesis before astype(int)
#normalised = (255*(embedding1 - np.min(embedding1))/np.ptp(embedding1)).astype(int)   
normalised = (embedding1 - np.min(embedding1))/np.ptp(embedding1) 

#data = im.fromarray(normalised)

#data.save("sentence1.jpg")

plt.imshow(normalised)
plt.savefig("sentences1.png")

embedding2 = embeddings[788] #REALMADRID 4 SUREBarcelona is just good those daysi want u 2 b sure that thier days will b over soon!!!!!!!!!
embedding2 = np.reshape(embedding2, (16,24))

normalised = (embedding2 - np.min(embedding2))/np.ptp(embedding2)

plt.imshow(normalised)
plt.savefig("sentences2.png")