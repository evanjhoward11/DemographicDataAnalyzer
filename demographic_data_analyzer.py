import pandas as pd

dec_num = 1
df = pd.read_csv('adult.data.csv')

# How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
race_count = df['race'].value_counts()
# print(race_count)

# What is the average age of men?
average_age_men = df[df.sex.eq('Male')].age.mean().round(dec_num)
# print(average_age_men)

# What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = round(df.education.value_counts(normalize=True).Bachelors * 100, dec_num)
# print(percentage_bachelors)

# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
# What percentage of people without advanced education make more than 50K?

# with and without `Bachelors`, `Masters`, or `Doctorate`
higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate']).sum()
# print(higher_education)

lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].count()[0]
# print(lower_education)

# percentage with salary >50K
higher_education_rich = round(((df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].salary == '>50K').sum() / higher_education) * 100, dec_num)
# print(higher_education_rich)

lower_education_rich = round(((df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].salary == '>50K').sum() / lower_education) * 100, dec_num)
# print(lower_education_rich)

# What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = df['hours-per-week'].min()
# print(min_work_hours)

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min_workers = (df['hours-per-week'] == 1).sum()
# print(num_min_workers)

rich_percentage = round((((df['hours-per-week'] == 1) & (df['salary'] == '>50K')).sum() / num_min_workers) * 100, dec_num)
# print(rich_percentage)

# What country has the highest percentage of people that earn >50K?
country_tots = df['native-country'].value_counts()
# print(country_tots)
salary_50K = df[df['salary'] == '>50K']
highest_earning_country = (salary_50K['native-country'].value_counts() / country_tots).idxmax()
# print(highest_earning_country)

highest_earning_country_percentage = round((salary_50K['native-country'].value_counts() / country_tots).max() * 100, dec_num)
# print(highest_earning_country_percentage)

# Identify the most popular occupation for those who earn >50K in India.
salary_50K_IN = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
# print(salary_50K_India)
top_IN_occupation = salary_50K_IN['occupation'].value_counts().index.tolist()[0]
# print(top_IN_occupation)
