import matplotlib.pyplot as plt
import numpy as np

I = np.array([[0, 255], [1, 0]])

plt.imshow(I, vmin=0, vmax=255)
plt.show()