#S3
#list
# ()append یک عنصر را به انتهای لیست اضافه می کند
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)
#
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)
#()clear تمام عناصر یک لیست را حذف می کند.
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

#()copy یک کپی از لیست مشخص شده را برمی گرداند
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)
#()count تعداد شمارش عناصر با مقدار مشخص شده را برمی گرداند
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)
#
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)
#()extend عناصر لیست مشخص شده  را به انتهای لیست فعلی اضافه می کند
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
#()index موقعیت اولین وقوع مقدار مشخص شده را برمی گرداند.
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)
#
fruits =['apple', 'banana', 'cherry', 'kiwi', 'mango',
'orange', 'cherry']
x = fruits.index("cherry", 4)
print(x)
#()insert مقدار مشخص شده را در موقعیت مشخص شده درج می کند.
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)
#()pop عنصر را در موقعیت مشخص شده حذف می کند
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)
# ()remove اولین مورد از عنصری که مقدار مشخص شده را دارد، حذف می کند.
fruits = ['apple','banana','cherry','banana']
fruits.remove("banana")
print(fruits)
# del این دستور می تونه یه آیتم خاص رو از لیست حذف کنه یا حتی کل لیست رو از حافظه پاک کن
my_list = [1, 2, 3]
del my_list[1]
#del my_list
print (my_list)
#()reverse ترتیب مرتب سازی عناصر را معکوس می کند
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
#()sort به طور پیش فرض لیست را به صورت صعودی مرتب می کند
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)


#Tuples



#یک تاپل مجموعه ای است که مرتب و غیرقابل تغییر است .
#تاپل ها )Tuples )با براکت های گرد نوشته می شوند.


thistuple = ("apple", "banana", "cherry")
print(thistuple)


#می توانند آیتم هایی با مقادیر یکسان داشته باشند
thistuple =("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#می توان از سازنده ی ()tuple برای ایجاد یک تاپل استفاده کرد.
thistuple =tuple(("apple", "banana", "cherry"))
# note the double round-brackets
print(thistuple)

#می توانید با ارجاع به شماره اندیس، داخل کروشه، به آیتم های تاپل دسترسی پیدا کنید
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


#اندیس گذاری منفی به معنای شروع از انتها است
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#با مشخص کردن نقطه شروع و پایان محدوده، طیفی از شاخص ها را مشخص کرد
thistuple =("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#تعیین اینکه آیا یک آیتم مشخص شده در یک تاپل وجود دارد یا خیر، ازi
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:print("Yes, 'apple' is in the fruits tuple")


#به روز رسانی تاپل
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#۱ تبدیل به لیست :
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
#.۲ اضافه کردن چندتایی به یک چندتایی
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#تاپل ها غیرقابل تغییر هستند
thistuple = ("apple", "banana", "cherry") 
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
#حذف تاپل
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)
#*به نام متغیر اضافه کنید و مقادیر به صورت یک لیست به متغیر اختصاص داده می شوند
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
#
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
#با استفاده از یک حلقهfor ، آیتم های تاپل را پیمایش کنید
thistuple = ("apple", "banana", "cherry")
for x in thistuple:print(x)
#با استفاده از یک حلقه while ، آیتم های تاپل را پیمایش کنید

thistuple = ("cherry ","banana ","apple") 
i = 0
while i < len(thistuple):print(thistuple[i])
i = i + 1
#برای اتصال دو یا چند تاپل می توانید از عملگر + زیر استفاده کنید
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
#ضرب
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
#()count تعداد دفعاتی که یک مقدار مشخص شده در تاپل ظاهر می شود را برمی گرداند.
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)
#()indexاگر مقدار مورد نظر پیدا نشود، متد یک استثنا ایجاد می کند
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
#مجموعه های پایتون
#()set برای ایجاد یک مجموعه استفاده کرد
thisset = set(("apple", "banana", "cherry"))
print(thisset)
#مجموعه ها به عنوان اشیاء با نوع داده ' set ' تعریف می شوند:
myset = {"apple", "banana", "cherry"}
print(type(myset))
# با استفاده از یک حلقه for ، آیتم های مجموعه را پیمایش کنید، یا با استفاده از کلمه کلیدی in ، وجود یک مقدار مشخص در یک مجموعه را جویا شوید
thisset = {"apple", "banana", "cherry"}
for x in thisset:print(x)
#برای اضافه کردن یک آیتم به یک مجموعه از متد ()add استفاده کنید
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#برای اضافه کردن آیتم ها از یک مجموعه دیگر به مجموعه فعلی، از این متد ()update استفاده کنید
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
#برای حذف یک آیتم در یک مجموعه، از متد ()remove، یا ()discard استفاده کنید
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#()pop روش برای حذف یک آیتم استفاده کنید، اما این روش یک آیتم تصادفی را حذف می کند،
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#()clear مجموعه را خالی می کند
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#el کلیدی مجموعه را به طور کامل حذف می کند
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
#با استفاده از یک حلقه for ، آیتم های مجموعه را پیمایش کنید
thisset = {"apple", "banana", "cherry"}
for x in thisset:print(x)
# ()union یک مجموعه جدید با تمام آیتم های هر دو مجموعه را برمی گرداند
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#|برای اتصال دو مجموعه استفاده کنید:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)
#()union روش به شما امکان می دهد مجموعه ای را با انواع داده دیگر، مانند لیست ها یا تاپل ها، پیوند دهید
x = {"c ","b ","a"}
y = (1, 2, 3)
z = x.union(y)
print(z)
#()update تمام آیتم های یک مجموعه را در مجموعه دیگر درج می کند
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
#()intersection یک مجموعه جدید برمی گرداند که فقط شامل آیتم هایی است که در هر دو مجموعه وجود دارند
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)


