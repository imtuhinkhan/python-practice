import phonenumbers
from phonenumbers import geocoder, carrier, timezone
number = "+8801717402382"
ch_number = phonenumbers.parse(number, "CH")
location = geocoder.description_for_number(ch_number, "en")
print(ch_number)
print(location)

ro_number = phonenumbers.parse(number, "RO")
carrier = carrier.name_for_number(ro_number, "en")
print(carrier)

gb_number = phonenumbers.parse(number, "GB")
time = timezone.time_zones_for_number(gb_number)
print(time)
