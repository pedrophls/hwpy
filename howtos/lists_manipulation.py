ten_things = "Apples Oranges Crows Telephone Light Sugar"
stuff = ten_things.split(' ')

len(ten_things)

if len(stuff) < 10:
    more_stuff = ["Day", "Night", "Song", "Frisbee",
            "Corn", "Banana", "Girl", "Boy"]
    while len(stuff) != 10:
        next_item = more_stuff.pop()
        stuff.append(next_item)

if len(stuff) > 10:
    while len(stuff) != 10:
        stuff.pop()

print(f"There are {len(stuff)} itens on the list now!")

print(f"stuff -1 {stuff[-1]}")

print(' '.join(stuff))