# 模板：数据分析（pandas + 可视化）

数据文件: ${data/measurement.csv}（列: ${sample,group,value}）

主要分析问题: ${比较组均值/分组统计/回归}

可视化需求: ${箱线图/散点图/热图}

输出表格: ${group_summary.csv,stats_table.tex}

要求:
1) 使用 `pandas` 做加载与清洗，清楚说明缺失值处理。
2) 提供统计方法代码（t-test/ANOVA/回归）并说明适用条件。
3) 使用 `matplotlib`/`seaborn` 保存高分辨率图片（dpi=300）。
