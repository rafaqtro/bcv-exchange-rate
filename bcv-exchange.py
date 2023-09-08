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

#get date
date_posn = text_decode.find('Fecha Valor:')
rest_of_text = text_decode[date_posn:]
date = re.search(r'<span \w+=".+">(\w+, \d+ \w+  \d+)</span>', rest_of_text)

def match_curr(currency, text):
    if currency == "EUR" or currency == "CNY":
        posn = text.find('<span> '+currency+' </span>	 </div>')
        rest_text = text[posn:]
        curr_val = re.search(r'<strong> (\d+,\d+) </strong>', rest_text)
    elif currency == "TRY" or currency == "RUB" or currency == "USD":
        posn = text.find('<span> '+currency+'</span>	 </div>')
        rest_text = text[posn:]
        curr_val = re.search(r'<strong> (\d+,\d+) </strong>', rest_text)
    return curr_val

test_euro = match_curr('EUR', text_decode)
test_cny  = match_curr('CNY', text_decode)
test_try  = match_curr('TRY', text_decode)
test_rub  = match_curr('RUB', text_decode)
test_usd  = match_curr('USD', text_decode)


def get_value(re_match):
    if re_match:
        value = re_match.group(1)
    else:
        value = "can't get value"
    return value

def show(u, d, cs):
    print("---------------------------")
    print(f"{cs} BCV = {u} ")
    print(f"{d}")
    print("---------------------------")

eur_v = get_value(test_euro)
cny_v = get_value(test_cny)
try_v = get_value(test_try)
rub_v = get_value(test_rub)
usd_v = get_value(test_usd)
date_v = get_value(date)

#change the form nn,nn to nn.nn
# ex 33,33 to 33.33
#usd_v2 = usd_v.replace(",",".")
#usd_float = float(usd_v2)
#usd_round = round(usd_float, 4)
 
show(eur_v, date_v,"€")
show(cny_v, date_v,"¥")
show(try_v, date_v,"₺")
show(rub_v, date_v,"₽")
show(usd_v, date_v,"$")



