import pandas as pd

kostium = pd.read_csv('Halloween.csv', header=2)
# print(kostium.head())
# print(kostium[:10][['region', '1']])
print(kostium.index)
print(kostium.region.is_unique)
kostium.set_index('region', inplace=True)
# kostium.reset_index(inplace=True)
# print(kostium)
# kostium.to_excel('kostiumy.xlsx')

kostium.loc['Arizona', '1'] = 'Batman'
print(kostium.loc['Arizona'])
print(kostium.iloc[3, 2])
