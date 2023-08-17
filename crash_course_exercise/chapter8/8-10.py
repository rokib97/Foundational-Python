def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]


magician_names = ["Harry Houdini", "David Copperfield",
                  "Penn Jillette", "Teller", "Derren Brown"]

make_great(magician_names)
show_magicians(magician_names)
