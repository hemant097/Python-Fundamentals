# Match-case statement (like switch)

# using multiple if elif
def day_of_week(day):
    if day==1:
        return "Monday"
    elif day==2:
        return "Tuesday"
    elif day==3:
        return "Wednesday"
    elif day==4:
        return "Thursday"
    elif day==5:
        return "Friday"
    elif day==6:
        return "Saturday"
    elif day==7:
        return "Sunday"
    else:
        return "Not a valid day"

# print(day_of_week(2))

#using match
def day_of_week_match(day):
    match (day):
        case 1 :
            return "Monday"
        case 2 :
            return "Tuesday"
        case 3 :
            return "Wednesday"
        case 4 :
            return "Thursday"
        case 5 :
            return "Friday"
        case 6 :
            return "Saturday"
        case 7:
            return "Sunday"
        case _: #default case
            return "Not a valid day"

print(day_of_week_match(2))

def is_weekend(day):
    match (day):
        case "Friday" | "Saturday" | "Sunday" : return True
        case _: return False

print(is_weekend("Sunday"))
