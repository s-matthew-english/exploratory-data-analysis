import json
import pprint
import collections
import itertools

with open('transactions000000000029.json', 'rb') as inpt:
# with open('toy_two.json', 'rb') as inpt:

    dict_hash_gas = list()
    for line in inpt:
        resource = json.loads(line)
        dict_hash_gas.append({resource['hash']:resource['gas']})
        # dict_hash_gas.append({resource['first']:resource['second']})

# Count up the values
counts = collections.Counter(v for d in dict_hash_gas for v in d.values())

counts = counts.most_common()

# Apply a threshold
threshold = 4275
counts = [list(group) for val, group in itertools.groupby(counts, lambda x: x[1] > threshold) if val]

print(counts)
