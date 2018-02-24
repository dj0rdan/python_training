#時給計算program

#時給の入力
user = input("時給なんぼよ")
jikyu = int(user)

#時間の入力
user = input("何時間働いたん")
jikan = int(user)

#計算
kyuryou = jikyu * jikan

#結果
fmt = '''
時給{0}円で、
{1}時間働いたので...

給料は、{2}円です。
'''

desc = fmt.format(jikyu, jikan, kyuryou)
print(desc)
