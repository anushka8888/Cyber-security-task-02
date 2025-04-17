#using a conditional statement
#getting a further path of image by user
#path=location of image
if __name__ == "__main__":
    image_path = input("Enter path of Image: ")
    key = int(input("Enter Key for encryption of Image: "))

    print("The path of file: ", image_path)
    print("Key for encryption: ", key)

  #a part for doing encrypion first 
  #getting decrypted img later
    encrypt_image(image_path, key)
    print("Encryption Done...")

    key = int(input("Enter Key for decryption of Image: "))

    encrypted_image_path = "encrypted_" + image_path
    print("The path of file: ", encrypted_image_path)
    print("Key for decryption: ", key)

  #a part for doing decrypion first 
  #getting encrypted img later
    decrypt_image(encrypted_image_path, key)
    print("Decryption Done...")

    key = int(input("Enter Key for enryption of Image: "))

    encrypted_image_path = "decrypted_" + image_path
    print("The path of file: ", decrypted_image_path)
    print("Key for encryption: ", key)
