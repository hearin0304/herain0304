shopping_bag = {}
print('{구입}')

while True:
    item = input("상품명")
    if item == ' ' or amount == 0:
        break
    amount = int(input('수량은?'))
    shopping_bag[item] = amount
    print(f'장바구니에 {item} 이 {amount}개가 담겼다')

print(f'\n>>> 장바구니 보기: {shopping_bag}')

print('\n[검색]')
t = input('장바구니에서 확인하고자 하는 상품은?')
if t in shopping_bag:
    print(f'{t}는 {amount}개가 담겨있다.')
else:
    print('이 상품은 장바구니에 담겨 있지 않다.')
