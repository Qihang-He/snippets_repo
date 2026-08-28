"""示例：生成 LaTeX 表格并保存为 tex 文件
运行：python latex_table_example.py
"""
from pathlib import Path


def write_table(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    content = r"""
\begin{table}[ht]
  \centering
  \begin{tabular}{lcc}\hline
  Group & Mean & SD \\
  GroupA & 1.23 & 0.45 \\
  GroupB & 2.34 & 0.67 \\
  \hline
  \end{tabular}
  \caption{示例表格 (Chinese + English).}
  \label{tab:example}
\end{table}
"""
    with open(path, 'w', encoding='utf8') as f:
        f.write(content)


if __name__ == '__main__':
    out = Path(__file__).resolve().parent / 'out' / 'table.tex'
    write_table(out)
    print('Wrote', out)
