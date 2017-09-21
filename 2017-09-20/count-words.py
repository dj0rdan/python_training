#単語の出現回数をカウント
text = """
Keep on asking, and it will be given you;
Keep on seeking, and you will find;
Keep on knocking, and it will be opened to you;
for everyone asking receives, and everyone seeking finds,
and to everyone knocking, it will be opened.
"""

#単語を区切る
text = text.replace(";","")  #;を削除
text = text.replace(",","")  #,を削除
text = text.replace(".","")  #.を削除
words = text.split()  #空白で区切ってリスト型を作成

#単語を数える
counter = {}  #counterという空の辞書型を作成
for w in words:
    ws = w.lower()  #小文字に変換
    if ws in counter:  #もし辞書型にすでにキーがアレば値を一つ追加
        counter[ws] += 1
    else:
        counter[ws] = 1  #もし辞書型にキーが無ければ、値を1としてキーも登録

#結果を表示
for k,v in sorted(counter.items()):  #counterキーをアルファベット順として範囲に指定
    if v >= 3:
        print(k,v)
