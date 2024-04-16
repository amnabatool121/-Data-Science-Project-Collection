import csv
import requests
from bs4 import BeautifulSoup

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the average annual salary tag
annual_average_salary_tags = soup.find_all('Average_Annual_Salary')

# Find all language tags
language_tags = soup.find_all('h2', class_='h2')

# Initialize a list to store language names
languages = []

# Extract language names
for tag in language_tags:
    languages.append(tag.text.strip())

# Check if languages were found
if languages:
    print("Languages found:", languages)

    # Write the data to a CSV file
    with open('popular-languages.csv', 'w', newline='') as csvfile:
        fieldnames = ['Language']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for language in languages:
            writer.writerow({'Language': language})

    print("Data saved to popular-languages.csv")
else:
    print("No languages found on the page")
