# send email using python through(used in variable)

import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
# server se connect karna hota hai
ob.starttls()
ob.login('deepikabaror07@gmail.com','P@SsWed1982')
subject="test python"
# message main kya likh kar bhje sakti hai 'body'
body="I Love Python"
massage="subject:{}\n\n{}".format(subject,body)
listadd=['deepikabaror07@gmail.com',
         '20cse020@gweca.ac.in']
ob.sendmail('deepikabaror07@gmail.com',listadd,'message')
print("send mail")
ob.quit()


