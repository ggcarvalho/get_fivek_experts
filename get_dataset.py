import wget,os
import pandas as pd

def url(expert):
    if expert.lower() in ["a", "b", "c", "d", "e"]:
        return "https://data.csail.mit.edu/graphics/fivek/img/tiff16_" + expert.lower() + "/"
    return -1

def images_names():
    categories = pd.read_csv("categories.txt")
    names = categories["names"]
    images = [name + ".tif" for name in names]
    return images

def get_dataset(expert):
    SOURCE = url(expert)
    names = images_names()
    out_dir = "Expert_" + str(expert).upper()
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    for name in names:
        image_url = SOURCE + name
        if not os.path.exists(os.path.join(out_dir, name)):
            image = wget.download(image_url, out = out_dir)
            print("\nSuccessfully downloaded " + name)

def main():
    expert = input("Type the expert (A-E , a-e): ")
    get_dataset(expert)

if __name__ == "__main__":
    main()