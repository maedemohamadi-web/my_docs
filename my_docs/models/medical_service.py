from patient import Patient
from validation import *

class MedicalService:
    def __init__(self,patient:Patient,the_date,service_type,price):
        self.patient=patient
        self.the_date=the_date
        self.service_type=service_type
        self.price=price

    @property
    def patient(self):
        return self.__patient

    @patient.setter
    def patient(self,value):
        the_patient_validator(value)
        self.__patient=value

    @property
    def the_date(self):
        return self.__the_date

    @the_date.setter
    def the_date(self,value):
        the_date_validator(value)
        self.__the_date=value

    @property
    def service_type(self):
        return self.__service_type

    @service_type.setter
    def service_type(self,value):
        service_type_validator(value)
        self.__service_type=value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        price_validator(value)
        self.__price=value

    def __repr__(self):
        return f"MedicalService({self.__dict__})"