#Name: Nguyen Vo
#ID: 1673509

#define the function take list and sort descending
def selection_sort_descend_trace(ascenList):
    for i in range(len(ascenList) - 1):
        index = i
        #nested loop that compare value then swap descending order
        for j in range(i + 1, len(ascenList)):
            if ascenList[index] < ascenList[j]:
                index = j
        ascenList[i], ascenList[index] = ascenList[index], ascenList[i]
        #print output
        for num in ascenList:
            print(num, end=" ")
        print()
    return ascenList



#main part
if __name__ == "__main__":
    numbers = [int(x) for x in input("").split()]
    selection_sort_descend_trace(numbers)
