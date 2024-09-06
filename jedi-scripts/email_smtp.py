
# email smtp is a module that helps to send emails using python code
# data and time module to format date and time

# SMTP : Simple Mail Transfer Protocol
# smtp contains all the rules that determine how an email is received by mail servers
# passed on to next mail servers and how email can be sent around the internet.
# smtp is basically a postman
import smtplib
import datetime as dt

# my_email = "manojsai.l2004@gmail.com"
# password = "ciys ahke wpsy dexp"
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
# 	connection.starttls()  # tls is a way of securing our connection to our email sever
# 	connection.login(user=my_email, password=password)
# 	connection.sendmail(
# 		from_addr=my_email,
# 		to_addrs=my_email,
# 		msg="Subject:Hello\n\nThis is a test email"
# 	)

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()
print(now)
print(year)
print(day_of_week)

date_of_birth = dt.datetime(year=2004, month=12, day=4, hour=10)
print(date_of_birth)