#Name: Nguyen Vo
#ID: 1673509


#First we need to split the name and age apart
parts = input().split()
Name = parts[0]
#the while loop read input until ending with -1
while Name != -1:
    try:
        age = int(parts[1]) + 1
    #program catch value error that string instead of integer
    except ValueError:
        age = 0
    print('{} {}'.format(Name, age))

    parts = input().split()
    Name = parts[0]
