def main():
    print(f"x is {get_int('what is x?')}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
