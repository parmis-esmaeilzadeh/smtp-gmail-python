import smtplib
m_e = "parmis.esmaeilzadeh1028@gmail.com"
password = "cgjd lgda rxgn qtis"

#conn=smtplib.SMTP('smtp.gmail.com')
#conn.starttls()
#conn.login(user=m_e, password=password)
#conn.sendmail(from_addr=m_e,
#              to_addrs="ostad7test@gmail.com",
#              msg="Subject: Hello\n\nParmis Esmaeilzadeh")
#conn.close()

with smtplib.SMTP('smtp.gmail.com') as conn:
    conn.starttls()
    conn.login(user=m_e, password=password)
    conn.sendmail(from_addr=m_e,
                  to_addrs="ostad7test@gmail.com",
                  msg="Subject: Hello\n\nParmis Esmaeilzadeh")