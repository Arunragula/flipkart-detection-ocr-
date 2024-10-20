from googleapiclient.discovery import build
import os
import requests
from PIL import Image
from io import BytesIO

def search_and_download_images(terms, api_key, search_engine_id, num_images_per_term=50, output_dir='images'):
    service = build("customsearch", "v1", developerKey=api_key)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    for term in terms:
        print(f"Searching and downloading for term: {term}")
        term_dir = os.path.join(output_dir, term.replace(' ', '_'))
        os.makedirs(term_dir, exist_ok=True)

        start_index = 1
        downloaded_count = 0

        while downloaded_count < num_images_per_term:
            try:
                # Perform search
                res = service.cse().list(
                    q=f"{term} product",
                    cx=search_engine_id,
                    searchType='image',
                    num=10,
                    start=start_index,
                ).execute()

                if 'items' not in res:
                    print(f"No items found for term: {term}")
                    break

                for item in res['items']:
                    if downloaded_count >= num_images_per_term:
                        break

                    image_url = item['link']
                    try:
                        # Download the image
                        response = requests.get(image_url)
                        response.raise_for_status()  # Raise an error for bad responses
                        
                        img = Image.open(BytesIO(response.content))
                        
                        # Generate a unique image name
                        img_name = f"{term.replace(' ', '_')}_{downloaded_count + 1}.jpg"
                        img.save(os.path.join(term_dir, img_name))

                        downloaded_count += 1
                        print(f"Downloaded {img_name}")

                    except Exception as e:
                        print(f"Failed to download {image_url}: {e}")

                start_index += 10

            except Exception as e:
                print(f"An error occurred while searching for {term}: {e}")
                break

    print(f"Download complete. Images saved to {output_dir}")

# Example usage
api_key = "AIzaSyBVFrLpWn720BppY0NvB10kWNrHAAYywhM"



search_engine_id = "1671ae3ab101241a1"

# List of products
products = [
    "Headphones",
    "Bluetooth Speakers","earpods"
    "Power Banks","Lays",
    "Bingo",
    "Kurkure",
    "Washing Powder","Toothpaste",
    "Shampoo","chargers"
    "Soap","Knives","laptops","collegebags",'bottles',"shoes","mugs","toothbrush"
]


num_images_per_term = 8 # Number of images to download per term
output_dir = "dataset"  # Directory to save images

search_and_download_images(products, api_key, search_engine_id, num_images_per_term, output_dir)
'''[11:08 PM, 10/18/2024] Rajini Hstl: AIzaSyBVFrLpWn720BppY0NvB10kWNrHAAYywhM
[11:10 PM, 10/18/2024] Rajini Hstl: <script async src="https://cse.google.com/cse.js?cx=1671ae3ab101241a1">
</script>
<div class="gcse-search"></div>'''