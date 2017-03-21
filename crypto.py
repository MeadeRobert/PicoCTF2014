import string


def calculate_frequencies(s):
    total_letters = 0
    freq_dict = dict.fromkeys(string.ascii_lowercase, 0)
    for i in range(0, len(s)):
        if s[i] in string.ascii_lowercase:
            total_letters += 1
            freq_dict[s[i]] += 1
    for k, v in freq_dict.items():
        freq_dict[k] = v / total_letters
    return freq_dict


def map_letters(freq_dict, ref_dict):
    letter_map = {}
    for k1, v1 in ref_dict.items():
        letter = k1
        delta = abs(ref_dict[letter] - freq_dict[letter])
        for k2, v2 in freq_dict.items():
            if abs(ref_dict[k2] - freq_dict[letter]) < delta:
                delta = abs(ref_dict[k2] - freq_dict[letter])
                letter = k2
        letter_map.update({letter: k1})
    return letter_map


def cipher(s, letter_map):
    out = ""
    for i in range(0, len(s)):
        if s[i] in string.ascii_lowercase:
            out += letter_map[s[i]]
        else:
            out += s[i]
    return out
