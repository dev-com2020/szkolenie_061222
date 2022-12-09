import ftplib

ftp = ftplib.FTP('test.rebex.net')
logowanie = ftp.login('demo', 'password')
print(logowanie)
katalog = ftp.nlst('/pub/example')
print(katalog)
# x = ftp.retrbinary('RETR readme.txt', open('README.txt', 'wb').write)
x = ftp.retrbinary('RETR pub/example/WinFormClient.png', open('../plik.png', 'wb').write)
