import random 
import matplotlib.pyplot as plt
import numpy as np

'''
a = [1,2,3,4]
b = [5,6,7,8]
np_a = np.array(a)
np_b = np.array(b)
n2_d = np.array([a,b])
print(n2_d)
print(n2_d[:,0:3])
print(n2_d.shape)
print(a.index(2))

print(np.extract(np_a == 1, np_b))
'''
life_exp = [random.sample(range(100), 20)]
print(life_exp)
plt.hist(life_exp, 20)
plt.show()
