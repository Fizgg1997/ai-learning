# with open("./Assignment/notes.txt", "w") as file:
#     file.write("This is assignment for the knowledge check")
#     file.close()



with open("./Assignment/notes.txt", "r") as file:
    data = file.read()
    print(data)