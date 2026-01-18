import novice


def make_thumbnail(filename, width=100):
    picture = novice.open(filename)
    new_height = int(picture.height * float(width) / picture.width)
    picture.size = (width, new_height)
    return picture
    