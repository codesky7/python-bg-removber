from rembg import remove
from PIL import Image

input_path = 'I:\\python\\bgremover\\img.png'
output_path = 'I:\\python\\bgremover\\imgbg.png'

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)
