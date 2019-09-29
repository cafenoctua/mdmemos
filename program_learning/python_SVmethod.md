# Basic
- print
  - args
    - sep
      - 区切り文字を指定できる
    - end
      - 終了文字を指定できる
    - file
      - 開いているファイルオブジェクトに書き込む
- help
  - 関数の使用方法を見れる
- 型
  - 文字列
    - row
      - バックスラッシュ等の特殊文字も通常文字に変換したい場合使える
    - ダブルコーテーションは文章を格納できる
      - 改行したくないときは改行位置にバックスラッシュを入れる
    - 文字列 * n
      - n回文字列を繰り返す
    - + は文字列を連結できる
      - 生の文字列同士なら+　いらない
      - ()でくくることで改行にも対応
        - ()が嫌いな場合は改行位置にバックスラッシュ
    - スライス機能が使える
    ```python
    word = 'abcdefg'
    word[1]
    > 'b'
    word[0:2]
    > 'abc'
    ```
    - 文字列の特定位置の直接代入できない
    ```python
    word = 'abcdf'
    word[0] = 'g' # 不可
    word[0] = 'g' + word[1:-1] # 指定場所以外は残して文字列
    > 'gbcdf'
    ```
    - method
      - .startswith('')
        - メソッドで指定した文字列で始めっているか判定
      - .find('')
        - 指定した文字列が何文字目に入るか数値を返す
      - .count('')
        - 指定した文字列の個数をカウント
      - .capitalize()
        - 文字列のはじめだけ大文字残り小文字
      - .upper()
        - すべて大文字
      - .lower()
        - upper()逆
      - .replace('', '')
        - 文字列置換
    - {}使い方
    ```python
    'a is {}'.format('test')
    > 'a is test'
    'a is {0} {1}'.format('My', 'name')
    >a is My name
    'a is {1} {0}'.format('My', 'name')
    >a is name My
    ```
    - f-strings
      - formatより高速に動作する
    ```python
    a = 'a'
    print(f'a is {a}')
    > 'a is a'
    ```
  - list型
    - 操作
      - [::2]
        - 2ステップで配列の値を取得
      - [::-1]
        - 逆順にする
    - method
      - .append()
        - 末尾追加
      - .insert()
        - 先頭に追加
      - .pop()
        - argsなしだと末尾を取り出す
        - index指定可能
      - .remove()
        - 指定したインデックスの値を消す
      - .extend
        - 別リストを末尾に結合
      - .index
        - 中身の値のインデックスを返す
        - args
          - 検索したい値
          - 何個か
      - .sort
        - 昇順ソート
      - .reverse()
        - 降順にソート
      - .join
        - リスト要素を結合する
        - args
          - 結合する間に入れたい文字列
  - タプル型
    - 決め打ちの変数を使いときに有用
  - 辞書型
    - method
      - .keys
        - 辞書型のキーを取得
      - update()
        - 同一キーの別辞書型のvalueを反映する
      - .clear()
        - 中身をクリアする
      - in はキーの有無を見る
  - 集合型
    - キーなしの辞書型
    - 集合の演算が行える
     
  | cmd | action |
  | --- | --- |
  | | | 和集合 |
  | - | 差集合 |
  | & | 積集合 |
  | ^ | 否定 |
    - method
      - add
        - 末尾に追加
    - 型はdict

- 制御文
  - while
    - else
      - ループが正規に終了後に処理が行われる
  - for
    - else
      - while同様の処理
    - インデックス変数は[ _ ]で使わないよう明示できる
    - zip関数
      - 変数をまとめられる
        - アンパックしてデータ取得
    - 辞書型
      - keys, valuesがアンパッキングされfor文が回る
