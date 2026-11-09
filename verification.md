# Verification: algorithmic bias in clinical risk tools (narrative review)

Main text word count (abstract included; tables, figure, references excluded): **2810** (limit 4,000). Abstract: 285 words.

## Citations (13). Each title, authors, year, journal, volume, pages and DOI matched Crossref (PASS)

| Source | DOI | What was read |
|---|---|---|
| Obermeyer et al. 2019, Science 366:447 | 10.1126/science.aax2342 | abstract |
| Vyas, Eisenstein & Jones 2020, NEJM 383:874 | 10.1056/NEJMms2004740 | Crossref only; no abstract; claims limited to title and as cited by Grobman et al. |
| Inker et al. 2021, NEJM 385:1737 | 10.1056/NEJMoa2102953 | abstract (PMC8822996); 33 authors, first 19 listed per APA |
| Delgado et al. 2022, AJKD 79:268 | 10.1053/j.ajkd.2021.08.003 | abstract incl. recommendations |
| Sjoding et al. 2020, NEJM 383:2477 | 10.1056/NEJMc2029240 | full text (PMC7808260). A correction notice exists (NEJM 2021;385:2496); NOT read, so check figures against the corrected version |
| Wong et al. 2021, JAMA Netw Open 4:e2131674 | 10.1001/jamanetworkopen.2021.31674 | abstract (Europe PMC) |
| Fawzy et al. 2022, JAMA Intern Med 182:730 | 10.1001/jamainternmed.2022.1906 | abstract (Europe PMC); pages 730-738 confirmed in Europe PMC (Crossref lists start page only) |
| Vyas et al. 2019, Women's Health Issues 29:201 | 10.1016/j.whi.2019.04.007 | Crossref only; no abstract; claims limited to title |
| Grobman et al. 2021, AJOG 225:664.e1 | 10.1016/j.ajog.2021.05.021 | full text (PMC8611105) |
| Wiens et al. 2019, Nat Med 25:1337 | 10.1038/s41591-019-0548-6 | abstract |
| Rajkomar et al. 2018, Ann Intern Med 169:866 | 10.7326/M18-1990 | abstract |
| Seyyed-Kalantari et al. 2021, Nat Med 27:2176 | 10.1038/s41591-021-01595-0 | abstract |
| Paulus & Kent 2020, npj Digit Med 3:99 | 10.1038/s41746-020-0304-9 | abstract |

## Figure traceability
43 of 53 extracted values appear in the manuscript text; the others are in the data file only (confidence intervals plotted in Figure 1, etc.).

