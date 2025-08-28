import pandas as pd
import glob

path = 'input_files/*.csv'
#look inside the input_files folder and
# find any file with csv

all_files = glob.glob(path)
#returns a LIST with all the files in form of their path
#all_files will look like: 
#['input_files\\sales_january.csv', 'input_files\\sales_february.csv', ...]

for f in all_files:
    print(f)
#prints everything to make sure its working
 

li = []
#To put the Dataframes inside

for filename in all_files:
#looping through the LIST of all_files so pandas can read every one.
#the 'filename' variable will hold the path to one CSV file

    df = pd.read_csv(filename, index_col=None, header=0)
    #pd.read_csv() reads our file, converts it into a DataFrame
    # 'filename' -> The path to the file to read.
    # 'header=0' -> This tells pandas that the first row (index 0) 
    # of the CSV contains the column names.
    # 'index_col=None' -> This tells pandas not to use 
    # any of the columns from the CSV as the row index.
    #Instead, pandas will generate a default numerical index
    #  (0, 1, 2, ...)

    li.append(df)
    #The .append() method adds the newly created DataFrame 
    # ('df') to our container list ('li')

master_frame = pd.concat(li, axis=0, ignore_index=True)
#pd.concat() is the primary function for combining DataFrames.
#'li' -> The list of DataFrame objects to be combined.
#'axis=0' -> This specifies the direction of the concatenation. 
# axis=0 means we stack them vertically (on top of each other), 
# appending rows. This makes the final table taller.
# 'ignore_index=True' -> This is a crucial argument for clean data. 
# It tells pandas to discard the original indexes from the individual 
# files and generate a new, continuous index (0, 1, 2, 3...) 
# for the final, combined DataFrame.
print(master_frame)
#preview of the final report to save

master_frame.to_csv('master_report.csv', index=False, sep=';')
# The .to_csv() method is used to save a DataFrame to a CSV file.
# 'master_report.csv' -> This is the name of the output file 
# that will be created.
# 'index=False' -> This is an important command that
#prevents pandas from writing the DataFrame's index
# (the row numbers 0, 1, 2, 3...) as an extra column in the CSV file.
#sep=';' -> This is just so excel doesn't dump everything in one column