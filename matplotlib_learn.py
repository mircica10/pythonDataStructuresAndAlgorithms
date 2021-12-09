import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np

plt.style.use('seaborn-whitegrid')


x = np.linspace(0, 10, 100)

"""
# 1
fig= plt.figure()

plt.subplot(2,1,1)
plt.plot(x, np.sin(x), '-')

plt.subplot(2,1,2)
plt.plot(x, np.cos(x), '--')

plt.show()
"""

# 2
"""
fix, ax = plt.subplots(2)

ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))

plt.show()

"""

# 3

"""

plt.plot(x, np.sin(x), color = 'blue')
plt.plot(x, np.sin(x - 1), color = 'g')
plt.plot(x, np.sin(x - 2), color= '0.7')
plt.show()

"""

#4 

plt.plot(x, np.sin(x), linestyle='dashed', color = 'red')
plt.plot(x, np.sin(x - 1), linestyle = 'solid')
plt.plot(x, np.sin(x - 2), linestyle = 'dashdot')

plt.show()