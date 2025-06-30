num1 = float(input('１目の数字を入力してください:'))
num2 = float(input('２目の数字を入力してください:'))

while True:
    print('どの計算をしますか？')
    print('1:足し算')
    print('2:引き算')
    print('3:掛け算')
    print('4:割り算')

    operation = input('番号を入力してください:')
    if operation in ['1', '2', '3', '4']:
        break
    print('無効な入力です。１～４の番号を入力してください。')


if operation == '1':
    result = num1 + num2
    print(f"計算結果: {result}")

elif operation == '2':
    result = num1 - num2
    print(f"計算結果: {result}")

elif operation == '3':
    result = num1 * num2
    print(f"計算結果: {result}")

elif operation =='4':
    if num2 != 0:
        result = num1 / num2
        print(f"計算結果: {result}")
    else:
        print('エラー:０で割ることができません')

