from cryptography.fernet import Fernet

def generateKey():
	key = Fernet.generate_key()
	FILE = open('secerateKey.txt','w')
	FILE.write(key)
	FILE.close()
	print("A new key has successfully been generated")
	return key

def importKey():
		FILE = open('secerateKey.txt','r')
		key = FILE.read()
		return key
		

def encrypt():
	while 1:
		choice = raw_input("ENCRYPTION MENU:\n 1)Import an existing key \n 2)Generate a new key\n 99)Go Back\n")
		if  choice == "1":
			try:
				key = importKey()
				break
			except:
				c1 = raw_input("No valid key found!\nWould you like to generate a new one?(y/n)")
				if c1.upper() == 'Y':
					key = generateKey()
					break
				elif c1.upper() == 'N':
					print("Returning to preivous menu...")
				else:
					print("Invalid choice returning to previous menu...")
		elif choice == "2":
			print ("Generating...")
			key = generateKey()
			break
		elif choice == "99":
			print	("Going back")
			return
		else:
			print ("Invalid choice!")
			pass
	plainTextmsg = raw_input("Input the message you would like to encrypt:\t")
	encryptor = Fernet(key)
	cipherText = encryptor.encrypt(plainTextmsg)
	FILE = open("SecerateMsg.txt","w")
	FILE.write(cipherText)
	FILE.close()
	print("Message successfully encyrpted!")
	return

def decrypt():
	try:
		FILE = open("SecerateMsg.txt","r")
		cipherText = FILE.read()
		FILE.close()
	except:
		print("No valid cipher text found returning to main menu...")
		return
	try:
		key = importKey()
	except:
		print("No valid key found returning to main menu...")
		return
	decryptor = Fernet(key)
	plainText = decryptor.decrypt(cipherText)
	print("Message successfuully decrypted:\t"+plainText)
	x = raw_input("Press enter to continue")

print("Adam Lock's Assessable Workshop 1. Student number: 10424430")
while 1:
	choice = raw_input("MAIN MENU\nWhat would you like to do?\n 1)Generate a new key\n\
 2)Encrypt a message\n 3)Decrpyt a message\n 99)Exit program\n")
	if choice == "1":
		generateKey()
	elif choice == "2":
		encrypt()
	elif choice == "3":
		decrypt()
	elif choice == "99":
		break
	else:
		print("Invalid choice")