| key | value | source | DOI | where found | status |
|---|---|---|---|---|---|
| ob_pct_before | 17.7 | Obermeyer et al. 2019 | 10.1126/science.aax2342 | abstract (Black patients receiving extra help at current threshold) | in text |
| ob_pct_after | 46.5 | Obermeyer et al. 2019 | 10.1126/science.aax2342 | abstract (after remedying the disparity) | in text |
| inker_val_studies | 12 | Inker et al. 2021 | 10.1056/NEJMoa2102953 | abstract | in text |
| inker_val_n | 4,050 | Inker et al. 2021 | 10.1056/NEJMoa2102953 | abstract | in text |
| inker_val_black_pct | 14.3 | Inker et al. 2021 | 10.1056/NEJMoa2102953 | abstract | in text |
| inker_cur_black | 3.7 | Inker et al. 2021 | 10.1056/NEJMoa2102953 | abstract | in text |
| inker_cur_black_lo | 1.8 | Inker et al. 2021 | 10.1056/NEJMoa2102953 | abstract 95% CI | data file only |
| inker_cur_black_hi | 5.4 | Inker et al. 2021 | 10.1056/NEJMoa2102953 | abstract 95% CI | data file only |
| inker_cur_nonblack | 0.5 | Inker et al. 2021 | 10.1056/NEJMoa2102953 | abstract | in text |
| inker_cur_nonblack_lo | 0 | Inker et al. 2021 | 10.1056/NEJMoa2102953 | abstract 95% CI | in text |
| inker_cur_nonblack_hi | 0.9 | Inker et al. 2021 | 10.1056/NEJMoa2102953 | abstract 95% CI | data file only |
| inker_norace_adj_black | 7.1 | Inker et al. 2021 | 10.1056/NEJMoa2102953 | abstract (current equation with race term simply dropped) | in text |
| inker_new_black | 3.6 | Inker et al. 2021 | 10.1056/NEJMoa2102953 | abstract | in text |
| inker_new_black_lo | 1.8 | Inker et al. 2021 | 10.1056/NEJMoa2102953 | abstract 95% CI | data file only |
| inker_new_black_hi | 5.5 | Inker et al. 2021 | 10.1056/NEJMoa2102953 | abstract 95% CI | data file only |
| inker_new_nonblack | 3.9 | Inker et al. 2021 | 10.1056/NEJMoa2102953 | abstract | in text |
| inker_new_nonblack_lo | 3.4 | Inker et al. 2021 | 10.1056/NEJMoa2102953 | abstract 95% CI | in text |
| inker_new_nonblack_hi | 4.4 | Inker et al. 2021 | 10.1056/NEJMoa2102953 | abstract 95% CI | data file only |
| inker_within30 | 85 | Inker et al. 2021 | 10.1056/NEJMoa2102953 | abstract (85% or more of eGFRs within 30% of measured GFR for all equations) | in text |
| sj_mich_black | 11.7 | Sjoding et al. 2020 | 10.1056/NEJMc2029240 | PMC7808260 full text (88 of 749) | in text |
| sj_mich_white | 3.6 | Sjoding et al. 2020 | 10.1056/NEJMc2029240 | PMC7808260 full text (99 of 2778) | in text |
| sj_multi_black | 17 | Sjoding et al. 2020 | 10.1056/NEJMc2029240 | PMC7808260 full text (160 of 939) | in text |
| sj_multi_white | 6.2 | Sjoding et al. 2020 | 10.1056/NEJMc2029240 | PMC7808260 full text (546 of 8795) | in text |
| sj_auc_black | 0.84 | Sjoding et al. 2020 | 10.1056/NEJMc2029240 | PMC7808260 full text | in text |
| sj_auc_white | 0.89 | Sjoding et al. 2020 | 10.1056/NEJMc2029240 | PMC7808260 full text | in text |
| sj_pairs_mich | 10,789 | Sjoding et al. 2020 | 10.1056/NEJMc2029240 | PMC7808260 full text | in text |
| sj_pairs_multi | 37,308 | Sjoding et al. 2020 | 10.1056/NEJMc2029240 | PMC7808260 full text | in text |
| sj_hospitals | 178 | Sjoding et al. 2020 | 10.1056/NEJMc2029240 | PMC7808260 full text (ICU patients 2014-2015) | in text |
| wong_n | 87,971 | Wong et al. 2021 | 10.1001/jamanetworkopen.2021.31674 | abstract | in text |
| wong_hidden_all | 5.5 | Wong et al. 2021 | 10.1001/jamanetworkopen.2021.31674 | abstract | data file only |
| wong_hidden_black | 6.8 | Wong et al. 2021 | 10.1001/jamanetworkopen.2021.31674 | abstract | in text |
| wong_hidden_white | 4.9 | Wong et al. 2021 | 10.1001/jamanetworkopen.2021.31674 | abstract | in text |
| wong_hidden_hisp | 6 | Wong et al. 2021 | 10.1001/jamanetworkopen.2021.31674 | abstract | in text |
| wong_hidden_asian | 4.8 | Wong et al. 2021 | 10.1001/jamanetworkopen.2021.31674 | abstract | in text |
| wong_mort_black_hidden | 21.1 | Wong et al. 2021 | 10.1001/jamanetworkopen.2021.31674 | abstract (Black patients with hidden hypoxemia) | in text |
| wong_mort_black_nohidden | 15 | Wong et al. 2021 | 10.1001/jamanetworkopen.2021.31674 | abstract (Black patients without) | in text |
| wong_icus | 382 | Wong et al. 2021 | 10.1001/jamanetworkopen.2021.31674 | abstract | in text |
| fawzy_patients | 7,126 | Fawzy et al. 2022 | 10.1001/jamainternmed.2022.1906 | abstract | data file only |
| fawzy_occ_black | 28.5 | Fawzy et al. 2022 | 10.1001/jamainternmed.2022.1906 | abstract | in text |
| fawzy_occ_white | 17.2 | Fawzy et al. 2022 | 10.1001/jamainternmed.2022.1906 | abstract | in text |
| fawzy_hr_black | 0.71 | Fawzy et al. 2022 | 10.1001/jamainternmed.2022.1906 | abstract (recognition of treatment eligibility vs White) | in text |
| fawzy_hr_lo | 0.63 | Fawzy et al. 2022 | 10.1001/jamainternmed.2022.1906 | abstract 95% CI | in text |
| fawzy_hr_hi | 0.8 | Fawzy et al. 2022 | 10.1001/jamainternmed.2022.1906 | abstract 95% CI | in text |
| fawzy_delay_h | 1 | Fawzy et al. 2022 | 10.1001/jamainternmed.2022.1906 | abstract | in text |
| fawzy_never_n | 451 | Fawzy et al. 2022 | 10.1001/jamainternmed.2022.1906 | abstract | in text |
| fawzy_never_black_pct | 54.8 | Fawzy et al. 2022 | 10.1001/jamainternmed.2022.1906 | abstract | in text |
| gr_n | 11,687 | Grobman et al. 2021 | 10.1016/j.ajog.2021.05.021 | abstract | in text |
| gr_vbac_pct | 74 | Grobman et al. 2021 | 10.1016/j.ajog.2021.05.021 | abstract | in text |
| gr_auc_new | 0.75 | Grobman et al. 2021 | 10.1016/j.ajog.2021.05.021 | abstract | in text |
| gr_auc_old | 0.75 | Grobman et al. 2021 | 10.1016/j.ajog.2021.05.021 | abstract (previous model with race/ethnicity) | in text |
| gr_black_share | 36.3 | Grobman et al. 2021 | 10.1016/j.ajog.2021.05.021 | PMC8611105 full text | in text |
| gr_registry_years | 1999-2002 | Grobman et al. 2021 | 10.1016/j.ajog.2021.05.021 | PMC8611105 full text | data file only |
| wong_hospitals | 215 | Wong et al. 2021 | 10.1001/jamanetworkopen.2021.31674 | abstract | data file only |

