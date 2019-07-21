# Basic
- パス関連
    - '.../'はカレントのパス以下を示す
- オブジェクト指向
    ```
    互いに密接に関連するデータと手続き（処理手順）をオブジェクト（object）と呼ばれる一つのまとまりとして定義し、様々なオブジェクトを組み合わせて関連性や相互作用を記述していくことによりシステム全体を構築していく手法
    ```
- オブジェクト指向プログラミング
    ```
    関連するデータの集合体と、それを操作する手続きを「オブジェクト」（object）と呼ばれるひとまとまりの単位として一体化し、オブジェクトの組み合わせとしてプログラムを記述する手法。
    ```
    - 継承
        - 既存クラスを呼び出し(基底クラス)それをベースに新しいクラスを作成する
        - 多重継承
            - 基底クラスを複数定義すること
    - カプセル化
        - method名の前に「__」をつける事でprivate関数としそのクラス内でしか使えないようにできる
- Class
    ```
    class ClassName(object):
        def __init__(self, args):
            ---
        def method(self,args):
            ---
        def __method(self,args):
            ---
        def __del__(self,args):
            ---
    ```
    - __init__
        ````
        オブジェクト生成時に呼び出される特殊な関数
        ```
    - method
        ```
        ユーザーが定義した関数
        ```
    - __method
        ```
        ユーザーが定義した関数(カプセル化されたもの)
        ```
    - __del__
        ```
        オブジェクトが不要となりPythonが削除する時に自動で実行される関数
        ```
- os
    - .listdir(dir)
        - 指定ディレクトリのファイルをリストで取得 = ls
- del
    - オブジェクトの削除
- _, item = function()
  - _, でitemに返り値をタプルで受け取る
- .replace
  - 文字列置換
- print
  - 出力
  - 文字列内に{}で変数の値を挿入
    - {:,.3f}
      - .3fは3桁の浮動小数点数表示指定
  - .format(variables)
- yield
  - 処理一旦停止して指定した値を返す
  - 重いデータを小刻みに取得するのに使える
  - [参照先](http://ailaby.com/yield/)
- list
  - .appendで要素追加
  - 他変数に普通に代入すると変数同士がリンクしてしまう
    ```
    ex.
    t = [1,2,3] 
    tcopy = t
    tcopy[0] = 5
    tcopy
    > [5,2,3]
    t
    > [5,2,3]
    ```
  - リンクさせたくない場合は.copyメソッドを指定して代入する
    ```
    ex.
    t = [1,2,3] 
    tcopy = t.copy()
    ```
# io
- .StringIO
    - これがどう便利かというと、「ファイルオブジェクトのように見えるオブジェクト」を作れます
    - 入力値をファイルオブジェクトとして扱えるためpandasに読みっとってもらうことができる
- BytesIO
  - メモリ上でバイナリデータを扱うための機能です。
# tqdm
```
走らせた処理の進捗状況をプログレスバーとして表示するためのパッケージ
```
- tqdm
  - 
# Pandas
- .copy
  - 変数のコピー
  - 非同期で扱うために使う
- pd.read_csv
    - csvデータの読み込み
- data.head()
    - データの先頭行を確認
- data.info()
    - データ数と型の確認
- dat.describe()
    - 基本統計量を計算
    - (include=['O']) - str型のデータの基本統計量計算
- data.isnull()
    - データ欠損値確認-Nanの確認
    - .sum()で各列の合計が見れる
    - .any()-存在するかのBool
- .fillna('',inplace=)
    - Nanを置き換える
    - ''-Nanを埋める値
    - inplace-True:置き換え
- data.plot
  - (kind="scatter", x="longitude", y="latitude", alpha=0.1)
    - kind:グラフ種類
    - alpha: データ密度色付け
    - .pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True)
ax[0].set_title('Survived')
        - データを円グラフで表示
        - explode-グラフの間隔
        - ax-プロット箇所
    - .hist(x, bins=None, range=None, normed=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, hold=None, data=None, **kwargs)
        - ヒストグラム
        - ax-プロット位置設定
        - bins-データ切り分け数
        - edgecolor-枠線色
        - color-色
    - .barh(width=0.8)
        - 横棒図のプロット
- data.T
    - .boxplot()
        - 箱ひげ図をプロット
- pandas.crosstab(index, columns, values=None, rownames=None, colnames=None, aggfunc=None, margins=False, margins_name='All', dropna=True, normalize=False)
    - クロス集計表作成
    - index-行データ
    - columns-列データ
    - margins-行列毎の合計算出
- data.groupby([,])[]
    - データのカテゴリ毎に区分した後その他のデータがどのカテゴリいるか確認する
    - .count()-数
    - .sum()-合計
    - .mean()-平均
- .merge(data1, data2)
    - データをマージする左外部結合
    - data1に対応するデータがない場合はNanが入る
- data.cut()
    - 値をもとにビン分割-数値データ
- data.qcut()
    - 量をもとにビン分割-カテゴリデータ
- .ravel
    - numpyの多次元配列を一次元配列に変換
- .agg(['count', 'mean', 'max', 'min', 'sum']).reset_index()
    - 集計の種類を指定してまとめて集計できる
- .maen()
    - 平均計算
- .std()
    - 不偏標準偏差計算
    - ddof=False
        - 標本標準偏差
- .var()
    - 不偏分散
    - ddof=False
        - 標本分散
- .corr()
    - 相関係数を計算
- .str.extract()
    - 正規表現で分割
    - '([A-Za-z]+)\.'-で「.」がつく単語を取得
- .replace([1],[2],inplace=)
    - 置換
    - [1]-置き換えたいデータ
    - [2]-置き換えるデータ
    - inplace-True:置き換え
- .loc([])
    - 特定の要素の指定
    - []-カラム名
- .value_counts().to_frame()
    - 列のカテゴリ数をカウント
- .drop()
    - カラム削除
- .get_dummies(data)
    - 指定データをonehotエンコーディング
- DataFrame.align(data, join = how, axis = 1)
    - 各軸インデックスに対して指定された結合方法で、それらの軸上の2つのオブジェクトを整列させます。
    - data:DataFrameに整合したいデータ
    - join:結合方法の指定
        - {‘outer’, ‘inner’, ‘left’, ‘right’}, default ‘outer’
    - axis:結合方向
        - index (0), columns (1), or both (None)
- .columns
  - 列の指定
  - .levels
    - 列グループ指定
    - defaultは0
    - 2グループ以上存在する場合はlevels[1〜]から指定
    - 使いどころ
      - aggで計算した値を列毎に分解する場合
- .skew()
  - 歪度計算
- .kurt()
  - 尖度計算
- .concat()
  - データの連ータ全部をバッチという表現をしていて、ミニバッチとはバッチの
# numpy
- [次元操作参ータ全部をバッチという表現をしていて、ミニバッチとはバッチのatenadiary.jp/entry/2017/05/17/105549)
- .zeros
  - 指定した行ータ全部をバッチという表現をしていて、ミニバッチとはバッチの
- .concatenateータ全部をバッチという表現をしていて、ミニバッチとはバッチの
    - 既存の軸ータ全部をバッチという表現をしていて、ミニバッチとはバッチの
- .argsort
    - 多次元配ータ全部をバッチという表現をしていて、ミニバッチとはバッチの
    - 末尾[::-ータ全部をバッチという表現をしていて、ミニバッチとはバッチの
- .linspace(miータ全部をバッチという表現をしていて、ミニバッチとはバッチの
    - min-maxータ全部をバッチという表現をしていて、ミニバッチとはバッチの値を出力
- .exp
  - 対数を計算ータ全部をバッチという表現をしていて、ミニバッチとはバッチの
- .maximum
  - 入力値の最ータ全部をバッチという表現をしていて、ミニバッチとはバッチの
- .tanh
  - tanhを計算ータ全部をバッチという表現をしていて、ミニバッチとはバッチの
- .random
  - .randint
    - 整数の乱数を生成
  - .uniform(low,high,size)
    - low以上high未満の一様乱数をsize分生成
  - .shuffle
    - 配列を並び替える
  - .permutation
    - 並び替えた配列のコピーを生成する
- expand_dims()
  - 軸を指定して次元を増やす。
  - axis = 0:[1 2 3] -> [[1 2 3]]
  - axis = 1:[1 2 3] -> [[1] [2] [3]]
  - a1[np.newaxis, :]と同義
- .r_[a,b]
  - 行結合
- .c_[a,b]
  - 列結合
- .allclose
  - 2つのNdarrayが近い値かどうかを比べる
- fliplr
  - 配列を左右に反転します。 各行のエントリを左右に反転します。列は保持されますが、以前とは異なる順序で表示されます。
- clip
  - 引数に最小値と最大値を指定すると、その範囲外の値は最小値または最大値に置き換えられる。
- prod
  - 配列要素の積
    - ex:
    ```
    np.prod(x[2,3])
    >2*3 = 6
    ```
- corrcoef(x, y=None, rowvar=True, bias=_NoValue, ddof = _NoValue)
  - 相関係数を要素に持つ行列が返されます。
  - ex:
    ``` python
    cor = np.corrcoef(train_transaction['TransactionDT'], train_transaction[i])[0,1]
    # [0,1]は相関係数のみ取得する
    ```
# scipy
- .stats
  - 一通り確率密度関数から検定までが実装されています
  - .probplot(data, plot)
    - 確率プロットの分位数を計算し、必要に応じてプロットを表示します
    - plot
      - 分位数と最小二乗法をプロットします
  - .norm
    - - 正規分布を計算
    - .fit(data)
- .special
  - .boxcox(data, lam)
    - Box-Cox変換を計算する
    - Box-Cox
      - データを正規分布に近づけてくれる
    - lam
      - 変換のパワーパラメータ
# matplotlib
## .pyplot
- .subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
    - nrows-行数
    - ncols-列数
    - figsize=(,)-図の大きさ指定
- plt.gcf()
    - get current figureの指定
- plt.gca()
    - current Axesの指定
- plt.figure()
  - figを定義
- plt.add_subplot()
  - サブプロットを追加
- .bar(x,y)
  - 棒グラフ表示
- .barh(x,y)
  - 棒グラフ(横)表示
- subplots_adjust
  - 左右の余白は wspace、上下の余白は hspace で指定します。
- add_subplot(行, 列, 場所)
  - subplotの追加
# seaborn
- .countplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, orient=None, color=None, palette=None, saturation=0.75, dodge=True, ax=None, **kwargs)
  - カテゴリ値をカウントして棒グラフでプロット
  - x-X軸データ
  - hue-カウントするデータ
  - data-使用データ
  - ax-プロット位置
  - ex:
  ```python
  sns.countplot(x="ProductCD", ax=ax[0], hue = "isFraud", data=train_transaction)
  ```
- .factorplot(x,y,hue='',data=, col=)
    - 複数の離散変数と1つ以下の連続変数の分布を可視化するグラフ
    - col-カテゴリでプロット切り分け
- .violinplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, bw='scott', cut=2, scale='area', scale_hue=True, gridsize=100, width=0.8, inner='box', split=False, dodge=True, orient=None, linewidth=None, color=None, palette=None, saturation=0.75, ax=None, **kwargs)
    - x-X軸データ
    - y-Y軸データ
    - hue-プロットデータ
    - split-True:対比データを並べる;False:各データ表示
- .barplot([1],[2],data=,ax=)
    - [1]-X軸データ
    - [2]-Y軸データ
    - data-プロットしたいデータ
    - ax-プロット位置
- .distplot(a, bins=None, hist=True, kde=True, rug=False, fit=None, hist_kws=None, kde_kws=None, rug_kws=None, fit_kws=None, color=None, vertical=False, norm_hist=False, axlabel=None, label=None, ax=None)
    - ヒストグラムと密度近似関数を表示
    - a-Data
    - kde-密度近似関数
    - ex:
    ```python
    sns.distplot(train_transaction.loc[train_transaction['isFraud'] == 1][cn], bins=50)
    ```
- .heatmap(data, vmin=None, vmax=None, cmap=None, center=None, robust=False,
                annot=None, fmt='.2g', annot_kws=None, linewidths=0,
                linecolor='white', cbar=True, cbar_kws=None, cbar_ax=None,
                square=False, ax=None, xticklabels=True, yticklabels=True,
                mask=None, **kwargs)
    - 色付き表のプロット
    - data-data.corr()
    - vmin, vmax
      - 最小値、最大値
    - cmap-カラーマップ指定
    - squre
      - True:グラフを正方形に保つ
- .pairplot(data, hue='Survived', palette = 'seismic',size=1.2,diag_kind = 'kde',diag_kws=dict(shade=True),plot_kws=dict(s=10) )
    -  hue-プロットしたいデータ
- .PairGrid(data = plot_data, size = 3, diag_sharey=False,hue = 'TARGET',vars = [x for x in list(plot_data.columns) if x != 'TARGET'])
    - データセット内にペアワイズ関係をプロットするためのサブプロットグリッド。
    ```
    ペアワイズ相関分析:
    ペアワイズ相関分析は、Griffin & Gonzalez(1995)が提案したペアデータに特化した統計手法
    ```

- .kdeplot(df.ix[df['TARGET'] == 0, var_name], label = 'TARGET == 0')
    - カーネル密度推定
    ```
    母集団の標本のデータが与えられたとき、カーネル密度推定を使えばその母集団のデータを外挿できる
    ```
- .boxplot(x,y,data)
  - 箱ひげ図
- set
  - デフォルトスタイルのセット
  - ex:
  ```python
  sns.set(font_scale=1.2)
  ```

# plotly
- offline
    - .iplot()
        - グラフの表示
- graph_objs
  - Figure(data, layout)
    - プロットの表示
    - data: プロットしたいデータタイプとそこに含むデータが定義されたグラフオブジェクト
    - layout: 辞書型で定義した情報を入力
    - ex:
    ```python
    trace2 = go.Bar(
     x=x ,
     y=y,
     marker=dict(
         color=y,
         colorscale = 'Viridis',
         reversescale = True
     ),
     name="Imbalance",    
    )
    layout = dict(
        title="Data imbalance - isFraud",
        #width = 900, height = 500,
        xaxis=go.layout.XAxis(
        automargin=True),
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=True,
    #         domain=[0, 0.85],
        ), 
    )
    fig1 = go.Figure(data=[trace2], layout=layout)
    ```
  - [Bar](https://plot.ly/python/reference/#bar)
    - ex:
    ```python
    trace2 = go.Bar(
        x=x ,
        y=y,
        marker=dict(
            color=y,
            colorscale = 'Viridis',
            reversescale = True
        ),
        name="Imbalance",    
    )
    ```
# gc
- .enable()
    - 自動ガベージコレクションを有効にします。
- .disable()
    - 自動ガベージコレクションを無効にします。
# IPython
- .display
  - SVG
    - オブジェクトのSVG表現を表示します。
# PIL
- Image
  - .open(img_dir)
    - イメージファイル読み込み
    - useex:
      - np.array(Image.open(img_dir))
        - 画像をnumpy配列で読み込み
  - resize(size)
    - 画像のサイズを変更
  - fromarray(np.ndarray)
    - ndarray型で読み込んだ画像データを画像データに再変換
  - save(image_name)
    - 画像の保存
# functools
- partial
  - 簡易的なラッパ関数を作成できる
  - 初期値が冗長な関数をラップするのに使える
# glob
- カレントディレクトリのファイル一覧を取得する