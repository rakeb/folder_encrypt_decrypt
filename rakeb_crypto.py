'''
@author Rakeb Mazharul Islam
@email mislam7@uncc.edu, rakeb.mazharul@gmail.com
'''
import getpass
import os

import pyAesCrypt

supported_file_extension = ['.mov', '.mp4']
DELETE_ORIGINAL = 'y'


def start_encrypt(file_list, delete_original_file):
    password = "rakeb"
    try:
        password = getpass.getpass('Enter your password: ')
    except Exception as error:
        print('ERROR', error)

    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024

    for plain_file in file_list:
        cypher_file = plain_file + '.enc'
        try:
            pyAesCrypt.encryptFile(plain_file, cypher_file, password, bufferSize)
            if delete_original_file == DELETE_ORIGINAL:
                os.remove(plain_file)
            print("File: %s has successfully encrypted to: %s" % (plain_file, cypher_file))
        except ValueError as e:
            print("Error: ", e)


def travers_files(rootdir):
    file_list = []
    for currentpath, folders, files in os.walk(rootdir):
        for file in files:
            this_file = os.path.join(currentpath, file)
            filename, file_extension = os.path.splitext(this_file)

            if file_extension:
                file_list.append(this_file)

    return file_list


def start_decrypt(file_list, delete_original_file):
    password = "rakeb"
    try:
        password = getpass.getpass('Enter your password: ')
    except Exception as error:
        print('ERROR', error)

    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024

    for cypher_file in file_list:
        filename, file_extension = os.path.splitext(cypher_file)
        if file_extension == '.enc':
            plain_file = cypher_file.replace('.enc', '')
            try:
                pyAesCrypt.decryptFile(cypher_file, plain_file, password, bufferSize)
                if delete_original_file == DELETE_ORIGINAL:
                    os.remove(cypher_file)
                print("File: %s has successfully decrypted to: %s" % (cypher_file, plain_file))
            except ValueError as e:
                print("Error: ", e)


if __name__ == '__main__':
    rootdir = input("Enter Root Directory or File name (absolute path): ")  # Python 3

    delete_original_file = input("Type 'y' to delete original file, press Enter otherwise: ")  # Python 3

    type = input("Type 'e' for encryption or 'd' for decryption: ")  # Python 3

    if rootdir == '' or rootdir is None:
        rootdir = '/Users/mislam7/Dropbox/Camera Uploads/movie/mp4/test'

    if os.path.isdir(rootdir):
        file_list = travers_files(rootdir)
    else:
        file_list = [rootdir]

    if type == 'e':
        start_encrypt(file_list, delete_original_file)
    elif type == 'd':
        start_decrypt(file_list, delete_original_file)
    else:
        print("Type either 'e'  or 'd' for encryption or decryption")
