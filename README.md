# utf8_to_sjis
- utf8のファイルをshift-jisへ変換するプログラム。
- 大したことないけど使う頻度が高いから登録しておく。

## メモ
- utf8からShift-JISへ変換する際、エラーが出ることがあり（Shift-JISの方が文字数が少ないため）、その場合は'?'に置換して、処理を続行させるコードが入ってる。
```
import codecs
codecs.register_error('none', lambda e: ('?', e.end))
with open(file, mode='w', encoding='sjis', errors='none') as f:
	～
```
