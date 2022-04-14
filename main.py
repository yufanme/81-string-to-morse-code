# todo 1 input a string
# todo 2 convert character to morse code, leave the punctuation mark as it is
# todo 3 join all the morse code together

import time
from playsound import playsound


morse_dict = {
    # letters
    "A": "·-",
    "B": "-···",
    "C": "-·-·",
    "D": "-··",
    "E": "·",
    "F": "··-·",
    "G": "--·",
    "H": "····",
    "I": "··",
    "J": "·---",
    "K": "-·-",
    "L": "·-··",
    "M": "--",
    "N": "-·",
    "O": "---",
    "P": "·--·",
    "Q": "--·-",
    "R": "·-·",
    "S": "···",
    "T": "-",
    "U": "··-",
    "V": "···-",
    "W": "·--",
    "X": "-··-",
    "Y": "-·--",
    "Z": "--··",
    "0": "-----",
    # numbers
    "1": "·----",
    "2": "··---",
    "3": "···--",
    "4": "····-",
    "5": "·····",
    "6": "-····",
    "7": "--···",
    "8": "---··",
    "9": "----·",
    # punctuations
    ".": "·-·-·-",
    ",": "--··--",
    "?": "··--··",
    "!": "-·-·--",
    "=": "-···-",
    ":": "---···",
    ";": "-·-·-·",
    "'": "·----·",
    "/": "-··-·",
    "-": "-····-",
    "_": "··--·-",
    '"': "·-··-·",
    "(": "-·--·",
    ")": "-·--·-",
    "$": "···-··-",
    "&": "·-···",
    "@": "·--·-·",
    "+": "·-·-·"
}

user_input = input("Please input content:")
morse_list = []

for char in user_input:
    if char == " ":
        morse_list.append("/")
    else:
        char = char.upper()
        morse_list.append(morse_dict[char])

morse_string = " ".join(morse_list)


print(morse_string)
for symbol in morse_string:
    if symbol == "·":
        playsound("DIT.wav")
    elif symbol == "-":
        playsound("DAH.wav")
    else:
        time.sleep(0.5)


