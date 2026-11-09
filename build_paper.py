"""Builds latex/manuscript.tex and manuscript.pdf. Numbers in the prose come from data/extracted_figures.csv and outputs/results.json.
Run after analysis.py:  python3 build_paper.py   (needs pdflatex)"""
import json, os, shutil, subprocess
import pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "outputs"); TEX = os.path.join(HERE, "latex")
df = pd.read_csv(os.path.join(HERE, "data", "extracted_figures.csv"), dtype=str); F = dict(zip(df.key, df.value))
R = json.load(open(os.path.join(OUT, "results.json")))
REPO = "https://github.com/willhhx/algorithmic-bias-clinical-risk-tools-review"
def g(k):
    v = float(F[k]); return f"{v:,.0f}" if v >= 1000 else f"{v:g}"
def f1(k): return f"{float(F[k]):.1f}"

abstract = (
 "Background: Clinical risk tools turn patient data into numbers that steer care, such as who gets extra help, how well the kidneys work, or whether oxygen levels are safe. When such a tool works worse for some groups, the harm is built into routine decisions. "
 "Methods: This narrative review draws on 13 verified peer-reviewed sources covering five well-documented cases and the main proposals for auditing and fixing them. It asks how bias enters these tools, what harm has been measured, what patterns recur, how strong the evidence is, and what is missing. "
 f"Findings: Three mechanisms recur: a stand-in outcome that measures access to care and not illness, a race variable written into an equation, and a device or dataset that works less well for some patients. In one widely used care-management algorithm, correcting the bias would raise the share of Black patients flagged for extra help from {g('ob_pct_before')} to {g('ob_pct_after')} percent. Pulse oximeters missed low blood oxygen in {g('sj_mich_black')} percent of readings from Black patients versus {g('sj_mich_white')} percent from White patients in one hospital and {g('sj_multi_black')} versus {g('sj_multi_white')} percent across 178 hospitals; later studies found gaps of different sizes, and one tied the error to delayed eligibility for COVID-19 treatment. Removing race from a kidney function equation shifted the error and did not remove it, while a vaginal birth after cesarean calculator kept the same discrimination (area under the curve {g('gr_auc_new')}) without race. "
 "The evidence is mostly observational and relies on self-reported race. Few studies show whether fixing a tool improves patient outcomes. "
 "Conclusions: Bias in clinical tools is measurable and, in several cases, fixable, but fixes should be audited against real outcomes, and race-based and race-free versions should be compared before and after adoption."
)
intro = [
 "A clinical risk tool is a formula, score, device reading, or computer model that turns patient information into a number used to guide a decision. Examples include equations that estimate kidney function, calculators that predict the chance of a successful vaginal birth after a cesarean, pulse oximeters that estimate blood oxygen, and algorithms that decide which patients are offered extra care. These tools are meant to make decisions more consistent. When they perform worse for some groups, the inconsistency is hidden inside the number, and it can travel through an entire health system.",
 "This review asks five questions. How does bias get into clinical risk tools? What harm has been measured? What patterns repeat across cases? How strong is the evidence? And what is still missing? It uses five cases that are well documented in peer-reviewed work: a commercial care-management algorithm (Obermeyer et al., 2019), race-based kidney function equations and their revision, pulse oximetry, a vaginal birth after cesarean (VBAC) calculator, and imaging algorithms that underdiagnose under-served patients. It then looks at proposals for auditing and mitigation.",
 "Terms are used as the sources use them. Race and ethnicity in these studies are labels, mostly recorded in health records or reported by patients, and are social categories, not biological ones. Several of the sources make that point directly.",
]
methods = [
 "This is a narrative review, not a systematic review. It followed no registered protocol and used no formal risk-of-bias tool. One reviewer selected the sources.",
 "Sources were chosen to cover the cases set as the scope of this review: the Obermeyer algorithm study, race-based estimated glomerular filtration rate (eGFR) and its revision, pulse oximetry and skin tone or race, the VBAC calculator, and at least one source on mitigation and auditing. Candidate articles were located in November 2026 through Crossref and Europe PMC searches. Thirteen peer-reviewed sources were kept. For each, the title, authors, year, journal, volume, pages, and DOI were confirmed against Crossref. Numbers were taken from the full text where it was freely available (Sjoding et al., 2020; Grobman et al., 2021) and otherwise from the abstract. For two sources (Vyas et al., 2019, 2020) and for the Wiens and colleagues roadmap, no abstract with findings was available to the reviewer, so claims about them are limited to their titles and how other sources describe them.",
 "Figures are recorded in a data file with their source and location. Ratios and differences were calculated by script and are labeled as the reviewer's calculations. Evidence on pulse oximetry is described by race, as the studies report it, even though the mechanism concerns skin pigmentation; the studies did not measure skin tone directly, and this review does not claim they did. The Sjoding letter was later corrected (a correction notice exists in the journal, which the reviewer did not read), so those figures should be checked against the corrected version.",
 "Limitations of the method are that other relevant work was probably missed, that the cases were chosen because they are well known, and that cases where a tool was found to be fair are underrepresented in the sources by design.",
]
mech = {
 "A stand-in outcome that measures access, not illness": [
  f"Obermeyer and colleagues (2019) examined a widely used commercial algorithm that helps health systems pick patients for extra help with complex needs. At a given risk score, Black patients were considerably sicker than White patients, as shown by signs of uncontrolled illness. The cause they identified was the target the algorithm was trained to predict. It predicted future health care costs, not illness, and because unequal access to care means less money is spent on Black patients than on White patients with the same needs, cost looked like an effective stand-in for health while carrying the bias. The authors report that correcting this would raise the share of Black patients flagged for extra help from {g('ob_pct_before')} to {g('ob_pct_after')} percent, a {R['ob_ratio_after_vs_before']:g}-fold increase (reviewer's calculation). They suggest that convenient, seemingly effective proxies for the true target are a general source of algorithmic bias.",
 ],
 "A race variable written into the equation": [
  "Some tools include race as an input. Vyas and colleagues (2020) called for reconsidering this practice of race correction in clinical algorithms, and Vyas and colleagues (2019) challenged the inclusion of race in the VBAC calculator. In the kidney case, Inker and colleagues (2021) state that race in eGFR equations is a social and not a biologic construct. Grobman and colleagues (2021) describe the concern behind the VBAC revision as the worry that including these variables may reify a biologic construct of race and ethnicity and perpetuate health disparities.",
 ],
 "A device or dataset that works less well for some patients": [
  "Sjoding and colleagues (2020) noted that questions about pulse oximeter technology had been raised because of its original development in populations that were not racially diverse. Seyyed-Kalantari and colleagues (2021) found that artificial intelligence classifiers applied to chest radiographs consistently and selectively underdiagnosed under-served patient populations, with higher underdiagnosis rates for intersectional groups such as Hispanic female patients. Paulus and Kent (2020) add that model, data, or sampling problems can cause biased predictions even where fairness concerns are not the main issue, and that fairness criteria can be mutually incompatible.",
 ],
}
harms = {
 "Pulse oximetry": [
  f"Sjoding and colleagues (2020) compared pulse oximeter readings with arterial blood measurements taken within 10 minutes. They defined occult hypoxemia as arterial oxygen below 88 percent while the oximeter read 92 to 96 percent. At the University of Michigan ({g('sj_pairs_mich')} paired measures, January to July 2020), this happened in {g('sj_mich_black')} percent of measurements from Black patients and {g('sj_mich_white')} percent from White patients. Across intensive care units in {g('sj_hospitals')} hospitals ({g('sj_pairs_multi')} pairs, 2014 to 2015), the figures were {g('sj_multi_black')} and {g('sj_multi_white')} percent. That is about {R['sj_mich_ratio']:g} and {R['sj_multi_ratio']:g} times as often (reviewer's calculation). The oximeter also detected low oxygen less well in Black patients (area under the curve {g('sj_auc_black')} versus {g('sj_auc_white')}).",
  f"Later studies found gaps of different sizes in other settings. Wong and colleagues (2021) analyzed {g('wong_n')} hospital encounters across {g('wong_icus')} intensive care units and found hidden hypoxemia, defined as an oximeter reading of at least 88 percent with arterial oxygen below 88 percent, in {g('wong_hidden_black')} percent of Black, {g('wong_hidden_hisp')} percent of Hispanic, {g('wong_hidden_asian')} percent of Asian, and {g('wong_hidden_white')} percent of White patients. Among Black patients, in-hospital mortality was {g('wong_mort_black_hidden')} percent with hidden hypoxemia and {g('wong_mort_black_nohidden')} percent without. Those groups were similar at baseline, but this is an association and may reflect illness severity as well as the oximeter error. In patients with COVID-19, Fawzy and colleagues (2022) reported occult hypoxemia in {g('fawzy_occ_black')} percent of Black patients and {g('fawzy_occ_white')} percent of White patients. Black patients had a {R['fawzy_hazard_reduction_pct']} percent lower hazard of being recognized as eligible for oxygen-threshold COVID-19 therapies (hazard ratio {g('fawzy_hr_black')}, 95 percent confidence interval {g('fawzy_hr_lo')} to {f1('fawzy_hr_hi')}), and a median of {g('fawzy_delay_h')} hour longer delay when they were recognized. Of {g('fawzy_never_n')} patients whose eligibility was never recognized, {g('fawzy_never_black_pct')} percent were Black.",
 ],
 "Kidney function equations": [
  f"Inker and colleagues (2021) developed race-free eGFR equations and tested them against measured GFR in a validation set of {g('inker_val_studies')} studies and {g('inker_val_n')} participants ({g('inker_val_black_pct')} percent Black). The current equation, which includes a race term, overestimated measured GFR by a median of {g('inker_cur_black')} mL/min/1.73 m\\textsuperscript{{2}} in Black participants and {g('inker_cur_nonblack')} in non-Black participants. Simply dropping the race adjustment underestimated GFR in Black participants by {g('inker_norace_adj_black')}. A new creatinine equation without race underestimated GFR in Black participants by {g('inker_new_black')} and overestimated it in non-Black participants by {g('inker_new_nonblack')}. For every equation, at least {g('inker_within30')} percent of estimates were within 30 percent of measured GFR. Creatinine and cystatin C equations without race were more accurate, with smaller differences between groups.",
  f"The race-free creatinine equation therefore did not eliminate group error. It reversed its direction for Black participants, and the Black versus non-Black gap in median error was larger than under the current equation ({abs(R['egfr_gap_new']):g} versus {R['egfr_gap_current']:g} mL/min/1.73 m\\textsuperscript{{2}}; reviewer's calculation from the reported medians). The task force of Delgado and colleagues (2022) weighed five approaches against six attributes. It recommended immediate adoption of the creatinine equation refit without race in all US laboratories, citing that it excludes race, included diversity in its development, is available to all laboratories, and has acceptable performance. It also recommended wider use of cystatin C to confirm estimates. The choice was made on several grounds at once, not on accuracy alone.",
 ],
 "Vaginal birth after cesarean": [
  f"Grobman and colleagues (2021) rebuilt the VBAC calculator from the same registry used for the earlier tool, which included race and ethnicity, but without those variables. The registry covered {g('gr_n')} eligible individuals ({F['gr_registry_years'].replace('-', ' to ')} data; {g('gr_black_share')} percent non-Hispanic Black), of whom {g('gr_vbac_pct')} percent had a vaginal birth. The new model, which uses age, height, pre-pregnancy weight, obstetric history, the indication for the prior cesarean, and chronic hypertension, had an area under the curve of {g('gr_auc_new')}, the same as the earlier model ({g('gr_auc_old')}). Race-free prediction was thus possible without a loss of discrimination. The authors note the data are nearly two decades old and that calibration was strong. This evidence is from a single registry and does not show whether the new calculator changes who attempts labor or how they fare.",
 ],
 "Algorithms that decide who gets help": [
  "The Obermeyer study (Table 1 and above) is the clearest example of harm through resource allocation: the algorithm ranked patients by a score that understated the needs of Black patients, so extra help went less often to Black patients who were as sick as others. Seyyed-Kalantari and colleagues (2021) describe a related risk in imaging, where underdiagnosis can delay access to care. Neither source measured the downstream health outcomes of those errors.",
 ],
}
patterns = [
 "Four patterns repeat across the cases. First, the problem is often upstream of the algorithm: the choice of target (cost), the data used to build it (populations not racially diverse), or the way a device is calibrated. Second, the error runs in different directions in different tools. Cost-based scoring understates need, the oximeter overstates oxygen, and the eGFR equation with a race term overestimates kidney function in Black participants on average. Third, removing race helps in some cases and reshuffles error in others: VBAC prediction held its discrimination, while the race-free eGFR equation changed the error. Fourth, in the kidney case the more accurate option added information, a second kidney marker (cystatin C), and did not only delete a variable.",
 "Table 1 collects the main quantified findings. Magnitudes differ widely across studies, from about a 1.4-fold difference in hidden hypoxemia (Wong et al., 2021) to about a 3-fold difference in occult hypoxemia (Sjoding et al., 2020, Michigan), partly because the definitions, patient groups, and settings differ.",
]
quality = [
 "Strengths. Several sources use large samples: tens of thousands of paired oxygen measurements, more than 87,000 encounters, and thousands of participants with measured GFR. Obermeyer and colleagues link the bias to a specific, testable mechanism. The Inker and Grobman papers compare race-based and race-free versions on the same data, which is a stronger design than a single before-and-after comparison.",
 "Weaknesses. Most studies are observational and retrospective. Race is usually recorded in records or self-reported and is a coarse proxy for what is mechanistically relevant: skin pigmentation for oximetry, social and health care access factors for cost. The pulse oximetry studies did not measure skin tone, so they cannot separate pigmentation from other factors correlated with race. Occult hypoxemia can only be assessed where arterial blood was drawn, which is not done for every patient, so the samples may not represent all patients (reviewer's inference). Mortality and treatment-delay associations may be shaped by illness severity. For eGFR, the validation data come from pooled research studies, which may differ from routine care (reviewer's inference). The VBAC data are from a registry covering 1999 to 2002. Findings from different cases are not on a common scale, so Table 1 and Figure 1 describe patterns, not a ranking of harm.",
 "Several of the 13 sources (Vyas et al., 2019, 2020; Wiens et al., 2019; Rajkomar et al., 2018; Paulus & Kent, 2020; Delgado et al., 2022; and the Sjoding letter) are commentaries, frameworks, recommendations, or a short letter and not full tests of a tool. Evidence about whether fixes work is thinner than evidence that problems exist. The review's source selection also favors well-known cases, so it cannot say how common biased tools are overall.",
]
mitig = [
 "The sources describe mitigation at three levels. At the design level, Rajkomar and colleagues (2018) argue that machine learning can worsen disparities through model design, biased data, and the way predictions interact with clinicians and patients, and that principles of distributive justice should be built into design, deployment, and evaluation. They describe technical ways to pursue equal patient outcomes, equal performance, and equal resource allocation, and they guide clinicians on when to prioritize each. Wiens and colleagues (2019) present a roadmap for responsible machine learning in health care that runs from problem formulation to deployment and involves a team of stakeholders.",
 "At the evaluation level, Paulus and Kent (2020) separate algorithmic fairness, which applies to decisions where one outcome is clearly preferred (such as allocating scarce resources), from algorithmic bias, review ways to diagnose and remedy bias, and propose a provisional framework for evaluating clinical prediction models. They note that fairness remedies can be more problematic than diagnosis because there is no agreed definition of fairness. Seyyed-Kalantari and colleagues (2021) show one form of audit: comparing underdiagnosis rates across subgroups, including intersectional ones. Obermeyer and colleagues (2019) show another: testing whether patients at the same score have the same illness burden.",
 "At the correction level, the cases above are real-world revisions: a race-free kidney equation adopted nationally (Delgado et al., 2022) and a race-free VBAC calculator (Grobman et al., 2021). Neither source proves that revision improved outcomes. The Fawzy and Wong findings suggest that a device whose error varies by group warrants monitoring and supplementary measurement (Sjoding et al. note that the Food and Drug Administration requires demographic subgroup reporting in device applications), but the evidence reviewed here does not show which correction works best.",
]
gaps = [
 "Several gaps stand out. First, outcome evidence is scarce: few studies follow patients before and after a tool was changed to see whether decisions or health improved. Second, skin tone was not measured directly in the oximetry studies reviewed, so mechanism and race are not separated. Third, intersectional and other groups (for example, Asian, Hispanic, and Indigenous patients) are covered less than Black and White comparisons. Fourth, audits are done by research teams, one tool at a time; the sources do not describe routine, independent auditing of deployed tools. Fifth, the sources do not agree on a definition of fairness, so a tool can pass one audit and fail another (Paulus & Kent, 2020). Sixth, this review did not examine newer tool types, such as large language models, because they fell outside the sources assigned.",
]
conclusion = [
 "Across the cases reviewed, clinical risk tools showed measurable gaps by race: algorithms that treated cost as health, oximeters that read higher than arterial oxygen more often in Black patients, and equations that carried race as a variable. Removing race can work, as in the VBAC calculator, but in the kidney case it moved the error without ending it, and adding a second marker helped more. The evidence is strong that these problems exist and weaker on whether fixes improve outcomes. Tool developers and health systems should audit performance by group, report the results, and compare versions before and after any change.",
]
kt = ("Key takeaway: Clinical risk tools can work worse for some groups through three repeated routes: a stand-in outcome that measures access to care, a race variable in the equation, and a device or dataset built on non-diverse data. "
      "Removing race helped in some cases (the birth calculator kept its accuracy) but only shifted the error in others (kidney function), so fixes need to be audited against real patient outcomes, which few studies have done.")

