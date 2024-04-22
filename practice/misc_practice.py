groups = [["Alice", "Bob"], ["Carl", "David", "Elise"], ["Francis", "Georgia"]]
i = 1
for group in groups:
    print("Group" + str(i) + " members:")
    i = i + 1
    for name in names: # names is wrong here
        print(name)