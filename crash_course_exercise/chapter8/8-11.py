def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    great_magicians = []
    for magician in magicians:
        great_magicians.append("the Great " + magician)
    return great_magicians


magician_names = ["Harry Houdini", "David Copperfield",
                  "Penn Jillette", "Teller", "Derren Brown"]

modified_magicians = make_great(magician_names[:])  # Create a copy of the list
show_magicians(magician_names)  # Display original list
print("\n")
show_magicians(modified_magicians)
