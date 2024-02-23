import pandas as pd

# Load the data
df = pd.read_excel('transistors.xlsx')

# Apply ranking for each parameter
df['NFmin_2.4GHz_Rank'] = df['NFmin at 2.4GHz'].rank(method='min')
df['Gain_2.4GHz_Rank'] = df['Gain at 2.4GHz'].rank(ascending=False, method='min')
df['NFmin_4GHz_Rank'] = df['NFmin at 4GHz'].rank(method='min')
df['Gain_4GHz_Rank'] = df['Gain at 4GHz'].rank(ascending=False, method='min')

# Assign weights to emphasize Gain over NFmin
# Gain parameters are given more weight by multiplying by a factor > 1
gain_weight = 2
nfmin_weight = 1

# Calculate weighted total rank
df['Total_Rank'] = (df['NFmin_2.4GHz_Rank'] * nfmin_weight + 
                    df['Gain_2.4GHz_Rank'] * gain_weight + 
                    df['NFmin_4GHz_Rank'] * nfmin_weight + 
                    df['Gain_4GHz_Rank'] * gain_weight)

# Sort the DataFrame by the weighted Total_Rank and then extract the top 5 devices
top_devices_sorted = df.sort_values(by='Total_Rank').reset_index(drop=True)
top_five_devices = top_devices_sorted.head(5)

# Prepare the output for the top 5 devices
top_five_devices_output = top_five_devices[['Device name', 'Total_Rank']]
print("Top 5 devices based on combined NFmin and Gain performance, with Gain given more importance:")
print(top_five_devices_output)

# Save the sorted DataFrame to a new Excel file
output_file_path = 'sorted_transistors_with_weighted_gain.xlsx'
top_devices_sorted.to_excel(output_file_path, sheet_name='Sorted Devices', index=False)
print(f"Data saved to '{output_file_path}' successfully.")
