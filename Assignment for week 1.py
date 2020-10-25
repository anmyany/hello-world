import datetime
import os
import sched



from ftplib import FTP

f = FTP(ftdq121@testingmoo.com)
f.login('dq121@testingmoo.com', 'K#Xwx3Sp.gmL')
f.cwd("/202007/")
remote_file = 'Customer_Info.xlsx'

today = datetime.today()
today_date = datetime.date(today)

sender = 'anmyany@gamil.com'
receivers = ['job123@gmail.com']
password = 'password'
smtp_server = 'smtp.gmail.com'

sent_from = 'anmyany@gmail.com'
to = ['job123@gmail.com']
subject = 'Daily Customer Info Updated'
body = 'The daily Customer Info has been updated successfully.'

email_text = """\ 
From: %s 
To: %s Subject: %s %s """ % (sent_from, ", ".join(to), subject, body)
