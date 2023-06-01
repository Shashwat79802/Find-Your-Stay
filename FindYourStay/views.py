from django.shortcuts import render
import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.core.paginator import Paginator
from os.path import exists
import os
import time
from pathlib import Path
import schedule
import pytz
from datetime import datetime, timedelta
import os
import logging


# logger = logging.getLogger(__name__)


BASE_DIR = Path(__file__).resolve().parent.parent
# dir_path = '/media/shashwat/2E9AD3589AD31AE3/MiniProject/data'
dir_path = os.path.join(BASE_DIR, 'data')


def output_file_name_generator(city, state):
    if ' ' in state:
        state = state.split(' ')
        state = '-'.join(state)

    return 'data/' + city + '_' + state + '.csv'


# -----------------------------------------------------------------------------------------------------------------------


def combine_csv(input_file1, input_file2, output_file):
    # Read data from input files
    data1 = []
    with open(input_file1, 'r') as file1:
        reader1 = csv.reader(file1)
        next(reader1)
        for row in reader1:
            data1.append(row)

    data2 = []
    with open(input_file2, 'r') as file2:
        reader2 = csv.reader(file2)
        next(reader2)
        for row in reader2:
            data2.append(row)

    # Combine data from input files
    combined_data = data1 + data2

    # Write combined data to output file
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Hotel Name', 'Price', 'Image', 'Address', 'Float Rating', 'Rating', 'Hotel URL'])
        for row in combined_data:
            writer.writerow(row)


# -----------------------------------------------------------------------------------------------------------------------


