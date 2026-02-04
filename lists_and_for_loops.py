
days_of_the_week = ["Sunday",
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday"]

weekends = weekends_days = ("Saturday", "Sunday")


# for var is list 
print("Days of the week are:")
for day in days_of_the_week:
    if day in weekends_days:
        print(f"{day} is a weekend day!")
    else:
        print(f"{day} is a weekday.")


# enumerate(List) retruns the index and the value for each item in the list
for index, day in enumerate(days_of_the_week):
    print(f"{day} is day number {index + 1} of the week. ") #using + 1 to make 


# continue is a keyword that tells our loop to move on to the next item. No code

for day in days_of_the_week:
    if "u" in day: # strings are just fancy lists, so we can use for and in on 
        continue 
    print(f"{day} does not contain the letter 'u'")