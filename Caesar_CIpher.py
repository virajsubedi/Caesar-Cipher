import string

# Create a string of all uppercase alphabets
alphabets = (string.ascii_uppercase)

# Function to display a welcome message
def welcome():
    print('Welcome to the Caesar Cipher\nThis program encrypts and decrypts text using Caesar Cipher.')

# Function to encrypt the plaintext using the given key
def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.upper()  # Convert letter to uppercase
        if letter == " ":
            ciphertext += letter  # Keep spaces as is
        if not letter == ' ':
            index = alphabets.find(letter)  # Find index of letter in alphabets
            if index == -1:
                ciphertext += letter  # If character is not in alphabets, keep it as is
            else:
                new_index = index + key  # Shift the letter by the key value
                if new_index >= 26:
                    new_index -= 26  # Wrap around if new index exceeds 25
                ciphertext += alphabets[new_index]
    print(ciphertext)  # Print the encrypted message
    
    # Ask user if they want to encrypt or decrypt another message
    while True:
        againnn = input("Do you want to encrypt or decrypt again? (y/n)")
        if againnn == "y":
            combine()  # Call the main function to restart the process
            break
        elif againnn == "n":
            thanks()  # Thank the user and end the program
            break
        else:
            print("Invalid Input")
            continue    

# Function to decrypt the ciphertext using the given key
def decrypt(ciphertext, key):
    plaintext = ' '
    for letter in ciphertext:
        letter = letter.upper()  # Convert letter to uppercase
        if letter == " ":
            plaintext += letter  # Keep spaces as is
        if not letter == ' ':
            index = alphabets.find(letter)  # Find index of letter in alphabets
            if index == -1:
                plaintext += letter  # If character is not in alphabets, keep it as is
            else:
                new_index = index - key  # Shift the letter back by the key value
                if new_index < 0:
                    new_index += 26  # Wrap around if new index is negative
                plaintext += alphabets[new_index]
    print(plaintext)  # Print the decrypted message
    
    # Ask user if they want to encrypt or decrypt another message
    while True:
        againnn = input("Would you like to encrypt or decrypt another message? (y/n):")
        if againnn == "y":
            combine()  # Call the main function to restart the process
            break
        elif againnn == "n":
            thanks()  # Thank the user and end the program
            break

# Display the welcome message
welcome()

# Main function to get user input and perform encryption or decryption
def main():
    while True:
        input_of_user = input('Would you like to encrypt(e) or decrypt(d)?: ')
        if input_of_user == 'e':
            text = input('What message would you like to encrypt: ')
            # Ensure the user enters a valid shift number
            while True:
                try:
                    Shift_number = int(input('What is the shift number: '))
                    ciphertext = encrypt(text, Shift_number)
                    break
                except ValueError:
                    print("Enter a valid number!")
                    continue
            break        
        elif input_of_user == 'd':
            text = input('What message would you like to decrypt: ')
            # Ensure the user enters a valid shift number
            while True:
                try:
                    Shift_number = int(input('What is the shift number: '))
                    plaintext = decrypt(text, Shift_number)
                    break
                except ValueError:
                    print("Enter a valid number!")
                    continue
            break 
        else:
            print("Invalid Mode")
            continue

# Function to thank the user
def thanks():
    print("Thanks for using the program, goodbye!")

# Function to combine and restart the main function
def combine():
    main()

# Start the program
combine()
