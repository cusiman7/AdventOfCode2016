#!/usr/bin/env python3

import hashlib
from collections import defaultdict

def md5_hexdigest(salt, index):
    v = salt + str(index)
    b = v.encode()
    return hashlib.md5(b).hexdigest()

def md5_hexdigest_stretched(salt, index):
    digest = md5_hexdigest(salt, index)

    for i in range(2016):
        digest = hashlib.md5(digest.encode()).hexdigest()

    return digest

def gen_keys(hash_fn):
    threes = defaultdict(list)

    keys = []

    salt ='jlmsuwbz' 
    index = 0

    while True:
        digest = hash_fn(salt, index)

        for i in range(len(digest) - 2):
            char = digest[i]
            if char == digest[i+1] and char == digest[i+2]:
                if i < len(digest) - 4 and char == digest[i+3] and char == digest[i+4]:

                    for key_index in threes[char]:
                        if index - key_index < 1000:
                            keys.append(key_index)

                            if len(keys) == 64:
                                return key_index

                    threes[char] = []
                else:
                    threes[char].append(index)
                    break
        index += 1

print(f'Part 1: {gen_keys(md5_hexdigest)}')
print(f'Part 2: {gen_keys(md5_hexdigest_stretched)}')
