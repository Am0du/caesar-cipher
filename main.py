#imports replit clear function
from replit import clear
#from the art file it imports logo
from art import logo


#List of alphabet to check through
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#This function decrypts and encodes the message 
def ceaser (text_input, shift_input, cypher_direction):

    cypher_message = ""
    #Checks if the direction is either encode or decode
    if cypher_direction == "encode" or  cypher_direction == "decode":
        for char in text_input:
            #Checks if the text input is the alphabet
            if char in alphabet:
                text_position = alphabet.index(char)
                if cypher_direction == "encode":
                    shift_position = text_position + shift_input
                    cypher_message += alphabet[shift_position]
                    
                elif cypher_direction == "decode":
                    shift_position = text_position - shift_input
                    cypher_message += alphabet[shift_position]
                
            else: 
                cypher_message += char
       

        print(f"Your {cypher_direction}d message is: \n {cypher_message}")
        
    else:
        print("Invalid direction")

#While loop to repeat the function until the user ends it 
run_again = True 
while run_again is True:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    ceaser(text_input = text , shift_input = shift, cypher_direction = direction)

    rerun = input("Type 'yes ' to continue and 'no' to end: ")
    if rerun == 'yes':
        run_again = True
        clear()
    else:
        run_again = False
        clear()
        print("Goodbye")