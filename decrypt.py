from enigma.machine import EnigmaMachine
machine = EnigmaMachine.from_key_sheet(
    rotors='II V III',
    reflector='B',
    ring_settings='1 1 1',
    plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')

#rotor settings
machine.set_display('FAC') #set to the same as sender

msg_key = machine.process_text('LEJB')#enter encoded key recieved from sender
print(msg_key)


ciphertext = "RVLREVHR"#enter encoded text from sender

plaintext = machine.process_text(ciphertext)

print(plaintext)
