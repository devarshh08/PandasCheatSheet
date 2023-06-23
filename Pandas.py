def space():
    print(" ")
    print(" ")

import pandas as pd

#dataframe is a main object in pandas which is used to present data with rows and columns(tabular or excel spreadsheet like data)

df = pd.read_csv("E:\\CODING\\GitHub Repos\\PandasCheatSheet\\Data\\DATAAAAA.csv")
print(df)

#reading dataframe from dictionary
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}
df = pd.DataFrame(weather_data)
print(df)
space()

#printing rows and columns 
rows, columns = df.shape #shape means the dimensions
print(f"Rows : {rows}")
print(f"Columns : {columns}")
space()

print(df.shape)
space()

#df.head gives convenience of printing few rows from top
print(df.head(2))
space()

#df.tail prints rows from bottom
print(df.tail(3))
space()

#slicing:
#printing row
print(df[2:5]) #non-inclusive of last index
space()

#printing column
print(df.columns) #this will print no. of columns
space()

#to print a specific column:
print(df.event)
space()

#or can specify this was
print(df['event'])
space()

#to print multiple columns
print(df[['event', 'day']])
space()

#type:
print(type(df['event']))
space()

#some operations with dataframe
#finding max of int
print(df.temperature.max())
space()

#can also perform other operations such as min, mean, std : standard deviation
print(df.temperature.min())
space()

print(df.temperature.mean())
space()

print(df.temperature.std())
space()

#can also use df.describe which will print the statistics on data set, it prints statistics of integer type columns
print(df.describe())
space()

#how to conditionally select data in dataframe
print(df[df.temperature >= 32])
space()

print(df[df.temperature == df.temperature.max()])
space()

#set index
#pandas assigns index to dataframe automatically

print(df.index)
space()
#upon running this you can see the index range

#to change this to something else
df.set_index('day', inplace = True)
print(df)
space()

#this gives advantage that we can run loc function
print(df.loc['1/4/2017'])
space()

#to reset index to original:
df.reset_index(inplace = True)
print(df)

