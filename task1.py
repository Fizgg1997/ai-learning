# Task 1

# Store 5 student marks in list.
marks = [50,60,80,100]
# Task 2

# Use loop to print each mark.
for i in marks:
    print(i)

# Task 3

# Print total marks.
print(sum(marks))
# Task 4

# Print average marks.
def average(mymarks):
    total = sum(mymarks)
    return total / len(mymarks)

print(average(marks))
# Task 5

# Use if condition:
for i in marks:
    if i > 80:
        print("Excellent")
    if i < 50:
        print("Fail")
    else:
        print("Pass")