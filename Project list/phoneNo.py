# phone no detail conuntry, sm, kon se country time jum main hai india just like austelliya

import phonenumbers
from phonenumbers import timezone,gecoder,carrier
number = input("Enter Your No. with +__:")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone, "en")
reg = gecoder.description_for_number(phone,"en")
print(time)
print(car)
print(time)
print(reg)