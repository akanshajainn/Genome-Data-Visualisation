#Importing required packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Importing Data
data=pd.read_csv('Assignment1_gene_data-2.csv',index_col=0)
meta=pd.read_csv('Assignment1_Meta-2.csv')

#Reviewing data
data.head()

#Reviewing data
meta.head()

#Dropping Unit Column since it is of no use, setting index sample ID's and renaming it to 'sample'
meta=meta.drop(['Unit'],axis=1)
meta.set_index(['sIdx'],inplace=True)
meta.index.name='sample'
meta

#Extracting mentioned genes for the problem; Lgals4 and Kif2c
gene1=data.loc[data['symbol'] == 'Lgals4']
gene2=data.loc[data['symbol'] == 'Kif2c']
display(gene1)
display(gene2)

#Converting the data for gene1 into column, removing unwanted row and setting index as 'sample' which is same for meta data
gene1=gene1.transpose()
gene1=gene1.drop(gene1.index[0])
gene1.index.name='sample'
gene1.columns=['Lgals4']
gene1

#Converting the data for gene2 into column, removing unwanted row and setting index as 'sample' which is same for meta data
gene2=gene2.transpose()
gene2=gene2.drop(gene2.index[0])
gene2.index.name='sample'
gene2.columns=['Kif2c']
gene2

#Combining all the dataframes into one single dataset for visualisation
data=pd.concat([meta['Time'],gene1['Lgals4'],gene2['Kif2c']],axis=1)
data

data.index

#Scatter Plot
plt.figure(1)
fig,ax= plt.subplots(2,sharex=True)
ax[0].scatter(data['Time'],data['Lgals4'],color='r')
ax[0].set_title('Lgals4')
ax[1].scatter(data['Time'],data['Kif2c'], color='b')
ax[1].set_title('Kif2c')
plt.xlabel('Time', fontsize=20)
plt.ylabel('Signal Intensity',fontsize=10)
fig

#To clear the plots
plt.gcf().clear()

#Box Plot
plt.figure(2)
x=data['Time'].astype(np.float)
y=data['Lgals4'].astype(np.float)
z=data['Kif2c'].astype(np.float)
sns.boxplot(x=x, y=y, data=data)
plt.show()
sns.boxplot(x=x,y=z,data=data)
plt.show()