#Bài 1:
#Viết chương trình trả ra từ điển với key là các số trong list, value là số lần xuất hiện của số trong list
#my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
#Trả ra
#{10: 1, 21: 2, 40: 3, 52: 2, 1: 2, 2: 4, 11: 4, 25: 1, 24: 2, 60: 1}

print("Bài 1:")

#cách 1:
print("Cách 1:")
my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
from collections import Counter
count=Counter(my_list)
my_dict = dict(count)
print("Trả ra sau quy đổi:",my_dict)

print("Cách 2:")
#cách 2:
my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
count = {}
for i in my_list:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i]=1
print("Trả ra sau quy đổi:",count)


#Bài 2:
#Print Star
#Hãy viết chương trình in ra các hình sau (dùng ký tự '*' và ký tự space) với n là số dòng. Vd: n = 4:

print("Bài 2:")

#Hình 1:
n = 4
 
print("Vẽ Hình số 1:")
for i in range(1, n+1):
    for j in range(n-i,0,-1):
        print("", end = "  ")
  
 
    for j in range(n,n-i,-1):
        print(" *", end = "")
    
    
    print()

#Hình 2:
n = 4
print("Vẽ hình số 2:")

for i in range(1, n+1):
    for j in range(n-i,0,-1):
        print("", end = "  ")
  
 
    for j in range(n,n-i,-1):
        print(" *", end = "")
    
    
    print()

for i in range(2*n-1, n-1, -1):
    for j in range(1, n+1):
        print("", end = "  ")

    for j in range(n+1, i+2):
        print(" *", end = "")
    print()

#Hình 3:



#Bài 4:
#Unique value Dictionary:
#Cho một list gồm 1 hoặc nhiều từ điển (Dictionary). Viết chương trình để trả ra tập hợp tất cả các giá trị (values) duy nhất trong tất cả danh sách các từ điển trên.

#[VD1]: Trường hợp dưới đây danh sách đầu vào có 1 từ điển map tên người vào tuổi của họ. Trả ra set các tuổi duy nhất.

#unique_value_dict([dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]) == {22, 25, 26, 27, 38}
#[VD2]: Trường hợp dưới đây danh sách đầu vào có 7 dicts, mỗi dict chỉ có 1 cặp key-values. 5 giá trị trả về là duy nhất.

#unique_value_dict([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]) == {'S009', 'S007', 'S002', 'S001', 'S005'}

print("Bài 4:")
#Cách 1:
print("Cách 1:")
my_dict = [dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]
def unique_value_dict(my_dict):
    return set( val for dic in my_dict for val in dic.values())

unique_value_dict(my_dict)

#Cách 2:
print("Cách 2:")
n = int(input("nhập số cặp key, value của dictionary:"))
d = {}

for i in range(n):
    keys = input("Nhập key  string nhé:") 
    values = int(input("nhập value  số nguyên nhé:")) 
    d[keys] = values
    list1 =[] 
    for val in d.values(): 
      if val in list1: 
         continue 
      else:
         list1.append(val)

print ("danh sách value duy nhất:",list1)

#Bài 5:
#Cho list A chứa các số nguyên đã sắp xếp theo thứ tự tăng dần.
#Vd A = [3, 6, 7, 9, 11, 12] và một số nguyên sum. Tìm tất cả các cặp số (a,b) trong mảng A có tổng bằng sum
#vd ở đây nếu sum = 18 thì kết quả là [(7,11), (6,12)]. Nếu không có cặp số nào thỏa mãn thì in ra list rỗng []
print("Bài 5:")
#Cách 1:
my_list = list(map(int, input("Nhập list các số nguyên đã sắp xếp theo thứ tự tăng dần: ").split()))
print("Nhập số nguyên tổng:")
sum = int(input())
for i in my_list:
    for j in my_list:
        if ((int(i) + int(j)) == sum) and (int(i) != int(j)):
          print("Cặp số cần tìm:",[int(i),int(j)])

# Cách 2:
A = [3, 6, 7, 9, 11, 12]
def find_pair(A, sum):
    ans = []
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == sum:
                ans.append((A[i], A[j]))
    return ans
find_pair([3, 6, 7, 9, 11, 12], 18)
    
    

#Bài 3:
#Viết chương trình in ra thời gian đếm ngược đến XMas 2021 sau mỗi khoảng thời gian nhất định.

#vd in ra sau mỗi 5s:

#Countdown to Xmas 2021: 112 days, 11:47:01.339588
#Countdown to Xmas 2021: 112 days, 11:46:56.324008
#Countdown to Xmas 2021: 112 days, 11:46:51.310473

print("Bài 3:")

import time
from datetime import datetime

while True:
    time.sleep(10)
    XMAS_DATE = datetime(year=2021, month=12, day=24)
    countdown = XMAS_DATE - datetime.now()
    print(f"Countdown to Xmas 2021: {countdown}")
    if countdown == 0:
        break