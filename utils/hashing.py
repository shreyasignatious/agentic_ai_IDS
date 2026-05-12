import hashlib


def generate_hash(data):

    try:

        hash_object = hashlib.sha256(
            data.encode()
        )

        return hash_object.hexdigest()

    except Exception as error:

        return f"Hash generation failed: {error}"