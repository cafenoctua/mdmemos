# Basic Tecnique
- リストに分類器をまとめることで複数の分類器を繰り返しで計算可能

# MLAlgorithm
## fuature engineering
- .preprocessing
  - MinMaxScaler
    - 正規化
  - .LabelEncoder
      - クラスラベルを整数に変換
      - .fit_transform(classlables)
  - .PolynomialFeatures(degree=)
      - 多項式の生成
      - degree:次数
  - Imputer(strategy="")
    - 欠損値の埋め方等を指定して補完する
    - strategy:mean, median, mode
## Classification
### XG Boost
- XGBClassifier
    - n_estimators
    - learning_rate
### sklearn
- model
    - __class__
        - クラス情報取得
        - __name__
            - モデル名取得
- .svm
    - サポートベクターマシン
    - .SVC(kernel='rbf',C=1,gamma=0.1)
        - kernel-rbf:カーネル使用;linear:線形
        - C-正則化
        - gamma-カーネルのパラメータ
- .linear_model
    - LogisticRegression
        - ロジスティック回帰
        - penalty-正則化
- .ensemble
    - RandomForestClassifier
        - ランダムフォレスト
    - VotingClassifier
        - 複数の学習済みモデルを用意して多数決などで推論の結果を決めるという手法
        - estimators-モデル
        - voting-hard:予測の精度が高いものを採用;soft:結果の平均
    - BaggingClassifier
        ```
        バギング法は、元のトレーニングセットのランダムなサブセットにブラックボックス推定器を構築し、個々の予測を集約して最終的な予測を形成する、アルゴリズムのクラスを形成します。
        ```
        - base_estimator-モデル
        - n_estimators-生成するモデル量
    - AdaBoostClassifier
        ```アダブーストは、ランダムよりも少し精度がいいような弱い識別機を組みわせて、強い識別機を作成しようとする機械学習モデル
        ```
        - n_estimators-ブースティング数
        - learning_rate-学習率
    - GradientBoostingClassifier
        ```まず勾配ブースティングとは複数の弱学習器を組み合わせたアンサンブル学習の一種で、その中でも1つずつ順番に弱学習器を構築していく手法
        ```
        - n_estimators
        - learning_rate

- .neighbors
    - KNeighborsClassifier
        - k近傍法
        - n_neighbors-分類数
- .naive_bayes
    - GaussianNB
        - ガウシアンナイーブベイズ
        ```
        分類問題ってベイズの定理を使えば解けるんじゃね？
        ```
- .tree
    - DecisionTreeClassifier
        - 決定木

# Calc Technique
- .model_selection
    - KFold
        - データを指定した割合で分割
        - n_splits-割合:ex.10
        - shuffle-データのシャッフ:True
        - random_state-乱数の割合:ex.10
    - cross_val_score
    - cross_val_predict
    - GridSearchCV
        - 設定したパラメータの組み合わせをすべて試す
        - estimator-モデル
        - param_grid=入力パラメータ
        - verbose-ログ表示周期


# DataOperation
- .model_selection
    - train_test_split

# Evaluation
- metrics
    - .confucion_matrix(Y,y_pred)
        - 混同行列計算
        - Y:正解ラベル
        - y_pred:予測ラベル
    - .f1_score(Y,y_pred)
        - F1スコア計算
        - Y:正解ラベル
        - y_pred:予測ラベル
    - .roc_curve(Y, y_pred)
        - ROC曲線を計算
        - 偽陽性と真陽性と閾値計算
        - Y:正解ラベル
        - y_pred:予測ラベル
    - .auc(fpr, tpr)
        - ROC曲線を計算
        - fpr:偽陽性
        - tpr:真陽性
    