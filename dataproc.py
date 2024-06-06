import pandas as pd
import numpy as np


df1 = pd.read_csv('data1.csv')

# # create second csv
df2 = pd.DataFrame({
    'id': range(1000),
    'performance_score': np.random.randint(1, 10, size=1000),
    'salary': np.random.randint(30000, 100000, size=1000)
})

# create csv
df1.to_csv('data1.csv', index=False)

extracted_df = df1[['name/first', 'age', 'city']]
print(extracted_df)

# # Filtering rows based on condition
filtered_df = extracted_df[extracted_df['age'] > 25]
print(filtered_df)

df1['years_experience'] = [2, 5, 1, 10, 7]* (1000 // len([2, 5, 1, 10, 7]))
# df1['years_experience'] = years_experience
print(df1['years_experience'])

df1.rename(columns={'city': 'location'}, inplace=True)

print(df1['location'])
# df1.drop(columns=['department'], inplace=True)
print(df1)

# grouped_data= df1.groupby('department').agg({'salary':'mean', 'age':'max'})
# print(grouped_data)

sort_salary= df1.sort_values(by='dollar', ascending=False)
print(sort_salary)

# replaced_location= df1['location'].replace({'New York': 'NYC', 'Los Angeles': 'LA'})
# print(df1)

# df1['dollar']=df1['dollar']/1000
df1['dollar'] = pd.to_numeric(df1['dollar'], errors='coerce') / 1000
print(df1)

pivot_table = df1.pivot_table(index='age', values='dollar', aggfunc='mean')

print(pivot_table)

merged_df = pd.merge(df1, df2, on='id')

print(merged_df)

# Load the DataFrame into a MySQL table using SQLAlchemy
from sqlalchemy import create_engine, text


# Create an engine and connect to MySQL
engine = create_engine('mysql+pymysql://root:password@localhost:3306/EmpData')

with engine.connect() as connect:

# # Load the merged DataFrame into the new MySQL database
    merged_df.to_sql(name='employee_imported', con=connect, if_exists='replace')
    connect.close()

bouns_data = pd.Series([1000] * 500 + [None] * 500, name='bouns')
df1= pd.concat([df1, bouns_data], axis=1)
# fill_data= df1.fillna([0])
df1['bonus'] = df1['bouns'].fillna(0, inplace=True)
print(df1)

df1.dropna(inplace=True)

df1['age'].astype(float)

df1['total_compensation']= df1['dollar']+ df1['bouns']
df1['total_compensation'].astype(float)
print(df1['total_compensation'])
print(df1.columns)

unique_age = df1['years_experience'].unique()
print(unique_age)

filtered_df = df1[(df1['age'] > 25) & (df1['zip'] < 3000)]
print(filtered_df.index)

cumulative_salary = df1['dollar'].cumsum()
print(cumulative_salary)
print(df1)