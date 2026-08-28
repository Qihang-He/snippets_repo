"""示例：数据分析脚本（可运行）
依赖：pandas, numpy, matplotlib, seaborn
运行：python data_analysis_example.py
"""
import pathlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def generate_sample_csv(path: pathlib.Path):
    df = pd.DataFrame({
        "sample": np.arange(1, 51),
        "group": np.where(np.arange(1, 51) <= 25, "A", "B"),
        "value": np.concatenate([np.random.normal(5, 1, 25), np.random.normal(6, 1.2, 25)])
    })
    df.to_csv(path, index=False)
    return df


def analyze_and_plot(csv_path: pathlib.Path, out_dir: pathlib.Path):
    df = pd.read_csv(csv_path)
    summary = df.groupby('group')['value'].agg(['mean', 'std', 'count']).reset_index()
    out_dir.mkdir(parents=True, exist_ok=True)
    summary.to_csv(out_dir / 'group_summary.csv', index=False)

    sns.set(style='whitegrid')
    fig, ax = plt.subplots(figsize=(4, 4), dpi=300)
    sns.boxplot(data=df, x='group', y='value', ax=ax, palette='colorblind')
    ax.set_title('Group comparison')
    plt.tight_layout()
    fig.savefig(out_dir / 'boxplot.png', dpi=300)


if __name__ == '__main__':
    repo_root = pathlib.Path(__file__).resolve().parents[2]
    data_dir = repo_root / 'snippets' / 'examples' / 'data'
    data_dir.mkdir(parents=True, exist_ok=True)
    csv_path = data_dir / 'sample_data.csv'

    if not csv_path.exists():
        print('Generating sample CSV...')
        generate_sample_csv(csv_path)

    print('Running analysis and saving outputs...')
    analyze_and_plot(csv_path, data_dir)
    print('Done. Outputs in', data_dir)
