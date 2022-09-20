import numpy as np
import matplotlib.pyplot as plt
a=np.load("Data/Mask/2005.npy")
plt.imshow(a,'gray',origin='lower')
plt.show()
