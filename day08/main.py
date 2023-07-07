alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

from art import logo


def caesar(input_text, shift_amount, cipher_direction):

    output_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in input_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount

        #ENCRYPTION LOOPING
        if new_position > 25 and cipher_direction == "encode":
            while (new_position > 25):
                new_position %= 25
                new_position -= 1

        # DECRYPTION LOOPING
        if new_position < 0 and cipher_direction == "decode":
            while (new_position < 0):
                new_position += 26

        new_letter = alphabet[new_position]
        output_text += new_letter

    print(f"The {cipher_direction}d text is : {output_text}")


# THE MAIN PROGRAM

print(logo)

program = True

while program:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(input_text=text, shift_amount=shift, cipher_direction=direction)
    run = input(
        "\n\nType 'yes' if you want to go again, else type 'no'. \n").lower()
    if run == "yes":
        program = True
    elif run == "no":
        program = False
        print("Goodbye")

