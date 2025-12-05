#S3
#شرط و دستورات 
#a == b مساوی
#a != b برابر نیست 
#a < b کوچکتر از
#a <= کوچکتر یا مساوی
#a > b بزرگتر از
#a >= bبزرگتر یا مساوی

a = 33
b = 200
if b > a :
    print("b is greater than a")
#
#تورفتگی
#تو رفتگی در پایتون مهم است 
a = 33
b = 200
if b > a:
    print("b is greater than a")

#
#
#ELIF
#به این صورت است که می گوید »اگر شرایط قبلی درست نبود، این شرط را امتحان کن«
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
    
#
#
#ELSE
#هر چیزی را که توسط شرایط قبلی گرفته نشده است، می گیرد

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
#
# 
# می توان else را بدون elif داشته باشید
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")    
#کلمه کلیدی and یک عملگر منطقی است و برای ترکیب عبارات شرطی استفاده می شود
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
#کلمه کلیدیor یک عملگر منطقی است و برای ترکیب عبارات شرطی استفاده می شود
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")    
#کلمه کلیدی not یک عملگر منطقی است و برای معکوس کردن نتیجه عبارت شرطی استفاده می شود
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")
#
#
#IF تو در تو
#می توانید دستورات if را درون دستورات if دیگر داشته باشید، به این حالت دستورات if تو در تو می گویند
x = 41
if x > 10:
    print("Above ten,")
if x > 20:
    print("and also above 20!")
else:
    print("but not above 20.")
    #
    #
#شرط های ترکیبی با عملگرهای منطقی
# score = 85
if ss >= 90:
 print("Grade: A")
elif ss >= 80 and ss < 90:
 print("Grade: B")
elif ss >= 70:
 print("Grade: C")
else:
 print("Grade: F")    
 #
 #
 #دستورات انتخاب
 #به جای نوشتن تعداد زیادی دستور else..if، می توانید از دستور match استفاده کنید
 #دستور match یکی از بلوک های کد زیادی را که باید اجرا شود، انتخاب می کند
 match expression:
case x:
code block
case y:
code block
case z:
code block

#
#
#
#The Python Match Statement
#نحوه کار دستور match به این صورت است:
# عبارت match یک بار ارزیابی می شود.
# مقدار عبارت با مقادیر هر یک از case ها مقایسه می شود
# اگر تطابقی وجود داشته باشد، بلوک کد مرتبط اجرا می شود
day = 4
match day:
case 1:
print("Monday")
case 2:
print("Tuesday")
case 3:
print("Wednesday")
case 4:
print("Thursday")
case 5:
print("Friday")
case 6:
print("Saturday")
case 7:
print("Sunday")
#
#
#
#اگر می خواهید یک بلوک کد زمانی که هیچ تطابق دیگری وجود ندارد اجرا شود، از کاراکتر زیرخط _ به عنوان آخرین مقدار case استفاده کنید
day = 4
match day:
case 6:
       print("Today is Saturday")
case 7:
         print("Today is Sunday")
case _:
         print("Looking forward to the Weekend")
#
#
#
#If Statements as Guards
#در ارزیابی case از if ، به عنوان یک بررسی شرط اضافی، دستوراتی اضافه کنید

month=5
day = 4
match day:
case 1 | 2 | 3 | 4 | 5 if month == 4:
         print("A weekday in April")
case 1 | 2 | 3 | 4 | 5 if month == 5:
         print("A weekday in May")
case _:
         print("No match")
#
#
#حلقه While
# condition : شرطی که تا زمانی که True باشد، حلقه ادامه پیدا می کند
#اگر شرط از ابتدا False باشد، حلقه هیچ گاه اجرا نمی شود 
while condition: 
# ode of block 
#می توانیم مجموعه ای از دستورات را تا زمانی که یک شرط درست باشد، اجرا کنیم
i = 1
while i < 6:
print(i)
i += 1
#به یاد داشته باشید که i را افزایش دهید، در غیر این صورت حلقه برای همیشه ادامه خواهد یافت
#حلقه while نیاز به آماده بودن متغیرهای مربوطه دارد،
#در این مثال باید یک متغیر اندیس گذاری به نام i تعریف کنیم که آن را روی 1 تنظیم می کنیم

#پایتون دو دستور حلقه دارد while and for

#
#
#While-The break Statement
#با دستور break می توانیم حلقه را حتی اگر شرط while درست باشد، متوقف کنیم
#وقتی i برابر با 3 شد، از حلقه خارج شو
i = 1
while i < 6:
print(i)
if i == 3:
break
i += 1

#
#
#
#While-The continue Statement
#با استفاده از دستور continue می توانیم تکرار فعلی را متوقف کنیم و تکرار بعدی را ادامه دهیم
i = 0
while i < 6:
i += 1
if i == 3:
continue
print(i)

# 
#
#
#دستور else
# else می توانیم یک بلوک کد را زمانی که شرط دیگر درست نباشد، یک بار اجرا کنیم:
#وقتی شرط نادرست شد، یک پیام چاپ کن
i = 1
while i < 6:
print(i)
i += 1
else:
print("i is no longer less than 6")

#
#
#
#حلقه FOR
#با حلقه for می توانیم مجموعه ای از دستورات را اجرا کنیم، یک بار برای هر آیتم در یک لیست، چندتایی، مجموعه و غیره
#Variable: متغیری که در هر تکرار مقدار جدیدی از iterable می گیرد
#Iterable :مجموعه ای قابل پیمایش مثل لیست، رشته، دیکشنری، یا تابعrange 
for variable in iterable:
 # block of code

#
#
#
fruits = ["apple", "banana", "cherry"]
for x in fruits:
print(x)

#
#
#
#FOR- The break Statement
#با استفاده از دستور break می توانیم حلقه را قبل از اینکه تمام آیتم ها را پیمایش کند، متوقف کنیم
fruits = ["apple", "banana", "cherry"]
for x in fruits:
print(x)
if x == "banana":
break
#
#
fruits = ["apple", "banana", "cherry"]
for x in fruits:
if x == "banana":
break
print(x)
#
#
#
