from vehicle import *
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
         spot_type=input("if it's a car spot write car, if it's a motorcycle spot write motor. if you want to exit click enter")
         if spot_type=="car" or spot_type=="motor":
            if spot_type=="car":
               car=CarSpot()
               self.spots.append(car)
            elif spot_type=="motor":
               motor=MotorcycleSpot()
               self.spots.append(motor)
         else:
            break 
    def find_spot(self,id):
         for spot in self.spots:
            if spot.spot_id==id:
               return spot
         else:
            print("جایگاه پیدا نشد")   

    def remove_spot(self,id):
      if self.spots:
         selected_spot=self.find_spot(id)
         if selected_spot==None:
            print("جایگاه مورد نظر وجود ندارد")
         elif selected_spot.is_occupied==True:
            print("جایگاه پر است") 
         else:   
            self.spots.remove(selected_spot)
            print("جایگاه حذف شد")
      else:
          print("جایگاهی در پارکینگ وجود ندارد")

    def show_free_spots(self):
       free_spots=list()
       for spot in self.spots:
          if spot.is_occupied==False:
             free_spots.append({"id":spot.spot_id})
       return free_spots 
     
    def find_vehicle(self,plate):
      for spot in self.spots:
         if spot.parked_vehicle!=None and plate==spot.parked_vehicle.plate_number:
            return spot
               
    def enter_vehicle(self,vehicle):
         for spot in self.spots:
            if spot.parked_vehicle!= None:
               continue
            elif spot.is_occupied==True:
               continue
            elif isinstance(vehicle,Car) and isinstance(spot,CarSpot):
                  print("ورود ماشین انجام شد")
                  spot.is_occupied=True
                  spot.parked_vehicle=vehicle
                  vehicle.entry_status="enter"
                  break
            elif isinstance(vehicle,Motorcycle) and isinstance(spot,MotorcycleSpot):
                  print("ورود موتور انجام شد")
                  spot.is_occupied=True
                  spot.parked_vehicle=vehicle
                  vehicle.entry_status="enter"
                  break
         else:
            print("جایگاه مناسبی وجود ندارد")   
    def exit(self,plate):
      selected_spot=self.find_vehicle(plate) 
      if selected_spot:
         print(f"خروج پلاک {plate} انجام شد")
         selected_spot.is_occupied=False
         selected_spot.parked_vehicle.entry_status="exit"
         selected_spot.parked_vehicle=None
      else:
         print("ماشین پیدا نشد") 
    def show_parked_vehicles(self):
      parked_vehicles=list()
      for spot in self.spots:
         if spot.is_occupied==True:
            parked_vehicles.append({"plate":spot.parked_vehicle.plate_number,"owner name":spot.parked_vehicle.owner_name})
      return parked_vehicles   

    def final_cost(self,plate,hour):
       selected_spot=self.find_vehicle(plate)
       constatnt_cost=10000
       if selected_spot==None:
          return("وسیله موردنظر موجود نیست")
       elif hour<5:
         return constatnt_cost+selected_spot.hourly_rate*hour
       else:
         jarime=50000
         return constatnt_cost+selected_spot.hourly_rate*hour + jarime
          