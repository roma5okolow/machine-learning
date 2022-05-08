import re
with open ("sentences.txt", 'r') as f:
    L = []
    for line in f:
        L.append(re.split('[^a-z]', line.lower()))

COPY = []
for line in L:
    copy = []
    for str in line:
        if (str != ''):
            copy.append(str)
    COPY.append(copy)
L = COPY

words_list = dict()
index = 0
for line in L:
    for word in line:
        if word in words_list.keys():
             continue
        words_list[word] = index
        index += 1

import numpy as np
n = len(L)
m = len(words_list)
words_freq = np.zeros((n, m))

i = 0
for line in L:
    j = 0
    for word in words_list.keys():
        for k in range (0, len(line)):
            if line[k] == word:
                words_freq[i, j] += 1
        j += 1
    i += 1

from scipy.spatial import distance
cos_distance = []
for i in range (1, n):
    dist = distance.cosine(words_freq[0], words_freq[i])
    cos_distance.append(dist)
print(cos_distance)

index_min1 = np.argmin(cos_distance)
print(index_min1)

cos_distance.remove(min(cos_distance))

index_min2 = np.argmin(cos_distance)
print(index_min2)

file_obj = open('submission-1.txt', 'a')
file_obj.write("6 ")
file_obj.write("4")
file_obj.close()