#تابع ()frozenset
# ()frozenset یک شیء frozenset در خروجی برمیگرداند که مشابه set است با این تفاوت که نمی تواند تغییر کند
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)
#
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
x[1] = "strawberry"


#دیکشنری


# از دیکشنری ها برای ذخیره مقادیر داده در جفت های کلید: مقدار استفاده می شود. یک دیکشنری مجموعه ای است که مرتب، قابل تغییر و غیرقابل
#تکرار است
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(thisdict)
#
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(thisdict["brand"])


#()dict برای ساخت دیکشنری استفاده کرد
thisdict = dict(name = "John",
age= 36,country= "Norway")
print(thisdict)
#مقدار کلید " model " را دریافت می کند
thisdict = {
"brand": "Ford","model": "Mustang","year": 1964 }
x = thisdict["model"]
print(x)
#()get وجود دارد که همان نتیجه را به شما می دهد:
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = thisdict.get("model")
print(x)
#()keys لیستی از تمام کلیدهای موجود در دیکشنری را برمی گرداند
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = thisdict.keys()
print(x)
#
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x)#after the change
print (car)
#()values لیستی از تمام مقادیر موجود در دیکشنری را برمی گرداند.
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = thisdict.values()
print(x)
#()items هر آیتم را در یک دیکشنری، به عنوان تاپل در یک لیست، برمی گرداند
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = thisdict.items()
print(x)
# در یک دیکشنری وجود دارد یا خیر، از کلمه in کلیدی زیر استفاده کنید:
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
if "model" in thisdict:print("Yes, 'model' is one of the keys in the thisdict dictionary")
#()update ، دیکشنری را با آیتم های موجود در آرگومان داده شده به روزرسانی می کند.
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
#
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# ()pop ، آیتمی را که نام کلید مشخص شده را دارد، حذف می کند:
thisdict ={
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.pop("model")
print(thisdict)
#()popitem آخرین آیتم درج شده را حذف می کند 
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.popitem()
print(thisdict)
# del همچنین می تواند دیکشنری را به طور کامل حذف کند
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
del thisdict["model"]
print(thisdict)
#()clear، دیکشنری را خالی می کند
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.clear()
print(thisdict)


#حلقه زدن در دیکشنری



#با استفاده از حلقه For می توانید در یک دیکشنری حلقه بزنید
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
for x in thisdict:print(thisdict[x])
#
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
for x in thisdict:print(x)
#
thisdict = {
"brand":"Ford",
"model":"Mustang",
"year":1964
}
for x in thisdict:print(x,thisdict[x])




#()values برای برگرداندن مقادیر یک دیکشنری استفاده کنید:
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
for x in thisdict.values():print(x)
#)keys برای برگرداندن کلیدهای یک دیکشنری استفاده کنید
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
for x in thisdict.keys():print(x)
#()items ، روی کلیدها و مقادیرحلقه بزنید:
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
for x, y in thisdict.items():print(x, y)




#کپی از دیکشنری




# ()copy، یک کپی از دیکشنری تهیه کنید
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
mydict = thisdict.copy()
print(mydict)
#راه دیگر برای ایجاد کپی، استفاده از متد ()dict است
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
mydict = dict(thisdict)
print(mydict)






#دیکشنری های تو در تو




myfamily ={
"child1" : {
"name" : "Emil",
"year" : 2004
},
"child2" : {
"name" : "Tobias",
"year" : 2007
},
"child3" : {
"name" : "Linus",
"year" : 2011
}
}
print(myfamily)

#سه دیکشنری را به یک دیکشنری جدید اضافه کنید
child1 = {
"name" : "Emil",
"year" : 2004
}
child2 = {
"name" : "Tobias",
"year" : 2007
}
child3 = {
"name" : "Linus",
"year" : 2011
}
myfamily = {
"child1" : child1,
"child2" : child2,
"child3" : child3
}
print(myfamily)

#دسترسی به آیتم ها
child1 = {
"name" : "Emil",
"year" : 2004
}
child2 = {
"name" : "Tobias",
"year" : 2007
}
child3 = {
"name" : "Linus",
"year" : 2011
}

print( myfamily ["child2"]["name"])

#می توانید با استفاده از ()items روی یک دیکشنری حلقه بزنید
myfamily = {
"child1" : {
"name" : "Emil",
"year" : 2004
},
"child2" : {
"name" : "Tobias",
"year" : 2007
},
"child3" : {
"name" : "Linus",
"year" : 2011
}
}
for x, obj in myfamily.items():print(x)
for y in obj:print(y + ':', obj[y])

#