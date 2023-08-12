def convert(input_str):
    converted_str = input_str.replace(":)", "🙂").replace(":(", "🙁")
    return converted_str


def main():
    user_input = input("Please enter a sentence: ")
    converted_input = convert(user_input)
    print("Converted input:", converted_input)


if __name__ == "__main__":
    main()
