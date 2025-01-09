import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.DataFrame({'x':np.random.randint(0, 17, 100),'y':np.random.randint(0, 5, 100)})
plt.scatter(df['x'],df['y'],color='r',marker='o')
plt.show()