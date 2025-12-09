print()


hours = int(input("How many hours did Denise sleep:"))

if hours >= 48:
    print("Not Possible")
elif hours >= 24:
    print(hours-24)
else:
    print(24-hours)