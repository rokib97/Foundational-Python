def make_album(name, title, number=0):
    album = {"name": name, "title": title}
    # print(isinstance(album, dict))
    if (number):
        album["number"] = number
    return album


# print(make_album("balam", "ki nesha", 10))
print(make_album("balam", "ki nesha"))
