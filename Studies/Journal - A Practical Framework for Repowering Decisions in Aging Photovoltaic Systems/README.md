# Study-Specific Modeling Files: PV Repowering Case Studies

This folder contains the modeling files, outputs, and plotting scripts used to generate the results presented in the study:

> *A Practical Framework for Repowering Decisions in Aging Photovoltaic Systems*

The materials here support the **residential, commercial, and second-life (reuse) case studies** discussed in the paper and associated Supporting Information.

---

## Folder Structure and Contents

### SAM Model Files (`.sam`)
These files implement the financial and performance models used in each case study.

- **01 - Residential PVWatts sweep cases.sam**  
  Residential reroofing / repowering analysis with parametric sweeps over system size and remaining lifetime.

- **02 - Commercial cases Colorado.sam**  
  Commercial rooftop repowering pathways modeled using Colorado electricity rates and assumptions.

- **03 - Commercial cases California.sam**  
  Commercial rooftop repowering pathways modeled using California electricity rates to capture high-rate sensitivity.

- **04 - 2nd life owner_resi_parametrics.sam**  
  Residential second-life (reuse recipient) analysis with parametric sweeps over remaining lifetime and BOS costs.

- **05 - 2nd life owner school_parametrics.sam**  
  Institutional (school-scale) second-life analysis evaluating new-build versus reused-module systems under multiple financing structures.

---

### Processed Output Data (`.csv`)
These files contain results exported from SAM and used to generate figures and tables in the manuscript.

- **01_Resi_SystemSize_vs_NPV.csv**  
  Residential breakeven analysis: NPV as a function of original system size.

- **01b_Resi_SystemSize_vs_PaybackPeriod.csv**  
  Residential payback time results corresponding to the same parametric sweep.

- **03_npv_heatmap_variable_cost.csv**  
  Parametric results used to generate the residential NPV heatmap (system size vs. remaining lifetime vs. reinstall cost).

- **04_2nd_life_npv_no_itc.csv**  
  Second-life residential NPV results assuming no ITC eligibility for reused modules.

---

### Analysis and Plotting

- **Paper_plots.ipynb**  
  Jupyter notebook used to generate figures included in the manuscript and Supporting Information.  
  This notebook reads the CSV outputs listed above and produces the final plots.

- **exports/**  
  Contains Python-script exports of the Jupyter notebook for users who prefer a non-notebook workflow or batch execution.

---

## Relationship to the Manuscript

- Figures and tables in the paper are generated directly from the CSV outputs and plotting scripts in this folder.
- Cost assumptions, lifetimes, and financing structures implemented in the SAM files correspond to values described in the Methods section.
- These files are intended to support **reproducibility and adaptation** of the analysis to other sites or scenarios.

---

## How to Use

The System Advisor Model (SAM) (\url{https://sam.nrel.gov/}) is an open-source techno-economic modeling platform developed by the National Renewable Energy Laboratory (NREL). With the files provided for SAM, users may:
- Open `.sam` files in NLR’s [System Advisor Model (SAM)](https://sam.nrel.gov/) to explore or modify assumptions
- Adjust electricity rates, financing terms, or system sizes to reflect local conditions
- Re-run parametric sweeps and regenerate figures using `Paper_plots.ipynb`

---

## Python Environment (for plotting only)

Plots in `Paper_plots.ipynb` require the repository Python environment.

From the repo root:

```bash
pip install -r requirements.txt
```

---

## Disclaimer

These models are screening-level tools intended for comparative analysis.  
Actual repowering decisions depend on site-specific engineering, permitting, contractual, and regulatory constraints not fully captured here.

---

## Citation

If you use materials from this folder, please cite the associated publication and reference the System Advisor Model (SAM) and other tools as described in the manuscript.