msg_sample=""
with open("Sample_Letter_Frequencies.txt","r") as f:
    data=f.readlines()
#     print(data)
    for d in data:
        print(d)
        print("=========================")
        msg_sample=msg_sample+d

from collections import Counter

import numpy as np
import matplotlib.pyplot as plt

msg_sample=msg_sample.replace(" ","")
c_data = Counter(msg_sample)
print("MESSAE IS : ",msg_sample)
print(c_data)
# c_data=dict(sorted(c_data.items()))
# plt.bar(c.keys(),c.values())

from collections import Counter
a = list(msg_sample)
counts = Counter(a)
# print(counts)
width = 120  # Adjust to desired width
longest_key = max(len(key) for key in counts)
graph_width = width - longest_key - 2
widest = counts.most_common(1)[0][1]
scale = graph_width / float(widest)
# print("Sorted:")
# print(sorted(counts.items(),key=lambda k:(k[1],k[0])))
for key, size in sorted(counts.items(),key=lambda k:(k[1],k[0])):
    print('{}: {}'.format(key, int(size * scale) * '*'))