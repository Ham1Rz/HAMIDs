
#S1

#متغیر ها در پایتون
x = 5
y = "John"
print(x)
print(y)

#دریافت نوع در پایتون
x = 5
y = "John"
print(type(x))
print(type(y))

#چند متغیر در یک خط
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#یک مقدار برای چندین متغیر
x = y = z = "Orange"
print(x)
print(y)
print(z)

#مجموعه
fruits = ["apple" ,"banana", "cherry"]
X , y, z = fruits
print(x)
print(y)
print(z)

#خروجی دادن چند متغییر  با +
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


x = 5
y = "John"
#print(x + y)

#متغیر سراسری
x = "awesome"
def myfunc(): 
    x = "fantastic"
print("Python is " + x)
myfunc()
print("Python is " + x)

#استفاده از یک متغییر سراسری با global
x = "awesome"
def myfunc():
    global x
x = "fantastic"
myfunc()
print("Python is " + x)




#S2

#پیمایش  رشته 
for x in "banana":
    print(x) 
    
    #پیمایش طول رشته
    a = "Hello, World!"
print(len(a))

#بررسی موجودیت کلمه در رشته

txt = "The best things in life are free!"
print("free" in txt)

#()upper متد رشته را با حروف بزرگ برمی گرداند.
a = "Hello, World!"
print(a.upper())

#()lower رشته را با حروف کوچک برمی گرداند.

a = "Hello, World!"
print(a.lower())

# ()replace یک رشته را با رشته دیگری جایگزین می کند
a = "Hello, World!"
print(a.replace("H", "J"))

# ()split لیستی را برمی گرداند که در آن متن بین جداکننده ی مشخص شده، به
#عنوان آیتم های لیست قرار می گیرد
a = "Hello, World!"
b = a.split(",")
print(b)

#الحاق رشته

a = "Hello"
b = "World"
c = a + b
print(c)
#
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#fstring  نشان دادن ترکیبی متغیرورشته که اول رشته f قرار میگیرد
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# placeholder شامل‌متغیرها‌،عملیات‌ها‌،توابع‌و‌اصالح‌کننده‌هایی‌برای‌قالب‌بندی‌مقدار
price = 59
txt = f"The price is {price} dollars"
print(txt)
#
txt = f"The price is {20 * 59} dollars"
print(txt)
#
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#####
name = "Alice"
age = 30
greeting = f"Hello, I'm {name} and I'm {age} years old."
print(greeting) 
#####
x = 10
y = 20
result = f"The sum of {x} and {y} is {x + y}."
print(result) 
#####
#وارد کردن کاراکتر هایی که در رشته غیر مجاز هستند با بک اسلش
txt = 'It\'s alright.'
print(txt) 
#
txt = "Hello\tWorld!"
print(txt) 
#
txt = "This will insert one \\ (backslash)."
print(txt) 
#
txt = "Hello \bWorld!"
print(txt) 
#
txt = "Hello\nWorld!"
print(txt) 
#
txt = "Hello\rWorld!"
print(txt)


#بولیندر پایتون درست یا غلط بودنرا نشان میدهد
print(10 > 9)
print(10 == 9)
print(10 < 9)
#
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


#()isinstance تابعی‌که‌می‌تواند‌برای‌تعیین‌اینکه‌آیا‌یک‌شیء‌از‌نوع‌داده‌
#خاصی‌است‌ یا‌خیر
x = 200
print(isinstance(x, int))


#عملگرهای حسابی
x = 5
y = 3
print(x + y)
#
x = 12
y = 3
print(x / y)
#
x = 15
y = 2
print(x // y)
#
x = 5
y = 3
print(x - y)
#
x = 5
y = 3
print(x * y)
#
x = 2
y = 5
print(x ** y) #

x = 5
y = 3
print(x + y)

#عملگرهای انتساب
x = 5
x += 3
print(x)

x = 5
print(x)

#عملگرهای مقایسه
x = 5
y = 3
print(x == y) 

x = 5
y = 3
print(x != y)

x = 5
y = 3
print(x >= y)

#عملگرهای منطقی

x = 5
print(x > 3 and x < 10)

x = 5
print(x > 3 or x < 4)

x = 5
print(not(x > 3 and x < 10))

#عملگرهای عضویت 
#اعتبار سنجی موجودیت در لیست
x = ["apple", "banana"]
print("banana" in x)

x = ["apple", "banana"]
print("pineapple" not in x)
