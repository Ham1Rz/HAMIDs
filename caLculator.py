def calculator():
    print("ماشین حساب ساده پایتون")
    print("عملیات:")
    print("1. جمع (+)")
    print("2. تفریق (-)")
    print("3. ضرب (*)")
    print("4. تقسیم (/)")

    choice = input("شماره عملیات را انتخاب کنید (1/2/3/4): ")

    num1 = float(input("عدد اول را وارد کنید: "))
    num2 = float(input("عدد دوم را وارد کنید: "))

    if choice == "1":
        print("نتیجه:", num1 + num2)

    elif choice == "2":
        print("نتیجه:", num1 - num2)

    elif choice == "3":
        print("نتیجه:", num1 * num2)

    elif choice == "4":
        if num2 != 0:
            print("نتیجه:", num1 / num2)
        else:
            print("خطا: تقسیم بر صفر مجاز نیست")

    else:
        print("انتخاب نامعتبر")


calculator()