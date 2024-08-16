from bs4 import BeautifulSoup
import requests

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.in/BROTHERS-Silent-Ticking-Operated-Decorative/dp/B0BN25CM3K/ref=sr_1_23_sspa?crid=26BDC9B7W7Z9A&dib=eyJ2IjoiMSJ9.ObUoZYKRiZ324eObexNe9YivLvlItXTkwoR31sv_7U0yzQKqnelyKYSsH2PcRbAA2YPfSADvs38GnRyXOPk3bGvn9aBvpBn9A6EsAKJ2c9t15hNq2qPektkMwPZGZUKExXwUgSztbVDEYtdPJ462gmS_kKPu7Bs5nyAiguzcYKK3gHimqHHXbXg6xTzUJzgv0HdScTf_EXhWC2z5q9pA564fK1sv3D1FuJe9HQ4aBLj1p_sXnEKxpL8xjgC4aS874nGaQ_W0ihGxciQQo3wI6Xe5oNFRQG8l7fR4dyufKKY.Ye2uuGu_B2iVreuJ3ke44CWjDLr6ePn_l7wCJ88ybRE&dib_tag=se&keywords=custom+wall+clock&qid=1723568274&sprefix=customise+wall+clock%2Caps%2C196&sr=8-23-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&psc=1"

response = requests.get(live_url)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

# Find the HTML element that contains the price
price = soup.find(class_="aok-offscreen").get_text()

# Remove the dollar sign using split
price_without_currency = price.split("₹")[1]

# Convert to floating point number
#price_as_float = float(price_without_currency)
print(price_without_currency)

price = price_without_currency.split(" ")
price_as_float = float(price[0])
print(price_as_float)