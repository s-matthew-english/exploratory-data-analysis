import json
import pprint
import collections
import itertools
import matplotlib.pyplot as plt
import numpy as np

with open('transactions000000000029.json', 'rb') as inpt:
# with open('toy_two.json', 'rb') as inpt:

    dict_hash_gas = list()
    for line in inpt:
        resource = json.loads(line)
        dict_hash_gas.append({resource['hash']:resource['gas']})
        # it would be interesting to include also gasUsed in a 
        # souble barchart
        # dict_hash_gas.append({resource['hash']:resource['gasUsed']})
        # dict_hash_gas.append({resource['first']:resource['second']})

# Count up the values
counts = collections.Counter(v for d in dict_hash_gas for v in d.values())

counts = counts.most_common()

# Apply a threshold
threshold = 1000
counts = [list(group) for val, group in itertools.groupby(counts, lambda x: x[1] > threshold) if val]

# print(counts)

# resort the list by the magnitude of the manifest values
# as opposed to the frequency 
counts[0].sort(key=lambda x:int(x[0]))

# print(counts)


# VISUALIZATION

# Transpose the data to get the x and y values
labels, values = zip(*counts[0])

# generates this representation: [0 1 2 3 4 5 6 7], 
# from the number of the length
indexes = np.arange(len(labels))
width = 1

# specify height
# plt.ylim(0, 109000)
plt.xlabel("amount of gas specified")
plt.ylabel("number of transactions")

plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()

