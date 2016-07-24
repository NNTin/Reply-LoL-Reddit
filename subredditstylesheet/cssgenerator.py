from PIL import Image
import glob

def createSingleChampionImage():
    sourcePaths = glob.glob('subredditstylesheet/championimagesresized/*')

    totalHeight = 0
    for path in sourcePaths:
        img = Image.open(path)
        (width, height) = img.size
        totalHeight += height

    blankImage = Image.new('RGB', (width, totalHeight))

    counter = 0
    for path in sourcePaths:
        img = Image.open(path)
        blankImage.paste(img, (0, counter * width))
        counter += 1

    blankImage.save('subredditstylesheet/singlechampionimage.png')

def generateCode():
    template = '.flair-zac::before,a[href="#c-{name}"]{background-position: -{width}px -{height}px}'
    sourcePaths = glob.glob('subredditstylesheet/championimagesresized/*')

    counter = 0
    result = ''
    for path in sourcePaths:
        name = path.replace('subredditstylesheet/championimagesresized\\', '').replace('.png', '').lower()
        partialResult = template.replace('{name}', name).replace('{width}', '0').replace('{height}', str(counter * 20))
        counter += 1
        result += partialResult + '\n'
    print(result)

def generateTestCode():
    sourcePaths = glob.glob('subredditstylesheet/championimagesresized/*')
    result = ''
    for path in sourcePaths:
        name = path.replace('subredditstylesheet/championimagesresized\\', '').replace('.png', '').lower()
        template = '[](#c-{name})'
        result += template.format(name=name)
    print(result)
