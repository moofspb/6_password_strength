import re
import getpass


PASSWORD_MIN_STRENGTH = 1


def check_password_length(password):
    return 2 if len(password) >= 8 else 0


def check_password_for_lowercase(password):
    return 1 if re.search(r'[a-z]+', password) else 0


def check_password_for_uppercase(password):
    return 1 if re.search(r'[A-Z]+', password) else 0


def check_password_for_digits(password):
    return 2 if re.search(r'\d', password) else 0


def check_password_for_symbols(password):
    return 3 if re.search(r'[^A-Za-z0-9]+', password) else 0


def get_password_strength(password):
    password_strength = (check_password_length(password) +
                         check_password_for_lowercase(password) +
                         check_password_for_uppercase(password) +
                         check_password_for_digits(password) +
                         check_password_for_symbols(password) +
                         PASSWORD_MIN_STRENGTH)
    return password_strength


if __name__ == '__main__':
    print('Hi! Let\'s check is your password strong enough?')
    print('The score is just a number between 1 (weak) and 10 (strong)')
    print("""Strong password is 8 or more characters in length and consists of:
          1. Upper-case and lower-case letters
          2. One ore more numerical digits
          3. Special symbols, such as #,%,@,$""")
    password = getpass.getpass(prompt='Enter your password: ')
    password_strength = get_password_strength(password)
    print('Password strength = ' + str(password_strength))
