import random
import string


class TxtGenerator:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, amount):
        with open('test_data.txt', 'w'):
            pass
        with open('test_data.txt', 'w') as file:
            for i in range(amount):
                file.write(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randrange(3, 10))) + ';')
