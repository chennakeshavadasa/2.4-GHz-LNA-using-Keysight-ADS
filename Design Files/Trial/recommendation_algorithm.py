import pandas as pd

# Load the data
df = pd.read_excel('transistors.xlsx')

# Apply ranking with a specified method for handling ties, here using 'min' as an example
df['NFmin_2.4GHz_Rank'] = df['NFmin at 2.4GHz'].rank(method='min')
df['Gain_2.4GHz_Rank'] = df['Gain at 2.4GHz'].rank(ascending=False, method='min')
df['NFmin_4GHz_Rank'] = df['NFmin at 4GHz'].rank(method='min')
df['Gain_4GHz_Rank'] = df['Gain at 4GHz'].rank(ascending=False, method='min')

# Calculate total rank
df['Total_Rank'] = df[['NFmin_2.4GHz_Rank', 'Gain_2.4GHz_Rank', 'NFmin_4GHz_Rank', 'Gain_4GHz_Rank']].sum(axis=1)

# Sort the DataFrame by Total_Rank and then extract the top 5 devices
top_devices_sorted = df.sort_values(by='Total_Rank').reset_index(drop=True)
top_five_devices = top_devices_sorted.head(5)

# Prepare the output for the top 5 devices
top_five_devices_output = top_five_devices[['Device name', 'Total_Rank']]
print("Top 5 devices based on combined NFmin and Gain performance:")
print(top_five_devices_output)

# Save the sorted DataFrame to a new Excel file
output_file_path = 'sorted_transistors.xlsx'
top_devices_sorted.to_excel(output_file_path, sheet_name='Sorted Devices', index=False)
print(f"Data saved to '{output_file_path}' successfully.")
