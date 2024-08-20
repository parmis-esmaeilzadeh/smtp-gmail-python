import smtplib
from datetime import datetime
import random

m_e = "parmis.esmaeilzadeh1028@gmail.com"
password = "cgjd lgda rxgn qtis"


now = datetime.now()
wd = now.weekday()
if wd == 1:
    with open("quotes.txt") as q:
        a_q = q.readlines()
        qu = random.choice(a_q)
with smtplib.SMTP('smtp.gmail.com') as conn:
    conn.starttls()
    conn.login(user=m_e, password=password)
    conn.sendmail(from_addr=m_e,
                  to_addrs="parmis.esmaeilzadeh1028@gmail.com",
                  msg=f"Subject: HI \n\n{qu}")
