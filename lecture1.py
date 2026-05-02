# print("This is Faizan Tanveer")
# for i in marks:
    # print(i)

marks = [1,2,3,4,5]




def myaverage(mylist):
    total = 0
    a = len(mylist)
    for i in mylist:
        total+=i
    return total, a

total_m, count = myaverage(marks)

print(total_m/count)


# print(addfu(1,4))

# print(addfu(9,3))