t1 = "\n".join([
 f"Obermeyer et al. (2019) & Care-management algorithm & Black patients flagged for extra help: {g('ob_pct_before')}\\% now vs {g('ob_pct_after')}\\% if bias corrected \\\\",
 f"Sjoding et al. (2020) & Occult hypoxemia (Michigan; 178 hospitals) & Black {g('sj_mich_black')}\\% vs White {g('sj_mich_white')}\\%; Black {g('sj_multi_black')}\\% vs White {g('sj_multi_white')}\\% \\\\",
 f"Wong et al. (2021) & Hidden hypoxemia, {g('wong_n')} encounters & Black {g('wong_hidden_black')}\\%; White {g('wong_hidden_white')}\\% \\\\",
 f"Fawzy et al. (2022) & Occult hypoxemia, COVID-19 & Black {g('fawzy_occ_black')}\\% vs White {g('fawzy_occ_white')}\\%; hazard ratio for recognized eligibility {g('fawzy_hr_black')} \\\\",
 f"Inker et al. (2021) & eGFR median error (mL/min/1.73 m\\textsuperscript{{2}}) & Current: Black +{g('inker_cur_black')}, non-Black +{g('inker_cur_nonblack')}; race-free creatinine: Black $-${g('inker_new_black')}, non-Black +{g('inker_new_nonblack')} \\\\",
 f"Grobman et al. (2021) & VBAC calculator, area under the curve & {g('gr_auc_new')} without race vs {g('gr_auc_old')} with race \\\\",
])
caption = ("Panel A: share of patients whose low blood oxygen was missed by a pulse oximeter, Black vs White patients, in four studies (definitions and settings differ). "
           "Panel B: median error of the kidney function (eGFR) equation against measured GFR, Black vs non-Black participants, for the current equation and a new race-free creatinine equation (whiskers are 95\\% confidence intervals). "
           "Sources: Sjoding et al. (2020), Fawzy et al. (2022), Wong et al. (2021), and Inker et al. (2021).")

