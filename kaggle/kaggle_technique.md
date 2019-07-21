# Import
## Ptn1
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
%matplotlib inline
import matplotlib.pyplot as plt  # Matlab-style plotting
import seaborn as sns
color = sns.color_palette()
sns.set_style('darkgrid')
import warnings
def ignore_warn(*args, **kwargs):
    pass
warnings.warn = ignore_warn #ignore annoying warning (from sklearn and seaborn)

from scipy import stats
from scipy.stats import norm, skew #for some statistics

# Read Data
### Ptn1
pd.read_csv()

# Check Data
- dataframe.head()
- dataframe.info()
- dataframe.describe()
- dataframe.describe(include=['O'])
  - カテゴリ値を説明する
- dataframe.shape

## Skew
### Ptn1
``` python
numeric_feats = all_data.dtypes[all_data.dtypes != "object"].index

skewed_feats = all_data[numeric_feats].apply(lambda x: skew(x.dropna())).sort_values(ascending=False)
print("Skew in numeric features:\n")
skewness = pd.DataFrame({'Skew': skewed_feats})
skewness.head(10)
```
# Data Process
## Merge
### Ptn1
``` python
all_data = pd.concat((train, test)).reset_index(drop=True)
```
## Check Null
### Prn1
``` python
all_data.isnull().sum()
```
## 正規化
### Ptn1(Box-Cox)
``` python
skewness = skewness[abs(skewness) > 0.75]
print("{} skewed numerical features to Box Cox transform".format(skewness.shape[0]))

from scipy.special import boxcox1p
skewed_features = skewness.index
lam=0.15

for feat in skewed_features:
    all_data[feat] = boxcox1p(all_data[feat], lam)
```
## Drop
### column
all_data_na_percent.drop('Column', axis=1)
### record
all_data_na_percent.drop(all_data_na_percent['Column']>??.index)

# Plot
## Scatter
### Ptn1
``` python
fig, ax = plt.subplots()
ax.scatter(x=train['XColumn'], y=train['YColumn'])
plt.ylabel('SalePrice', fontsize=13)
plt.xlabel('GrLivArea', fontsize=13)
plt.show()
```

## Dist
### Ptn1
sns.distplot(train['Column'], fit=norm)

(mu, sigma) = norm.fit(train['Column'])
print('mu={:.2f}, sigma={:.2f}\n'.format(mu,sigma))

plt.legend(['Normal dist ($\mu=$ {:.2f} $\sigma=$ {:.2f})'.format(mu,sigma)], loc="best")
plt.ylabel('Frequency')
plt.title('Column distribution')

fig = plt.figure()
res = stats.probplot(train['Column'], plot=plt)
plt.show()

