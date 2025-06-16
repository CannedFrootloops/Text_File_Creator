Text_File_Creatorname = input("What's your name? \n")
color = input("What's your favorite color? \n")
with open('example.txt', 'w') as file:
    file.write(f"{Text_File_Creatorname} created this file")
    file.write(f"{color} is their favorite color")