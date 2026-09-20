from vehicle import *
from persian import *
class ParkingSpot():
   id=1
   def __init__(self ,is_occupied=False ,parked_vehicle=None ,hourly_rate=0 ):
      self.spot_id=ParkingSpot.id
      self.is_occupied=is_occupied
      self.parked_vehicle=parked_vehicle
      self.hourly_rate=hourly_rate
      ParkingSpot.id+=1

class CarSpot(ParkingSpot):
   def __init__(self, is_occupied=False, parked_vehicle=None, hourly_rate=30000):
      super().__init__(is_occupied, parked_vehicle, hourly_rate)
  
class MotorcycleSpot (ParkingSpot):
   def __init__(self, is_occupied=False, parked_vehicle=None, hourly_rate=20000):
      super().__init__(is_occupied, parked_vehicle, hourly_rate)
  
class ParkingLot():
    def __init__(self):
       self.spots=list()
    def add_spot(self): 
       while True:
         spot_type=input(rtl("اگر جایگاه مربوط به ماشین است 1 را وارد کنید و اگر جایگاه مربوط به موتور است 2 را وارد کنید."
         "اگر میخواهید خارج شوید دکمه enter را بزنید"))
         if spot_type=="":
            break
         try:
            spot_type=int(spot_type)
         except (ValueError,TypeError):
            print(rtl("کار مورد نظر یافت نشد"))
            continue
         
         if spot_type==1 or spot_type==2:
            if spot_type==1:
               car_spot=CarSpot()
               self.spots.append(car_spot)
            elif spot_type==2:
               motor_spot=MotorcycleSpot()
               self.spots.append(motor_spot)
         else:
            print(rtl("فقط عدد 1 یا 2 را وارد کنید"))
            continue

    def find_spot(self,id):
         for spot in self.spots:
            if spot.spot_id==id:
               return spot
    def remove_spot(self,id):
      if self.spots:
         selected_spot=self.find_spot(id)
         if selected_spot==None:
            print(rtl("جایگاه مورد نظر وجود ندارد"))
         elif selected_spot.is_occupied==True:
            print(rtl("جایگاه پر است")) 
         else:   
            self.spots.remove(selected_spot)
            print(rtl("جایگاه حذف شد"))
      else:
          print(rtl("جایگاهی در پارکینگ وجود ندارد"))

    def show_free_spots(self):
       free_spots=list()
       for spot in self.spots:
          if spot.is_occupied==False:
             free_spots.append({"id":spot.spot_id,"type":type(spot).__name__})
       return free_spots 
     
    def find_vehicle(self,plate):
      for spot in self.spots:
         if spot.parked_vehicle!=None and plate==spot.parked_vehicle.plate_number:
            return spot
               
    def enter_vehicle(self,vehicle):
         if self.find_vehicle(vehicle.plate_number)!=None:
            print(rtl("وسیله نقلیه در پارکینگ ، پارک شده است"))
            return
         for spot in self.spots:
            if spot.parked_vehicle!= None or spot.is_occupied==True:
               continue
            elif isinstance(vehicle,Car) and isinstance(spot,CarSpot):
                  print(rtl("ورود ماشین انجام شد"))
                  spot.is_occupied=True
                  spot.parked_vehicle=vehicle
                  vehicle.entry_status="enter"
                  break
            elif isinstance(vehicle,Motorcycle) and isinstance(spot,MotorcycleSpot):
                  print(rtl("ورود موتور انجام شد"))
                  spot.is_occupied=True
                  spot.parked_vehicle=vehicle
                  vehicle.entry_status="enter"
                  break
         else:
            print(rtl("جایگاه مناسبی وجود ندارد"))   
    def exit(self,plate,hour):
      selected_spot=self.find_vehicle(plate) 
      if selected_spot:
         self.final_cost(plate,hour)
         print(rtl(f"خروج پلاک {plate} انجام شد"))
         selected_spot.is_occupied=False
         selected_spot.parked_vehicle.entry_status="exit"
         selected_spot.parked_vehicle=None
      else:
         print(rtl("وسیله نقلیه پیدا نشد")) 
    def show_parked_vehicles(self):
      parked_vehicles=list()
      for spot in self.spots:
         if spot.is_occupied==True:
            parked_vehicles.append({rtl("پلاک"):spot.parked_vehicle.plate_number,rtl("نوع وسیله"):type(spot.parked_vehicle).__name__})
      print(parked_vehicles )  

    def final_cost(self,plate,hour):
       if hour < 0:
        print(rtl("ساعت توقف نمی‌تواند منفی باشد"))
        return
       selected_spot=self.find_vehicle(plate)
       constatnt_cost=10000
       if selected_spot==None:
          print(rtl("وسیله موردنظر موجود نیست"))
          return
       elif hour<5:
         print(constatnt_cost+selected_spot.hourly_rate*hour)
       else:
         jarime=50000
         print(constatnt_cost+selected_spot.hourly_rate*hour + jarime) 
          