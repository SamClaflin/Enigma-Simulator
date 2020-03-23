__author__ = "Sam C."
# WWII Enigma machine recreation

# -----------------------------------------[CREATE COMPONENT OBJECTS]---------------------------------------------------

# Set globals
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
roman_numerals = ["I", "II", "III", "IV", "V"]

# Initialize rotors and wiring schemes
wiring_schemes = ["JGDQOXUSCAMIFRVTPNEWKBLZYH",     # Rotor I
                  "NTZPSFBOKMWRCJDIVLAEYUXHGQ",     # Rotor II
                  "JVIUBHTCDYAKEQZPOSGXNRMWFL",     # Rotor III
                  "ESOVPZJAYQUIRHXLNFTGKDCMWB",     # Rotor IV
                  "VZBRGITYUPSDNHLXAWMJQOFECK"]     # Rotor V

reflector_schemes = ["EJMZALYXVBWFCRQUONTSPIKHGD",  # Reflector A
                     "YRUHQSLDPXNGOKMIEBFZCWVJAT",  # Reflector B
                     "FVPJIAOYEDRZXWGCTKUQSBNMHL"]  # Reflector C

# Link rotors
rotor_1 = wiring_schemes[0]
rotor_2 = wiring_schemes[1]
rotor_3 = wiring_schemes[2]
rotor_4 = wiring_schemes[3]
rotor_5 = wiring_schemes[4]

# Link reflectors
reflector_a = reflector_schemes[0]
reflector_b = reflector_schemes[1]
reflector_c = reflector_schemes[2]

# -----------------------------------------------[USER CONFIGURATION]---------------------------------------------------

# Set plug board configuration
plugs = [("A", "X"),
         ("B", "Q"),
         ("R", "V"),
         ("U", "Z"),
         ("E", "H"),
         ("J", "Y"),
         ("O", "S"),
         ("M", "C"),
         ("D", "F"),
         ("G", "I"),
         ("K", "P"),
         ("L", "N"),
         ("T", "W")]

# Initialize component choices
position_1 = rotor_4
position_2 = rotor_1
position_3 = rotor_5
reflector_choice = reflector_c

# Rotor offsets
offset_1 = 21
offset_2 = 8
offset_3 = 14

# -----------------------------------------------[INFORMATION STRINGS]--------------------------------------------------

# Output strings
reflector_string = ""
if reflector_choice == reflector_a:
    reflector_string = "A"
elif reflector_choice == reflector_b:
    reflector_string = "B"
elif reflector_choice == reflector_c:
    reflector_string = "C"

position_indexes = []
position_list = [position_1, position_2, position_3]
for position in position_list:
    for scheme in wiring_schemes:
        if position == scheme:
            position_indexes.append(roman_numerals[wiring_schemes.index(scheme)])

# -------------------------------------------[FUNCTION DEFINITIONS]-----------------------------------------------------


# Function to rotate rotors
def rotate(config):
    return config[-1] + config[:len(config) - 1]


# Function to find alphabetic index of input
def get_index(let):
    for letter in alphabet:
        if let == letter:
            return alphabet.index(letter)


# Function to translate a given letter to its specified "plug" value
def check_plugs(let):
    for tup in plugs:
        if let in tup:
            for letter in tup:
                if letter != let:
                    return letter


# Function to encrypt characters using rotors
def rotor_encrypt(rotor, encrypt):
    return rotor[get_index(encrypt)]


# -----------------------------------------------[MAINLOOP]--------------------------------------------------------------

# Initialize offsets
position_1 = position_1[offset_1: len(position_1)] + position_1[: offset_1]
position_2 = position_2[offset_2: len(position_2)] + position_2[: offset_2]
position_3 = position_3[offset_3: len(position_3)] + position_3[: offset_3]

key_presses = 0
print("================[ENIGMA I]================\n"
      "SETTINGS:\n"
      f"POSITION 1: ROTOR {position_indexes[0]}; OFFSET: {offset_1}\n"
      f"POSITION 2: ROTOR {position_indexes[1]}; OFFSET: {offset_2}\n"
      f"POSITION 3: ROTOR {position_indexes[2]}; OFFSET: {offset_3}\n"
      f"REFLECTOR: {reflector_string}\n"
      "==========================================\n")

while True:
    # Get user input and use plug board to determine selected letter
    inp = input().upper()
    final_string = ""

    # Encrypt each letter individually and turn rotor after each one
    for char in inp:

        # Check for spaces
        if char == " ":
            final_string += char
            continue

        # Send string through plug board
        char = check_plugs(char)

        # Send encryption through rotors
        encrypted_letter = rotor_encrypt(position_1, char)
        encrypted_letter = rotor_encrypt(position_2, encrypted_letter)
        encrypted_letter = rotor_encrypt(position_3, encrypted_letter)

        # Implement reflector
        encrypted_letter = rotor_encrypt(reflector_choice, encrypted_letter)

        # Send encryption back through rotors
        pos = position_3.index(encrypted_letter)
        encrypted_letter = alphabet[pos]
        pos = position_2.index(encrypted_letter)
        encrypted_letter = alphabet[pos]
        pos = position_1.index(encrypted_letter)
        encrypted_letter = alphabet[pos]

        # Send encryption back through plug board
        encrypted_letter = check_plugs(encrypted_letter)

        # Append encryption to final string
        final_string += encrypted_letter

        # Control rotor rotation
        key_presses += 1
        position_1 = rotate(position_1)
        if key_presses % 26 == 0:
            position_2 = rotate(position_2)
        if key_presses % 26 ** 2 == 0:
            position_3 = rotate(position_3)

    # Return final string
    print(final_string)
