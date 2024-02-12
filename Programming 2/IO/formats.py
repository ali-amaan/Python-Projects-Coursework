s='Arvot ovat 1«{}», {} ja {}'.format('a', 1, True)
dashes = '-' * 26
nl = '\n'


def info_box(mother, father, hline, nl):
    print('{2}{3}Mother: {0}{3}{2}{3}Father: {1}{3}{2}'.format(mother, father, hline, nl))

info_box('Virpi Varpunen', 'Keijo Kotka', 22 * '-', '\n')

info_box('Teea Tilhi', 'Pertti Pääskynen', '', '\n')


print('People claim that {firstname} {lastname} answers to all email sent to {email}'.format(firstname='Noam', lastname='Chomsky', email='chomsky@mit.edu'))
chomsky={'firstname': 'Noam', 'lastname': 'Chomsky', 'email': 'chomsky@mit.edu'}
print('People claim that {firstname} {lastname} answers to all email sent to {email}'.format(**chomsky))
