import pandas as pd
import os
class datacollection():
    def __init__(self):
        pass
    def data_collection(Self):
        df=pd.read_csv(r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\Telecom_Customers_Churn.csv')
        df
        os.makedirs(r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\data\raw_Data',exist_ok=True)
        df.to_csv(r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\data\raw_Data\raw.csv',index=False)


if __name__=='__main__':
    try:
        obj=datacollection()
        obj.data_collection()
    except Exception as e:
        raise e

