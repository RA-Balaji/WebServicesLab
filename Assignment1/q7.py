import code128
from PIL import Image
import treepoem

def generate_fun(number):
    code128.image('image/' + number + '.png')
    with open("../UI/images/barcode/"+number+'.svg', "w") as f:
            f.write(code128.svg(number))