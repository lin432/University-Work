"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message1.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.

    >>>main()
    EQFZSRTEAPNXLSRJAMNGAT
    GLCEGMOTMTRWKHAMGNME

    REQ: DECK_FILENAME != None
    REQ: MSG_FILENAME != None
    REQ: MODE == "e" or MODE == "d"
    """

    deck_file = open(DECK_FILENAME)
    message_file = open(MSG_FILENAME)

    deck = cipher_functions.read_deck(deck_file)
    messages = cipher_functions.read_messages(message_file)

    deck_file.close()
    message_file.close()

    translated = cipher_functions.process_messages(deck, messages, MODE)

    for a in translated:
        print(a)

main()
