import pandas as pd

kostium = pd.read_csv('Halloween.csv', header=2)
# print(kostium.head())
# print(kostium[:10][['region', '1']])
# print(kostium.index)
# print(kostium.region.is_unique)
# kostium.set_index('region', inplace=True)
# kostium.reset_index(inplace=True)
# print(kostium)
# kostium.to_excel('kostiumy.xlsx')
# kostium.loc['Arizona', '1'] = 'Batman'
# print(kostium.loc['Arizona'])
# print(kostium.iloc[3, 2])
#
# for index, zawartosc in kostium.iterrows():
#     if zawartosc['1'] == 'Rabbit':
#         print(zawartosc['region'])


# print(kostium[kostium['1'] == 'Rabbit'])
# print(kostium[(kostium['1'] == 'Rabbit') | (kostium['1'] == 'Dinosuar')])
# print(kostium[(kostium['1'] == 'Rabbit') & (kostium['2'] == 'Pirate')])

kostium['Nowa'] = '0'
kostium.loc[kostium['1'] == 'Harley Quinn', 'Nowa'] = 1
# print(kostium.rename(columns={'1': "Pierwszy"}))
# print(kostium.drop('5', axis=1))
kostium['Połączone'] = kostium['3'] + " | " + kostium['4']
kostium[['6', '7']] = kostium.Połączone.str.split('|', expand=True)
print(kostium)
kostium.to_excel('test.xlsx')
