import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#set the path
file_path = r'E:\xkoolWorkshop\workshop\people_stream_data\2017121419.tsv'

#read the file
data = pd.read_csv(file_path, sep = '\t')

#subset the data and delete useless info
str_data  = pd.DataFrame(data, columns = ['lng', 'lat', 'val'])

#import seaborn
import seaborn as sns
sns.set()


#construct a new data frame, from long data to matrix
str_new_data = str_data.pivot("lat", "lng", "val")

#set the cell size
f, ax = plt.subplots(figsize=(9, 6))

#plot it
this_heatmap = sns.heatmap(str_new_data)
final = this_heatmap.invert_yaxis()

from pylab import savefig
savefig('111.png')

print('done')

lng_list = data['lng']
dif_lng_num = len( set(lng_list) )