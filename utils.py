def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print('Value cannot be negative.')
                continue
            return value
        except ValueError:
            print('Please enter a number.')

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value < 0:
                print('Value cannot be negative.')
                continue

            return value

        except ValueError:
            print('Please enter a number.')