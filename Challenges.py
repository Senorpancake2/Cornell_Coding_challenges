print()

#Challenge 1

hours = int(input("How many hours did Denise work:"))

if hours >= 48:
    print("Not Possible")
elif hours >= 24:
    print("Hours slept:", hours-24)
else:
    print("Hours slept:", 24-hours)

    #Challenge 2

score=int(input("Enter score: "))

wins = score%42

ties = wins%10

print(ties)


#Challenge 3

