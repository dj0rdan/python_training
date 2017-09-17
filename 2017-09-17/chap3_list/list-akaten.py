#国語点数一覧
points = [80,40,23,14,29,58]

#30点未満のデータのみ選び赤点リストへ
akaten = []
for p in points:
    if p < 30:
        akaten.append(p)

#選んだデータを表示
print(akaten)
