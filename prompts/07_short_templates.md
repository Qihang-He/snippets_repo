# 短版模板（Short templates）

这些模板为节省 token 的短提示，适用于快速生成最小可运行代码或写作片段。

- `tpl:cg`：生成可运行 Python 脚本，返回仅代码；英文变量名；中文注释；含最小示例数据。
- `tpl:da`：简洁数据分析脚本（加载/清洗/可视化/保存高分辨率图片）。
- `tpl:figs`：绘图最小参数（类型/尺寸/色板/保存命令）。
- `tpl:ltx`：LaTeX 片段（section/figure/table caption + BibTeX 示例）。
- `tpl:gitc`：commit/PR 模板（类型、issue、摘要）。
- `tpl:rev`：代码审查要点（路径、关注点、1-2 行重构示例）。

使用方式：将此内容作为 prompt 的起始模板，或直接在 VS Code snippet 中触发对应前缀。
