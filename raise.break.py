# -*- coding: utf-8 -*-
#한글

shops = {
    "에이문구": {"가위": 500, "크레파스": 3000},
    "비문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "씨문구": {"풀": 500, "목공본드": 2000, "화분": 3000},
    "디문구": {"풀": 600, "가위": 1000, "펜치": 5000}
}
print("풀파는 문구 : 가격")
for shop, products in shops.items():
    for product, price in products.items():
        if product == '풀':
            print("{}: {}원".format(shop, price))





