# Multithredding using concurrent.futures
import requests
import time
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a47ee8c1',
    'https://images.unsplash.com/photo-1522205407445-add114ad53c4',
    'https://images.unsplash.com/photo-1524481789034-a0f9e60b8265',
    'https://images.unsplash.com/photo-1519125323398-675f0ddb6308',
    'https://images.unsplash.com/photo-1508704019882-f233e62b79d4',
    'https://images.unsplash.com/photo-1519985176271-adbaf27c4e08',
    'https://images.unsplash.com/photo-1523397624644-d53e08f3f793',
    'https://images.unsplash.com/photo-1516892533046-a00d7d45f812',
    'https://images.unsplash.com/photo-1522364723953-23194d095f9b',
    'https://images.unsplash.com/photo-1513938709626-033611b8ccae'
]

t1 = time.perf_counter()

# Download all images using Threads
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_url} was downloaded...')

# Thread pool executor
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Start the threads
    executor.map(download_image, img_urls)

t2 = time.perf_counter()
print(f'Finished in {round(t2-t1, 2)} second(s)')