import requests, json, random

number = '79xxxxxxxxx'
qiwi_token = '' # qiwi.com/api
comment = random.randint(111111, 999999)
urlPay = 'https://qiwi.com/payment/form/99?extra[%27account%27]={}&amountFraction=0&currency=643&extra[%27comment%27]={}&blocked[1]=account&blocked[2]=comment'

print(f'Number: {number}\nComment: {comment}\n')
print('Link: ', urlPay.format(f'{number}', int(comment)))
answ = input('Check (T/F): ')

def check_pay():
    h = requests.get(f'https://edge.qiwi.com/payment-history/v1/persons/{number}/payments?rows=50',
        headers={'Accept': 'application/json',
                 'Content-Type': 'application/json',
                 'Authorization': f'Bearer {qiwi_token}'})
    req = json.loads(h.text)
    for i in range(len(req['data'])):
        if req['data'][i]['comment'] == f"{comment}":
            amount = req['data'][i]['sum']['amount']
            amount = round(amount)
            print(f'{amount} rub sended!')
            break

if answ == 'T':
    check_pay()
elif answ == 'F':
    exit(0)
else:
    exit(0)
