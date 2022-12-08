import csv

with open('../dane.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Nazwy kolumn to: {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t\t\t\t\t{row[0]}, {row[1]}, {row[2]}')
            line_count += 1
lista = [['John Smith2', 'IT', 'March'], ['John Smith3', 'IT', 'March'], ['John Smith4', 'IT', 'March']]

with open('../dane2.csv', 'w', newline="") as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"')
    employee_writer.writerow(['name', 'department', 'birthday month'])
    employee_writer.writerow(['John Smith', 'IT', 'March'])
    employee_writer.writerow(['Erica Smith', 'Data Science', 'November'])
    employee_writer.writerows(lista)
