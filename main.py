import smtplib
import pandas
import datetime as dt
import random

rand_num = random.randint(1, 3)


# 3. If step 2 is true, pick a random letter from letter templates and
# replace the [NAME] with the person's actual name from birthdays.csv
def gen_email():
    global rand_num

    # 1. Update the birthdays.csv
    with open(f"letter_templates/letter_{rand_num}.txt") as letter_file:
        letter = letter_file.readlines()

    # Create a new text file containing the edited content
    with open(f"letter_templates/letter_{to_name}.txt", "w") as letter_file:
        for i in letter:
            if "[NAME]" in i:
                i = i.replace("[NAME]", to_name)
            letter_file.write(i)
    with open(f"letter_templates/letter_{to_name}.txt") as letter_file:
        new_letter = letter_file.readlines()

    # Generate the message as a string from the list.
    new_string = ""
    for i in new_letter:
        new_string += i

    return new_string


# 4. Send the letter generated in step 3 to that person's email address.
def send_email():
    # pass
    # Create the email connection
    my_email = "SENDING EMAIL ADDRESS"
    password = "ENTER YOUR PASS"

    with smtplib.SMTP("ENTER MAIL SERVER") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject: Happy Birthday!!!\n\n{gen_email()}")


# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthday_dict = data.to_dict(orient="records")


# Set the current day to compare
now = dt.datetime.now()


for recipient in birthday_dict:
    to_name = recipient["name"]
    to_email = recipient["email"]
    month = recipient["month"]
    day = recipient["day"]

    if (month, day) == (now.month, now.day):
        send_email()

