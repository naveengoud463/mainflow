import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
data = pd.read_csv('C:\\Users\\nagap\\OneDrive\\Documents\\customers.csv')
display(data.head(10))
#Scatter pllot with year aganist own
plt.scatter(data['year'],data['own']
            #adding title to the plot
            plt.title("Scatter Plot")
            #Setting the x snd Y Labels
            plt.xlabel('year')
            plt.ylabel('own')
            #Showing the result
            plt.show()
#Line chart with year aganist own
            plt.plot(data['year'])
            plt.plot(data['own'])
            #adding title to the plot
            plt.title("Line Chart")
            #Setting the x and y Labels
            plt.xlabel('year')
            plt.ylabel('own')