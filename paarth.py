hNow = int(input("what is the hour now (use 24 hr clock)? ")) 
mNow = int(input("what is the minute now (use 24 hr clock)? "))

hThen = int(input("what is the hour when class ends (use 24 hr clock)? "))
mThen = int(input("what is the minute when class ends (use 24 hr clock)? "))

timeNow = 60*hNow + mNow
timeThen = 60*hThen + mThen

print(str(timeThen - timeNow) + " minutes")
