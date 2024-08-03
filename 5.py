def is_leap(year):
    leap = False
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is divisible by 100
        if year % 100 == 0:
            # Check if the year is also divisible by 400
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))