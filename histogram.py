import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.DataFrame({'x':np.random.randint(0, 10, 100)})  # 100 random integers between 0 and 9  
plt.hist(df['x'],color='g',bins=10)  # 10 bins for 10 integers between 0 and 10
plt.legend(['x'])  # Legend
plt.xticks(np.arange(0, 10, step=1))  # x-axis ticks
plt.grid(axis='y', alpha=0.75)  # Grid lines
plt.xlabel('x')
plt.ylabel('Frequency') # Frequency of each integer
plt.title('Histogram')  # Title of the histogram
plt.show()