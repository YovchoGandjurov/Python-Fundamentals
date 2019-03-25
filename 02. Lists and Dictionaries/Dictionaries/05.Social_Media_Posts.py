dct = {}

while True:
    inp = input()
    if inp == "drop the media":
        break

    command = inp.split(" ")[0]
    post_name = inp.split(" ")[1]

    if command == "post":
        dct[post_name] = {"Likes": 0, "Dislikes": 0, "Comments": {}}

    elif command == "like":
        dct[post_name]["Likes"] += 1

    elif command == "dislike":
        dct[post_name]["Dislikes"] += 1

    elif command == "comment":
        dct[post_name]["Comments"].update(
            {inp.split(" ")[2]: inp.split(" ")[3:]}
            )

for key, value in dct.items():
    print("Post: {} | Likes: {} | Dislikes: {}\nComments:". format(
          key, value['Likes'], value['Dislikes'])
          )

    if value["Comments"] == {}:
        print("None")
    else:
        for x, y in value["Comments"].items():
            print("*  {}: {}".format(x, " ".join(y)))
