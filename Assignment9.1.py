'''
Mia Coleman
August 3, 2020
CIS 245
Assignment 9.1

This week we will create a program that performs file processing activities. 
Your program this week will use the OS library in order to validate that a directory 
exists before creating a file in that directory.  Your program will prompt the user 
for the directory they would like to save the file in as well as the name of the file.  
The program should then prompt the user for their name, address, and phone number.  
Your program will write this data to a comma separated line in a file and store the 
file in the directory specified by the user. 

Once the data has been written your program should read the file you just wrote to the 
file system and display the file contents to the user for validation purposes. 

Submit a link to your Github repository.
'''

import os
# Imports operating system

print("\nLet's create a text file!\n")

directory = input("Enter the directory you want to save the file: ")
# Gets the name of the directory to use from the user.

if os.path.isdir(directory):
# Checks if the directory path entered by the user exists. If true, asks user for
# input (file name, name, address, and phone number). Using the information from the 
# user, it writes a file (fileName) that contains (name, address, and phoneNum). After
# writing the file, the file is opened and read, contents of the file are then printed.
	fileName = input("Enter the file name (include .txt): ")
	name = input("Enter your name: ")
	address = input("Enter your address: ")
	phoneNum = input("Enter your phone number: ")

	writeFile = open(os.path.join(directory, fileName),"w")
	# Creates file path in the directory.
	writeFile.write(name+', '+address+', '+phoneNum+'\n')
	# Writes the .txt file (name, address, phoneNum) with user input.
	writeFile.close()

	print("\nFile contents: ")
	readFile = open(fileName,"r")
	# Opens the file that was created and reads it.
	print(readFile.read())
	# Prints the contents of the file.
	readFile.close()
else:
	print("Sorry! That directory does not exist!")