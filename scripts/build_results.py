from pathlib import Path
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from research.analysis import make_demo_data, simple_ols_coefficients

def latex_escape(text: str) -> str:
    replacements = {"&": r"\\&", "%": r"\\%", "$": r"\\$", "#": r"\\#", "_": r"\\_", "{": r"\\{", "}": r"\\}"}
    return "".join(replacements.get(char, char) for char in text)

def main() -> None:
    figures = ROOT / "outputs/figures"
    tables = ROOT / "outputs/tables"
    processed = ROOT / "data/processed"
    for directory in (figures, tables, processed):
        directory.mkdir(parents=True, exist_ok=True)

    data = make_demo_data()
    data.to_csv(processed / "demo_data.csv", index=False)
    intercept, treatment_effect = simple_ols_coefficients(data)

    fig, ax = plt.subplots(figsize=(6.2, 3.8), constrained_layout=True)
    groups = [data.loc[data["treatment"] == g, "outcome"] for g in (0, 1)]
    ax.boxplot(groups, tick_labels=["Control", "Treatment"])
    ax.set_ylabel("Outcome")
    ax.set_title("Synthetic example: outcome by group")
    ax.grid(axis="y", alpha=0.25)
    fig.savefig(figures / "treatment_effect.pdf", bbox_inches="tight")
    plt.close(fig)

    rows = [
        ("Observations", f"{len(data):d}"),
        ("Estimated intercept", f"{intercept:.3f}"),
        ("Treatment coefficient", f"{treatment_effect:.3f}"),
    ]
    lines = [r"\begin{tabular}{lr}", r"\toprule", r"Statistic & Estimate \\", r"\midrule"]
    lines.extend(f"{latex_escape(label)} & {value} \\\\" for label, value in rows)
    lines.extend([r"\bottomrule", r"\end{tabular}", ""])
    (tables / "summary_statistics.tex").write_text("\n".join(lines), encoding="utf-8")
    print("Generated figure, table, and synthetic dataset.")

if __name__ == "__main__":
    main()
