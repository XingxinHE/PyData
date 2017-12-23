import pandas as pd

#set the path



day_int = 20
time_int = 10

while time_int <= 17:
    day = str(day_int)
    time = str(time_int)
    fileType = '.tsv'
    file_pre_path = '201712'
    file_path = file_pre_path+day+time+fileType
    
    #read the file
    data = pd.read_csv(file_path, sep = '\t')
    max_val = data.val.max()
    print('The maximum value of '+time+ ' on December '+day+' is '+str(max_val)+'.')
    time_int += 1