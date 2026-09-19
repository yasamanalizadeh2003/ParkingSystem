import re
class Vehicle():
    def __init__(self, plate_number="",owner_name="",entry_status=""):
        self.plate_number = plate_number
        self.owner_name=owner_name
        self.entry_status=entry_status
    @property
    def plate_number(self):
        return self._plate_number
    @plate_number.setter
    def plate_number(self,value):
        if not value:
            raise ValueError("empty plate number")
        pattern=r"\d{2}[بجدرسصطقلمنوهی]\d{5}"
        if re.fullmatch(pattern,value):
             self._plate_number=value
        else:
            raise ValueError("invalid plate")

    @property
    def owner_name(self):
        return self._owner_name
    @owner_name.setter
    def owner_name(self,value):
        if not value:
            raise ValueError("empty owner name")
        else:
            self._owner_name=value
  
    @property  
    def entry_status(self):
        return self._entry_status
    @entry_status.setter  
    def entry_status(self,value):
        if value in {"enter","exit"}:
           self._entry_status=value         
        else:
            raise ValueError("invalid entry")
      
    def show(self):
        print(self.plate_number,self.owner_name,self.entry_status)  
            
class Car(Vehicle):
   def __init__(self, plate_number="", owner_name="", entry_status="", tedad_sarneshin=0):
       super().__init__(plate_number, owner_name, entry_status)
       self.tedad_sarneshin= tedad_sarneshin
   @property
   def tedad_sarneshin(self):
       return self._tedad_sarneshin
   @tedad_sarneshin.setter
   def tedad_sarneshin(self,value):
       if not value:
           raise ValueError("empty tedad sarneshin")
       else:
           if value>0 and value<=5:
               self._tedad_sarneshin=value
           else:  
            raise ValueError("invalid tedad sarneshin")
                 
class Motorcycle(Vehicle):
    def __init__(self, plate_number="", owner_name="", entry_status="",hajm_motor=0):
        super().__init__(plate_number, owner_name, entry_status)
        self.hajm_motor=hajm_motor

    @property
    def hajm_motor(self):
            return self._hajm_motor
    @hajm_motor.setter
    def hajm_motor(self,value):
        if not value:
            raise ValueError("empty hajm motor")
        else:
            if value>0:
                self._hajm_motor=value
            else:
                raise ValueError("invalid hajm motor")    


# x=Motorcycle("12ی12345","yas","exit"و2)
# x.show()