from PIL import Image
import glob


def resizeImages():
    originalImagesPaths = glob.glob('subredditstylesheet/imagesoriginal/*')
    for path in originalImagesPaths:
        img = Image.open(path)


        img = img.resize((20, 20))
        path = path.replace('imagesoriginal', 'imagesresized')
        img.save(path)
