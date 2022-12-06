mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchange_rate': 103.25
}

#  Your Code Starts from here
mobile_name = mobile_data.get('data')[0].get('name')
mobile_price = mobile_data.get('data')[0].get('price')[0:3]
country = mobile_data.get('data')[0].get('made')
bdt_rate = mobile_data.get('exchange_rate')
bdt = int(mobile_price)* int(bdt_rate)

sentence = f'I am using {mobile_name}. It is made in {country}. Price of this mobile is {mobile_price} USD which is almost equal to {bdt} BDT.'
print(sentence)