refs = [
 r"Delgado, C., Baweja, M., Crews, D. C., Eneanya, N. D., Gadegbeku, C. A., Inker, L. A., Mendu, M. L., Miller, W. G., Moxey-Mims, M. M., Roberts, G. V., St. Peter, W. L., Warfield, C., \& Powe, N. R. (2022). A unifying approach for GFR estimation: Recommendations of the NKF-ASN Task Force on Reassessing the Inclusion of Race in Diagnosing Kidney Disease. \emph{American Journal of Kidney Diseases, 79}(2), 268--288.e1. \url{https://doi.org/10.1053/j.ajkd.2021.08.003}",
 r"Fawzy, A., Wu, T. D., Wang, K., Robinson, M. L., Farha, J., Bradke, A., Golden, S. H., Xu, Y., \& Garibaldi, B. T. (2022). Racial and ethnic discrepancy in pulse oximetry and delayed identification of treatment eligibility among patients with COVID-19. \emph{JAMA Internal Medicine, 182}(7), 730--738. \url{https://doi.org/10.1001/jamainternmed.2022.1906}",
 r"Grobman, W. A., Sandoval, G., Rice, M. M., Bailit, J. L., Chauhan, S. P., Costantine, M. M., Gyamfi-Bannerman, C., Metz, T. D., Parry, S., Rouse, D. J., Saade, G. R., Simhan, H. N., Thorp, J. M., Tita, A. T. N., Longo, M., \& Landon, M. B. (2021). Prediction of vaginal birth after cesarean delivery in term gestations: A calculator without race and ethnicity. \emph{American Journal of Obstetrics and Gynecology, 225}(6), 664.e1--664.e7. \url{https://doi.org/10.1016/j.ajog.2021.05.021}",
 r"Inker, L. A., Eneanya, N. D., Coresh, J., Tighiouart, H., Wang, D., Sang, Y., Crews, D. C., Doria, A., Estrella, M. M., Froissart, M., Grams, M. E., Greene, T., Grubb, A., Gudnason, V., Guti\'errez, O. M., Kalil, R., Karger, A. B., Mauer, M., Navis, G., \ldots Levey, A. S. (2021). New creatinine- and cystatin C--based equations to estimate GFR without race. \emph{New England Journal of Medicine, 385}(19), 1737--1749. \url{https://doi.org/10.1056/NEJMoa2102953}",
 r"Obermeyer, Z., Powers, B., Vogeli, C., \& Mullainathan, S. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. \emph{Science, 366}(6464), 447--453. \url{https://doi.org/10.1126/science.aax2342}",
 r"Paulus, J. K., \& Kent, D. M. (2020). Predictably unequal: Understanding and addressing concerns that algorithmic clinical prediction may increase health disparities. \emph{npj Digital Medicine, 3}(1), Article 99. \url{https://doi.org/10.1038/s41746-020-0304-9}",
 r"Rajkomar, A., Hardt, M., Howell, M. D., Corrado, G., \& Chin, M. H. (2018). Ensuring fairness in machine learning to advance health equity. \emph{Annals of Internal Medicine, 169}(12), 866--872. \url{https://doi.org/10.7326/M18-1990}",
 r"Seyyed-Kalantari, L., Zhang, H., McDermott, M. B. A., Chen, I. Y., \& Ghassemi, M. (2021). Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations. \emph{Nature Medicine, 27}(12), 2176--2182. \url{https://doi.org/10.1038/s41591-021-01595-0}",
 r"Sjoding, M. W., Dickson, R. P., Iwashyna, T. J., Gay, S. E., \& Valley, T. S. (2020). Racial bias in pulse oximetry measurement. \emph{New England Journal of Medicine, 383}(25), 2477--2478. \url{https://doi.org/10.1056/NEJMc2029240}",
 r"Vyas, D. A., Eisenstein, L. G., \& Jones, D. S. (2020). Hidden in plain sight: Reconsidering the use of race correction in clinical algorithms. \emph{New England Journal of Medicine, 383}(9), 874--882. \url{https://doi.org/10.1056/NEJMms2004740}",
 r"Vyas, D. A., Jones, D. S., Meadows, A. R., Diouf, K., Nour, N. M., \& Schantz-Dunn, J. (2019). Challenging the use of race in the vaginal birth after cesarean section calculator. \emph{Women's Health Issues, 29}(3), 201--204. \url{https://doi.org/10.1016/j.whi.2019.04.007}",
 r"Wiens, J., Saria, S., Sendak, M., Ghassemi, M., Liu, V. X., Doshi-Velez, F., Jung, K., Heller, K., Kale, D., Saeed, M., Ossorio, P. N., Thadaney-Israni, S., \& Goldenberg, A. (2019). Do no harm: A roadmap for responsible machine learning for health care. \emph{Nature Medicine, 25}(9), 1337--1340. \url{https://doi.org/10.1038/s41591-019-0548-6}",
 r"Wong, A. I., Charpignon, M., Kim, H., Josef, C., de Hond, A. A. H., Fojas, J. J., Tabaie, A., Liu, X., Mireles-Cabodevila, E., Carvalho, L., Kamaleswaran, R., Madushani, R. W. M. A., Adhikari, L., Holder, A. L., Steyerberg, E. W., Buchman, T. G., Lough, M. E., \& Celi, L. A. (2021). Analysis of discrepancies between pulse oximetry and arterial oxygen saturation measurements by race and ethnicity and association with organ dysfunction and mortality. \emph{JAMA Network Open, 4}(11), Article e2131674. \url{https://doi.org/10.1001/jamanetworkopen.2021.31674}",
]
def esc(s):
    return s.replace("&", r"\&").replace("%", r"\%").replace("_", r"\_").replace("#", r"\#")
