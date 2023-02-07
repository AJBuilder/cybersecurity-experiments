

# Shift a lowercase letter by the specified 'shift'
def shiftLetter(character, shift): 
    character = chr(ord(character) + shift) # Add shift
    if ord(character) > ord('z'): # If exceeded the alphabet
        # Add the remainder to the start of the alphabet
        character = chr(ord('a') + (ord(character) % (ord('z') + 1)))
    return character

if __name__ =='__main__':
    
    message = 'xqluvkd'
    
    for shifting in range(0, 23): # Test every shift 0-22
        newMess = ''
        for character in range(0, len(message)): # Shift every character
            newMess += shiftLetter(message[character], shifting)
        print("Shift: " + str(shifting) + " -> " + str(newMess))