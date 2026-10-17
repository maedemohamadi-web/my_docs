from medical_service import MedicalService
from datetime import date
from patient import Patient

our_patient=Patient("Rose","Holand",888,54,"female")
the_service_date=date(2027,7,6)
my_medical_service=MedicalService(our_patient,the_service_date,"Surgery",50000000)
print(my_medical_service)
my_medical_service.patient=Patient("Bob","Holand",878,94,"male")
print(my_medical_service)

my_medical_service.service_type="CT"
my_medical_service.the_date=date(2026,12,11)
my_medical_service.price=100000000
print(my_medical_service)