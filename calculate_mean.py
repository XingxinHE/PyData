import pandas as pd

#set the path



day_int = 14
time_int = 0


while day_int <= 20:
    while time_int <= 23:
        day = str(day_int)
        time = str(time_int)
        fileType = '.tsv'
        file_pre_path = '201712'
        if time_int <= 9:
            file_path = file_pre_path+day+'0'+time+fileType
        else:
            file_path = file_pre_path+day+time+fileType
        

        #read the file
        data = pd.read_csv(file_path, sep = '\t')
        max_val = data.val.mean()
        print('The average value of '+time+ ' on December '+day+' is '+str(max_val)+'.')
        time_int += 1
    time_int = 0
    day_int +=1


#while time_int <= 23:
#    while day_int <= 20:
#        day = str(day_int)
#        time = str(time_int)
#        fileType = '.tsv'
#        file_pre_path = '201712'
#        if time_int <= 9:
#            file_path = file_pre_path+day+'0'+time+fileType
#        else:
#            file_path = file_pre_path+day+time+fileType
#        
#
#        #read the file
#        data = pd.read_csv(file_path, sep = '\t')
#        max_val = data.val.mean()
#        print('The average value of '+time+ ' on December '+day+' is '+str(max_val)+'.')
#        day_int += 1
#    day_int = 14
#    time_int +=1      