def paras(l): return "\n\n".join(p if "\\textsuperscript" in p else esc(p) for p in l)
def fix(p): return esc(p).replace("\\\\textsuperscript", "\\textsuperscript") if "\\textsuperscript" in p else esc(p)
def paras(l): return "\n\n".join(fix(p) for p in l)
def block(d): return "\n\n".join(f"\\subsection*{{{k}}}\n" + paras(v) for k, v in d.items())

tex = r"""\documentclass[12pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{graphicx,booktabs,url,setspace,caption,amsmath,float,array}
\usepackage[T1]{fontenc}\usepackage{lmodern}\usepackage[hidelinks]{hyperref}\usepackage{xurl}
\captionsetup{font=small,labelfont=bf,justification=justified}
\setstretch{1.15}
\title{When the Number Is Not Neutral: Bias in Clinical Risk Prediction Tools. A Narrative Review}
\author{Haoxi Hu\thanks{Corresponding author: \href{mailto:hu.haoxi@northeastern.edu}{hu.haoxi@northeastern.edu}}\\[2pt]
\small Khoury College of Computer Sciences and Bouv\'e College of Health Sciences,\\
\small Northeastern University}
\date{}
\begin{document}
\maketitle
\vspace{-2em}
\begin{abstract}
""" + fix(abstract) + r"""
\end{abstract}
\noindent\textbf{Keywords:} algorithmic bias; clinical prediction; health equity; pulse oximetry; eGFR; auditing

\section*{Introduction}
""" + paras(intro) + r"""

\section*{Methods}
""" + paras(methods) + r"""

\section*{How Bias Enters Clinical Risk Tools}
""" + block(mech) + r"""

\section*{Documented Harms}
""" + block(harms) + r"""

\begin{table}[H]
\centering\small
\caption{Main quantified findings from the cases reviewed. Definitions, settings, and groups differ by study, so rows are not directly comparable.}
\resizebox{\linewidth}{!}{%
\begin{tabular}{p{3.4cm}p{5cm}p{8.6cm}}
\toprule
Source & Tool or measure & Reported result \\
\midrule
""" + t1 + r"""
\bottomrule
\end{tabular}%
}
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=\linewidth]{figures/figure1_clinical_algorithm_bias.png}
\caption{""" + caption + r"""}
\end{figure}

\section*{Patterns Across Cases}
""" + paras(patterns) + r"""

\section*{Strengths and Weaknesses of the Evidence}
""" + paras(quality) + r"""

\section*{Auditing and Mitigation}
""" + paras(mitig) + r"""

\section*{Gaps}
""" + paras(gaps) + r"""

\section*{Conclusion}
""" + paras(conclusion) + r"""

\section*{Data and Code Availability}
{\raggedright The extracted figures with their sources, the scripts that produce the figure and this manuscript, and the verification log are available at \url{""" + REPO + r"""}.\par}

\section*{References}
\begingroup\small\setlength{\parindent}{-0.5in}\setlength{\leftskip}{0.5in}\setlength{\parskip}{4pt}
""" + "\n\n".join(refs) + r"""
\endgroup
\end{document}
"""
shutil.copy(os.path.join(OUT, "figure1_clinical_algorithm_bias.png"), os.path.join(TEX, "figures"))
open(os.path.join(TEX, "manuscript.tex"), "w").write(tex)
for _ in range(2):
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "manuscript.tex"], cwd=TEX, capture_output=True, text=True)
print("pdflatex rc", r.returncode, [l for l in r.stdout.splitlines() if l.startswith("!")][:5])
main = [abstract] + intro + methods + sum(mech.values(), []) + sum(harms.values(), []) + patterns + quality + mitig + gaps + conclusion
wc = sum(len(p.replace("\\textsuperscript{2}", "2").split()) for p in main); wca = len(abstract.split())
allp = " ".join(main) + kt
assert "\u2014" not in allp and "---" not in allp
for bad in ("causes ", "caused by", "leads to", "due to the"):
    assert bad not in allp.lower(), bad
assert wc <= 4000
json.dump({"words_main_text_incl_abstract_excl_tables_figures_refs": wc, "words_abstract": wca, "key_takeaway": kt}, open(os.path.join(OUT, "wordcount.json"), "w"), indent=1)
print("main words", wc, "abstract", wca)
