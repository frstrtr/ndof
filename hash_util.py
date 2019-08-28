import hashlib
import json


def hash_string_256(string):
    return hashlib.sha256(string).hexdigest()


def hash_block(block):
    """Hashes a block and returns a string representation of it.

    Arguments:
        :block: The block that should be hashed.
    """
    # test json format output
    # print(hashlib.sha256(json.dumps(block).encode()))
    return hash_string_256(json.dumps(block, sort_keys=True).encode())
    # old relese: '-'.join([str(block[key]) for key in block])
