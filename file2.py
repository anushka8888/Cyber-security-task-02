def encrypt_image(image_path, key):
    with image.open(image_path, 'r') as img:
        pixel_data = list(img.getdata())

    encrypted_data = [value ^ key for value in pixel_data]

    with image.new(img.mode, img.size) as new_img:
        new_img.putdata(encrypted_data)
        new_img.save('encrypted_' + image_path)
#defining the encrypted image part

def decrypt_image(encrypted_image_path, key):
    with image.open(encrypted_image_path, 'r') as img:
        pixel_data = list(img.getdata())

    decrypted_data = [value ^ key for value in pixel_data]

    with image.new(img.mode, img.size) as new_img:
        new_img.putdata(decrypted_data)
        new_img.save('decrypted_' + encrypted_image_path)
#defining the decrypted image part
