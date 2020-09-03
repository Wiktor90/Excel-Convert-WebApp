from django.db import models
import pandas as pd
import numpy as np
import math

# Create your models here.
class Excel(models.Model):
    country = models.CharField(default= "", max_length = 20)
    file = models.FileField(upload_to ='excel')
    corrected = models.BooleanField(default=False) # pandas correction status
    file_end = models.BooleanField(default=False) # format checker
    file_content = models.BooleanField(default=False) # df required columns checker


    def __str__(self):
        return self.file.name
    

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)


    def save_excel(self, dataframe):
         excelWriter = pd.ExcelWriter(self.file.path)
         dataframe.to_excel(excelWriter, index=False)
         excelWriter.save()

    def odo(self):
        #cleaning df
        df = pd.read_excel(self.file.path)
        df.loc[:,"ODOMETER_FW"] = df.loc[:,"ODOMETER_FW"].fillna(0).astype('int')
        df.dropna(inplace = True)
        df.sort_values(by=['VEHICLE_ID_FW','TRANSACTION_DATE_FW','TRANSACTION_TIME_FW'], ascending=[True,False,False],inplace=True)
        df['ODOMETER_FW'] = df['ODOMETER_FW'].apply(lambda x: 0 if x <1000 else x)
        df.set_index(['VEHICLE_ID_FW'], inplace=True)
        
        #create of unique Vehicle IDs list
        ids = df.index.unique().tolist()

        #create new df to store corrected data from dawnloaded df
        df_corrected = pd.DataFrame()

        #odo correction and storing data in df_corrected
        for i in ids:
            temp_df = df.loc[i]
            odo = df.loc[i,"ODOMETER_FW"].tolist()
            
            if type(odo) == list:
                odo.sort(reverse=True)
            
                for j in range(len(odo)-1):
                    if abs(odo[j] - odo[j+1]) > 9999 or odo[j] - odo[j+1] < 0:
                        odo[j+1] = 0
                    
                temp_df.loc[:,"ODOMETER_FW"] = odo #temp_df["ODOMETER_FW"] = odo
                df_corrected = df_corrected.append(temp_df)
        
            else:
                df_corrected = df_corrected.append(temp_df)
                
        df_corrected.reset_index(inplace=True)
        df_corrected.rename(columns = {'index':'VEHICLE_ID_FW'}, inplace = True)
        return df


    def format_check(self): # file format check
        if self.file.name.lower().endswith(('.xlsx', '.xls', '.csv')):
            self.file_end = True
            return self.file_end
        else:
            return self.file_end


    def columns_check(self): # columns check
        df = pd.read_excel(self.file.path)
        cols_in_files = [col for col in df.columns]
        mandatory_cols = ['TRANSACTION_DATE_FW','TRANSACTION_TIME_FW','VEHICLE_ID_FW','ODOMETER_FW']
        for col in mandatory_cols:
            if col in cols_in_files:
                pass
            else:
                self.file_content = False
                return self.file_content        
        self.file_content = True
        return self.file_content