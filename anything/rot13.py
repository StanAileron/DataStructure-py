#!/user/bin/python
# -*-coding:UTF-8-*-

"""凯撒加密算法：
将给定的字母在字母表中移动k为得到加密后的字字母。
"""

CHARS = "abcdefghijklmnopqrstuvwxyz"


def encryption(message: str, step: int) -> str:
    encryption_lst = []

    for s_ in message:
        encryption_lst.append(CHARS[(CHARS.find(s_) + step) % 26])

    return "".join(encryption_lst)


def decrypt(message: str, step: int) -> str:
    decrypt_lst = []

    for s_ in message:
        decrypt_lst.append(CHARS[(CHARS.find(s_) - step + 26) % 26])

    return "".join(decrypt_lst)


if __name__ == '__main__':
    s = "helloworld"

    encryption_s = encryption(s, step=14)
    print("encryption message: ", encryption_s)  # encrypt message:  vszzckcfzr

    decrypt_s = decrypt(encryption_s, step=14)
    print("decrypt message: ", decrypt_s)  # decrypt message:  helloworld
