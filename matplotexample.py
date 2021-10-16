import matplotlib.pyplot as plt

import numpy as np




#X is the bottom
#Y is the up and down info

bottom = np.array(['2019', '2020', '2021'])
top = np.array([96,77,83])
width =0.2
plt.xlabel('Per Year')
plt.ylabel('Homicides')
plt.title('Albuquerque,NM Homicide Statistics')
plt.bar(bottom, top, color='red', width=width)
plt.show()
