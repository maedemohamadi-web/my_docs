import re
from datetime import date,datetime

#Patient
def name_validator(name):
    if not isinstance(name,str) or not re.match("^[a-zA-Z\s]{3,20}$",name):
        raise ValueError("Invalid Name")
    return name

def family_validator(family):
    if not isinstance(family,str) or not re.match("^[a-zA-Z\s]{3,50}$",family):
        raise ValueError("Invalid Family")
    return family

def code_validator(code):
    if not isinstance(code,int):
        raise ValueError("Invalid Code")
    return code

def age_validator(age):
    if not isinstance(age,int) or age>150:
        raise ValueError("Invalid Age")
    return age

def gender_validator(gender):
    if not isinstance(gender,str) or gender not in ["male","female"]:
        raise ValueError("Invalid Gender")
    return gender

#Doctor
def the_family_validator(the_family):
    if not isinstance(the_family,str) or not re.match("^[a-zA-Z\s]{3,50}$",the_family):
        raise ValueError("Invalid Family")
    return the_family

def specialization_validator(specialization):
    if not isinstance(specialization,str) or specialization not in ["Cardiology","Neurology","Oncology","Pediatrics","Radiology","Emergency Medicine"]:
        raise ValueError("Invalid Specialization")
    return specialization

def medical_council_number_validator(medical_council_number):
    if not isinstance(medical_council_number,str) or not re.match("^[1-9][0-9]{4,5}$",medical_council_number):
        raise ValueError("Invalid Medical Council Number")
    return medical_council_number

#Medical Service
def the_patient_validator(patient):
    if type(patient).__name__!="Patient":
        raise ValueError("Invalid Patient")
    return patient

def the_date_validator(the_date):
    if not isinstance(the_date,(date,datetime)):
        raise ValueError("Invalid Date")
    return the_date

def service_type_validator(service_type):
    if not isinstance(service_type,str) or service_type not in ["Visit","Test","Surgery","Chemotherapy","Vaccination","Physical Therapy","CT","MRI","X-Ray"]:
        raise ValueError("Invalid Service Type")
    return service_type

def price_validator(price):
    if not isinstance(price,int)or price<0:
        raise ValueError("Invalid Price")
    return price

#Visit
def the_doctor_validator(the_doctor):
    if type(the_doctor).__name__!="Doctor":
        raise ValueError("Invalid Doctor")
    return the_doctor