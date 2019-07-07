import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com',587)

print(smtpObj.ehlo())


print(smtpObj.starttls())

print(smtpObj.login('saurabhkdm721@gmail.com','Halls1234$'))

print(smtpObj.sendmail('saurabhkdm721@gmail.com','notkadam@gmail.com','Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob'))
print(smtpObj.quit())