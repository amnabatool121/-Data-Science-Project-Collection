import pandas as pd
dataset_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"
df=pd.read_csv(dataset_url)
print(df.head())
print("Number of rows in the dataset:", len(df))
print("Number of columns in the dataset:", len(df.columns))
print(df.dtypes)
mean_age=df['Age'].mean()
print("Mean age of the survey participants:", mean_age)
unique_countries = df['Country'].nunique()
print("Number of unique countries in the dataset:", unique_countries)
