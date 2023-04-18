# import requests
# from bs4 import BeautifulSoup
#
# # Set the URL and headers
# url = "https://www.oyorooms.com/search/?location=Durg%2C%20Chhattisgarh&latitude=21.1938475&longitude=81.3509416"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Referer": "https://www.google.com/",
#     "Connection": "keep-alive",
#     "Content-Type": "text/html",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Upgrade-Insecure-Requests": "1",
#     "Cache-Control": "max-age=0",
# }
#
# html_code = requests.get(url, headers=headers, timeout=50).text
# hotel_name = []
# Prices = []
# images = []
# hotel_add = []
# h_ratings = []
# soup = BeautifulSoup(html_code, 'lxml')
#
# hotel_card = soup.find_all('h3', class_="listingHotelDescription__hotelName d-textEllipsis")
# for rows in hotel_card:
#     hotel_name.append(rows.text)
# print(hotel_name)
# print(len(hotel_name))
#
#
# prices = soup.find_all('span', class_="listingPrice__finalPrice")
# for r in prices:
#     Prices.append(r.text)
# print(Prices)
# print(len(Prices))
#
# img = soup.find_all('div', class_="c-ahj8kj")
# for i in img:
#     images.append((i.find('img')).get('src'))
# print(images)
# print(len(images))
#
# address = soup.find_all('div', class_="d-body-lg listingHotelDescription__hotelAddress")
# for a in address:
#     hotel_add.append(a.text)
# print(hotel_add)
# print(len(hotel_add))
#
#
# ratings = soup.find_all('div', class_="hotelRating__wrapper")
# for g in ratings:
#     h_ratings.append(g.text)
# print(h_ratings)
# print(len(h_ratings))



# others = []

# other_images = soup.find_all('div', class_='c-ahj8kj')
# for img in other_images:
#     others.append(img.find('img').get('src'))
# print(other_images)
# print(others)
# print(len(others))


# image_divs = soup.find_all('div', class_='listingImageCard__img')
#
# for img in image_divs:
#     each_img = img.find('img', class_='c-2tglnv listingImageCard__img--full ')
#     others.append(each_img)
#
# print(others)
#
#
# # print(other_images)
# # print(others)
# print(len(others))



# import requests
# from bs4 import BeautifulSoup
#
# # Set the URL and headers
# # url = "https://www.oyorooms.com/search/?location=Durg%2C%20Chhattisgarh&latitude=21.1938475&longitude=81.3509416"
# url = "https://www.oyorooms.com/search?location=Jaipur%2C%20Rajasthan&latitude=26.9124&longitude=75.7873"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Referer": "https://www.google.com/",
#     "Connection": "keep-alive",
#     "Content-Type": "text/html",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Upgrade-Insecure-Requests": "1",
#     "Cache-Control": "max-age=0",
# }
#
# html_code = requests.get(url, headers=headers, timeout=50).text
# hotel_name = []
# Prices = []
# images = []
# hotel_add = []
# h_ratings = []
# soup = BeautifulSoup(html_code, 'lxml')
#
# hotel_card = soup.find_all('h3', class_="listingHotelDescription__hotelName d-textEllipsis")
# for rows in hotel_card:
#     hotel_name.append(rows.text)
# print(hotel_name)
# print(len(hotel_name))
#
#
# prices = soup.find_all('span', class_="listingPrice__finalPrice")
# for r in prices:
#     Prices.append(r.text)
# print(Prices)
# print(len(Prices))
#
#
# img = soup.find_all('div', class_="c-ahj8kj")
# for i in img:
#     images.append((i.find('img')).get('src'))
# print(images)
# print(len(images))
#
# address = soup.find_all('div', class_="d-body-lg listingHotelDescription__hotelAddress")
# for a in address:
#     hotel_add.append(a.text)
# print(hotel_add)
# print(len(hotel_add))
#
# ratings = soup.find_all('div', class_="hotelRating__wrapper")
# for g in ratings:
#     h_ratings.append(g.text)
# print(h_ratings)
# print(len(h_ratings))


