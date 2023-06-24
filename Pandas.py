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
space()

#different ways of creating dataframe
#reading csv file:
#df = pd.read_csv("file_name.csv")

#reading excel file:
#df = pd.read_excel("file_name.xlsx", "sheet1")

#using python dictionary
#weather = {Dictionary}
#df = pd.DataFrame(weather)

#using tuple list
#weather = [(tuple list1), (tuple list2)]
#while creating this you need to provide column names
#df = pd.DataFrame(weather, columns = ["day", "temperature", "wind", "event"])

#using list of dictionaries
#weather = [{Dictionary1}, {Dictionary2}, {Dictionary3}] 
#each dictionary in list represents a row value along with its column name as key
#df = pd.DataFrame(weather)

#https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

#read and write excel csv file
#if we dont have header, we can do this:
df = pd.read_excel("E:\\CODING\\GitHub Repos\\PandasCheatSheet\\Data\\Stock.xlsx", header = None, names = ["Column1", "Column2", "Column3", "Column4", "Column5"])
#the names we passed in list after header = None will be passed as header
print(df)
space()

df = pd.read_excel("E:\\CODING\\GitHub Repos\\PandasCheatSheet\\Data\\Stock.xlsx")
print(df)
#this prints first row and other headers as na, so to fix that we use:
space()

df = pd.read_excel("E:\\CODING\\GitHub Repos\\PandasCheatSheet\\Data\\Stock.xlsx", skiprows= 1) #this means it will skip first row
print(df)
space()

#if we only want to read certain number of rows
df = pd.read_excel("E:\\CODING\\GitHub Repos\\PandasCheatSheet\\Data\\Stock.xlsx", nrows=3)
print(df)
space()

#cleanup data by replacing empty/non-number values
df = pd.read_excel("E:\\CODING\\GitHub Repos\\PandasCheatSheet\\Data\\Stock.xlsx", na_values=["not available", "n.a."])
print(df)
space()

#company revenue cannot be zero, so we need to change it NaN, and in that case even earning per share(eps) will be converted to NaN
#so in that case we use suppy dictionary instead of supplying list
df = pd.read_excel("E:\\CODING\\GitHub Repos\\PandasCheatSheet\\Data\\Stock.xlsx", na_values = {"eps" : ["not available", "n.a."],
                                                                                                "revenue" : ["not available", "n.a.", -1],
                                                                                                "people" : ["not available", "n.a."]
                                                                                                })
print(df)
space()
#its giving en error here, but it runs in replit

#writing back to csv
df.to_excel('E:\\CODING\\Github Repos\\PandasCheatSheet\\Data\\new.xlsx', index=False)#we use index = False to now write index in file

#if we want to write only 2 columns 
print(df.columns)
df.to_excel('E:\\CODING\\Github Repos\\PandasCheatSheet\\Data\\new.xlsx', columns=["tickers", "eps"])

#to skip exporting header
df.to_excel('E:\\CODING\\Github Repos\\PandasCheatSheet\\Data\\new.xlsx', sheet_name= "Sheet1", header=False, index=False)
#we can also specify startrow and startcol

#using converter:
def convert_people(cell):
    if cell == "n.a.":
        return "sam"
    return cell

df = pd.read_excel("E:\\CODING\\GitHub Repos\\PandasCheatSheet\\Data\\Stock.xlsx", "Sheet1", converters={
    'people': convert_people
})
print(df)

#writing to excel file
df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64 ],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})

with pd.ExcelWriter("E:\\CODING\\GitHub Repos\\PandasCheatSheet\\Data\\Write_Excel.xlsx") as writer:
    df_stocks.to_excel(writer,sheet_name='Stocks', index=False) #write stock data sheet
    df_weather.to_excel(writer,sheet_name='Weather', index=False) #write weather data sheet

