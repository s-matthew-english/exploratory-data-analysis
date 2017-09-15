#data processing
import re
import pprint
#sorting
import operator
from collections import Counter
#visualization rendering
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter



# read in the data
# data = open('toy.json', 'r')
data = open('transactions000000000029.json', 'r')

new_dict = {}

for line in data: 
    identifier = re.search('(\"hash\"\:\s?\"(\w+)\")', line)
    if identifier:
        found_identifier = identifier.group(2)
        # print(found)
    gas = re.search('(\"gas\"\:\s?\"(\w+)\")', line)
    if gas:
        found_gas = gas.group(2)
        # print(found)
    new_dict.update({found_identifier:found_gas})


# make it into tuple
sorted_x = sorted(new_dict.items(), key=operator.itemgetter(1))

# prepare for counter
# flat_list = [x[1] for x in sorted_x if int(x[1]) > 1]
flat_list = [x[1] for x in sorted_x]
# count 'em up
flat_list = Counter(flat_list)

# prune threshold
to_remove = set()
for key, value in flat_list.viewitems():
   if value < 1000:
      to_remove.add(key)
for key in to_remove:
    del flat_list[key]

pprint.pprint(flat_list)



# visualization
c = Counter(flat_list).items()
c.sort(key=itemgetter(1))
labels, values = zip(*c)

indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()





