"""Marty Mooney, for Capstone class of spring 2023"""

import datetime, calendar
# get a dictionary that contains the month number and has shorthand and full month name
possible_answer_dict = {}
for x in range(1,13):
    possible_answer_dict[x]=[calendar.month_name[x].lower(),calendar.month_abbr[x].lower()]


def main():
    current_month_list=get_current_month()
    user_name, user_birthmonth = get_user_info()
    output_message(current_month_list, user_name, user_birthmonth)

# grabing the current month and creating the list to include any the versions that is recognisable as a month. 
def get_current_month():
    current_month= datetime.datetime.now().month
    current_month_list=[current_month,possible_answer_dict[current_month][0],
    possible_answer_dict[current_month][1]]
    current_month_list.append(current_month)
    return current_month_list

# asking the user for the data needed
def get_user_info():
    user_name= input("What is your name? ").title()
    user_birhday_month=input("What is your Birthday Month? ").lower()
    if user_birhday_month.isnumeric():
        user_birhday_month = int(user_birhday_month)
    return user_name, user_birhday_month

# the funtion name says it all... this does technically check for the month and logic. 
def output_message(current_month_list, user_name, user_birthmonth):
    print(f"Thanks for the info {user_name}, ", end="")
    if user_birthmonth in current_month_list:
        print(f"Happy Birth Month!")
    else:
        print("bit it seems it is not your birthmonth... Have a good month either way!")

main()