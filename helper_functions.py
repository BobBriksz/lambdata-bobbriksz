import pandas as pd
import numpy as np 



# class MyDataFrame(pd.DataFrame):
#     """custom methods on pd.dataframe class"""
#         def num_cells(self):
#                 return self.shape[0] * self.shape[1]
        
#         def null_count(self):
#                 missing = self.isnull().sum()
#                 return "There are " + missing + " values in your dataframe"
        
        



def train_test_split(df, frac):
    """"Train_test_split of data frame """""
#    TODO -implement train test split

    arr_rand = np.random.rand(df.shape[0])  #randomly arrange the rows on the index of the data frame
    split = arr_rand < np.percentile(arr_rand, (frac*100))   #create a percentile cutoff for the split
    df_test = df[split]  #upper half of the split
    df_train = df[~split]  #lower half of split
    return df_test, df_train


def null_count(df):
    #TODO - run a null count of the dataframe
     missing = df.isnull().sum()
     return "There are "+ missing + "values in your dataframe"

def df_summary (df,upper=False):
     nrows = df.shape[0]
     ncolumns= df.shape[1]
     missing = df.isnull().sum()
  #converting to nested dictionary for cleaner output
     if(upper==False):
             labels= list(df.columns)
     else:
             labels = [x.upper() for x in df.columns]
     dict = {
             'nrows':nrows,
             'ncolumns':ncolumns,
             'missing':missing,
             'labels':labels
  }
     for k,v in dict.items():
            print(k)
            print(v)    