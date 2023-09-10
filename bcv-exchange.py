from urllib.request import urlopen
import re

bcv = "http://www.bcv.org.ve/"
exchange = []

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
        posn = text.find('<span> '+currency+'</span>	 </div>')
        rest_text = text[posn:]
        curr_val = (currency, re.search(r'<strong> (\d+,\d+) </strong>', rest_text))
    elif currency == "TRY" or currency == "RUB" or currency == "USD":
        posn = text.find('<span> '+currency+'</span>	 </div>')
        rest_text = text[posn:]
        curr_val = (currency, re.search(r'<strong> (\d+,\d+) </strong>', rest_text))
    return curr_val

#test_euro = match_curr('EUR', text_decode)
#test_cny  = match_curr('CNY', text_decode)
#test_try  = match_curr('TRY', text_decode)
#test_rub  = match_curr('RUB', text_decode)
#test_usd  = match_curr('USD', text_decode)

currency_list = ['EUR', 'CNY', 'TRY', 'RUB', 'USD']
list_match = []

def match_curr_all(c_list,text_d,match_l):
    for c in c_list:
        match_l.append(match_curr(c,text_d))

match_curr_all(currency_list,text_decode,list_match)
print(list_match)
        
def get_value(re_match):
    if re_match:
        value = re_match.group(1)
    else:
        value = "can't get value"
    return value


#for c in currency_list:
#    match_curr(c,text_decode) 

list_curr_val = []

def get_curr_val(list_c_re):
    list_v = []
    for i in list_c_re:
        list_v.append((i[0],get_value(i[1])))
    return list_v

list_curr_dot = []

def replace_to_dot(list_v):
    list_v_d = []
    for i in list_v:
         list_v_d.append((i[0],i[1].replace(",",".")))
    return list_v_d

list_curr_val = get_curr_val(list_match)
print(list_curr_val)
list_curr_dot = replace_to_dot(list_curr_val)
print(list_curr_dot)

#list_curr_float = []    
#for s in list_curr_val2:
#    if s[1] == "can't get value":
#        list_curr_float.append((s[0],s[1]))
#    else:
#        list_curr_float.append((s[0], float(s[1])))

#convert list to dict
#for i in list_curr_float:
#    cd = {'currency':i[0], 'val_ves':i[1]}
#    exchange.append(cd)

#print(list_curr_val)
#print(list_curr_val2)
#print(list_curr_float)
#print(exchange)


def show(u, d, cs):
    print("---------------------------")
    print(f"{cs} BCV = {u} ")
    print(f"{d}")
    print("---------------------------")

#eur_v = get_value(test_euro)
#cny_v = get_value(test_cny)
#try_v = get_value(test_try)
#rub_v = get_value(test_rub)
#usd_v = get_value(test_usd)
#date_v = get_value(date)

#change the form nn,nn to nn.nn
# ex 33,33 to 33.33
#usd_v2 = usd_v.replace(",",".")
#usd_float = float(usd_v2)
#usd_round = round(usd_float, 4)
 
#show(eur_v, date_v,"€")
#show(cny_v, date_v,"¥")
#show(try_v, date_v,"₺")
#show(rub_v, date_v,"₽")
#show(usd_v, date_v,"$")



