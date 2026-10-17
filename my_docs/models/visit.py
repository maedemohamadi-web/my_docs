from doctor import Doctor
from medical_service import MedicalService
from patient import Patient
from validation import *

class Visit(MedicalService):
    def __init__(self,patient:Patient,the_date,the_doctor:Doctor,price,service_type="Visit"):
        super().__init__(patient=patient,the_date=the_date,service_type=service_type,price=price)
        self.doctor=the_doctor

    @property
    def the_doctor(self):
        return self.__doctor

    @the_doctor.setter
    def the_doctor(self,value):
        the_doctor_validator(value)
        self.__the_doctor=value

    def __repr__(self):
        return f"Visit({self.__dict__})"