row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]

map = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}\n")


treasure=input("Where do you want to put the treasure")

horizontal = int(treasure[0]) - 1
vertical = int(treasure[1]) - 1

row = map[vertical][horizontal] = "X"

print(f"{row1}\n{row2}\n{row3}\n")