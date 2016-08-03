# NLP100本ノック第１章のメモ

## 00. 文字列の逆順
`s[i:j:k]`は 「slice of s from i to j with step k」を表す
開始位置はは含むが、終了位置は含まない
s[begin:end:step]
stepが負の値だと末尾から逆に数えたindexとなる

[slidenote url="http://d.hatena.ne.jp/redcat_prog/20111104/1320395840" slideId="79"]

## 01. 「パタトクカシーー」
リストから文字列へ変換
```
"".join(list)
```

## 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
### zip関数
複数のシーケンスに並行して同時にアクセスするforループを作るのに役立つ
zipは基本的には、引数にシーケンスを指定するとタプルのリストを返す

```
L1 = [1,2,3,4]
L2 = [5,6,7,8]

zip(L1, L2)    #=> [(1, 5), (2, 6), (3, 7), (4, 8)]
```

#### zip関数を利用してディクショナリを作成
```
keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]
D2 = {}
for (k, v) in zip(keys, vals): D2[k] = v

# ビルトイン関数dictを使用
D3 = dict(zip(keys, vals))
```

## 03. 円周率
[slidenote url="http://orangain.hatenablog.com/entry/20100503/1272900555" slideId="80"]

### 文字列どうしの置換
```
text = "I like coffee."
answer = text.replace("coffee", "latte")
```

### 正規表現を使った置換
```
import re
text = "abc123ghi."
answer = re.sub(r'[\d]+', 'def', text)
```

## 05. n-gram
Q. 文字n-gramの場合、空白はどうするのか？

## 06. 集合
### Pythonの集合演算まとめ
```
# set s の基数
len(s)

# s のメンバに x があるか調べる
x in s

# s のメンバに x がないか調べる
x not in s

# t に sのすべての要素が含まれるか調べる
x.issubset(t)

# s に t のすべての要素が含まれるか調べる
s.issuperset(t)

# s と t に含まれるすべての要素を持った新しいsetを作成
s.union(t)

# s と t 共通に含まれる要素を持った新しいsetを作成
s.intersection(t)

# s には含まれるが t には含まれない要素を持った新しいsetを作成
s.difference(t)

# s と t のうち、両者には含まれない要素を持った新しいsetを作成
s.symmetric_difference(t)

# s の浅井コピーを持った新しいsetを作成
s.copy()
```
参考
[slidenote url="http://docs.python.jp/2.5/lib/types-set.html" slideId="81"]

## まとめ
いろいろメモしていたら1.5時間ほどかかった
