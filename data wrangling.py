import pandas as pd
file = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"
df = pd.read_csv(file)
duplicates=df.duplicated()
print(duplicates)
drop_duplicates=df.drop_duplicates(inplace=True)
print(drop_duplicates)
missing_values = df.isnull().sum()
print(missing_values)
missing_workloc = df['WorkLoc'].isna().sum()
print(missing_workloc)
workloc_value_counts = df['WorkLoc'].value_counts()
print(workloc_value_counts)
majority_workloc = workloc_value_counts.idxmax()
print(majority_workloc)
df['WorkLoc'].fillna(majority_workloc, inplace=True)
missing_workloc_after = df['WorkLoc'].isna().sum()
print("Number of missing rows in the 'WorkLoc' column after imputation:", missing_workloc_after)
compfreq_categories = df['CompFreq'].unique()
print( compfreq_categories)




