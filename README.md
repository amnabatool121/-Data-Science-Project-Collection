#  Data Science Project Collection

This repository contains a set of beginner-to-intermediate level data science mini-projects using **Python**. These cover data cleaning, visualization, and web scraping — all essential skills for real-world data analysis.


##  Project Overview

### 1. **Salary Data Analysis & Visualization**
- **File**: `salary_analysis.py`
- **Dataset**: [Survey Data CSV](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m2_survey_data.csv)

**Description**:  
Analyzes survey participants’ annual salaries (`ConvertedComp`) and age distributions. Visualizes these metrics and detects salary outliers.

**Key Features**:
- Salary histogram and KDE plot
- Boxplot to detect outliers
- Calculates IQR, upper/lower bounds, and filters outliers
- Median salary comparison by gender
- Correlation of numeric fields with age


### 2.  **Data Wrangling**
- **File**: `data_wrangling.py`
- **Dataset**: [Survey Data CSV](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv)

**Description**:  
Performs data cleaning by removing duplicates and imputing missing values, especially in the `WorkLoc` column.

**Key Features**:
- Detects and removes duplicate rows
- Identifies missing values
- Fills missing `WorkLoc` entries using mode (most frequent location)
- Explores compensation frequency (`CompFreq`) categories

---

### 3.  **Web Scraping: Popular Programming Languages**
- **File**: `scraping.py`
- **Website**: [Sample HTML Dataset](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html)

**Description**:  
Scrapes popular programming language names from an HTML page using `requests` and `BeautifulSoup`, and saves them to a CSV file.

**Key Features**:
- Fetches HTML content using HTTP GET
- Extracts `h2` headers with class `h2`
- Stores programming languages into `popular-languages.csv`
- Handles missing tags gracefully


##  Requirements

Install all packages using pip:
pip install pandas numpy matplotlib seaborn requests beautifulsoup4

