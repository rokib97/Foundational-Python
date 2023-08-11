dog = {
    "kind": "dog",
    "owner": "rokib"
}
cat = {
    "kind": "cat",
    "owner": "hasib"
}
elephant = {
    "kind": "elephant",
    "owner": "hasan"
}

animals = [dog, cat, elephant]

for animal in animals:
    print(f"This is Mr. {animal['kind']} and Owner is {animal['owner']} ")
