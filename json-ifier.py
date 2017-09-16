import json
import pprint
import collections

with open('toy_two.json', 'rb') as inpt:

    dict_hash_gas = list()
    for line in inpt:
        resource = json.loads(line)
        dict_hash_gas.append({resource['first']:resource['second']})

print(dict_hash_gas)

counts = collections.Counter(v for d in dict_hash_gas for v in d.values())

print(counts)
