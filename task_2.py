
import random
import string


users = []

#Random string generator
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#Email verifyer
def email_verify(email):
	if '@' and '.' not in email:
		return False
	else:
		return True

print("Welcome to Hng tech")

first_name = input("First Name: ")
last_name = input("Last Name: ")
email = input("Email Address: ")
while email_verify(email)==False:
	email = input("Not a valid email address! Try again\nEmail Address: ")

password = first_name[:2]+last_name[:2]+randomString(5)
print("Your Password: "+password)
ask = input("do you like the password? please reply 'yes' or 'no'.")

if ask.lower() != 'yes':
	password = input("Please input your preferred password (not less than 7 characters:\n")
	while len(password) < 7:
		password = input("Improper password length, please input your password again (not less than 7 characters)")
else:
	user = {'fn':first_name, 'ln':last_name, 'em':email, 'pw':password,}
	print("Your information:\n\tFirst Name: "+user.fn+"\n\tLast Name: "+user.ln+"\n\tEmail: "+user.em+"\n\tPassword: "+user.pw)
	users.append(user)


