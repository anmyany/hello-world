import os
from ftplib import FTP
import mysql.conector
import schedule
import time
import smtplib

def job():

    ftp_addr = 'ftp.jobready123.com'

    username = 'dq121@testingmoo.com'
    password = 'K#Xwx3Sp.gmL'
    ftp.login(username, password)

    ftp.cwd("/202007/") #or should it be "202007"

def ftp_download():
    file_remote = 'Customer_Info.xlsx'
    file_local ='C:\xampp\mysql\data\Coop 2010'
    file_handle = open(filename, "wb").write
    ftp.retrbinary   ('RETR %s' % file_remote, file_handle, blocksize=1024)

ftp.close()
ftp.quit()

today = datetime.today()
today_date = datetime.date(today)

    sender = 'anmyany@gamil.com'
    receivers = 'job123@gmail.com'
    password = 'password'
    smtp_server = 'smtp.gmail.com'
    port = '465'

    subject = 'Daily Customer Info Updated'
    body = 'The daily Customer Info has been updated successfully.'

    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server,port)
    server.login(sender,password)
    server.sendmail(sender,receivers,body)

server.quit()


schedule.every().day.at("9:00").do(job)

while true:
    schedule.run_pending()
    time.sleep(1)
