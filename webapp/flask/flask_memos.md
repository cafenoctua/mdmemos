# Basic
- hasattr(objects, attribute)
  - 指定のオブジェクトが特定の属性を持っているかを確認する
  
# Composition
- run.py
  - アップリケーション起動用ファイル
- models.py
  - ビジネスロジックのモジュールです。分析処理（散布図行列の生成）とDBアクセスを行います。
- schema.sql
  - データベースのテーブル定義を記述しています。
- requirements.txt
  - pipでインストールする対象モジュールです。
- static
  - cssなどの静的ファイルを配置するディレクトリです。また、配下のresultディレクトリには分析で作成したグラフの画像データを格納します。
- templates
  - テンプレート（htmlの雛形）を配置するディレクトリです。テンプレートは親子関係があり、base.htmlが共通となる親テンプレート、それ以外が子テンプレートとなります。
  - ファイル構成
    - base.html
    - index.html
    - edit.html
    - view.html
# Template
- jinja2
  - htmlのテンプレート
  - pythonで生成した変数を埋め込める

# @app.route
- /
  - index
    - Top画面（結果一覧
      - GET/POST
- /create
  - create
    - 新規分析作成画面
      - GET/POST
- /analysis
  - analysis
    - 分析処理
      - POST
- /delete/
  - delete
    - 削除処理
      - POST
- /view/
  - vies
    - 参照処理
      - GET/POST
※URLにパラメータを加えたい場合は'/delete/<pk>'の<pk>のように記述

# request
- .form['formtype']
  - フォームで定義したタイプを指定して値を取得
  - .get('name')
    - タブで定義したnameを元に値を取得

# sqlite3
- connect(sqlitepath)
  - sqliteに接続
  - sqlitepath: 読み込みたいsqliteのパスを設定
- .Row
  - レコード数を取得
# Other
- 実行方法
    ```
    # 環境変数に登録して実行(現在は一般的らしい)
    export FLASK_APP=run.py
    flask run
    ```
