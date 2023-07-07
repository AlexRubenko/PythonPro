class Colorizer:
    def __init__(self, color_code):
        self.color_code = color_code

    def __enter__(self):
        print(f'\033[{self.color_code}m', end='')

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('\033[0m', end='')


print('\033[93m', end='')
print('aaa')
print('bbb')
print('\033[0m', end='')
print('ccc')

with Colorizer("95"):
    print('printed in red')
print('printed in default color')
