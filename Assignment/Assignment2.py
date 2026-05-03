import csv


# data = [
#     ['Name', 'Age', 'City'],
#     ['Alice', 30, 'New York'],
#     ['Bob', 25, 'Los Angeles'],
#     ['Charlie', 35, 'Chicago']
# ]



# with open("./Assignment/my.csv", "w", newline='') as file:
#     wirter = csv.writer(file)
#     wirter.writerows(data)

with open("./Assignment/my.csv", "r") as file:
    data = csv.reader(file)
    for row in data:
        print(row)