## Derived numbers (reviewer's calculations, outputs/results.json)

- ob_ratio_after_vs_before: 2.63
- ob_pp_gain: 28.8
- sj_mich_ratio: 3.25
- sj_multi_ratio: 2.74
- sj_auc_gap: 0.05
- wong_ratio: 1.39
- wong_pp_gap: 1.9
- wong_mort_diff_pp: 6.1
- fawzy_ratio: 1.66
- fawzy_pp_gap: 11.3
- fawzy_hazard_reduction_pct: 29
- egfr_gap_current: 3.2
- egfr_gap_new: -7.5
- egfr_abs_gap_new: 7.5

## Checks and known issues

- Obermeyer ratio 46.5/17.7 = 2.63: PASS (recomputed in analysis.py with assertion).
- Sjoding Michigan 88/749 = 11.7% and 99/2778 = 3.6%; multicenter 160/939 = 17.0% and 546/8795 = 6.2%: PASS (recomputed by hand from the full text counts).
- Wong hidden hypoxemia definition (SpO2 >=88% with SaO2 <88%) and Fawzy occult hypoxemia definition (SaO2 <88% with SpO2 92-96%) confirmed from raw Europe PMC abstract text.
- eGFR: the race-free creatinine equation widened the Black vs non-Black gap in median error (7.5 vs 3.2 mL/min/1.73 m2, reviewer calculation using signed medians). Reported as is.
- No em dashes (asserted in build_paper.py). No causal verbs from a banned list (asserted). Race is described as a recorded label, not a biological construct.
- Items to check by hand: (1) Sjoding correction notice; (2) Vyas 2019 and 2020 and Wiens were not read beyond metadata/abstract; (3) an FDA pulse oximetry statement is attributed only to the Sjoding letter.
- The manuscript covers pulse oximetry by race, not skin tone, because the studies cited recorded race.
