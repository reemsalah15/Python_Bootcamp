# Caesar Cipher

This is a Python program that implements the Caesar cipher, a simple encryption technique. It allows you to encrypt and decrypt messages by shifting the letters in the alphabet.

## Usage

1. Make sure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Run the program by executing the following command:

```shell
python caesar_cipher.py
```

4. Follow the prompts to input the necessary information:
   - Choose whether to encode or decode the message.
   - Enter the message you want to encrypt or decrypt.
   - Specify the shift number, which determines how many positions each letter should be shifted in the alphabet.
   - Choose whether to try again or exit the program.

## Requirements

- Python 3.x

## How it works

1. The program uses the `art` library to display a logo.
2. The alphabet is defined as a list of lowercase letters.
3. The `caesar` function takes three parameters: `text` (the message to be encrypted or decrypted), `shift` (the number of positions to shift each letter), and `direction` (the action to perform: encode or decode).
4. Within the `caesar` function, the input `text` is iterated in reverse order to process each character.
5. If the character is in the alphabet, it is either shifted forward (for encoding) or backward (for decoding) based on the provided `shift` value.
6. Non-alphabetic characters are added as-is to the `end_text` variable.
7. The final `end_text` is reversed and displayed as the result.
8. The main program loop allows the user to enter the desired action, message, and shift repeatedly until they choose to exit.