# returns the longitude and latitude of the input city
def forward_geocoding(city, state):
    url = "https://forward-reverse-geocoding.p.rapidapi.com/v1/forward"

    querystring = {"city": city, "state": state, "accept-	language": "en", "polygon_threshold": "0.0"}

    headers = {
        "X-RapidAPI-Key": "a68e5f91c9mshd868962b85709dbp1b9a06jsn11ff340fcaec",
        "X-RapidAPI-Host": "forward-reverse-geocoding.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    result = [response[0]['lon'], response[0]['lat']]
    print('Forward Geocoding')

    return result


# -----------------------------------------------------------------------------------------------------------------------


def sort_csv(input_file, output_file, sorting_type):
    # read the csv file into a pandas DataFrame
    df = pd.read_csv(input_file)

    if sorting_type == 1:
        sort_col_index = 4
        ascending = False
    elif sorting_type == 2:
        sort_col_index = 4
        ascending = True
    elif sorting_type == 3:
        sort_col_index = 1
        ascending = False
    else:
        sort_col_index = 1
        ascending = True

    # sort the DataFrame by the specified column index
    df.sort_values(by=df.columns[sort_col_index], ascending=ascending, inplace=True, na_position='last')

    # write the sorted DataFrame to the output file
    df.to_csv(output_file, index=False)

    print('Sort CSV')


# -----------------------------------------------------------------------------------------------------------------------


def data_cleaner(filename: str):
    df = pd.read_csv(filename)

    df.dropna(subset=[df.columns[0], df.columns[-1]], inplace=True)

    df.to_csv(filename, index=False)

    print('Data Cleaner')


# -----------------------------------------------------------------------------------------------------------------------


def oyo_scrapper(city, state):
    print("Inside Oyo Scrapper")
    geocoding = forward_geocoding(city, state)
    url = f"https://www.oyorooms.com/search/?location={city}%2C%20{state}&latitude={geocoding[1]}&longitude={geocoding[0]}"

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

    with open('data/oyo.csv', mode='w', newline='', encoding='utf-8') as file:
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

    print('Outside Oyo, file done')


# -----------------------------------------------------------------------------------------------------------------------

def yatra_selenium_scrapper(url) -> list:
    print('inside yatra selenium')

    driver = webdriver.Chrome()

    driver.get(url)

    a_tags = driver.find_elements(By.CSS_SELECTOR, 'a.bold.txt-green.pr5.dib.notOpenCal')
    data = []
    yatra_ratings = []

    for a_tag in a_tags:
        spans = a_tag.find_elements(By.CSS_SELECTOR, 'span')
        for i, span1 in enumerate(spans):
            if i % 5 == 0:
                continue
            elif i % 5 == 1:
                continue
            else:
                data.append(span1.text)

    for i in range(0, len(data), 3):
        result = data[i] + data[i + 1] + " " + data[i + 2]
        yatra_ratings.append(result)

    data.clear()
    fs_sm_spans = driver.find_elements(By.CSS_SELECTOR, 'span.fs-sm')
    for i in range(0, len(fs_sm_spans), 2):
        data.append(fs_sm_spans[i].text)

    # print(data)

    for i in range(0, len(yatra_ratings)):
        yatra_ratings[i] = yatra_ratings[i] + " " + data[i]

    print(yatra_ratings)
    driver.quit()
    return yatra_ratings


# -----------------------------------------------------------------------------------------------------------------------


def yatra_scrapper(city):
    print("inside yatra")
    # yatra scrapper

    url = f"https://www.yatra.com/hotels/hotels-in-{city}"  # https://www.yatra.com/hotels/hotels-in-bilaspur

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

    hotel_names = []
    prices = []
    images = []
    # hotel_add = []
    # h_ratings = []
    ratings = []
    Address = []
    hotel_urls = []

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    hotel_card = soup.find_all('h3', class_="text-dark mb5 fs-lg fs18 hotel-hd")
    for rows in hotel_card:
        hotel_names.append(rows.text.strip())
        hotel_urls.append("https://www.yatra.com" + rows.find('a').get('href'))

    price_tags = soup.find_all('span', class_="fs-xlg bold text-dark bold init-pop")
    for r in price_tags:
        prices.append(int(r.text.strip()[3:].replace(',', '')))

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

    yatra_ratings = yatra_selenium_scrapper(url)
    print('outside yatra selenium')

    float_ratings = []
    for r in yatra_ratings:
        if r != '':
            limit = r.find('/5')
            float_ratings.append(float(r[0:limit]))
        else:
            float_ratings.append(4)

    with open('data/yatra.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Hotel Name', 'Price', 'Image', 'Address', 'Float Rating', 'Rating', 'Hotel URL'])

        for i in range(
                max(len(hotel_names), len(prices), len(images), len(Address), len(yatra_ratings), len(hotel_urls))):
            hotel_name = hotel_names[i] if i < len(hotel_names) else None
            price = prices[i] if i < len(prices) else None
            image_url = images[i] if i < len(images) else None
            address = Address[i] if i < len(Address) else None
            float_rating = float_ratings[i] if i < len(float_ratings) else None
            yatra_rating = yatra_ratings[i] if i < len(yatra_ratings) else None
            url = hotel_urls[i] if i < len(hotel_urls) else None

            writer.writerow([hotel_name, price, image_url, address, float_rating, yatra_rating, url])

    print('outside yatra, file done')


# -----------------------------------------------------------------------------------------------------------------------

