#6
#ایجاد یک کالس و شی
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)
#
#متدهای کالس پایتون
#__init__  این‌متد‌سازنده (Constructor (است
#greet یک‌متد‌معمولی‌است‌که‌باید‌به‌صورت‌دستی‌فراخوانی‌شود
class Person:
    def __init__(self, name):
        self.name = name
def greet(self):
    print("Hello, my name is " + self.name)
p1 = Person("Emil")
p1.greet()
#متدهای دارای پارامتر
class Calculator:
    def add(self, a, b):
        return a + b
def multiply(self, a, b):
    return a * b
calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))
#متد ()__init__
#سازنده‌ای‌که‌هنگام‌ساخت‌شیء‌اجرا‌می‌شود‌و‌ویژگی‌ها‌را‌مقداردهی‌می‌کند
#هر‌بار‌که‌از‌کالس‌برای‌ایجاد‌یک‌شیء‌جدید‌استفاده می‌شود‌،به‌طور‌خودکار‌فراخوانی‌می‌شود‌
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Emil", 36)
print(p1.name)
print(p1.age)
#پارامتر self در متد پایتون
#self همیشه‌اولین‌پارامتر‌متدهای‌کالس‌است. به‌شیء‌جاری‌)همان‌نمونه‌ای‌که‌ساخته‌شده(‌اشاره‌می‌کندبا‌استفاده‌از‌ self می‌توانیم‌به‌ویژگی‌ها‌و‌متدهای‌همان‌شیء‌دسترسی‌داشته‌باشیم
class Person:
    def __init__(self, name):
        self.name = name
def printname(self):
    print(self.name)
p1 = Person("Tobias")
p2 = Person("Linus")
p1.printname()
p2.printname()
#دسترسی به ویژگی ها
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
car1 = Car("Toyota", "Corolla")
print(car1.brand)
print(car1.model)
#روشی که مقدار یک ویژگی را تغییر می دهد
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def celebrate_birthday(self):
    self.age += 1
    print(f" Happy birthday! You are now {self.age}")
p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()
#str این متد‌،یک‌متد‌ویژه‌است‌که‌کنترل‌می‌کند‌هنگام‌چاپ‌شیء‌،چه‌چیزی‌برگردانده‌شود
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Emil", 36)
print(p1)
#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def __str__(self):
    return f"{self.name} ({self.age})"
p1 = Person("Tobias", 36)
print(p1)
#ایجاد چندین متد در یک کالس
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
def add_song(self, song):
    self.songs.append(song)
print(f"Added: {song}")
def remove_song(self, song):
    if song in self.songs:
        self.songs.remove(song)
print(f"Removed: {song}")
def show_songs(self):
    print(f"Playlist '{self.name}':")
for song in self.songs:
    print(f"- {song}")
my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()
#حذف یک متد از یک کالس
class Person:
    def __init__(self, name):
        self.name = name
def greet(self):
    print("Hello!")
p1 = Person("Emil")
del Person.greet
p1.greet() # This will cause an error
#ایجاد کالس والد برای‌ایجاد‌کالسی‌که‌عملکرد‌را‌از‌کالس‌دیگری‌به‌ارث‌می‌برد‌،هنگام‌ایجاد‌کالس‌فرزند‌،کالس‌والد‌را‌به‌عنوان‌پارامتر‌ارسال‌کنید 
x = Student("Mike", "Olsen")
x.printname()
#ایجاد یک کالس داخلی
class Outer :
    def __init__(self):
        self.name = "Outer Class"
class Inner:
    def __init__(self):
        self.name = "Inner Class"
def display(self):
    print("This is the inner class")
outer = Outer()
print(outer.name)
#دسترسی به کالس داخلی از بیرون
#برای‌دسترسی‌به‌کالس‌داخلی‌،ابتدا‌یک‌شیء‌از‌کالس‌خارجی‌ایجاد‌کنید‌و‌سپس‌یک‌شیء‌از‌کالس‌داخلی‌بسازید
class Outer :
    def __init__(self):
        self.name = "Outer"
class Inner:
    def __init__(self):
        self.name = "Inner"
def display(self):
    print("Hello from inner class")
outer = Outer()
inner = outer.Inner()
inner.display()
#دسترسی به کالس بیرونی از کالس درونی
#گر‌می‌خواهید‌کالس‌داخلی‌به‌کالس‌خارجی‌دسترسی‌داشته‌باشد‌،باید‌نمونه‌کالس‌خارجی‌را‌به‌عنوان‌پارامتر‌ارسال‌کنید
class Outer :
    def __init__(self):
        self.name = "Emil"
class Inner:
    def __init__(self, outer):
        self.outer = outer
def display(self):
    print(f"Outer class name:{self.outer.name}")
outer = Outer()
inner = outer.Inner(outer)
inner.display()
#
#از یک کالس داخلی برای نمایش موتور ماشین استفاده کنید
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()
class Engine:
    def __init__(self):
        self.status = "Off"
def start(self):
    self.status = "Running"
print("Engine started")
def stop(self):
    self.status = "Off"
print("Engine stopped")
def drive(self):
    if self.engine.status == "Running":
        print(f"Driving the {self.brand} {self.model}")
    else:
        print("Start the engine first!")
car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()
#چندین کالس داخلی
#یک کالس می تواند چندین کالس داخلی داشته باشد
class Computer :
    def __init__(self):
        self.cpu = self.CPU()
        self.ram = self.RAM()
class CPU:
    def process(self):
        print("Processing data...")
class RAM:
    def store(self):
        print("Storing data...")
computer = Computer()
computer.cpu.process()
computer.ram.store()
#چندریختی پایتون
#چندریختی‌اغلب‌در‌متدهای‌کالس‌استفاده‌می‌شود‌،جایی‌که‌می‌توانیم‌چندین‌کالس‌با‌نام‌متد‌یکسان‌داشته‌باشیم
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
def move(self):
    print("Drive!")
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
def move(self):
    print("Sail!")
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
def move(self):
    print("Fly!")
car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object
for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
#