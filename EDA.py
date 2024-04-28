import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m2_survey_data.csv"
df=pd.read_csv(file_path)
converted_comp_data=df['ConvertedComp']
sns.histplot(converted_comp_data, bins=30)  # Adjust the number of bins as needed
plt.title('Distribution of Annual Salaries')
plt.xlabel('Annual Salary (USD)')
plt.ylabel('Frequency')
plt.show()

sns.kdeplot(converted_comp_data,color='red', linestyle='dashed')
plt.title('Distribution of Annual Salaries')
plt.xlabel('Annual Salary (USD)')
plt.ylabel('Frequency')
plt.show()

median_camp=np.median(converted_comp_data)
print(median_camp)
man_count = df[df['Gender'] == 'Man'].shape[0]
print(man_count)
woman_data = df[df['Gender'] == 'Woman']
median_converted_comp_woman = woman_data['ConvertedComp'].median()
print(median_converted_comp_woman)
print(woman_data)
age_median=df['Age'].median()
print(age_median)

sns.histplot(df['Age'], bins=30)  # Adjust the number of bins as needed
plt.title('histogram of Age')
plt.xlabel('AGE')
plt.ylabel('Frequency')
plt.show()

#outliers
plt.figure(figsize=(8, 6))
plt.boxplot(converted_comp_data, vert=False)
plt.title('Box plot of ConvertedComp')
plt.xlabel('ConvertedComp')
plt.show()

Q1 = converted_comp_data.quantile(0.25)
Q3 = converted_comp_data.quantile(0.75)
IQR=Q3-Q1
print(IQR)

upper_bound = Q3 + 1.5 * IQR
lower_bound = Q1 - 1.5 * IQR
print(upper_bound)
print(lower_bound)

outliers = (converted_comp_data < lower_bound) | (converted_comp_data > upper_bound)
num_outliers = outliers.sum()
print(num_outliers)
median_out=np.median(num_outliers)
print(median_out)
mean_out=np.mean(num_outliers)
print(mean_out)
new_df = df[(df['ConvertedComp'] >= lower_bound) & (df['ConvertedComp'] <= upper_bound)]
print(new_df)

#corelation
numeric_df = df.select_dtypes(include=['number'])
correlation_matrix = numeric_df.corr()
age_correlation = correlation_matrix['Age'].drop('Age')
print(age_correlation)

