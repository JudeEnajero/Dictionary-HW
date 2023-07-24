def create_code_dict():
    codes = {
        'A': '%', 'a': '9',
        'B': '@', 'b': '#',
        'C': '&', 'c': '3',
        'D': '*', 'd': '7',
        'E': '$', 'e': '1',
        'F': '^', 'f': '5',
        'G': '!', 'g': '0',
        'H': '+', 'h': '8',
        'I': '?', 'i': '6',
        'J': '(', 'j': ')',
        'K': '-', 'k': '=',
        'L': '<', 'l': '>',
        'M': '[', 'm': ']',
        'N': '{', 'n': '}',
        'O': '|', 'o': '\\',
        'P': '/', 'p': ':',
        'Q': ';', 'q': '.',
        'R': ',', 'r': ' ',
        'S': '~', 's': '`',
        'T': '_', 't': '\'',
        'U': '\"', 'u': '\"',
        'V': 'ä', 'v': 'ö',
        'W': 'ü', 'w': 'ß',
        'X': 'Ä', 'x': 'Ö',
        'Y': 'Ü', 'y': '§',
        'Z': '©', 'z': '®',   
    }
    return codes

def decode_message(encoded_message, code_dict):
    decoded_message = ''
    for char in encoded_message:
        found = False
        for key, value in code_dict.items():
            if char == value:
                decoded_message += key
                found = True
                break
        if not found:
            decoded_message += char
    return decoded_message

def main():
    codes = create_code_dict()

    # Read the contents of the "encrypted.txt" file
    with open('encrypted.txt', 'r') as file:
        encoded_text = file.read()

    # Decode the message using the code dictionary
    decrypted_message = decode_message(encoded_text, codes)

    # Display the decrypted contents on the screen
    print("Decrypted Contents:")
    print(decrypted_message)

if __name__ == "__main__":
    main()