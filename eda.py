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

def generate_eda_plot(df: pd.DataFrame, columns: Optional[list[str]] = None) -> None:

    if columns is None:
        columns = df.columns

    n_plots = len(columns)
    
    fig, axes = plt.subplots(1, n_plots, figsize=(5 * n_plots, 4))
    
    for i, column in enumerate(columns):
        if df[column].dtype in ['int64']:
            sns.boxplot(df[column].sort_values(), ax=axes[i])
            axes[i].set(
                xlabel=column, 
                ylabel=f'{column} Counts', 
                title=f'{column} Distribution'
            )
        elif df[column].dtype in ['float64']:
            sns.histplot(df[column].sort_values(), kde=True, ax=axes[i])
            axes[i].set(
                xlabel=column, 
                ylabel=f'{column} Counts', 
                title=f'{column} Distribution'
            )
        elif df[column].dtype in ['O', 'str']:
            sns.countplot(x=df[column].sort_values(), ax=axes[i])
            axes[i].set(
                xlabel=column, 
                ylabel=f'{column} Counts', 
                title=f'{column} Count Distribution'
            )
            axes[i].bar_label(axes[i].containers[0])
    
    plt.tight_layout()
    plt.show()