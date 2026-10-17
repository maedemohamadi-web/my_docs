from visit import Visit
from datetime import date
from patient import Patient
from doctor import Doctor

our_patient=Patient("Rose","Holand",888,54,"female")
doctor1=Doctor("hami","Neurology","190999")
the_visit_date=date(2027,7,6)
visit1=Visit(patient=our_patient,the_doctor=doctor1,the_date=the_visit_date,price=500000)
print(visit1)