# import requests
# from bs4 import BeautifulSoup
#
# # url = "https://www.oyorooms.com/search?location=Jaipur%2C%20Rajasthan&latitude=26.9124&longitude=75.7873"
# url = "https://www.oyorooms.com/search/?location=Durg%2C%20Chhattisgarh&latitude=21.1938475&longitude=81.3509416"
#
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Referer": "https://www.google.com/",
#     "Connection": "keep-alive",
#     "Content-Type": "text/html",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Upgrade-Insecure-Requests": "1",
#     "Cache-Control": "max-age=0",
# }
#
# html_code = requests.get(url, headers=headers, timeout=50).text
# hotel_name = []
# Prices = []
# images = []
# hotel_add = []
# h_ratings = []
# soup = BeautifulSoup(html_code, 'lxml')
#
# hotel_card = soup.find_all('h3', class_="listingHotelDescription__hotelName d-textEllipsis")
# for rows in hotel_card:
#     try:
#         hotel_name.append(rows.text)
#     except:
#         hotel_name.append(None)
# print(hotel_name)
# print(len(hotel_name))
#
#
# prices = soup.find_all('span', class_="listingPrice__finalPrice")
# for r in prices:
#     try:
#         Prices.append(r.text)
#     except:
#         Prices.append(None)
# print(Prices)
# print(len(Prices))
#
#
# img = soup.find_all('div', class_="c-ahj8kj")
# for i in img:
#     try:
#         images.append((i.find('img')).get('src'))
#     except:
#         images.append(None)
# print(images)
# print(len(images))
#
# address = soup.find_all('div', class_="d-body-lg listingHotelDescription__hotelAddress")
# for a in address:
#     try:
#         hotel_add.append(a.text)
#     except:
#         hotel_add.append(None)
# print(hotel_add)
# print(len(hotel_add))
#
# ratings = soup.find_all('div', class_="hotelRating__wrapper")
# for g in ratings:
#     try:
#         h_ratings.append(g.text)
#     except:
#         h_ratings.append(None)
# print(h_ratings)
# print(len(h_ratings))



# import requests
# from bs4 import BeautifulSoup
# import csv
#
# # url = "https://www.oyorooms.com/search?location=Jaipur%2C%20Rajasthan&latitude=26.9124&longitude=75.7873"
# url = "https://www.oyorooms.com/search/?location=Durg%2C%20Chhattisgarh&latitude=21.1938475&longitude=81.3509416"
#
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Referer": "https://www.google.com/",
#     "Connection": "keep-alive",
#     "Content-Type": "text/html",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Upgrade-Insecure-Requests": "1",
#     "Cache-Control": "max-age=0",
# }
#
# html_code = requests.get(url, headers=headers, timeout=50).text
# hotel_name = []
# Prices = []
# images = []
# hotel_add = []
# h_ratings = []
# soup = BeautifulSoup(html_code, 'lxml')
#
# hotel_card = soup.find_all('h3', class_="listingHotelDescription__hotelName d-textEllipsis")
# for rows in hotel_card:
#     try:
#         hotel_name.append(rows.text)
#     except:
#         hotel_name.append(None)
#
#
# prices = soup.find_all('span', class_="listingPrice__finalPrice")
# for r in prices:
#     try:
#         Prices.append(r.text)
#     except:
#         Prices.append(None)
#
#
# img = soup.find_all('div', class_="c-ahj8kj")
# for i in img:
#     try:
#         images.append((i.find('img')).get('src'))
#     except:
#         images.append(None)
#
#
# address = soup.find_all('div', class_="d-body-lg listingHotelDescription__hotelAddress")
# for a in address:
#     try:
#         hotel_add.append(a.text)
#     except:
#         hotel_add.append(None)
#
#
# ratings = soup.find_all('div', class_="hotelRating__wrapper")
# for g in ratings:
#     try:
#         h_ratings.append(g.text)
#     except:
#         h_ratings.append(None)
#
#
# # Write to CSV file
# with open('oyo_rooms_data.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Hotel Name', 'Price', 'Image URL', 'Address', 'Ratings'])
#     for i in range(len(hotel_name)):
#         writer.writerow([hotel_name[i], Prices[i], images[i], hotel_add[i], h_ratings[i]])


