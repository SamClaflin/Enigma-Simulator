# Enigma Machine Simulator
This python script is a near-perfect recreation of the famous enigma machine used in WWII by Germany in order to
encode their messages. The only feature not implemented is the latch mechanism seen in later rotor designs
that caused the rotors to turnover upon reaching a certain letter (that's my understanding, at least). Instead,
the "rotors" in this script are designed to turn strictly on a based on how many characters have been entered into
the input string (to simulate individual keys being pressed). Operation instructions will be detailed below.

# Dependencies
None; the only thing required to run this simulation is the installation of a Python (I don't think version is too
critical, but you might get some issues if you go below ~3.5).

# Operation
**Encryption**  

Basic operation of the simulator is quite simple, simply run the program and enter a string into the input area.
Upon pressing enter, an encrypted string will promptly be returned back to the user. Either write this string 
down or copy it to your clipboard in order for future decryption. Additionally, **take note of your current 
settings (they'll be printed at the top of the input window upon first running the script)** if you plan on
changing them later. Changing even a single setting will result in *completely* different output.

**Decryption**  

If you attempt to re-enter the jumbled string back into the input box immediately after its encrypted, it 
**won't** return the input that originally produced it. This is because after each character is typed, the
"rotors" have all rotated to a certain degree based upon the length of the string. If you don't understand how
the original enigma machine worked, don't worry. Just know that every character typed will essentially change the
way in which the program jumbles the next letter.
*So...*
After either writing this string down or copying it, *re-reun the program*, this will reset all of the
configurations to the way the were prior to any characters being typed. In this state, entering in the jumbled
string will return the input that originally produced it.

# Changing Configurations
Changing the configurations is quite simple; near the top of the code is a block entitled "USER CONFIGURATION". 
Each variable in this block can be changed to whatever *valid* configuration you desire. This means that the same
rotor should not be used more than once, and the offset variables must be greater than or equal to zero and less
than or equal to 26. Additionally, Letters in pairs in the plugboard (plug variable) cannot be used more than
once.
