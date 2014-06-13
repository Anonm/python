maintext = input("Please enter Plaintext to Cipher: ")
number_shift = int(input("Please enter the shift: "))
#creating a blank variable ciphed
ciphed = ''
#every single string till maintext
for s in maintext:
    x= ord(s)#this probably takes the ascii code needed for the shifting of letters
    x= x + number_shift
    
    ciphed += chr(x)#here the chiped letter takes all the letters to be shifted 
#here is just to ask whether you want to see or not
m = input("Your text has been chiped.\nWant to see the ciphed text and your main text together?(y/n): ")
if m == "y":
    print ("\nYour main text was: "+maintext)
    print ("\nYour chiped text was: "+ciphed)
    input("press enter to close.....")
else:
    print ("It wont be shown ;)")
    input("press enter to close.....")
