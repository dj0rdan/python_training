import random

#格言をリストに代入
kakugen = [
    "脳ある爪は鷹を隠す",
    "力こそパワー",
    "武士の侍が馬から落馬",
    "May the force be with you"]

#ランダムに数値を一つ選ぶ
i = random.randint(0, len(kakugen)-1)

#表示する
print(kakugen[i])
