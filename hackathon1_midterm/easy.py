# 1
from datetime import datetime
import time
def day_diff(release_date, code_complete_day):
    day_left = datetime.strptime(release_date, '%d/%m/%Y') - datetime.strptime(code_complete_day, '%Y-%d-%m')
    return day_left.days
#print(day_diff("19/12/2021","2021-17-05"))


# 2
import re
#str1 = "Emma25 is Data scientist50 and AI Expert"
def alpha_num(sentence):
    list1 = []
    for i in sentence.split():
        if i.isalpha():
            pass
        elif i.isdigit():
            pass
        else:
            list1.append(i)
    return list1
#print(alpha_num(str1))

    