import math
import binascii

N = 0xb197d3afe713816582ee988b276f635800f728f118f5125de1c7c1e57f2738351de8ac643c118a5480f867b6d8756021911818e470952bd0a5262ed86b4fc4c2b7962cd197a8bd8d8ae3f821ad712a42285db67c85983581c4c39f80dbb21bf700dbd2ae9709f7e307769b5c0e624b661441c1ddb62ef1fe7684bbe61d8a19e7
e = 65537
p = 0xc315d99cf91a018dafba850237935b2d981e82b02d994f94db0a1ae40d1fc7ab9799286ac68d620f1102ef515b348807060e6caec5320e3dceb25a0b98356399
q = 0xe90bbb3d4f51311f0b7669abd04e4cc48687ad0e168e7183a9de3ff9fd2d2a3a50303a5109457bd45f0abe1c5750edfaff1ad87c13eed45e1b4bd2366b49d97f
d = 0x496747c7dceae300e22d5c3fa7fd1242bda36af8bc280f7f5e630271a92cbcbeb7ae04132a00d5fc379274cbce8c353faa891b40d087d7a4559e829e513c97467345adca3aa66550a68889cf930ecdfde706445b3f110c0cb4a81ca66f8630ed003feea59a51dc1d18a7f6301f2817cb53b1fb58b2a5ad163e9f1f9fe463b901


def mod_exp(b, e, m):
    r = 0
    bc = b % m
    for i in range(0, math.ceil(math.log(e)/math.log(2)) + 1):
        if e & 1:
            r = bc if r == 0 else r * bc % m
        e >>= 1
        bc = bc ** 2 % m
    return r

value = 0x58ae101736022f486216e290d39e839e7d02a124f725865ed1b5eea7144a4c40828bd4d14dcea967561477a516ce338f293ca86efc72a272c332c5468ef43ed5d8062152aae9484a50051d71943cf4c3249d8c4b2f6c39680cc75e58125359edd2544e89f54d2e5cbed06bb3ed61e5ca7643ebb7fa04638aa0a0f23955e5b5d9

decrypted = binascii.unhexlify(format(mod_exp(value, d, N), '#04x')[2::])
print(decrypted)

# text = ""
# for i in range(0, len(ciphertext)):
#     print(chr(mod_exp(ord(ciphertext[i]), 7, 3)))
#     text +=


# print(text)