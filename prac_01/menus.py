MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Please enter your name:")
print(MENU)
choice = input(">>>").upper()
while choice != "Q":
    if choice == "H":
        print(f"hello {name}")
    elif choice == "G":
        print(f"goodbye {name}")
    else:
        print("invalid message")
    print(MENU)
    choice = input(">>>").upper()
print("Program finished")
