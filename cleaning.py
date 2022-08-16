import pandas as pd

#importing all the data files
c_data_1 = pd.read_csv(r"D:\Google Data Analytics\capstone\Data\202108-divvy-tripdata.csv")
c_data_2 = pd.read_csv(r"D:\Google Data Analytics\capstone\Data\202109-divvy-tripdata.csv")
c_data_3 = pd.read_csv(r"D:\Google Data Analytics\capstone\Data\202110-divvy-tripdata.csv")
c_data_4 = pd.read_csv(r"D:\Google Data Analytics\capstone\Data\202111-divvy-tripdata.csv")
c_data_5 = pd.read_csv(r"D:\Google Data Analytics\capstone\Data\202112-divvy-tripdata.csv")
c_data_6 = pd.read_csv(r"D:\Google Data Analytics\capstone\Data\202201-divvy-tripdata.csv")
c_data_7 = pd.read_csv(r"D:\Google Data Analytics\capstone\Data\202202-divvy-tripdata.csv")
c_data_8 = pd.read_csv(r"D:\Google Data Analytics\capstone\Data\202203-divvy-tripdata.csv")
c_data_9 = pd.read_csv(r"D:\Google Data Analytics\capstone\Data\202204-divvy-tripdata.csv")
c_data_10 = pd.read_csv(r"D:\Google Data Analytics\capstone\Data\202205-divvy-tripdata.csv")
c_data_11 = pd.read_csv(r"D:\Google Data Analytics\capstone\Data\202206-divvy-tripdata.csv")
c_data_12 = pd.read_csv(r"D:\Google Data Analytics\capstone\Data\202207-divvy-tripdata.csv")

#merging the data into a single dataframe later we can export this file as csv to import into Tableau 
c_data_final = pd.concat([c_data_1, c_data_2, c_data_3,c_data_4,c_data_5,c_data_6,c_data_7,c_data_8,c_data_9,c_data_10,c_data_11,c_data_12])


#counting the null values in the data frames
#We chcek the 'ride_id', 'member_casual' columns for blank or null values.
#as most of our analysis will be dependent on these columns
c_data_2['User Type'].isna().sum()
c_data_2['User Type'].isnull().sum()
c_data_2.isna().sum().sum()


c_data_final.info()
c_data_final.head()


#converting the data type of start_time, end_time to date time
c_data_final['started_at'] = pd.to_datetime(c_data_final['started_at'])
c_data_final['ended_at'] = pd.to_datetime(c_data_final['ended_at'])

#checking for duplicates in ride_id
dups = c_data_final.pivot_table(index = 'ride_id', aggfunc = 'size')
dups = dups.to_frame()
dups.columns = ['Size']
dups.info()
print(dups[dups['Size']>1])
#no duplicates found 


#exporting the data as a csv file
c_data_final.to_csv(r"D:\Google Data Analytics\capstone\data_final.csv")

#Rest all the calculations are done in Tableau
