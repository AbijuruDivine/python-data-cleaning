import pandas as pd
df=pd.read_csv("customer.csv")
#checking missing 
print(df.isnull().sum()
      
#filling missing values
df["age"]=
df["age"].fillna(df["age"].mean())
df["gender"]=
df["gender"].fillna(df["unknown")
df=df.drop_duplicates()

df["registration_date"]=pd.to_datetime(df[registration_date])

#save cleaned data
df.to_csv("cleaned_customers.csv",index=false)
print("Data Cleaning completed successfully.")
