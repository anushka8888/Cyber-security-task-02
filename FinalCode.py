#file1
from email.mime import image
import PIL.Image
#file2
def encrypt_image(image_path, key):
    with image.open(image_path, 'r') as img:
        pixel_data = list(img.getdata())

    encrypted_data = [value ^ key for value in pixel_data]

    with image.new(img.mode, img.size) as new_img:
        new_img.putdata(encrypted_data)
        new_img.save('encrypted_' + image_path)

def decrypt_image(encrypted_image_path, key):
    with image.open(encrypted_image_path, 'r') as img:
        pixel_data = list(img.getdata())

    decrypted_data = [value ^ key for value in pixel_data]

    with image.new(img.mode, img.size) as new_img:
        new_img.putdata(decrypted_data)
        new_img.save('decrypted_' + encrypted_image_path)
#file3
if __name__ == "__main__":
    image_path = input("Enter path of Image: ")
    key = int(input("Enter Key for encryption of Image: "))

    print("The path of file: ", image_path)
    print("Key for encryption: ", key)

    encrypt_image(image_path, key)
    print("Encryption Done...")

    key = int(input("Enter Key for decryption of Image: "))

    encrypted_image_path = "encrypted_" + image_path
    print("The path of file: ", encrypted_image_path)
    print("Key for decryption: ", key)

    decrypt_image(encrypted_image_path, key)
    print("Decryption Done...")