# prime scrapper function that call all the other scrapper functions, cleans the data and combines it.
def scrapper(city, state):
    oyo_scrapper(city, state)
    yatra_scrapper(city)
    data_cleaner('data/oyo.csv')
    data_cleaner('data/yatra.csv')

    output_file = output_file_name_generator(city, state)

    combine_csv('data/oyo.csv', 'data/yatra.csv', output_file)

    print('Successful...')

    # geocoding = forward_geocoding(city, state)
    #
    # url = f"https://www.oyorooms.com/search/?location={city}%2C%20{state}&latitude={geocoding[1]}&longitude={geocoding[0]}"
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
    # print('Inside Oyo')
    #
    # html_code = requests.get(url, headers=headers, timeout=50).text
    # hotel_name = []
    # Prices = []
    # images = []
    # hotel_add = []
    # h_ratings = []
    # hotel_urls = []
    # soup = BeautifulSoup(html_code, 'lxml')
    #
    # hotel_card = soup.find_all('div', class_="hotelCardListing__descriptionWrapper")
    # for rows in hotel_card:
    #     hotel_name.append(rows.find('h3', class_="listingHotelDescription__hotelName d-textEllipsis").text)
    #
    # for rows in hotel_card:
    #     hotel_urls.append('https://www.oyorooms.com' + rows.find('a', class_='c-nn640c u-width100')['href'])
    #
    # prices = soup.find_all('span', class_="listingPrice__finalPrice")
    # for r in prices:
    #     Prices.append(int(r.text[1:]))
    #
    # img = soup.find_all('div', class_="c-ahj8kj")
    # for i in img:
    #     images.append((i.find('img')).get('src'))
    #
    # address = soup.find_all('div', class_="d-body-lg listingHotelDescription__hotelAddress")
    # for a in address:
    #     hotel_add.append(a.text)
    #
    # ratings = soup.find_all('div', class_="hotelRating__wrapper")
    # for g in ratings:
    #     h_ratings.append(g.text)
    #
    # float_ratings = []
    # for g in ratings:
    #     float_ratings.append(float(g.text[0:3]))
    #
    # with open('data/oyo.csv', mode='w', newline='', encoding='utf-8') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(['Hotel Name', 'Price', 'Image', 'Address', 'Float Rating', 'Rating', 'Hotel URL'])
    #     for i in range(max(len(hotel_name), len(Prices), len(images), len(hotel_add), len(h_ratings), len(hotel_urls))):
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
    #         if i < len(float_ratings):
    #             row.append(float_ratings[i])
    #         else:
    #             row.append(None)
    #         if i < len(h_ratings):
    #             row.append(h_ratings[i])
    #         else:
    #             row.append(None)
    #         if i < len(hotel_urls):
    #             row.append(hotel_urls[i])
    #         else:
    #             row.append(None)
    #         writer.writerow(row)
    #
    # print('Outside Oyo, file done')

    # print("inside yatra")
    # # yatra scrapper
    #
    # url = f"https://www.yatra.com/hotels/hotels-in-{city}"
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
    # response = requests.get(url, headers=headers)
    # soup = BeautifulSoup(response.content, 'html.parser')
    #
    # hotel_card = soup.find_all('h3', class_="text-dark mb5 fs-lg fs18 hotel-hd")
    # for rows in hotel_card:
    #     hotel_names.append(rows.text.strip())
    #     hotel_urls.append("https://www.yatra.com" + rows.find('a').get('href'))
    #
    # price_tags = soup.find_all('span', class_="fs-xlg bold text-dark bold init-pop")
    # for r in price_tags:
    #     prices.append(r.text.strip())
    #
    # img_section = soup.find_all('div', class_='col-sm-3 img-section rel result-item-image')
    # for section in img_section:
    #     images.append(section.find('img').get('src'))
    #
    # h_ratings = []
    # ratings_section = soup.find_all('div', class_='flex')
    # for section in ratings_section:
    #     h_ratings.append(section.text.strip())
    #
    # for a in h_ratings:
    #     ratings.append(a[0])
    #     Address.append(a[14:])
    #
    # print('inside yatra selenium')
    #
    # driver = webdriver.Chrome()
    #
    # driver.get(url)
    #
    # a_tags = driver.find_elements(By.CSS_SELECTOR, 'a.bold.txt-green.pr5.dib.notOpenCal')
    # data = []
    # yatra_ratings = []
    #
    # for a_tag in a_tags:
    #     spans = a_tag.find_elements(By.CSS_SELECTOR, 'span')
    #     for i, span1 in enumerate(spans):
    #         if i % 5 == 0:
    #             continue
    #         elif i % 5 == 1:
    #             continue
    #         else:
    #             data.append(span1.text)
    #
    # for i in range(0, len(data), 3):
    #     result = data[i] + data[i + 1] + " " + data[i + 2]
    #     yatra_ratings.append(result)
    #
    # data.clear()
    # fs_sm_spans = driver.find_elements(By.CSS_SELECTOR, 'span.fs-sm')
    # for i in range(0, len(fs_sm_spans), 2):
    #     data.append(fs_sm_spans[i].text)
    #
    # # print(data)
    #
    # for i in range(0, len(yatra_ratings)):
    #     yatra_ratings[i] = yatra_ratings[i] + " " + data[i]
    #
    # driver.quit()
    #
    # print('outside yatra selenium')
    #
    # with open('data/yatra.csv', mode='w', newline='', encoding='utf-8') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(['Hotel Name', 'Price', 'Image', 'Address', 'Rating', 'Hotel URL'])
    #
    #     for i in range(max(len(hotel_names), len(prices), len(images), len(Address), len(yatra_ratings), len(hotel_urls))):
    #         hotel_name = hotel_names[i] if i < len(hotel_names) else None
    #         price = prices[i] if i < len(prices) else None
    #         image_url = images[i] if i < len(images) else None
    #         address = Address[i] if i < len(Address) else None
    #         yatra_ratings = yatra_ratings[i] if i < len(yatra_ratings) else None
    #         url = hotel_urls[i] if i < len(hotel_urls) else None
    #
    #         writer.writerow([hotel_name, price, image_url, address, yatra_ratings, url])
    #
    # print('outside yatra, file done')

    # oyo_scrapper(city, state)
    # yatra_scrapper(city)
    # data_cleaner('data/oyo.csv')
    # data_cleaner('data/yatra.csv')
    # combine_csv('data/oyo.csv', 'data/yatra.csv')
    #
    # if sort is not None:
    #     sort_csv('data/data.csv', 'data/data.csv', sort, ascending)


