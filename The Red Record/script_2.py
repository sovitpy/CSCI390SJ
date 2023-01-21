import pandas as pd
with open('1894_by_month.txt','r') as f:
    data = f.readlines()
data = data[0].strip().split(';')
new_dict = {}
for datum in data:
    state, number= datum.split(',')
    new_dict[state.strip()] = [int(number.strip())]
df = pd.DataFrame.from_dict(new_dict)
df.to_csv('1894_by_month.csv')
