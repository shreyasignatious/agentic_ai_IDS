from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

import base64
import os


KEY_FILE = "aes_key.bin"


if os.path.exists(KEY_FILE):

    with open(KEY_FILE, "rb") as file:

        key = file.read()

else:

    key = get_random_bytes(32)

    with open(KEY_FILE, "wb") as file:

        file.write(key)


def encrypt_data(data):

    try:

        cipher = AES.new(
            key,
            AES.MODE_EAX
        )

        ciphertext, tag = (
            cipher.encrypt_and_digest(
                data.encode()
            )
        )

        encrypted_data = (
            cipher.nonce + ciphertext
        )

        encoded = base64.b64encode(
            encrypted_data
        ).decode()

        return encoded

    except Exception as error:

        return f"Encryption failed: {error}"


def decrypt_data(encrypted_data):

    try:

        decoded_data = base64.b64decode(
            encrypted_data
        )

        nonce = decoded_data[:16]

        ciphertext = decoded_data[16:]

        cipher = AES.new(
            key,
            AES.MODE_EAX,
            nonce=nonce
        )

        decrypted_data = cipher.decrypt(
            ciphertext
        )

        return decrypted_data.decode()

    except Exception as error:

        return f"Decryption failed: {error}"