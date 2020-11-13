#pip install faker
from faker import Faker
fake = Faker()

#Printing the fake info
print(fake.name())
print(fake.email())
print(fake.country())
print(fake.latitude(), fake.longitude())
print(fake.url())