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
# a_tag = soup.find('a', {'class': 'bold txt-green pr5 dib notOpenCal', 'data-reactid': '.0.1.1:$0.0.1.1.0.1.0.0.1'})
#
# span_tag = a_tag.find('span', {'data-reactid': '.0.1.1:$0.0.1.1.0.1.0.0.1.1'})
#
# data = span_tag.text
# print(data)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
# # launch the browser
# browser = webdriver.Chrome()
#
# # navigate to the webpage
# browser.get('https://www.yatra.com/hotels/hotels-in-durg')
#
# wait = WebDriverWait(browser, 10)
# a_tags = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "bold.txt-green.pr5.dib.notOpenCal")))
#
# # Loop through all the a tags and extract the desired data
# for a_tag in a_tags:
#     # Extract data from first span tag
#     span_tag_1 = a_tag.find_element(By.CSS_SELECTOR, "span[data-reactid='.0.1.1:$0.0.1.1.0.1.0.0.1.1']")
#     data_1 = span_tag_1.text
#
#     # Extract data from second span tag
#     span_tag_2 = a_tag.find_element(By.CSS_SELECTOR, "span[data-reactid='.0.1.1:$0.0.1.1.0.1.0.0.1.2']")
#     data_2 = span_tag_2.text
#
#     # Extract data from third span tag
#     span_tag_3 = a_tag.find_element(By.CSS_SELECTOR, "span[data-reactid='.0.1.1:$0.0.1.1.0.1.0.1.0.1']")
#     data_3 = span_tag_3.text
#
#     # Print the extracted data
#     print(data_1, data_2, data_3)
#
# # Close the driver
# browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.yatra.com/hotels/hotels-in-durg")
#
# a_tags = driver.find_elements(By.CSS_SELECTOR, 'a.bold.txt-green.pr5.dib.notOpenCal')
#
# for a_tag in a_tags:
#     spans = a_tag.find_elements(By.CSS_SELECTOR, 'span')
#     for span in spans:
#         print(span.text)
#
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.yatra.com/hotels/hotels-in-goa")
#
# a_tags = driver.find_elements(By.CSS_SELECTOR, 'a.bold.txt-green.pr5.dib.notOpenCal')
#
# for a_tag in a_tags:
#     spans = a_tag.find_elements(By.CSS_SELECTOR, 'span')
#     for span1 in spans:
#         print(span1.text)
#
# fs_sm_spans = driver.find_elements(By.CSS_SELECTOR, 'span.fs-sm')
# for span2 in fs_sm_spans:
#     print(span2.text)
#
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.yatra.com/hotels/hotels-in-bilaspur")

a_tags = driver.find_elements(By.CSS_SELECTOR, 'a.bold.txt-green.pr5.dib.notOpenCal')
data = []
results = []

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
    result = data[i] + data[i+1] + " " + data[i+2]
    results.append(result)

# print(results)
# print(data)

data.clear()
fs_sm_spans = driver.find_elements(By.CSS_SELECTOR, 'span.fs-sm')
for i in range(0, len(fs_sm_spans), 2):
    data.append(fs_sm_spans[i].text)

# print(data)

for i in range(0, len(results)):
    results[i] = results[i] + " " + data[i]

print(results)
# print(data)

driver.quit()

#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
#
# options = Options()
# options.add_argument('--headless')
# service = Service('driver/chromedriver')  # Replace with the path to your chromedriver
# driver = webdriver.Chrome(service=service, options=options, desired_capabilities=None)
#
# driver.get("https://www.yatra.com/hotels/hotels-in-durg")
#
# a_tags = driver.find_elements(By.CSS_SELECTOR, 'a.bold.txt-green.pr5.dib.notOpenCal')
# data = []
# results = []
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
#     results.append(result)
#
# data.clear()
# fs_sm_spans = driver.find_elements(By.CSS_SELECTOR, 'span.fs-sm')
# for i in range(0, len(fs_sm_spans), 2):
#     data.append(fs_sm_spans[i].text)
#
# for i in range(0, len(results)):
#     results[i] = results[i] + " " + data[i]
#
# print(results)
# print(data)
#
# driver.quit()
