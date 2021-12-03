import numpy as np

def bits_to_int(bits):
    return bits.dot(1 << np.arange(len(bits))[::-1])

data = np.genfromtxt('day03.txt', delimiter=1, dtype=int)

gamma = bits_to_int(2*np.sum(data, axis=0) > data.shape[0])
epsilon = gamma ^ (2**data.shape[1] - 1)
print(epsilon * gamma)

o2 = co2 = data
for i in range(data.shape[1]):
    if o2.shape[0] > 1:
        o2_bit = 2*np.sum(o2[:, i]) >= o2.shape[0]
        o2 = o2[o2[:, i] == o2_bit]
    if co2.shape[0] > 1:
        co2_bit = 2*np.sum(co2[:, i]) < co2.shape[0]
        co2 = co2[co2[:, i] == co2_bit]
print(bits_to_int(o2[0]) * bits_to_int(co2[0]))
