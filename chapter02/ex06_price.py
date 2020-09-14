def service_price():
    service = input('서비스 종류를 입력하세요, a/b/c: ')
    valueAdded = input('부가세를 포함합니까? y/n: ')
    prices = { 'a': 23, 'b': 40, 'c': 67 }

    price = prices[service] # need error handling

    if valueAdded == 'y':
        price *= 1.1

    print(str(round(price, 1))+'만원입니다')

service_price()
