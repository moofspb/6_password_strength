import re
import getpass


def get_password_strength(password):
    strength = 1  # minimal value
    length_points = 1
    lowercase_points = 1
    uppercase_points = 1
    digit_points = 2
    symbol_points = 3
    if len(password) >= 8:
        strength += length_points

    if re.search(r'[a-z]+', password):
        strength += lowercase_points

    if re.search(r'[A-Z]+', password):
        strength += uppercase_points

    if re.search(r'\d', password):
        strength += digit_points

    if re.search(r'[^A-Za-z0-9]+', password):
        strength += symbol_points

    return strength


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
