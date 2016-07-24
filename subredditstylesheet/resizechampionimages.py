from PIL import Image
import glob


def resizeChampionImages():
    originalImagesPaths = glob.glob('subredditstylesheet/championimagesoriginal/*')
    for path in originalImagesPaths:
        img = Image.open(path)
        img = img.resize((20, 20))
        path = path.replace('championimagesoriginal', 'championimagesresized')
        img.save(path)
