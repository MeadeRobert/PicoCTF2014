import crypto
import operator


file = open("encrypted.txt")
text = ""
for line in file:
        text += line
file.close()

ref_dict = {'a':.08167,'b':.01492,'c':.02782,'d':.04253,'e':.12702,'f':.02228,'g':.02015,'h':.06094,'i':.06966,'j':.00153,
            'k':.00772,'l':.04025,'m':.02406,'n':.06749,'o':.07507,'p':.01929,'q':.00095,'r':.05987,'s':.06327,'t':.09056,
            'u':.02758,'v':.00978,'w':.02360,'x':.00150,'y':.01974,'z':.00074}

ordered_ref_map = sorted(ref_dict.items(), key=operator.itemgetter(1))
ordered_ref_list = [pair[0] for pair in ordered_ref_map]

freq_dict = crypto.calculate_frequencies(text)
ordered_freq_list = []
ordered_freq_map = sorted(freq_dict.items(), key=operator.itemgetter(1))
print(ordered_freq_map)
ordered_freq_list = [pair[0] for pair in ordered_freq_map]
print(ordered_freq_list)

letterMap = dict(zip(ordered_freq_list, ordered_ref_list))
print(letterMap)

decrypted = crypto.cipher(text, letterMap)
print(decrypted)

