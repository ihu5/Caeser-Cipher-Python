"""
Author @journey6
Github link: https://github.com/journey6/
this is implementation of Caesar cipher which shifts characters and letters by specific number positive or negative
"""
import cipher
R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white


# encrypting text
print(C + "### encrypting plain text ###")
plain_text = "hi hello welcome back"
number = -1 # shift value
cipher_text = cipher.encoder(plain_text, number)
print(W + "shift number:", number)
print(W + "plain text:  ", R + plain_text)
print(W + "cipher text: ", G + cipher_text)

print('')

# decoding text
print(C + "### decoding cipher text ###")
cipher_text = "Xlmw mw e wigvix qiwweki"
number = 4 # shift value
plain_text = cipher.decoder(cipher_text, number)
print(W + "shift number: ", number)
print(W + "cipher text: ", R + cipher_text)
print(W + "plain text: ", G + plain_text)




