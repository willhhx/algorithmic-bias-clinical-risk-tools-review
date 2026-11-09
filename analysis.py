"""Project 5 (narrative review): derived numbers from data/extracted_figures.csv (each figure read from a cited source)
-> outputs/results.json, results.csv, figure1_clinical_algorithm_bias.png.   Run: python3 analysis.py   Needs: pandas, matplotlib."""
import json, os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "outputs"); os.makedirs(OUT, exist_ok=True)
df = pd.read_csv(os.path.join(HERE, "data", "extracted_figures.csv"), dtype=str)
S = dict(zip(df.key, df.value))
F = {k: float(v) for k, v in S.items() if k != "gr_registry_years"}
R = {"inputs": F}
rt = lambda a, b, n=1: round(F[a] / F[b], n)
R["ob_ratio_after_vs_before"] = rt("ob_pct_after", "ob_pct_before", 2)
R["ob_pp_gain"] = round(F["ob_pct_after"] - F["ob_pct_before"], 1)
R["sj_mich_ratio"] = rt("sj_mich_black", "sj_mich_white", 2)
R["sj_multi_ratio"] = rt("sj_multi_black", "sj_multi_white", 2)
R["sj_auc_gap"] = round(F["sj_auc_white"] - F["sj_auc_black"], 2)
R["wong_ratio"] = rt("wong_hidden_black", "wong_hidden_white", 2)
R["wong_pp_gap"] = round(F["wong_hidden_black"] - F["wong_hidden_white"], 1)
R["wong_mort_diff_pp"] = round(F["wong_mort_black_hidden"] - F["wong_mort_black_nohidden"], 1)
R["fawzy_ratio"] = rt("fawzy_occ_black", "fawzy_occ_white", 2)
R["fawzy_pp_gap"] = round(F["fawzy_occ_black"] - F["fawzy_occ_white"], 1)
R["fawzy_hazard_reduction_pct"] = round(100 * (1 - F["fawzy_hr_black"]))
# eGFR: signed error = estimated minus measured (overestimate positive)
R["egfr_gap_current"] = round(F["inker_cur_black"] - F["inker_cur_nonblack"], 1)
R["egfr_gap_new"] = round(-F["inker_new_black"] - F["inker_new_nonblack"], 1)  # Black -3.6 vs non-Black +3.9
R["egfr_abs_gap_new"] = abs(R["egfr_gap_new"])
assert R["ob_ratio_after_vs_before"] > 2.6 and R["ob_ratio_after_vs_before"] < 2.7
assert 3.2 < R["sj_mich_ratio"] < 3.3
pd.DataFrame([{"key": k, "value": v} for k, v in R.items() if k != "inputs"]).to_csv(os.path.join(OUT, "results.csv"), index=False)
json.dump(R, open(os.path.join(OUT, "results.json"), "w"), indent=1)

# ---- Figure 1 (Okabe-Ito, color-blind safe)
BLK, WHT, ORG = "#D55E00", "#0072B2", "#E69F00"
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
fig, ax = plt.subplots(1, 2, figsize=(13.5, 6.2), gridspec_kw={"width_ratios": [1.15, 1]})
a = ax[0]
labels = ["Sjoding 2020\nMichigan\n(occult*)", "Sjoding 2020\n178 hospitals\n(occult*)", "Fawzy 2022\nCOVID-19, Hopkins\n(occult*)", "Wong 2021\n215 hospitals\n(hidden†)"]
b = [F["sj_mich_black"], F["sj_multi_black"], F["fawzy_occ_black"], F["wong_hidden_black"]]
w = [F["sj_mich_white"], F["sj_multi_white"], F["fawzy_occ_white"], F["wong_hidden_white"]]
x = range(4); wd = 0.38
r1 = a.bar([i - wd/2 for i in x], b, wd, color=BLK, label="Black patients")
r2 = a.bar([i + wd/2 for i in x], w, wd, color=WHT, label="White patients")
for rr in (r1, r2):
    for p in rr: a.text(p.get_x() + p.get_width()/2, p.get_height() + 0.5, f"{p.get_height():.1f}", ha="center", fontsize=10)
a.set_xticks(list(x)); a.set_xticklabels(labels, fontsize=9.5)
a.set_ylabel("Patients with oxygen level missed by pulse oximeter (%)"); a.set_ylim(0, 35)
a.set_title("A. Missed low oxygen, Black vs White patients", loc="left", fontsize=12, fontweight="bold")
a.legend(frameon=False, loc="upper right")
a.text(0, -0.30, "*Occult: arterial O2 <88% while pulse oximeter read 92–96%.  †Hidden: arterial O2 <88% while pulse oximeter read ≥88%.\nDefinitions and settings differ by study, so bars are not comparable across studies.", transform=a.transAxes, fontsize=8.5, va="top")
c = ax[1]
eq = ["Current equation\n(with race term)", "New equation\n(race removed)"]
blk = [F["inker_cur_black"], -F["inker_new_black"]]; non = [F["inker_cur_nonblack"], F["inker_new_nonblack"]]
blk_ci = [(F["inker_cur_black_lo"], F["inker_cur_black_hi"]), (-F["inker_new_black_hi"], -F["inker_new_black_lo"])]
non_ci = [(F["inker_cur_nonblack_lo"], F["inker_cur_nonblack_hi"]), (F["inker_new_nonblack_lo"], F["inker_new_nonblack_hi"])]
xs = [0, 1]
def eb(vals, cis, off, col, lab):
    c.bar([i + off for i in xs], vals, wd, color=col, label=lab)
    c.errorbar([i + off for i in xs], vals, yerr=[[v - lo for v, (lo, hi) in zip(vals, cis)], [hi - v for v, (lo, hi) in zip(vals, cis)]], fmt="none", ecolor="black", capsize=4, lw=1.2)
    for i, v, (lo, hi) in zip(xs, vals, cis): c.text(i + off + 0.2*wd*0, (hi + 0.4) if v >= 0 else (lo - 1.0), f"{v:+g}", ha="center", fontsize=10)
eb(blk, blk_ci, -wd/2, BLK, "Black participants"); eb(non, non_ci, wd/2, WHT, "Non-Black participants")
c.axhline(0, color="black", lw=0.8); c.set_xticks(xs); c.set_xticklabels(eq)
c.set_ylabel("Median error: estimated minus measured GFR\n(mL/min/1.73 m²; + = overestimate)"); c.set_ylim(-8, 8)
c.set_title("B. Kidney function equation error", loc="left", fontsize=12, fontweight="bold")
c.legend(frameon=False, loc="lower left")
c.text(0, -0.22, "Bars: median; whiskers: 95% CI. Validation data: 12 studies, 4,050 participants (14.3% Black).", transform=c.transAxes, fontsize=8.5, va="top")
fig.text(0.01, -0.02, "Data sources: Sjoding et al. (2020), Fawzy et al. (2022), Wong et al. (2021), Inker et al. (2021); values transcribed from the articles (see data/extracted_figures.csv).", fontsize=8.5)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "figure1_clinical_algorithm_bias.png"), dpi=300, bbox_inches="tight")
print("ok", {k: v for k, v in R.items() if k != "inputs"})
