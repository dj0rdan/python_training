year = int(input("西暦何年？"))

#うるう年かどうか
is_leap = False
if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False

#結果
if is_leap:
    print("うるう年だね")
else:
    print("普通の年だね")
