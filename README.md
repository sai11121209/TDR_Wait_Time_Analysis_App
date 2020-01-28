# 東京ディズニーリゾート待ち時間測定アプリ
![](https://img.shields.io/badge/Pyhton-3.7.8-4169e1.svg)
![](https://img.shields.io/badge/Pyhtonista3-3.6-00fa9a.svg)
![](https://img.shields.io/badge/MySQL-5.7.27-4169e1.svg)  

## 標準ライブラリを含む使用ライブラリ
> mysql.connector  
> os  
> time  
> sshtunnel
> requests
> pandas  
## 使用ライブラリのインストール
```
$ pip install mysql.connector
$ pip install sshtunnel
$ pip install requests
$ pip install pandas
```
## 内容
今回はレンタルサーバXREAをお借りしてMySQLサーバを構築しました.

### 自宅PCでの処理の流れ

1. タスクスケジューラーを使用し開園時刻5分前にプログラムを起動.  
1. 自宅PC上でディズニー待ち時間APIのデータを取得.  
1. 取得した待ち時間データをMySQLサーバに送信.  
1. 閉園時刻と同時に1日の待ち時間データをMySQLサーバより取得.  
1. 取得データをcsvファイルに書き出す.  
1. MySQLサーバ待ち時間テーブルのデータを全消去とともにオートインクリメントをリセット.  

これらの処理のうち2,3の処理を開園時刻から閉園時刻まで指定間隔(ex:5分)で実行しMySQLサーバにデータを蓄積させる.  

### iPhone(Pyhtonista3)での処理の流れ
