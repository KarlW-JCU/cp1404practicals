"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

MENU_STRING = ("[H]ello\n"
               "[G]oodbye\n"
               "[Q]uit")

name = input("Enter name: ")
print(MENU_STRING)
selection = input(">>> ").upper()
while selection != "Q":
    if selection == 'H':
        print(f"Hello {name}.")
    elif selection == 'G':
        print(f"Goodbye {name}.")
    else:
        print(f"Invalid choice.")
    print(MENU_STRING)
    selection = input(">>> ").upper()
print("Finished.")
