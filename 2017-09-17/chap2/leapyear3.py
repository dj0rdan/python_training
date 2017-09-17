year = int(input("西暦何年じゃ"))

#うるう年なのか
is_leap = (year % 400 == 0) or (year % 100 != 0 )and(year % 4 == 0)

#結果
if is_leap:
    print("うううううるうううどし")
else:
    print("普通の年だわな")
