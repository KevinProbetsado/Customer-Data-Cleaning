import pandas as pd

df = pd.read_excel(r"C:\Users\Administrator\Downloads\Customer Call List.xlsx")

# Remove duplicates
df = df.drop_duplicates()

# Drop useless column
df = df.drop(columns="Not_Useful_Column")

# Clean last name
df["Last_Name"] = df["Last_Name"].str.strip("123./_")

# Remove non-digits from phone number
df["Phone_Number"] = df["Phone_Number"].str.replace(r'\D', '', regex=True)

# Convert to string and handle NaN
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x) if pd.notna(x) else '')

# Format phone number with dashes
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10] if len(x) >= 10 else '')

# Split address
df[["Street Address", "State", "Zip Code"]] = df["Address"].str.split(',', expand=True)

# Standardize Do_Not_Contact and Paying Customer
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes', 'Y', regex=False)
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No', 'N', regex=False)
df["Paying Customer"] = df["Paying Customer"].str.replace('Yes', 'Y', regex=False)
df["Paying Customer"] = df["Paying Customer"].str.replace('No', 'N', regex=False)

# Fill NaN
df = df.fillna('')

# Remove do not contact and empty phone numbers
df = df[df["Do_Not_Contact"] != "Y"]
df = df[df["Phone_Number"] != ""]

# Reset index
df = df.reset_index(drop=True)

print(df)
