# (1)
print("私は{name}です。".format(name="丹古母鬼馬二"))

#(2)
fmt = "年齢は{age}歳で、{job}をやっています。"
s = fmt.format(age=70, job="プログラマ")
print(s)


#分解してみる
print("俺は{namae}。{nenrei}と高齢だが、アレがアレで{are}をやっている。".format(namae="丹古母鬼馬二", nenrei=80, are="プログラマ"))