# import csv
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.oyorooms.com/search/?location=Durg%2C%20Chhattisgarh&latitude=21.1938475&longitude=81.3509416"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Referer": "https://www.google.com/",
#     "Connection": "keep-alive",
#     "Content-Type": "text/html",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Upgrade-Insecure-Requests": "1",
#     "Cache-Control": "max-age=0",
# }
#
# html_code = requests.get(url, headers=headers, timeout=50).text
# hotel_name = []
# Prices = []
# images = []
# hotel_add = []
# h_ratings = []
# soup = BeautifulSoup(html_code, 'lxml')
#
# hotel_card = soup.find_all('h3', class_="listingHotelDescription__hotelName d-textEllipsis")
# for rows in hotel_card:
#     hotel_name.append(rows.text)
# # print(hotel_name)
# # print(len(hotel_name))
#
#
# prices = soup.find_all('span', class_="listingPrice__finalPrice")
# for r in prices:
#     Prices.append(r.text)
# # print(Prices)
# # print(len(Prices))
#
#
# img = soup.find_all('div', class_="c-ahj8kj")
# for i in img:
#     images.append((i.find('img')).get('src'))
# # print(images)
# # print(len(images))
#
#
# address = soup.find_all('div', class_="d-body-lg listingHotelDescription__hotelAddress")
# for a in address:
#     hotel_add.append(a.text)
# # print(hotel_add)
# # print(len(hotel_add))
#
#
# ratings = soup.find_all('div', class_="hotelRating__wrapper")
# for g in ratings:
#     h_ratings.append(g.text)
# # print(h_ratings)
# # print(len(h_ratings))
#
#
# with open('oyo.csv', mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Hotel Name', 'Price', 'Image', 'Address', 'Rating'])
#     for i in range(max(len(hotel_name), len(Prices), len(images), len(hotel_add), len(h_ratings))):
#         row = []
#         if i < len(hotel_name):
#             row.append(hotel_name[i])
#         else:
#             row.append(None)
#         if i < len(Prices):
#             row.append(Prices[i])
#         else:
#             row.append(None)
#         if i < len(images):
#             row.append(images[i])
#         else:
#             row.append(None)
#         if i < len(hotel_add):
#             row.append(hotel_add[i])
#         else:
#             row.append(None)
#         if i < len(h_ratings):
#             row.append(h_ratings[i])
#         else:
#             row.append(None)
#         writer.writerow(row)


import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.oyorooms.com/search/?location=Durg%2C%20Chhattisgarh&latitude=21.1938475&longitude=81.3509416"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive",
    "Content-Type": "text/html",
    "Accept-Encoding": "gzip, deflate, br",
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "max-age=0",
}

html_code = requests.get(url, headers=headers, timeout=50).text
hotel_name = []
Prices = []
images = []
hotel_add = []
h_ratings = []
hotel_urls = []
soup = BeautifulSoup(html_code, 'lxml')

hotel_card = soup.find_all('div', class_="hotelCardListing__descriptionWrapper")
for rows in hotel_card:
    hotel_name.append(rows.find('h3', class_="listingHotelDescription__hotelName d-textEllipsis").text)


for rows in hotel_card:
    hotel_urls.append('https://www.oyorooms.com' + rows.find('a', class_='c-nn640c u-width100')['href'])


prices = soup.find_all('span', class_="listingPrice__finalPrice")
for r in prices:
    Prices.append(int(r.text[1:]))


img = soup.find_all('div', class_="c-ahj8kj")
for i in img:
    images.append((i.find('img')).get('src'))


address = soup.find_all('div', class_="d-body-lg listingHotelDescription__hotelAddress")
for a in address:
    hotel_add.append(a.text)


ratings = soup.find_all('div', class_="hotelRating__wrapper")
for g in ratings:
    h_ratings.append(g.text)


float_ratings = []
for g in ratings:
    float_ratings.append(float(g.text[0:3]))


with open('FindYourStay/data/oyo.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Hotel Name', 'Price', 'Image', 'Address', 'Float Rating', 'Rating', 'Hotel URL'])
    for i in range(max(len(hotel_name), len(Prices), len(images), len(hotel_add), len(h_ratings), len(hotel_urls))):
        row = []
        if i < len(hotel_name):
            row.append(hotel_name[i])
        else:
            row.append(None)
        if i < len(Prices):
            row.append(Prices[i])
        else:
            row.append(None)
        if i < len(images):
            row.append(images[i])
        else:
            row.append(None)
        if i < len(hotel_add):
            row.append(hotel_add[i])
        else:
            row.append(None)
        if i < len(float_ratings):
            row.append(float_ratings[i])
        else:
            row.append(None)
        if i < len(h_ratings):
            row.append(h_ratings[i])
        else:
            row.append(None)
        if i < len(hotel_urls):
            row.append(hotel_urls[i])
        else:
            row.append(None)
        writer.writerow(row)
