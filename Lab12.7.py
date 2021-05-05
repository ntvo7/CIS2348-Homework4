#Name: Nguyen Vo
#ID: 1673509


#First, we get input the person age range (18 - 75)
def get_age():
    age = int(input())
    #Raise message if wrong input
    if age < 18 or age > 75:
        raise ValueError('Invalid age.')
    return age

#calculating adult's fat burning heart rate
def fat_burning_heart_rate(age):
    return (220 - age)* .70


#main part
if __name__ == "__main__":
    try:
        age = get_age()
        print("Fat burning heart rate for a", age, "year-old:", fat_burning_heart_rate(age), "bpm")
    except ValueError as e:
        print(e)
        print("Could not calculate heart rate info.\n")