- 関数
  - 引数
    - デフォの引数でリストや辞書型をもたせると一度だけ初期化されてそれ以降値を持ち続ける
      - 参照渡しとなるため変数が生存し続ける
      - やりたい場合は基本的にNoneをもたせif文で初期化する
    - *args
      - 引数を可変で持つ
      - タプル型で変数を持つ
    - **kwargs
      - 辞書型で可変で変数を持つ
      - 変数名と値が必要
      - 直接辞書で渡す場合は
        - **{変数名}
    - 引数設定順序
      - 通常の引数 > *args > **kwargs
      - args kwargs切り替えポイントは変数名を明示した引数を渡したところ
  - 関数内関数使いドコロ
    - 同一処理をその関数でのみ使う場合に有用
  - クロージャー
    - 関数内関数をオブジェクトとして返す関数
    - 使いドコロ
      - 関数を実行するタイミングを制御したいとき
      - 引数を設定してその後それが変化しても追随しないようにしたい時
  - デコレーター
    - 関数の定形処理を継承したい時に使う
    - デコレーターを何個も重ねられるが上から指定したものを実行する入れ子関数になる
    ```python
    #継承した関数をどこで実行するかを指定してそのオブジェクトを返す
    def print_info(func):
      def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
      return wrapper

    @print_info #上記の関数を継承する
    def add_num(a, b):
      return a + b

    f = add_num(10, 20)
    print(r)
    ```
  - λ
    - 二行程度のdefをラムダ式に置き換えてファンクションを減らせる
  - ジェネレーター
    - yieldで指定した処理を呼び出し毎に処理する
    - yieldを見てpythonはジェネレーターだと判別する
    - 小分けで重い処理を実行する関数
    ```python
    def greeting():
      yield 'a'
      yield 'b'
      yield 'c'

    for i in greeting():
      print(i)
    >a
    >b
    >c
    ```
- 内包表記
  - 辞書型内包表記も存在する
  - 集合内包表記
  - ジェネレーター内包表記
    - 内包処理をタプルで囲む
- 例外処理
  - 制御した例外がある場合は try cache機能を使う
  ```python
  try:
    l[i]
  except:
    print('Error')
  else:
    print('done')
  finally:
    print('clean up')
  ```
  - exceptにErrorタイプを指定できる
    - Exception hierarchyでErrorタイプを参照できる
  - 全てのExceptionを指定するのは想定しない動きをする可能性があるためやらないほうが良い
  - finally
    - 例外処理で最終的に必ず実行したい処理を入れる
  - else
    - 例外が発生しなかった場合の処理を入れる
  - 独自例外
    - raiseで例外発生
    - 入ってほしくない値をエラーとして定義
    ```python
    class UpperacaseError(Exception):
      pass
    
    def check():
      words = ['APPLE', 'orenge', 'banana']
      for word in words:
        if word.isupper():
          raise UppercaseError(word)
      
    try:
      check()
    except  UppercaseError as exc:
      print('This is my fault. Go next')

    > ExtentionError: Apple
    ```
    - 独自作成のものは明示する必要がある
- Docstring
  - 書くことでhelpまたは.__doc__で出力可能
- モジュールとパッケージ
  - コマンドライン引数
    ```python
    import sys

    sys.argv
    ```
  - モジュール作成手順
    - パッケージフォルダを作成
    - __init__.py作成
      - 呼び出し時に必ず読み込まれる
      - アスタリスクを使って関数呼び出ししたい場合は__all__に関数名をリスト入れる
        - どんなモジュールが呼び出されるかわからないため禁止
    - 関数もしくはクラスを定義したファイルを作成する
  - モジュール呼び出しかた
    ```python
    import package.func
    from package import func
    ```
    - フルパスを読み込むようにするかモジュールで読み込むようにする
    - 絶対パス相対パス読み込み
    ```python
    #絶対パス
    from packagefolder.package import func
    #相対パス
    from ..package import func
    #..はひとつ上のdirを読む->可読性が下がるため禁止
    ```
  - setup.pyでパッケージ化(配布用)
  ```python
  from distutils.core import setup

  setup(

  )
  ```
    - setupの中に設定項目を入れることでまとめてパッケージ化できる
    - python setup.py sdistでパッケージ化
  - __name__
    - __main__が返されるのが現在実行しているスクリプトがわかる
    - それ以外の場合はそのファイル名が返される
    - 関数ファイル内にテストスクリプト書く等に有用
    ```python
    if __name__ == '__main__':
      proc
    ```
