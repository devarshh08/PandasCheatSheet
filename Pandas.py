import pandas as pd

#loading data in csv format

df = pd.read_csv("E:\\CODING\\GitHub Repos\\PandasCheatSheet\\survey_results_public.csv")

print(df)

print(df.shape)

print(df.info)

print(df.info())

#to see 85 columns
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
print(df)


schema_df = pd.read_csv("E:\\CODING\\GitHub Repos\\PandasCheatSheet\\survey_results_schema.csv")
print(schema_df)

