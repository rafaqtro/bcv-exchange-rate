from urllib.request import urlopen
import re

bcv = "http://www.bcv.org.ve/"

try:
    content = urlopen(bcv)
except:
    print("Error on urllib work.")
    print("The program will close.")
    exit()

text = content.read()
text_decode = text.decode('utf-8')
usd_posn = text_decode.find('<span> USD</span>	 </div>')

rest_of_text = text_decode[usd_posn:]

usd = re.search(r'<strong> (\d+,\d+) </strong>', rest_of_text)

date = re.search(r'Fecha Valor: <span \w+=".+">(\w+, \d+ \w+  \d+)</span>', rest_of_text)

def get_value(re_match):
    if re_match:
        value = re_match.group(1)
    else:
        value = "can't get value"
    return value

def show(u, d):
    print("---------------------------")
    print(f"$ BCV = {u} ")
    print(f"{d}")
    print("---------------------------")

usd_v = get_value(usd)
date_v = get_value(date)

#change the form nn,nn to nn.nn
# ex 33,33 to 33.33
usd_v2 = usd_v.replace(",",".")
usd_float = float(usd_v2)
usd_round = round(usd_float, 4)
 
show(usd_round, date_v)



