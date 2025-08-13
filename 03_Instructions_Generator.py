def instructions():
    print('''
  Instructions:
- template task 1
- template task 2
- template task 3 
    ''')

x = input("press enter to display instructions or any letter then enter to skip.")

if x == "":
    instructions()
