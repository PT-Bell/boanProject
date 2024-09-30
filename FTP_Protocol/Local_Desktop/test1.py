from ftplib import FTP
ftp = FTP("192.168.55.188")
print('banner:',ftp.getwelcome())
print('login:',ftp.login())
print('Current directory:', ftp.pwd())
print('list:',ftp.retrlines('LIST'))
# FTP boanproject.txt 파일에서 로컬 boan.txt로 내용 복사
print('RETR:', ftp.retrbinary('RETR boanproject.txt',
                    open('C:/Users/l2yoo/Desktop/boan.txt', 'wb').write))

# 로컬 boanproject2.txt 파일을 FTP 서버로 업로드
print('STOR:', ftp.storbinary('STOR boanproject2.txt',
                    open('C:/Users/l2yoo/Desktop/boanproject2.txt', 'rb')))

