from datetime import *

oggi = date.today()
print(f"oggi è: {oggi}")

print(f"oggi è il mese: {oggi.month}, dell'anno: {oggi.year},e n avemu {oggi.day}")

print(oggi.weekday())
giorni = ["lun", "mart", "merc", "giov", "ven", "sab", "dom"]
print(giorni[oggi.weekday()])