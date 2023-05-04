import sys


def encode_message(shift):
    message = input().upper()
    encoded = []
    for letter in message:
        if letter.isalpha():
            # shift the letter and wrap around if needed
            encoded_letter = chr(((ord(letter) - 65 + shift) % 26) + 65)
            encoded.append(encoded_letter)
    # print the encoded message in blocks of five
    for i in range(0, len(encoded), 5):
        print(" ".join(encoded[i:i + 5]))


if __name__ == "__main__":
    shift = int(sys.argv[1])
    encode_message(shift)
