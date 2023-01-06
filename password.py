import hashlib

# Ask the user to enter a password. Correct password is 'password1234'
password = input("Enter a password: ")

# Create a hash of the password using the sha256 algorithm
password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

#Display the hash of the text input by the user, this is just for testing purposes and would be removed in production.
print (password_hash)

# Store the known hash
known_hash = "b9c950640e1b3740e98acb93e669c65766f6670dd1609ba91ff41052ba48c6f3"

# Compare the password hash with the known hash
if password_hash == known_hash:
    print("The password is correct")
else:
    print("The password is incorrect")
