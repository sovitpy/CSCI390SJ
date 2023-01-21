# Importing pandas (we will use dataframe to process data and export it as CSV)
import pandas as pd

# Reading the text data
with open('data_2.txt', 'r') as f:
    data = f.readlines()
# Cleaning the data: removing whitespace and then removing blank lines from the array
data = list(map(lambda x: x.strip(), data))
filtered_data = [i for i in data if i != '']
# Adding the two murder data paragraphs together because they are in different paragraphs for some weird reason
#new_murder_data = filtered_data[31] + '; ' + filtered_data[32]

# Removing the two separate paragraphs
#filtered_data.pop(31)
#filtered_data.pop(31)

# Inserting the added paragraphs into the array
#filtered_data.insert(31, new_murder_data)

# Initializing the final_array to convert to dataframe later
final_array = []

# function to take key, values in the comma/semicolon format and convert it to dictionary then add it to the final array
def json_formatter(key, values):
    data = values.split(';')
    for datum in data:
        info = datum.split(',')
        date = info[0].strip()
        name = info[1].strip()
        try:
            address = info[2].strip() + ', ' + info[3].strip()
        except IndexError:
            print(info)
            address = info[2].strip()
        info_dict = {
        'Charge': key,
        'Date': date,
        'Name': name,
        'Address': address
        }
        final_array.append(info_dict)

# Iterating through our data and using json_formatter on data to append the processed json to final_array
for i in range(0, len(data), 2):
        key = filtered_data[i]
        values = filtered_data[i+1]
        json_formatter(key, values)

# Converting the final array to pandas dataframe and exporting it as csv.
df = pd.DataFrame(final_array)
df.to_csv('data_science_2.csv')
