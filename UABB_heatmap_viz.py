import matplotlib.pyplot as plt
import pandas as pd

#import seaborn
import seaborn as sns

day_int = 20
time_int = 0


while time_int <= 9:
    #set the path
    day = str(day_int)
    time = str(time_int)
    fileType = '.tsv'
    file_pre_path = '201712'
    file_path = file_pre_path+day+'0'+time+fileType
    
    #read the file
    data = pd.read_csv(file_path, sep = '\t')

    #subset the data and delete useless info
    str_data  = pd.DataFrame(data, columns = ['lng', 'lat', 'val'])


    sns.set()


    #construct a new data frame, from long data to matrix
    str_new_data = str_data.pivot("lat", "lng", "val")

    #set the cell size
    f, ax = plt.subplots(figsize=(9, 6))
    f.set_size_inches(16.5, 11.7)

    #plot it
    this_heatmap = sns.heatmap(str_new_data)
    final = this_heatmap.invert_yaxis()

    from pylab import savefig

    png_path = '12'+day+'0'+time+'.png'

    savefig(png_path, dpi = 300)
    
    time_int += 1
