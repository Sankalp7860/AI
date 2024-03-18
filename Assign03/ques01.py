import pandas as pd
data1 = {'Std_Name': ['Sankalp', 'Atul', 'Shripad', 'Shreshta',"Ayush"],
        'Roll_no': [2201176, 2201138, 2201188, 2201187,2201150],
        'CPI': [7.9, 9.8, 8.2, 8.5,5.8]}

df = pd.DataFrame(data1)

new_df = df[df['CPI'] > 6.0]
mean_cpi = df['CPI'].mean()
median_cpi = df['CPI'].median()
std_dev_cpi = df['CPI'].std()
print("Original DataFrame:")
print(df)

print("\nNew DataFrame (CPI > 6.0):")
print(new_df)

print("\nOverall Statistics:")
print(f"Mean CPI: {mean_cpi}")
print(f"Median CPI: {median_cpi}")
print(f"Standard Deviation CPI: {std_dev_cpi}")
