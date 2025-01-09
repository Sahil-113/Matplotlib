import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.DataFrame({'Ram': np.random.randint(0, 10, 10),'Shyam': np.random.randint(0, 30, 10),'hurry': np.random.randint(0, 25, 10)})
data.index = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct']
data.plot(kind='line')
plt.show()