- クラスとオブジェクト
  - クラスのパレンティスには必ずobjectを入れる
    - 継承等に使えるから
  - 初期化
    - def __init__(self):以下初期設定
  - 削除
    - __del__
  - 継承
    - 継承したいクラスを現クラスのパレンティスに入れると継承される
    - 継承メリット
      - 継承したクラスのメソッドを継承して簡単に機能拡張が可能
    - 多重継承したい時はクラスのパランティスに継承したクラスを入れる
      - クラス間で同じメソッドが存在する場合は左のクラスから優先される
      - なるべく使わない->可読性が下がるから
  - オーバーライド
    - super().__init__(model)
    - super()で親モデルの初期設定を呼び出せる
  - プロパティ
    - 設定値を変更されたくない時に使用(read only)
    - ex.
    ```python
    class Class():
      def __init__(self, property=True):
        self._property = property
      
      @property
      def property():
        return self._property
      
      @property.setter
      def property(self, is_enable):
        return self.property = is_enable
    ```
    - .setterを使うことで値の書き換えを許可する
      - パスワード等の変更を制御したい時に有用
    - __はクラス外には完全に隠蔽できる
      - クラス外で__を使って書き換えを行うと再定義の挙動で書き換えられる
  - ダックタイピング
    >もしもそれがアヒルのように歩き、アヒルのように鳴くのなら、それはアヒルである。

    [ダック・タイピング - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%80%E3%83%83%E3%82%AF%E3%83%BB%E3%82%BF%E3%82%A4%E3%83%94%E3%83%B3%E3%82%B0)

    >ポリモーフィズムとはオブジェクト指向プログラミングの概念の一つで、日本語では多態性・多様性などと訳されています。
    クラスが別であっても同じ名前のメソッドを使用することができ、異なるオブジェクトで同じ操作を切り替えて使うことができるというものです。

    [【Python入門】ダックタイピングをやってみる – ポリモーフィズム](https://code-graffiti.com/duck-typing-in-python/)
    - ex.
    ```python
    class Person(object):
      def __init__(self, age=1):
        self.age = age

        def drive(self):
          if self.age >= 18:
            print('ok')
          else:
            rase Exception('No drive')
    class Baby(Person):
      def __init__(self, age=1):
        if age < 18:
          super().__init__(age)
        else:
          raise ValueError
    class Adult(Person):
      def __init__(self, age=18):
        if age >= 18:
          super().__init__(age)
        else:
          raise ValueError
    
    class Car(object):
      def __init__(self, model=None):
        self.model = model
      def run(self):
        print('run')
      def ride(self, person):
        person.drive()
    
    baby = Baby()
    adult = Adult()

    car = Car()
    car.ride(adult)
    > ok
    car.ride(baby)
    > No drive
    ```
  - 抽象クラス
    - 継承時した子クラスに必ず定義してほしいメソッドを定義することでメソッドの定義忘れを防げる
    - コードスタイル上ではやらないほうが良い
  - クラス変数
    - クラス内で定義した変数でリスト等プログラムが終了するまで値を保持し続ける
    - クラス内のグローバル変数的役割
  - クラスメソッド
    - @classmethodのデコレーターをメソッドに当てることで__init__を実行しなくてもメソッドを実行できる
      - その場合メソッドの引数はclsとする
  - 特殊メソッド
    - アンダースコアが前後に2つのもの
    - pythonに埋め込まれている処理を実装したい時に使える
- ファイル操作
  - ファイル開く
    - 行末に追加する場合はopenに'a'をいれてappendで開く
    ```python
    f = open('text.txt', 'a')
    f.write('test')
    f.close()
    ```
    - .closeを忘れると開きっぱなしになる
    - 基本的にはwithステートメントを開く
      - withステートメントが終わると自動的にcloseする
    - f.readline
      - 一行づつ読む
    - f.tell()
      - 現在位置を取得
    - f.seek(n)
      - n文字目の位置の値を取得
  - テンプレート
    - 入れたい文章をテンプレートとして定義できさらに文章内に変数を定義できる
    - ex.
      ```python
      import string

      s = """\
      Hi $name.

      $contents

      Have a good day.
      """

      t = string.Template(s)
      contents = t.substitute(name='Mike', contents='How are you?')
      print(contents)

      >Hi Mike.
      How are you?
      Have a good day.
      ```
  - ファイル操作
    - ファイル操作は以下4つのライブラリを覚えれば大概のことができる
    - os
      - .exists
        - ファイルが存在するか
      - isfile
        - ファイルか確認する
      - isdir
        - ファルダか確認する
      - rename
        - ファイル名変更
      - symlink(orgfile, linkfile)
        - シンボリックリンク付きのファイル生成
      - mkdir
        - フォルダ作成
      - rmdir
        - ファルダ削除
        - 中身何か入っていたら消すことができない
      - remove
        - ファイル削除
      - listdir
        - lsと同等
      - getcwd()
        - 現在のパス取得
    - pathlib
      - Path
        - .touch
          - 空ファイル生成
    - glob
      - glob
        - 指定したディレクトリのファイルを全取得
        - ex.
        ```python
        import glob
        
        #フォルダ内のファイル取得
        glob.glob('dir/dir1/*')

        #フォルダ内のサブフォルダ含む全ファイル取得
        glob.glob('dir/dir1/**')
        ```
    - shutil
      - copy
        - ファイルコピー
    - 圧縮
      - tarfile
        ```python
        import tarfile
        # 圧縮
        with tarfile.open('test.tar.gz', 'w:gz') as tr:
          tr.add('test_dir')
        # 展開
        with tarfile.open('test.tar.gz', 'r:gz') as tr:
          tr.extractall(path='test_tar')
        
        # 展開せずに中身確認
        with tarfile.open('test.tar.gz', 'r:gz') as tr:
          with tr.extracfile('dir/tar.txt') as f:
            print(f.read())
            
        ```
      - zipfile
        ```python
        import glob
        import zipfile

        # zipファイル作成
        with zipfile.ZipFile('zipfile.zip', 'w') as z:
          for f in glob.glob('zipfile_dir/**', recursive=True):
            z.write(f)

        # zipファイルの読み込み
        with zipfile.ZipFile('zipfile.zip', 'r') as z:
          z.extractall('zzz1')
        
        # zipファイルの読み込み(展開せず)
        with zipfile.ZipFile('zipfile.zip', 'r') as z:
          with z.open('zipfile_dir/zipfile.txt') as f:
            print(f.read())
        ```
    - 一時ファイル
      - tempfile
        - バッファ内にファイルを作成してプログラムが終わったら自動的に削除される
        - テスト等で使える
    - subprocess
      - .run()
        - Linuxシェルを実行できる
        - args
          - shell=True
            - パイプ処理の実行を有効化
            - rm -rf *等の危険なコマンドをパイプに組み込まれてしまいセキュリティ上良くないため禁止
    - time
      - time.sleep(n)
        - n秒待つ
- 簡易的なアプリ作成について
  - MVCモデルを使ったフォルダ構成を作る
    - model, view, controllerのフォルダ作って役割明確に分ける
    - model
      - データ操作等を主に行う
      - データソースのアクセス等の基本的な操作用のクラスを作成してそれ以降のクラスはそれを継承してデータを操作する
      - 必ず実行させたい処理はデコレーターを使うと便利
    - view
      - ユーザーに見える箇所を担当
    - controller
      - modelとviewを操作する
    - template
      - 決まったで表示するファイルを集めたもの主にviewがアクセスして使う
      - txt形式のテンプレートファイルやHTMLを入れたりする
      - templateをユーザーに変更させたい場合は/tmpファルダにtemplateを作るようにして操作させる
        - パッケージとして配布する際にパッケージの中身を直接変更させるとバージョンアップ時にユーザーが変更した中身を上書きしてしまうため
        - パッケージのデフォで使っているものとユーザー独自のものを明示的に分けるため
  - モジュール間のimportは絶対パスでimport
  
# コードスタイル
- コードスタイルをチェックするパッケージ
  - pep8
    - pep スクリプトでチェクを実行
  - flake8
    - flake スクリプトでチェクを実行
      - pep8より厳しい
  - pylint
    - pylint スクリプトでチェクを実行
      - flake8より厳しい
  - どのルールを順守するか決める
- line長さ80以下
  - 長いlineで改行する場合は改行した文字列はインデントを合わせる
  - URLは無視して良い
    - 有効じゃなくなるから
- if無駄なパランティスをつけない
- インデントは4スペース
- 関数デフォルト引数への代入はスペース開けない
- 各行代入する場合は =  スペースを空ける
- class定義の間隔は改行2つ
  - methodは改行1つ
- 文字列の連結は+で連結する
  - テンプレートに文字列を入れる場合はformatをつかう
  - for文使った文字列の結合は次々に文字列連結させずにlistでappendでしてからjoinしたほうがメモリ効率と可読性が上がる
- ' と" の使い分けは開発する際に決める
  - 例として'は単純な文字列を格納するように使い"は特殊文字や埋め込み変数を使うさいに分けるとうしている
- ファイルを開くときは基本的にwithを使う
- TODOコメントについて
  - TODOの後に個人名をつけて誰のTODOか明示する
- import
  - 複数パッケージを一行でimportしない
  - 独自パッケージは必ず絶対パスで定義
- class名は基本的にキャメルケース
- 関数/変数名はスネークケース
- グローバル変数は大文字でスネークケース
- プログラムは必ずmain関数とif __name__=="__main__"を使う
  - importした際に間違って処理が始まらないように
- エクセプション
  - 全てのエクセプションを取るは使わない
- リスト内包表現に複雑な処理は入れない
- 変数名
  - わかりやすい名前にする
- generatorはfor文よりメモリ効率がよい
  - for文と同じ処理ができる場合はgeneratorを使った方が良い
- ラムダ
  - 簡易な処理なら良い
- 関数の引数
  - リストを引数にする場合は参照渡しの問題があるため初期値はNoneをいれ処理内で初期化する
- クロージャー
  - グローバル変数を隠蔽して関数を実行するため通常のグローバル変数を使った引数を隠蔽しているグローバル変数に入れないようにする
- デコレーター
  - デコレーターは基本的に@で宣言
- コメントの書き方
  - コメントは英語
  - google翻訳もok
  - 一番上にこのプログラムが何をするものか明記する
  - 関数/クラスはDocstringを活用
  - pylintでドキュメントの書き方を参考にする

# webとネットワーク
- XML
  - jsonより文量が長くなるため処理属度は劣るが古いフォーマットでは使用されている
  example:
  ```python
  import xml.etree.ElementTree as ET

  # write
  root = ET.Element('root')
  tree = ET.ElementTree(element=root)

  employee = ET.SubElement(root, 'employee')

  employ = ET.SubElement(employee, 'employ')
  employ_id = ET.SubElement(employ, 'id')
  employ_id.text = '111'
  employ_id = ET.SubElement(employ, 'name')
  employ_id.text = 'Mike'

  employ = ET.SubElement(employee, 'employ')
  employ_id = ET.SubElement(employ, 'id')
  employ_id.text = '222'
  employ_id = ET.SubElement(employ, 'name')
  employ_id.text = 'Nancy'

  tree.write('test.xml', encoding='utf-8', xml_declaration=True)

  # read
  tree = ET.ElementTree(file='test.xml')
  root = tree.getroot()

  for employee in root:
      for employ in employee:
          for person in employ:
              print(person.tag, person.text)
  ```
- jsonは辞書型変数と同じ構造
  example
  ```python
  import json

  j = {
      "employee":
          [
              {"id": 111, "name": "Mike"},
              {"id": 222, "name": "Nancy "}
          ]
  }

  # 表示
  print(j)
  print("###############")
  print(json.dumps(j))

  # Write
  with open('test.json', 'w') as f:
      json.dump(j, f)

  # Read
  print("############")
  with open('test.json', 'r') as f:
      print(json.load(f))
  ```
  - コード内で読み込み書き込むする場合はdump, loadの末尾sを付ける
- urllib
  - RESTに載っとったwebの操作を行う
  | cmd | action
  | --- | --- |
  | GET | データ参照
  | POST | データの新規登録
  | PUT | データの更新
  | DELETE | データの削除 

  - getでパラメータを送るときはurlの後ろに?を付ける
    - 複数パラメータは&でつなげる
  - postは?をつけない
  - コード例
  ```python
  import urllib.request
  import json

  payload = {'key1': 'value1', 'key2': 'value2'}

  url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
  # print(url)

  # GET
  with urllib.request.urlopen(url) as f:
      r = json.loads(f.read().decode('utf-8'))
      print(type(r))

  # POST
  payload = json.dumps(payload).encode('utf-8')
  req = urllib.request.Request(
      'http://httpbin.org/post', data=payload, method='POST')

  with urllib.request.urlopen(req) as f:
      print(json.loads(f.read().decode('utf-8')))

  # PUT
  req = urllib.request.Request(
      'http://httpbin.org/put', data=payload, method='PUT')

  with urllib.request.urlopen(req) as f:
      print(json.loads(f.read().decode('utf-8')))

  # DELETE
  req = urllib.request.Request(
      'http://httpbin.org/delete', data=payload, method='DELETE')

  with urllib.request.urlopen(req) as f:
      print(json.loads(f.read().decode('utf-8')))
  ```
- requests
  - urllibより直感的な操作が可能
  - urlにパラメータを入力せずに関数に入れれば良い
  - timeoutの設定もできる
  - コード例
  ```python
  import requests

  payload = {'key1': 'value1', 'key2': 'value2'}

  # GET
  r = requests.get('http://httpbin.org/get', params=payload)

  print(r.status_code)
  print(r.text)
  print(r.json())

  # POST
  r = requests.post('http://httpbin.org/post', params=payload)

  print(r.status_code)
  print(r.text)
  print(r.json())

  # PUT6
  r = requests.put('http://httpbin.org/put', params=payload)

  print(r.status_code)
  print(r.text)
  print(r.json())

  # DELETE
  r = requests.delete('http://httpbin.org/delete', params=payload)

  print(r.status_code)
  print(r.text)
  print(r.json())

  # POST タイムアウト処理
  # POST
  r = requests.post('http://httpbin.org/post', params=payload, timeout=1)

  print(r.status_code)
  print(r.text)
  print(r.json()) 
  ```
- ソケット通信
  - serverコード
  ```python
  import socket

  # TCP->クライアントの投げたデータを確かめる
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind(("127.0.0.1", 50007))
      s.listen(1)
      while True:
          conn, addr = s.accept()
          with conn:
              while True:
                  data = conn.recv(1024)
                  if not data:
                      break
                  print("data:{}, addr:{}".format(data, addr))
                  conn.sendall(b"Received: " + data)


  # UDP>クライアントの投げたデータを確かめない
  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
      s.bind(('127.0.0.1', 50007))
      while True:
          data, addr = s.recvfrom(1024)
          print("data: {}, addr: {}".format(data, addr))

  # WEB Serverを立ち上げる
  import http.server
  import socketserver

  with socketserver.TCPServer(('127.0.0.1', 8000),
          http.server.SimpleHTTPRequestHandler) as httpd:
      httpd.serve_forever()
  ``` 
  - clientコード
  ```python
  import socket

  #TCP
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect(('127.0.0.1', 50007))
      s.sendall(b'Hello')
      data = s.recv(1024)
      print(repr(data))

  # UDP
  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
      s.sendto(b'Hello UDP', ('127.0.0.1', 50007))
  ```
- Flask
  - serberコード
  ```python
  import sqlite3
  from flask import Flask
  from flask import g                 # globalのg
  from flask import render_template
  from flask import request
  from flask import Response


  app = Flask(__name__)

  def get_db():
      db = getattr(g, '_database', None)
      if db is None:
          db = g._database = sqlite3.connect('test_sqlite.db')
      return db

  @app.teardown_appcontext
  def close_connection(exception):
      db = getattr(g, '_database', None)
      if db is not None:
          db.close()

  @app.route('/employee', methods=['POST', 'PUT', 'DELETE'])
  @app.route('/employee/<name>', methods=['GET'])
  def employee(name=None):
      db = get_db()
      curs = db.cursor()
      curs.execute(
          'CREATE TABLE IF NOT EXISTS persons( '
          'id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
      )
      db.commit()

      name = request.values.get('name', name)
      if request.method == 'GET':
          curs.execute('SELECT * FROM persons WHERE name = "{}"'.format(name))
          person = curs.fetchone()
          if not person:
              return "No", 404
          user_id, name = person
          return '{}:{}'.format(user_id, name), 200
      if request.method == 'POST':
          curs.execute('INSERT INTO persons(name) values("{}")'.format(name))
          db.commit()
          return 'created {}'.format(name), 201
      
      if request.method == 'PUT':
          new_name = request.values['new_name']
          curs.execute('UPDATE persons set name = "{}" WHERE name = "{}"'.format(new_name, name))
          db.commit()

          return 'update {}:{}'.format(name, new_name), 200

      if request.method == 'DELETE':
          curs.execute('DELETE from persons WHERE name = "{}"'.format(name))
          db.commit()
          return 'deleted {}'.format(name), 200
  @app.route('/')
  def hello_world():
      return 'top'

  @app.route('/hello')
  @app.route('/hello/<username>')
  def hello_world2(username=None):
      # return 'hello world {}'.format(username)
      return render_template('hello.html', username=username)
  @app.route('/post', methods=['POST', 'PUT', 'DELETE'])
  def show_post():
      return str(request.values['username'])

  def main():
      app.debug = True
      app.run(host='127.0.0.1', port=5000)

  if __name__ == '__main__':
      main()
  ```
  - requestコード
  ```python
  import requests

  r = requests.get(
      'http://127.0.0.1:5000/employee/mike')
  print(r.text)
  r = requests.post(
      'http://127.0.0.1:5000/employee', data={'name': 'mike'}
  )
  print(r.text)
  r = requests.put(
      'http://127.0.0.1:5000/employee', data={'name': 'mike', 'new_name': 'miku'}
  )
  print(r.text)
  r = requests.delete(
      'http://127.0.0.1:5000/employee', data={'name': 'miku'}
  )
  print(r.text) 
  ```
  
