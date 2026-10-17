from patient import Patient

patient1=Patient("Rose","Holand",888,54,"female")
print(patient1)

patient1.gender="male"
patient1.name="bob"
print(patient1)

print(patient1.age)
patient1.age=78
patient1.family="deer"
print(patient1)