# -----------------------------------------------------------------------------------------------------------------------


def get_data(filename, sort):
    data_list = []

    if sort is not None:
        sort_csv(filename, filename, sort)

    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # skip header row
        for row in csv_reader:
            data_list.append(row)
    return data_list


def index(request):
    return render(request, 'FindYourStay/index.html', {})


def about_us(request):
    return render(request, 'FindYourStay/about-us.html', {})


# function that fetches result according to the provided user input
def search(request):
    url = request.get_full_path()  # taking the complete url of the current request to implement pagination query into it
    query = (request.GET['q']).split(', ')  # getting the user input from the request query
    print(query)

    required_file = output_file_name_generator(query[0], query[1])
    required_file_exists = exists(required_file)  # fetching the main data from the file

    sort = None
    if "&sort_by" in url:
        sort = int(request.GET['sort_by'])
        print(type(sort))

    if required_file_exists:
        result = get_data(required_file, sort)

    else:
        scrapper(query[0], query[1])
        result = get_data(required_file, sort)

    pages = Paginator(result, 7)  # implementing pagination, and making a Paginator object i.e. pages
    page_number = request.GET.get('page')  # getting which page number is requested
    final_data = pages.get_page(page_number)  # fetching the requested page using its page number

    if "&page=" in url:  # removing the existing &page=n from the url to obtain the base url with the user input
        url = url[:url.index("&page=")]

    if "&sort_by=" in url:  # removing the existing &page=n from the url to obtain the base url with the user input
        url = url[:url.index("&sort_by=")]

    # if "&sort_by=1" or "&sort_by=2" or "&sort_by=3" or "&sort_by=4":
    #     url = url.replace()

    return render(request, 'FindYourStay/search.html', {
        # data for the html page
        'result': final_data,
        'length': len(result),
        'page_list': [x for x in range(1, pages.num_pages + 1)],
        'url': url
    }
                  )


def delete_old_csv_files():
    # Get the current time
    current_time = time.time()

    # Get the list of all CSV files in the directory
    csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]

    # Loop through the CSV files and check their access time
    for file in csv_files:
        if file in ["oyo.csv", "yatra.csv"]:
            # Skip files named "oyo.csv" and "yatra.csv"
            continue
        file_path = os.path.join(dir_path, file)
        access_time = os.path.getatime(file_path)
        # Check if the file hasn't been accessed in the last three days
        if (current_time - access_time) // (24 * 3600) >= 3:
            # Delete the file
            os.remove(file_path)
        else:
            # Keep the file
            pass

    # Print a list of remaining files
    remaining_files = [f for f in os.listdir(dir_path) if f.endswith('.csv') and f not in ["oyo.csv", "yatra.csv"]]
    print("Remaining files:")
    for file in remaining_files:
        print(file)


# Schedule the script to run at 12:05 AM every day
# schedule.every().day.at("00:05").do(delete_old_csv_files)
#
# # Keep the script running
# while True:
#     schedule.run_pending()
#     time.sleep(1)


# scheduler = BlockingScheduler()
# scheduler.add_job(delete_old_csv_files, "cron", hour=12, minute=23)
# scheduler.start()

if __name__ == '__main__':
    while True:
        delete_old_csv_files()
        time.sleep(86400)
