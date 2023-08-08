"""
Author @ihu5
Github link: https://github.com/ihu5/
this is implementation of Caesar cipher which shifts characters and letters by specific number positive or negative
"""


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']


def encoder(text, shift_value):
    encoded_text = ""
    for i, val in enumerate(text):
        char_index = get_encoding_index(val, shift_value)
        if str.islower(val):
            encoded_text = encoded_text + small_letters[char_index]
        elif str.isupper(val):
            encoded_text = encoded_text + capital_letters[char_index]
        elif str.isdigit(val):
            encoded_text = encoded_text + numbers[char_index]
        else:
            encoded_text = encoded_text + val

    return encoded_text


def get_encoding_index(c, shift_value):
    if str.islower(c):
        for i, val in enumerate(small_letters):
            if c == val:
                shift_value = (i + shift_value % len(small_letters)) % len(small_letters)
                return shift_value

    elif str.isupper(c):
        for i, val in enumerate(capital_letters):
            if c == val:
                shift_value = (i + shift_value % len(capital_letters)) % len(capital_letters)
                return shift_value

    elif str.isdigit(c):
        for i, val in enumerate(numbers):
            if c == val:
                shift_value = (i + shift_value % len(numbers)) % len(numbers)
                return shift_value

    else:
        return -1


def decoder(text, shift_value):
    decoded_text = ""
    for i, val in enumerate(text):
        char_index = get_decoding_index(val, shift_value)
        if str.islower(val):
            decoded_text = decoded_text + small_letters[char_index]
        elif str.isupper(val):
            decoded_text = decoded_text + capital_letters[char_index]
        elif str.isdigit(val):
            decoded_text = decoded_text + numbers[char_index]
        else:
            decoded_text = decoded_text + val

    return decoded_text


def get_decoding_index(c, shift_value):
    if str.islower(c):
        for i, val in enumerate(small_letters):
            if c == val:
                shift_value = shift_value % len(small_letters)
                if (i-shift_value) < 0:
                    return (i - shift_value + len(small_letters)) % len(small_letters)
                else:
                    return (i - shift_value) % len(small_letters)

    elif str.isupper(c):
        for i, val in enumerate(capital_letters):
            if c == val:
                shift_value = shift_value % len(capital_letters)
                if (i-shift_value) < 0:
                    return (i - shift_value + len(capital_letters)) % len(capital_letters)
                else:
                    return (i - shift_value) % len(capital_letters)

    elif str.isdigit(c):
        for i, val in enumerate(numbers):
            if c == val:
                shift_value = shift_value % len(numbers)
                if (i-shift_value) < 0:
                    return (i - shift_value + len(numbers)) % len(numbers)
                else:
                    return (i - shift_value) % len(numbers)

    else:
        return -1
