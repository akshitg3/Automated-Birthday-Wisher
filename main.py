import pandas
import smtplib
import random
import datetime as dt

your_email = "Enter Your Email here"
password = "Enter the password for your Email here"

birthdays_DF = pandas.read_csv("birthdays.csv")

birthdays_DF_dictionary = {"name": [i for i in birthdays_DF['name']], "email": [i for i in birthdays_DF['email']],
                           "year": [i for i in birthdays_DF['year']], "month": [i for i in birthdays_DF['month']],
                           "day": [i for i in birthdays_DF['day']]}

today_now = dt.datetime.now()


def send_email(name, birthday_email_id):
    file_number = 1  # number of the template you would like to use
    with open(f"./letter_templates/birthday_letter_{file_number}.txt") as birthday_letter:
        birthday_letter_content = birthday_letter.read().replace("[NAME]", name)

    print(birthday_letter_content)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=your_email, password=password)
        connection.sendmail(from_addr=your_email, to_addrs=birthday_email_id,
                            msg=f"Subject:Happy Birthday\n\n{birthday_letter_content}")


for i in range(len(birthdays_DF_dictionary['name'])):
    if birthdays_DF_dictionary['day'][i] == today_now.day and birthdays_DF_dictionary['month'][i] == today_now.month:
        birthday_name = (birthdays_DF_dictionary['name'][i])
        birthday_email = (birthdays_DF_dictionary['email'][i])
        send_email(birthday_name, birthday_email)
