#5
#توابع پایتون
#توابع در پایتون یکی از مهم ترین ابزارها برای سازمان دهی، باز استفاده و ساده سازی کد هستند
#با استفاده از توابع می توان مجموعه ای از دستورات را در قالب یک واحد مستقل تعریف کرد و در هر جای برنامه آن را فراخوانی کرد.
#def : کلید واژه برای تعریف تابع
#me_function : نام تابع
#arameters : ورودی های تابع
#eturn : خروجی تابع 
def function_name (parameters):
# block of code
return result
#
#
#
#ایجاد یک تابع 
#یک تابع با استفاده از کلمه کلیدی def تعریف می شود
def greet():
    print("Hello from a function")
#
#
#
#فراخوانی یک تابع
#برای فراخوانی یک تابع، نام آن را نوشته و به دنبال آن پرانتز قرار دهید
def my_function():
    print("Hello from a function")
my_function()
#
# 
# 
#فراخوانی چند بار یک تابع 
def my_function():
    print("Hello from a function")
my_function()
my_function()
my_function()
#
#
#
#نام توابع
#ثوانین نام مانند فوانین نام متغییر هاست
#نام تابع باید با یک حرف یا زیرخط شروع شود
#حساس بودن روی کوچک وبزرگ
#نونه ای  دلیل برای استفاده از تابع
#بدون تابع
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)
temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)
temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)
#با استفاده از تابع
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))
#
#
#
#مقادیر بازگشتی
#توابع می توانند با استفاده از دستور return ، داده ها را به کدی که آنها را فراخوانی کرده است، ارسال کنند
#وقتی یک تابع به یک دستور return می رسد، اجرا را متوقف کرده و نتیجه را برمی گرداند
def get_greeting():
    return "Hello from a function"
message = get_greeting()
print(message)
###
def get_greeting():
    return "Hello from a function"
print(get_greeting())
#
#
#
#تابع را یکبار مینویسیم و چند بار میخوانیم
#تورفتگی در تابع مهم است
def greet():
    print('Hello World!')
# call the function
greet()
print('Outside function')
#
#
#
#pass در پایتون
#، این دستور pass یک دستور null است که می تواند به عنوان یک نگهدارنده برای کدهای آینده استفاده شود
#فرض کنید یک حلقه یا تابع داریم که هنوز پیاده سازی نشده است، اما می خواهیم در آینده آن را پیاده سازی کنیم. در چنین مواردی می توانیم
#از pass استفاده کنیم
n = 10
# use pass inside if statement
if n > 10:
    pass
print('Hello')
###
def future_function():
    pass
# this will execute without any action or error
future_function() 
#
#
#
#آرگومان ها
#در برنامه نویسی کامپیوتر، آرگومان مقداری است که توسط یک تابع پذیرفته می شود
#اینجا 1num و 2num پارامتر هستند
#یعنی نام های متغیرهایی که تابع انتظار دارد هنگام فراخوانی مقدار بگیرند.
# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
print("Sum: ", sum)
# function call with two values
add_numbers(5, 4)
#ینجا 5 و4 آرگومان هستند.
#یعنی مقادیری که به پارامترهای 1num و 2num داده می شوند
#
#
#
#def greet(name):
print("Hello", name)
# pass argument
greet("John")
#در اینجا، ما John را به عنوان آرگومان به تابع ()greet ارسال کردیم
#ما می توانیم در هر فراخوانی آرگومان های مختلفی ارسال کنیم و تابع را قابل استفاده مجدد و پویا کنیم
#آرگومان مقدار واقعی است که هنگام فراخوانی تابع به آن ارسال می شود
#اگر تابع شما انتظار ۲ آرگومان دارد، باید آن را دقیقاً با ۲ آرگومان فراخوانی کنید

def
print(fname + " " + lname)
my_function("Emil", "Refsnes")

#ارسال انواع داده مختلف
def my_function(fruits):
    for fruit in fruits:
        print(fruit)
my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)
###
def my_function(person):
    print("Name:", person["name"])
print("Age:", person["age"])
my_person = {"name": "Emil", "age": 25}
my_function(my_person)
#
#
#وقتی متغیرها را درون یک تابع تعریف می کنیم، این متغیرها دامنه محلی )درون تابع( خواهند داشت
def greet():
# local variablemessage = 'Hello'
print('Local', message)
greet()
# try to access message variable
# outside greet() function
print(message)
###
message = 'Hello'
def greet():
# declare local variable
print('Local', message)
greet()
print('Global', message)
###
#در پایتون، nonlocal کلمه کلیدی در توابع تو در تو استفاده می شود تا نشان دهد که یک متغیر محلی تابع داخلی نیست
def outer():message = 'local'
# nested function
def inner():
# declare nonlocal variable
nonlocal message
message = 'nonlocal'
print("inner:", message)
inner()
print("outer:", message)
outer()
####
#تابع درون تابع
def myfunc():
    x = 300
def myinnerfunc():
    print(x)
myinnerfunc()
myfunc()
###
#بازگشت زمانی است که یک تابع خودش را فراخوانی می کند
def countdown(n):
if n <= 0:
print("Done!")
else:
print(n)
countdown(n - 1)
countdown(5)
###
#حالت پایه و حالت بازگشتی
def factorial(n):
# Base case
if n == 0 or n == 1:
return 1
# Recursive case
else:
return n * factorial(n - 1)
print(factorial(5))
###
def fibonacci(n):
if n <= 1:
return n
else:
return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))
###
#تابع input در پایتون
name = input("Enter your name: ")
print("Hello, " + name)
