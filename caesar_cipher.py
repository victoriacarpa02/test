from string import ascii_lowercase as lcase


class Caesar:
    @staticmethod
    def encrypt(file_name, shift):
        with open(file_name, 'r') as def_file, open('encrypted_text.txt', 'w') as new_file:
            for line in def_file.readlines():
                sentence = ''
                for char in line.strip():
                    if char.isalpha():
                        if char.islower():
                            ind = lcase.index(char)
                            sentence += lcase[(ind + shift) % len(lcase)]
                        else:
                            ind = lcase.index(char.lower())
                            sentence += lcase[(ind + shift) % len(lcase)].upper()
                    else:
                        sentence += char
                new_file.write(sentence + '\n')

    @staticmethod
    def decrypt(file_name, shift):
        with open(file_name, 'r') as def_file, open('decrypted_text.txt', 'w') as new_file:
            for line in def_file.readlines():
                sentence = ''
                for char in line.strip():
                    if char.isalpha():
                        if char.islower():
                            ind = lcase.index(char)
                            sentence += lcase[(ind - shift) % len(lcase)]
                        else:
                            ind = lcase.index(char.lower())
                            sentence += lcase[(ind - shift) % len(lcase)].upper()
                    else:
                        sentence += char
                new_file.write(sentence + '\n')


obj = Caesar()
obj.encrypt('text.txt', 3)

obj.decrypt('encrypted_text.txt', 3)
