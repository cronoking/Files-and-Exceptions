import time
import os

#simulates a horrible ms-dos environment
print("File >")
time.sleep(1)
print("Save >")
time.sleep(1)
print(".", end="", flush = True)
time.sleep(1)
print(".", end="", flush = True)
time.sleep(1)
print(".", end="", flush = True)
time.sleep(1)

#takes the file path and name and creates a file at that location
def get_data(fileName, filePath):
  fileName = str(fileName + ".txt")
  filePath = str(filePath + fileName)
  try:
    with open(filePath, 'w') as file:
      file.write(f"{name},{address},{phone}")
  except:
    print("An error has occured.")
  return(filePath)

#reads the file, puts the data in a list, and prints it
def show_data(filePath):
  with open(filePath, 'r') as file:
    data = file.read()
  info = data.split(",")
  print(f"Name: {info[0]} \nAddress: {info[1]} \nPhone Number: {info[2]}")
  
#main loop
while (True):
  file_path = input("\nWhere would you like to save your file(Q to Quit): ")
  file_path = str(file_path)
  if file_path.title() == "Q":
    print("Have a good day!")
    quit()
  elif os.path.isdir(file_path):
    file_name = input("What is the file name: ")
    print("Let's get some info.")
    name = input("Please enter your name: ")
    address = input("Next, your address: ")
    phone = input("And finally, your phone number: ")
    file_path = get_data(file_name, file_path)
    show_data(file_path)
  else:
    print("That directory doesn't exist!")
  