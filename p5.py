import pandas as pd

age = pd.DataFrame({'Name': ['Michał', 'Adam', 'Ewa', 'Jakub'],
                    'Age': [39, 28, 19, 32]})

age2 = pd.DataFrame({'Name': ['Mike'],
                     'Age': [50]})

city = pd.DataFrame({'Name': ['Adam', 'Ewa', 'Ola', 'Krystian', 'Jacek'],
                     'City': ['Warszawa', 'Kraków', 'Poznań', 'Zakopane', 'Olsztyn']})

age_new = pd.concat([age, age2], keys=['age', 'age2'])
# print(pd.merge(age_new, city, on='Name', how='inner'))
# print(pd.merge(age_new, city, on='Name', how='outer'))
# print(pd.merge(age_new, city, on='Name', how='left'))
print(pd.merge(age_new, city, on='Name', how='right'))


