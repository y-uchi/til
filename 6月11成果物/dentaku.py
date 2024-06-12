def calculate():
  print("簡易電卓アプリケーションです。終了するには '=' を入力してください。")
  result = float(input("数値を入力してください： "))
  while True:
    operation = input("操作を入力してください（+, -, *, /, =): ")
    if operation == '=':
      print(f"計算結果： {result}")
      break
    elif operation in ('+', '-', '*', '/'):
      number = float(input("数値を入力してください："))
      if operation == '+':
        result += number
      elif operation == '-':
        result -= number
      elif operation == '*':
        result *= number
      elif operation == '/':
        if number != 0:
          result /= number
        else:
          print("0で割ることはできません!")
          continue
    else:
      print("無効な操作です。")
calculate()
