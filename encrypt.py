from enigma.machine import EnigmaMachine
machine = EnigmaMachine.from_key_sheet(
    rotors='II V III',
    reflector='B',
    ring_settings='1 1 1',
    plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')


#this is rotor setting
machine.set_display('FAC')#3 random characters

#this is message key
msg_key = machine.process_text('SICE')#set to random key
print(msg_key)

plaintext = "Wordplay"

ciphertext = machine.process_text(plaintext)

print(ciphertext)

