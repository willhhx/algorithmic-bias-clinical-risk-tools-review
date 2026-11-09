"""Writes verification.md: figure traceability, citation checks, discrepancies, word count."""
import json, os, re
import pandas as pd
H = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(H + "/data/extracted_figures.csv", dtype=str); W = json.load(open(H + "/outputs/wordcount.json")); R = json.load(open(H + "/outputs/results.json"))
flat = re.sub(r"\s+", " ", open(H + "/latex/manuscript.tex").read().replace("\\%", "%"))
def fmt(v):
    try: x = float(v)
    except ValueError: return v
    return f"{x:,.0f}" if x >= 1000 else f"{x:g}"
rows = []; used = 0
for _, r in df.iterrows():
    f = fmt(r.value); p = f in flat; used += p
    rows.append(f"| {r.key} | {f} | {r.source} | {r.doi_or_url} | {r.where_found} | {'in text' if p else 'data file only'} |")
cites = [
 ("Obermeyer et al. 2019, Science 366:447", "10.1126/science.aax2342", "abstract"),
 ("Vyas, Eisenstein & Jones 2020, NEJM 383:874", "10.1056/NEJMms2004740", "Crossref only; no abstract; claims limited to title and as cited by Grobman et al."),
 ("Inker et al. 2021, NEJM 385:1737", "10.1056/NEJMoa2102953", "abstract (PMC8822996); 33 authors, first 19 listed per APA"),
 ("Delgado et al. 2022, AJKD 79:268", "10.1053/j.ajkd.2021.08.003", "abstract incl. recommendations"),
 ("Sjoding et al. 2020, NEJM 383:2477", "10.1056/NEJMc2029240", "full text (PMC7808260). A correction notice exists (NEJM 2021;385:2496); NOT read, so check figures against the corrected version"),
 ("Wong et al. 2021, JAMA Netw Open 4:e2131674", "10.1001/jamanetworkopen.2021.31674", "abstract (Europe PMC)"),
 ("Fawzy et al. 2022, JAMA Intern Med 182:730", "10.1001/jamainternmed.2022.1906", "abstract (Europe PMC); pages 730-738 confirmed in Europe PMC (Crossref lists start page only)"),
 ("Vyas et al. 2019, Women's Health Issues 29:201", "10.1016/j.whi.2019.04.007", "Crossref only; no abstract; claims limited to title"),
 ("Grobman et al. 2021, AJOG 225:664.e1", "10.1016/j.ajog.2021.05.021", "full text (PMC8611105)"),
 ("Wiens et al. 2019, Nat Med 25:1337", "10.1038/s41591-019-0548-6", "abstract"),
 ("Rajkomar et al. 2018, Ann Intern Med 169:866", "10.7326/M18-1990", "abstract"),
 ("Seyyed-Kalantari et al. 2021, Nat Med 27:2176", "10.1038/s41591-021-01595-0", "abstract"),
 ("Paulus & Kent 2020, npj Digit Med 3:99", "10.1038/s41746-020-0304-9", "abstract"),
]
L = ["# Verification: algorithmic bias in clinical risk tools (narrative review)", "",
 f"Main text word count (abstract included; tables, figure, references excluded): **{W['words_main_text_incl_abstract_excl_tables_figures_refs']}** (limit 4,000). Abstract: {W['words_abstract']} words.", "",
 "## Citations (13). Each title, authors, year, journal, volume, pages and DOI matched Crossref (PASS)", "", "| Source | DOI | What was read |", "|---|---|---|"]
L += [f"| {a} | {b} | {c} |" for a, b, c in cites]
L += ["", "## Figure traceability", f"{used} of {len(df)} extracted values appear in the manuscript text; the others are in the data file only (confidence intervals plotted in Figure 1, etc.).", "",
 "| key | value | source | DOI | where found | status |", "|---|---|---|---|---|---|"] + rows
L += ["", "## Derived numbers (reviewer's calculations, outputs/results.json)", ""] + [f"- {k}: {v}" for k, v in R.items() if k != "inputs"]
L += ["", "## Checks and known issues", "",
 "- Obermeyer ratio 46.5/17.7 = 2.63: PASS (recomputed in analysis.py with assertion).",
 "- Sjoding Michigan 88/749 = 11.7% and 99/2778 = 3.6%; multicenter 160/939 = 17.0% and 546/8795 = 6.2%: PASS (recomputed by hand from the full text counts).",
 "- Wong hidden hypoxemia definition (SpO2 >=88% with SaO2 <88%) and Fawzy occult hypoxemia definition (SaO2 <88% with SpO2 92-96%) confirmed from raw Europe PMC abstract text.",
 "- eGFR: the race-free creatinine equation widened the Black vs non-Black gap in median error (7.5 vs 3.2 mL/min/1.73 m2, reviewer calculation using signed medians). Reported as is.",
 "- No em dashes (asserted in build_paper.py). No causal verbs from a banned list (asserted). Race is described as a recorded label, not a biological construct.",
 "- Items to check by hand: (1) Sjoding correction notice; (2) Vyas 2019 and 2020 and Wiens were not read beyond metadata/abstract; (3) an FDA pulse oximetry statement is attributed only to the Sjoding letter.",
 "- The manuscript covers pulse oximetry by race, not skin tone, because the studies cited recorded race."]
open(H + "/verification.md", "w").write("\n".join(L) + "\n")
print("ok", used, len(df))
