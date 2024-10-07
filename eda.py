import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Optional

def summarize_data(df: pd.DataFrame) -> None:
    print('\n------------------------Type & Null Analysis------------------------')
    print(df.info())

    print('\n------------------------Categorical Analysis------------------------')
    if len(df.select_dtypes(include='object').columns) > 0:
        print(df.describe(include='object'))
    else:
        print('No Categorical Columns')

    print('\n-------------------------Numerical Analysis-------------------------')
    if len(df.select_dtypes(exclude='object').columns) > 0:
        print(df.describe(exclude='object').round(2))
    else:
        print('No Numerical Columns')

def _eda_plot(df, column, ax):
    if df[column].dtype in ['int64']:
        sns.boxplot(df[column].sort_values(), ax=ax)
        ax.set(
            xlabel=column, 
            ylabel=f'{column} Counts', 
            title=f'{column} Distribution'
        )
    elif df[column].dtype in ['float64']:
        sns.histplot(df[column].sort_values(), kde=True, ax=ax)
        ax.set(
            xlabel=column, 
            ylabel=f'{column} Counts', 
            title=f'{column} Distribution'
        )
    elif df[column].dtype in ['O', 'str']:
        sns.countplot(x=df[column].sort_values(), ax=ax)
        ax.set(
            xlabel=column, 
            ylabel=f'{column} Counts', 
            title=f'{column} Count Distribution'
        )
        ax.bar_label(ax.containers[0])
        
def generate_eda_plot(df: pd.DataFrame, columns: Optional[list[str]] = None) -> None:

    if columns is None:
        columns = df.columns

    n_plots = len(columns)
    
    if n_plots == 1:
        fig, ax = plt.subplots(1, 1, figsize=(8, 4))
        _eda_plot(df, columns[0], ax)
    elif n_plots <= 3:
        fig, axes = plt.subplots(1, n_plots, figsize=(5 * n_plots, 4))
        for i, column in enumerate(columns):
            _eda_plot(df, column, axes[i])
    elif n_plots <= 6:
        fig, axes = plt.subplots(math.ceil(n_plots / 2), 2, figsize=(10, 4 * math.ceil(n_plots / 2)))
        k = 0
        for i in range(axes.shape[0]):
            for j in range(axes.shape[1]):
                _eda_plot(df, columns[k], axes[i][j])
                k += 1
                if k == n_plots:
                    break
    else:
        fig, axes = plt.subplots(math.ceil(n_plots / 4), 4, figsize=(16, 3 * math.ceil(n_plots / 2)))
        k = 0
        for i in range(axes.shape[0]):
            for j in range(axes.shape[1]):
                _eda_plot(df, columns[k], axes[i][j])
                k += 1
                if k == n_plots:
                    break

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    print('test')