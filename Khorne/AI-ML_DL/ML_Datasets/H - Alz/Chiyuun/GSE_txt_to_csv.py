import pandas as pd

read_file = pd.read_fwf (r'D:\Dinesh\GSE33000_raw_data.txt')
read_file.to_csv (r'D:\Dinesh\GSE33000_raw_data.csv', index=None)
