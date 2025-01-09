import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #importing libraries
data={'Name':['Ram','Sahil','Shanee','raman','Daman'],'Value':[10,20,30,40,50]} #data for pie chart
df=pd.DataFrame(data,columns=['Name','Value'])  #creating dataframe
plt.pie(df['Value'],autopct='%1.1f%%',startangle=90,shadow=False,explode=(0,0.2,0,0,0),colors=['r','g','b','y','c'],radius=1.5,center=(0,0),frame=True,rotatelabels=True) #plotting pie chart
plt.title('Employee Saving per month')  #title of pie chart
plt.legend(df['Name'],loc='upper right')  #legend of pie chart
plt.show()  #displaying pie chart