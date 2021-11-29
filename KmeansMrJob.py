from mrjob.job import MRJob
import re
from math import pow, sqrt

class KMeans(MRJob):
  def distance(self, p1, p2):
    res = 0
    for i in range(len(p1)):
      res += (pow(p1[i]-p2[i]))
    return sqrt(res)
  
  def getCentroids(self):
    self.centroids = []

  def mapper(self, _, line):
    point = []
    for p in line.split(' '):
      point.append(float(p))
    
    temp_dist = 100000
    point_class = 0

    for i in range(len(self.centroids)):
      dist = self.distance(point, self.centroids[i])
      if dist < temp_dist:
        temp_dist = dist
        point_class = i
    yield point_class, point
  def combiner(self, key, values):
    new_centroid = [0 for i in range(len(values[0]))]
    for point in values:
      for idx in range(len(point)):
        new_centroid [idx] += point[idx]
    for idx in range(len(point)):
      new_centroid [idx] = new_centroid [idx]/len(values)
    yield key, tuple(new_centroid)
  
  def reducer(self, key, values):
    new_centroid = [0 for i in range(len(values[0]))]
    for point in values:
      for idx in range(len(point)):
        new_centroid [idx] += point[idx]

    centroid_string = str(key)

    for idx in range(len(point)):
      new_centroid [idx] = new_centroid [idx]/len(values)
      centroid_string = centroid_string + "," + new_centroid [idx]
    
    yield (None, centroid_string)
