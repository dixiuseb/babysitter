
from night import Night

print("------------- Babysitter Pay Calculator -------------\n")
print("Enter all times as integers (ex: \"9\" for 9:00 PM)")
print("Start time must be 5:00 PM or later")
print("End time must be 4:00 AM or earlier")
print("Any number >= 5 will be assumed to be PM, any")
print("number <= 4 will be assumed to be AM")
print("")

start = input("Enter start time: ")

bedtime = input("Enter bedtime: ")

end = input("Enter end time: ")

earnings = Night(start=int(start), bedtime=int(bedtime), end=int(end)).earnings()

print("")
print("Earnings for the night: " + str(earnings))
