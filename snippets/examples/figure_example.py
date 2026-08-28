"""示例：绘图美化脚本（Matplotlib / Seaborn）
运行：python figure_example.py
"""
import pathlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def make_sample_plot(out_path: pathlib.Path):
    np.random.seed(0)
    df = pd.DataFrame({
        'x': np.linspace(0, 10, 200),
        'y': np.sin(np.linspace(0, 10, 200)) + np.random.normal(0, 0.2, 200),
        'category': np.random.choice(['A', 'B'], size=200)
    })

    sns.set_context('paper')
    sns.set_style('whitegrid')
    rc = {
        'font.size': 10,
        'axes.titlesize': 11,
        'axes.labelsize': 10
    }
    plt.rcParams.update(rc)

    fig, ax = plt.subplots(figsize=(4, 3), dpi=300)
    sns.lineplot(data=df, x='x', y='y', hue='category', ax=ax, palette='colorblind')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y value')
    ax.set_title('Publication-ready line plot')
    ax.legend(title='Category')
    plt.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=300, bbox_inches='tight')


if __name__ == '__main__':
    out = pathlib.Path(__file__).resolve().parent / 'out' / 'lineplot.png'
    make_sample_plot(out)
    print('Saved', out)
