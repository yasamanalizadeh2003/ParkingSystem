from parking import *
from vehicle import *
from persian import *
parking=ParkingLot()

while True:
    print("______________________________________________________________")
    task=input(rtl("چه کاری میخواهید انجام دهید؟ شماره کار مورد نظر را وارد کنید\n 1.ثبت جایگاه در پارکینگ  \n 2.حذف جایگاه" \
"\n 3.مشاهده جایگاه های خالی \n 4.ورود وسیله نقلیه \n 5.خروج وسیله نقلیه \n 6.مشاهده وسایل نقلیه پارک شده" \
"\n 7.محاسبه هزینه نهایی وسیله نقلیه"))

    try:
        task=int(task)
    except (ValueError,TypeError):
        print(rtl("کار مورد نظر یافت نشد"))
        continue

    if task<1 or task>7:
        print(rtl("کار مورد نظر یافت نشد"))
    elif task==1:
        parking.add_spot()
    elif task==2:
        id=input(rtl("ایدی جایگاه مورد نظر را وارد کنید"))
        try:
            id=int(id)
        except (ValueError,TypeError):
            print(rtl("ایدی مورد نظر یافت نشد"))
            continue
        parking.remove_spot(id)
    elif task==3:
        print(parking.show_free_spots())
    elif task==4:
        vehicle_type=input(rtl("اگر وسیله نقلیه ،ماشین است 1 را وارد کنید و اگر موتور است 2 را وارد کنید"))
        try:
            vehicle_type=int(vehicle_type)
        except (ValueError,TypeError):
            print(rtl("عدد وارد شده معتبر نیست"))
            continue
        if vehicle_type==1:
            plate=input(rtl("پلاک را وارد کنید"))
            owner_name=input(rtl("نام مالک خودرو را وارد کنید"))
            tedad_sarneshin=input(rtl("تعداد سرنشین را وارد کنید"))
            try:
                tedad_sarneshin=int(tedad_sarneshin)
            except (ValueError,TypeError):
                print(rtl("تعداد سر نشین معتبر نیست"))
                continue
            try:
                car=Car(plate,owner_name,"exit",tedad_sarneshin)
                parking.enter_vehicle(car)
            except ValueError as error:
                print(error)   
                continue 
            

        elif vehicle_type==2:
            plate=input(rtl("پلاک را وارد کنید"))
            owner_name=input(rtl("نام مالک موتور را وارد کنید"))
            hajm=input(rtl("حجم موتور را وارد کنید"))
            try:
                hajm=int(hajm)
            except (ValueError,TypeError):
                print(rtl(" حجم موتور معتبر نیست"))
                continue
            try:
                motor=Motorcycle(plate,owner_name,"exit",hajm)
                parking.enter_vehicle(motor) 
            except ValueError as error:
                print(error)   
                continue  
        else:
            print(rtl("فقط عدد 1 یا 2را وارد کنید"))      

    elif task==5:
        plate=input(rtl("پلاک را وارد کنید"))
        hour=input(rtl("ساعات توقف را وارد کنید"))  
        try:
            hour=int(hour)
        except (ValueError,TypeError):
            print(rtl("ساعت وارد شده معتبر نیست"))
            continue
        if hour<0 :
            print(rtl("ساعت وارد شده معتبر نیست"))
            continue
        parking.exit(plate,hour)
    elif task==6:
        parking.show_parked_vehicles()
    elif task==7:
        plate=input(rtl("پلاک را وارد کنید"))
        hour=input(rtl("ساعات توقف را وارد کنید"))  
        try:
            hour=int(hour)
        except (ValueError,TypeError):
            print(rtl("ساعت وارد شده معتبر نیست"))
            continue
        if hour<0 :
            print(rtl("ساعت وارد شده معتبر نیست"))
            continue

        parking.final_cost(plate,hour) 



