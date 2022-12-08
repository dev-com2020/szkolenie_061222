import json
from PIL import Image

with open("pogoda.json")as f:
    pogoda = json.load(f)

ikona = "116.png"

img = Image.open(ikona)
# img.show()
print(f"""
      🥷🏼🥷🏼🥷🏼
      Dane pogodowe dotyczące miejscowości: {pogoda["location"]["name"]}
      Temperatura powietrza wynosi: {pogoda["current"]["temp_c"]}
      Zachmurzenie: {pogoda["current"]["condition"]["text"]}
      Ikona: {pogoda["current"]["condition"]['icon']}
   

      🥷🏼🥷🏼🥷🏼 
""")