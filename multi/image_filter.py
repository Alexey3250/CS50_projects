import time
import concurrent.futures
from PIL import Image, ImageFilter

start = time.perf_counter()

img_names = [
    'photo-1508704019882-f233e62b79d4.jpg',
    'photo-1513938709626-033611b8ccae.jpg',
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1516892533046-a00d7d45f812.jpg',
    'photo-1519125323398-675f0ddb6308.jpg',
    'photo-1519985176271-adbaf27c4e08.jpg',
    'photo-1522205407445-add114ad53c4.jpg',
    'photo-1522364723953-23194d095f9b.jpg',
    'photo-1523397624644-d53e08f3f793.jpg',
    'photo-1524429656589-6633a47ee8c1.jpg',
    'photo-1524481789034-a0f9e60b8265.jpg',
    'photo-1532009324734-20a7a5813719.jpg'
]

size = (1200, 1200)

# process images
def process_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.BLUR)
    img.thumbnail(size)
    img.save(f'processed/{img_name}_blur.jpg')
    print(f'{img_name} was processed...')

# Process images using ProcessPoolExecutor
with concurrent.futures.ProcessPoolExecutor() as executor:
    # Explain the sintax of executor.map()
    
    executor.map(process_image, img_names)



t2 = time.perf_counter()
print(f'Finished in {round(t2-start, 2)} second(s)')

# Process images using ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(process_image, img_names)

t2 = time.perf_counter()
print(f'Finished in {round(t2-start, 2)} second(s)')