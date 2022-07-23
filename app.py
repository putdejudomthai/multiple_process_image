import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = [
    'ocean1.jpg',
    'ocean2.jpg',
    'ocean3.jpg',
    'ocean4.jpg',
    'ocean5.jpg',
    'ocean6.jpg',
    'ocean7.jpg',
    'ocean8.jpg',
    'ocean9.jpg',
    'ocean10.jpg',
    'sea1.jpg',
    'sea2.jpg',
    'sea3.jpg',
    'sea4.jpg',
    'sea5.jpg',
    'sea6.jpg',
    'sea7.jpg',
    'wave1.jpg',
    'wave2.jpg',
    'wave3.jpg',
    'wave4.jpg',
    'wave5.jpeg',
    'wave6.jpg',
    'wave7.jpg',
    'wave8.jpg',
    'wave9.jpg',
    'wave10.jpg'
]

t1 = time.perf_counter()

size = (300, 300)

###note::: can run only loop of multi process part

### for loop

for img_name in img_names:
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')


### multiple process
# def process_image(img_name):
#     img = Image.open(img_name)

#     img = img.filter(ImageFilter.GaussianBlur(15))

#     img.thumbnail(size)
#     img.save(f'processed/{img_name}')
#     print(f'{img_name} was processed...')


# with concurrent.futures.ProcessPoolExecutor() as executor:
#     executor.map(process_image, img_names)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')