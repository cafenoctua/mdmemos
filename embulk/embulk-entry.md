# GCPの構築手順
使用した環境
- Ubuntu18.04
- n1-standard1

# install Java v8
インスタンスにJavaの環境を作成します。

embulkの最新版が対応しているJavaのバージョンはv8なのでv8のJavaをインストールする。

```
sudo add-apt-repository ppa:openjdk-r/ppa
sudo apt-get update
sudo apt-get install openjdk-8-jdk
```

# install Embulk

```
curl --create-dirs -o ~/.embulk/bin/embulk -L "https://dl.embulk.org/embulk-latest.jar"
chmod +x ~/.embulk/bin/embulk
echo 'export PATH="$HOME/.embulk/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## Embulkで利用できる型の種類

| 型 | 説明
| --- | --- |
| boolean | true / false
|long | 64bit符号付き整数型
| timestamp| 日付。ナノ秒を含む
| double | 64bit浮動小数点型
| string | 文字列

## Embulkのプラグイン
Embulkはプラグインにて機能を拡張していくため自由に開発可能。

既存プラグインは以下参照。

[List of Plugins by Category](https://plugins.embulk.org/)

プラグインに追加方法
```
embulk gem install {plugins}
```

現在インストールしているプラグインの確認方法
```
embulk gem list
```

# Basic entry

## Download example folder
```
embulk example ./try1
```

## Guess to make minimal config yml
```
embulk guess ./try1/seed.yml -o config.yml
```

このGuessがtry1フォルダーにあるseed.ymlをもとに推測したカラムの型等を追加して補完したconfig.ymlを生成する

seed.yml
```
in:
  type: file
  path_prefix: '/home/vagrant/./try1/csv/sample_'
out:
  type: stdout
```

config.yml
```
in:
  type: file
  path_prefix: /home/vagrant/./try1/csv/sample_
  decoders:
  - {type: gzip}
  parser:
    charset: UTF-8
    newline: LF
    type: csv
    delimiter: ','
    quote: '"'
    escape: '"'
    null_string: 'NULL'
    trim_if_not_quoted: false
    skip_header_lines: 1
    allow_extra_columns: false
    allow_optional_columns: false
    columns:
    - {name: id, type: long}
    - {name: account, type: long}
    - {name: time, type: timestamp, format: '%Y-%m-%d %H:%M:%S'}
    - {name: purchase, type: timestamp, format: '%Y%m%d'}
    - {name: comment, type: string}
out: {type: stdout}
```

## Previewでdry-runの確認
previewでエラーがないか確認する
```
embulk preview config.yml
```
[dry-run](https://en.wikipedia.org/wiki/Dry_run_(testing))

## runで実行する
```
embulk run config.yml 
```
## outの書き換え
ファイルを出力できるようにプラグインを追加する
```
embulk gem install embulk-output-command
```

下記はoutの設定でcsvからcsv.gzに変換して吐き出す
この設定をconfig.ymlに入れてrunをすると実行される

```
out:
  type: command
  command: "cat - > task.$INDEX.$SEQID.csv.gz"
  encoders:
    - {type: gzip}
  formatter:
    type: csv
```



# ETL的使用
EmbulkではinでExtract、outでLoad、filterでTransformができる

## filter
filterを使ってサンプルcsvのaccountカラムをハッシュ化する

ハッシュ化のプラグインをインストール
```
embulk gem install embulk-filter-hash
```

filterの設定
```
filters:
  - type: hash
    columns:
    - { name: account }
```

previewで出力された形を確認できる

# liquidテンプレートエンジン
変数を使って値を入れることが可能。
ファイル名に.liquidというsuffixを付けることで使える。
```
in:
  type: mongodb
  uri: "mongodb://{{env.MONGO_HOST}}:27017/{{env.DB_NAME}}"
  collection: 'users'
  query: '{ updatedAt: { $gte: 1 } }'
  projection: '{ name: 1, updatedAt: 1 }'
  sort: '{ updatedAt: 1 }'
out:
  type: stdout
```

今回使用する環境変数を定義する
```
export MONGO_HOST=localhost
export DB_NAME=testdb
embulk preview config.yml.liquid
```

上記はmongodbに接続しにいきデータ取得しているためmongodbのプラグインが必要


# 参考URL
- https://christina04.hatenablog.com/entry/embulk-how-to-use
- https://github.com/embulk/embulk#running-example
- https://www.cnblogs.com/roger-yu/p/6397318.html
- https://github.com/Shopify/liquid
- https://christina04.hatenablog.com/entry/mongodb-to-bigquery-via-embulk
- https://qiita.com/da-sugi/items/13d4ead19c86d783ebb4
- https://qiita.com/hiroysato/items/da45e52fb79c39547f69
- https://techlog.voyagegroup.com/entry/2017/07/31/173839
- https://www.sbcloud.co.jp/help/best-practice/bigdata/018_enbulk-to-oss/
- https://www.1915keke.com/entry/embulk-plugin
- 