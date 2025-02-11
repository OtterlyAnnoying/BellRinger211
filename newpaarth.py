from datetime import datetime

c = datetime.now()

minNow = 60*int(c.strftime("%H")) + int(c.strftime("%M"))

minThen = 14*60 + 19

print(str(int(minThen) - int(minNow)) + " minutes")
