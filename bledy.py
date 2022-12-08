def check_age(users, age):
    count = 0
    for i, user in enumerate(users):
        try:
            user_age = int(user['age'])
        except KeyError:
            print(f'Niepoprawne dane: {user}')
        except ValueError:
            print(f'Niepoprawny wiek: {user}')
        else:
            count += 1 if user_age < age else 0
        finally:
            print(f"{i} - {user}")
    return count


valid_data = [{'name': 'Jan', 'age': '10'}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]
invalid_date = [{}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]
invalid_data2 = [{'name': 'Jan', 'age': 'age'}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]

print(check_age(valid_data, 15))
print(check_age(invalid_date, 15))
print(check_age(invalid_data2, 15))
