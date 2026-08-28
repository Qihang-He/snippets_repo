import pathlib
import pytest


def test_data_analysis_smoke(tmp_path):
    pd = pytest.importorskip("pandas")
    sns = pytest.importorskip("seaborn")
    from snippets.examples.data_analysis_example import generate_sample_csv, analyze_and_plot

    csv_path = tmp_path / "sample.csv"
    df = generate_sample_csv(csv_path)
    assert not df.empty

    out_dir = tmp_path / "out"
    analyze_and_plot(csv_path, out_dir)
    assert (out_dir / 'group_summary.csv').exists()
    assert (out_dir / 'boxplot.png').exists()


def test_figure_smoke(tmp_path):
    plt = pytest.importorskip("matplotlib")
    from snippets.examples.figure_example import make_sample_plot

    out = tmp_path / "lineplot.png"
    make_sample_plot(out)
    assert out.exists()


def test_latex_table_smoke(tmp_path):
    from snippets.examples.latex_table_example import write_table

    out = tmp_path / "table.tex"
    write_table(out)
    assert out.exists()
