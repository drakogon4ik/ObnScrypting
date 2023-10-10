import sys


dict = {
        'A': '56',
        'J': '45',
        'S': '64',
        'b': '13',
        'k': '32',
        't': '91',
        '.': '100',
        'B': '57',
        'K': '46',
        'T': '65',
        'c': '14',
        'l': '33',
        'u': '92',
        ';': '101',
        'L': '47',
        'U': '66',
        'd': '15',
        'm': '34',
        'v': '93',
        "'": '102',
        'D': '59',
        'M': '48',
        'V': '67',
        'e': '16',
        'n': '35',
        'w': '94',
        '?': '103',
        'E': '40',
        'N': '49',
        'W': '68',
        'f': '17',
        'o': '36',
        'x': '95',
        '!': '104',
        'F': '41',
        'O': '60',
        'X': '69',
        'g': '18',
        'p': '37',
        'y': '96',
        ':': '105',
        'G': '42',
        'P': '61',
        'Y': '10',
        'h': '19',
        'q': '38',
        'z': '97',
        'H': '43',
        'Q': '62',
        'Z': '11',
        'i': '30',
        'r': '39',
        ' ': '98',
        'I': '44',
        'R': '63',
        'a': '12',
        'j': '31',
        's': '90',
        ',': '99'



}


if sys.argv[1] == 'decrypt':
        try:
                with open('Encrypted_msg.txt') as ready:
                        r = ready.read()
                        r = r[:-1]
                        new_r = r.split(',')
                        new_string = ''
                        for i in new_r:
                                for j in dict:
                                        if dict[j] == i:
                                                new_string += j
                print(new_string)

        except:
                print('something has been written not right')


elif sys.argv[1] == 'encrypt':
        try:
                with open('Encrypted_msg.txt', 'w') as new:
                        string = input()
                        for i in range(len(string)-1):
                                new.write(dict[string[i]] + ',')
                        new.write(dict[string[-1]] + '.')
        except:
                print('something has been written not right')


