import re
import getpass


def get_password_strength(password):
    password_strength = 1
    if len(password) >= 8:
        print('Number of characters: OK!')
        password_strength += 2
    else:
        print('Number of characters: NOT OK!')

    if re.search(r'[a-z]+', password):
        print('Lowercase letters: OK!')
        password_strength += 1
    else:
        print('Lowercase letters: NOT OK!')

    if re.search(r'[A-Z]+', password):
        print('Uppercase letters: OK!')
        password_strength += 1
    else:
        print('Uppercase letters: OK!')

    if re.search(r'\d', password):
        print('Digits: OK!')
        password_strength += 2
    else:
        print('Digits: NOT OK!')

    if re.search(r'[^A-Za-z0-9]+', password):
        print('Symbols: OK!')
        password_strength += 3
    else:
        print('Symbols: NOT OK!')

    print('Password strength = ' + str(password_strength))


if __name__ == '__main__':
    password = getpass.getpass(prompt='Enter your password: ')
    get_password_strength(password)
