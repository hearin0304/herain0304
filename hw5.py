def read_single_digit (num) :
    if num == 0 : return '영'
    if num == 1 : return '일'
    if num == 2 : return '이'
    if num == 3 : return '삼'
    if num == 4 : return '사'
    if num == 5 : return '오'
    if num == 6 : return '육'
    if num == 7 : return '칠'
    if num == 8 : return '팔'
    if num == 9 : return '구'

def read_number (n) :
    digit1 = n // 100
    digit2 = (n % 100) // 10
    digit3 = n % 10
    print(read_single_digit(digit1))
    print(read_single_digit(digit2))
    print(read_single_digit(digit3))

number = int(input('세 자리 정수 입력'))
read_number(number)
