# import csv
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.yatra.com/hotels/hotels-in-durg"
#
# hotel_names = []
# prices = []
# images = []
# hotel_add = []
# h_ratings = []
# ratings = []
# Address = []
# hotel_urls = []
#
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/B04",
#     "Accept-Language": "en-US,en;q=0.9",
#     "Referer": "https://www.yatra.com/hotels/",
#     "Connection": "keep-alive",
#     "Content-Type": "text/html; charset=utf-8",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Upgrade-Insecure-Requests": "1",
#     "Cache-Control": "max-age=0"
# }
#
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, 'html.parser')
#
# hotel_card = soup.find_all('h3', class_="text-dark mb5 fs-lg fs18 hotel-hd")
# for rows in hotel_card:
#     hotel_names.append(rows.text.strip())
#
# price_tags = soup.find_all('span', class_="fs-xlg bold text-dark bold init-pop")
# for r in price_tags:
#     prices.append(r.text.strip())
#
#
# img_section = soup.find_all('div', class_='col-sm-3 img-section rel result-item-image')
# for section in img_section:
#     images.append(section.find('img').get('src'))
#
# ratings_section = soup.find_all('div', class_='flex')
# for section in ratings_section:
#     h_ratings.append(section.text.strip())
#
# for a in h_ratings:
#     ratings.append(a[0])
#     Address.append(a[14:])
#
# for rows in hotel_card:
#     hotel_names.append(rows.text.strip())
#     hotel_urls.append(rows.find('a').get('href'))
#
# # Write data to CSV file
# with open('hotels_data.csv', mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Hotel Name', 'Price', 'Image URL', 'Address', 'Rating', 'URL'])
#
#     for i in range(max(len(hotel_names), len(prices), len(images), len(Address), len(ratings), len(hotel_urls))):
#         hotel_name = hotel_names[i] if i < len(hotel_names) else None
#         price = prices[i] if i < len(prices) else None
#         image_url = images[i] if i < len(images) else None
#         address = Address[i] if i < len(Address) else None
#         rating = ratings[i] if i < len(ratings) else None
#         url = hotel_urls[i] if i < len(hotel_urls) else None
#
#         writer.writerow([hotel_name, price, image_url, address, rating, url])
#
# print("Data has been written to 'hotels_data.csv' file.")


import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.yatra.com/hotels/hotels-in-jaipur"

hotel_names = []
prices = []
images = []
hotel_add = []
h_ratings = []
ratings = []
Address = []
hotel_urls = []

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/B04",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.yatra.com/hotels/",
    "Connection": "keep-alive",
    "Content-Type": "text/html; charset=utf-8",
    "Accept-Encoding": "gzip, deflate, br",
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "max-age=0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

hotel_card = soup.find_all('h3', class_="text-dark mb5 fs-lg fs18 hotel-hd")
for rows in hotel_card:
    hotel_names.append(rows.text.strip())
    hotel_urls.append("https://www.yatra.com" + rows.find('a').get('href'))

price_tags = soup.find_all('span', class_="fs-xlg bold text-dark bold init-pop")
for r in price_tags:
    prices.append(r.text.strip()[3:])

img_section = soup.find_all('div', class_='col-sm-3 img-section rel result-item-image')
for section in img_section:
    images.append(section.find('img').get('src'))

h_ratings = []
ratings_section = soup.find_all('div', class_='flex')
for section in ratings_section:
    h_ratings.append(section.text.strip())

for a in h_ratings:
    ratings.append(a[0])
    Address.append(a[14:])

with open('FindYourStay/data/yatra.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Hotel Name', 'Price', 'Image', 'Address', 'Rating', 'Hotel URL'])

    for i in range(max(len(hotel_names), len(prices), len(images), len(Address), len(ratings), len(hotel_urls))):
        hotel_name = hotel_names[i] if i < len(hotel_names) else None
        price = prices[i] if i < len(prices) else None
        image_url = images[i] if i < len(images) else None
        address = Address[i] if i < len(Address) else None
        rating = ratings[i] if i < len(ratings) else None
        url = hotel_urls[i] if i < len(hotel_urls) else None

        writer.writerow([hotel_name, price, image_url, address, rating, url])
