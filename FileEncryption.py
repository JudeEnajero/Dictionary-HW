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

def encode_message(message, code_dict):
    encoded_message = ''
    for char in message:
        if char in code_dict:
            encoded_message += code_dict[char]
        else:
            encoded_message += char
    return encoded_message

def main():
    codes = create_code_dict()

    with open('info_security.txt', 'r') as file:
        text = file.read()

    encoded_message = encode_message(text, codes)

    
    with open("encrypted.txt", "w") as file:
        file.write(encoded_message)

    print("File encrypted and saved to 'encrypted.txt'.")

if __name__ == "__main__":
    main()
