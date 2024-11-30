import pandas as pd

df_csv = pd.read_csv('dataset.csv')
df_json = pd.read_json('dataset.json')

print("First 10 rows of CSV dataset:")
print(df_csv.head(10))
print("\nLast 10 rows of CSV dataset:")
print(df_csv.tail(10))

print("\nFirst 10 rows of JSON dataset:")
print(df_json.head(10))
print("\nLast 10 rows of JSON dataset:")
print(df_json.tail(10))

print("\nUnique values in a specific column of CSV dataset:")
print(df_csv['column_name'].unique())
print("\nNumber of unique values in the column:")
print(df_csv['column_name'].nunique())



print(df_csv.describe())
print(df_json.describe())

print(df_csv.info())
print(df_json.info())




print(df_csv.isnull().sum())
print(df_json.isnull().sum())

df_csv['numerical_column'].fillna(df_csv['numerical_column'].mean(), inplace=True)
df_csv['numerical_column'].fillna(df_csv['numerical_column'].mode()[0], inplace=True)
df_csv['numerical_column'].fillna(df_csv['numerical_column'].median(), inplace=True)

df_csv['categorical_column'].fillna(df_csv['categorical_column'].mode()[0], inplace=True)

df_csv.dropna(axis=0, inplace=True)
df_csv.dropna(axis=1, inplace=True)




df_csv['new_column'] = df_csv['existing_column1'] + df_csv['existing_column2']

df_csv.drop('column_to_drop', axis=1, inplace=True)
df_csv.drop(index=5, inplace=True)


X = df_csv.drop('target_column', axis=1)
y = df_csv['target_column']

print(X.head())
print(y.head())

