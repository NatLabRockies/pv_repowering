#!/usr/bin/env python
# coding: utf-8

# In[41]:


import numpy as np
import matplotlib.pyplot as plt

years = np.arange(26)

# After tax NPV
do_nothing = np.array([
    -13.56, -4.42, -2.44, -1.26, -0.56, 0.05, 0.36, 0.38, 0.06, -0.37,
    -0.84, -1.35, -1.42, -1.12, -0.86, -0.65, -0.47, -0.34, -0.23, -0.14,
    -0.08, -0.04, -0.01, -0.01, -0.01, 0.05
])

repair = np.array([
    -13.56, -4.42, -2.44, -1.26, -0.56, 0.05, 0.36, 0.38, 0.06, -0.37,
    -0.84, -2.29, -2.75, -2.23, -1.76, -1.35, -1.00, -0.69, -0.43, -0.20,
    -0.01, 0.15, 0.29, 0.40, 0.50, 0.65
])

decommission = np.array([
    -13.56, -4.42, -2.44, -1.26, -0.56, 0.05, 0.36, 0.38, 0.06, -0.37,
    -0.84, -2.54, -2.94, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
    0.00, 0.00, 0.00, 0.00, 0.00, 0.00
])

repower = np.array([
    -13.56, -4.42, -2.44, -1.26, -0.56, 0.05, 0.36, 0.38, 0.06, -0.37,
    -0.84, -9.74, -13.33, -12.44, -11.63, -10.89, -10.21, -9.60, -9.04,
    -8.52, -8.06, -7.63, -7.24, -6.89, -6.57, -6.20
])


# In[43]:


import numpy as np
import matplotlib.pyplot as plt

# Assumes these are already defined:
# years
# do_nothing
# repair
# decommission
# repower

observed_end = 10
scenario_start = 10
decom_year = 12

colors = {
    "Observed": "#333333",
    "Do nothing": "#156082",
    "Repair": "#E97132",
    "Decommission": "#196B24",
    "Repower": "#0F9ED5",
}

fig, ax = plt.subplots(figsize=(3.5, 2.4))

# -----------------------------
# Observed-period background
# Years 0–10
# -----------------------------
ax.axvspan(
    -0.5,
    10.5,
    color="0.9",
    alpha=0.5,
    zorder=0
)

# -----------------------------
# Observed trajectory
# Years 0–10
# -----------------------------
ax.plot(
    years[:observed_end + 1],
    do_nothing[:observed_end + 1],
    color=colors["Observed"],
    lw=2.0,
    label="_nolegend_",
    zorder=5
)

# -----------------------------
# Scenario trajectories
# Start at Year 10 so all
# scenarios connect continuously
# and diverge at Year 11
# -----------------------------
ax.plot(
    years[scenario_start:],
    do_nothing[scenario_start:],
    color=colors["Do nothing"],
    lw=1.8,
    label="Do nothing",
    zorder=3
)

ax.plot(
    years[scenario_start:],
    repair[scenario_start:],
    color=colors["Repair"],
    lw=1.8,
    label="Repair",
    zorder=3
)

ax.plot(
    years[scenario_start:],
    repower[scenario_start:],
    color=colors["Repower"],
    lw=1.8,
    label="Repower",
    zorder=3
)

# Decommission stops at Year 12
# and is plotted on top
ax.plot(
    years[scenario_start:decom_year + 1],
    decommission[scenario_start:decom_year + 1],
    color=colors["Decommission"],
    lw=2.1,
    label="Decommission",
    zorder=6
)

# -----------------------------
# Reference line
# -----------------------------
ax.axhline(
    0,
    color="0.35",
    lw=0.8,
    zorder=1
)

# Optional boundary between
# observed and scenario periods
ax.axvline(
    10.5,
    color="0.55",
    lw=0.7,
    ls=":",
    zorder=1
)

# -----------------------------
# Axes
# -----------------------------
ax.set_xlabel("Year")
ax.set_ylabel("Cumulative NPV ($M)")

ax.set_xlim(0, 25)
ax.set_ylim(-15, 2)

ax.set_xticks(np.arange(0, 26, 5))

# -----------------------------
# Grid
# -----------------------------
ax.grid(
    axis="y",
    color="0.85",
    linewidth=0.7,
    zorder=0
)

# -----------------------------
# Period labels
# -----------------------------
ymin, ymax = ax.get_ylim()
y_text = ymin + 0.6

ax.text(
    5,
    y_text,
    "Observed period",
    ha="center",
    va="bottom",
    fontsize=7
)

ax.text(
    18,
    y_text,
    "Scenario period",
    ha="center",
    va="bottom",
    fontsize=7
)

# -----------------------------
# Legend
# -----------------------------
ax.legend(
    frameon=False,
    fontsize=8,
    ncol=2,
    loc="lower center",
    bbox_to_anchor=(0.5, 1.01)
)

# -----------------------------
# Clean frame
# -----------------------------
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.tight_layout()

plt.savefig(
    "cumulative_npv.png",
    dpi=300,
    bbox_inches="tight"
)


plt.savefig(
    "cumulative_npv.pdf",
    bbox_inches="tight"
)

plt.savefig(
    "cumulative_npv.png",
    dpi=600,
    bbox_inches="tight"
)

plt.show()


# In[35]:


years = np.arange(26)

# ANNUAL CASH FLOW
do_nothing = np.array([
    -13.56, 9.96, 2.36, 1.53, 0.99, 0.94, 0.52, 0.03, -0.62, -0.95,
    -1.13, -1.32, -0.21, 0.94, 0.86, 0.79, 0.70, 0.61, 0.52, 0.44,
    0.35, 0.26, 0.16, 0.07, -0.03, 0.56
])

repair = np.array([
    -13.56, 9.96, 2.36, 1.53, 0.99, 0.94, 0.52, 0.03, -0.62, -0.95,
    -1.13, -3.75, -1.33, 1.64, 1.57, 1.50, 1.41, 1.33, 1.25, 1.18,
    1.10, 1.01, 0.92, 0.84, 0.75, 1.34
])

decommission = np.array([
    -13.56, 9.96, 2.36, 1.53, 0.99, 0.94, 0.52, 0.03, -0.62, -0.95,
    -1.13, -4.41, -1.13
])

repower = np.array([
    -13.56, 9.96, 2.36, 1.53, 0.99, 0.94, 0.52, 0.03, -0.62, -0.95,
    -1.13, -23.10, -10.16, 2.74, 2.73, 2.73, 2.70, 2.68, 2.67, 2.66,
    2.65, 2.63, 2.61, 2.60, 2.58, 3.24
])


# In[39]:


import numpy as np
import matplotlib.pyplot as plt

# Assumes these are already defined:
# years
# do_nothing
# repair
# decommission
# repower

observed_end = 10
scenario_start = 11
decom_year = 12

colors = {
    "Observed": "#333333",
    "Do nothing": "#156082",
    "Repair": "#E97132",
    "Decommission": "#196B24",
    "Repower": "#0F9ED5",
}

# --------------------------------------------------
# Custom x spacing
# Compress observed period, expand scenario period
# --------------------------------------------------
obs_spacing = 0.55
scen_spacing = 1.00
gap = 0.75

observed_years = years[:observed_end + 1]          # 0..10
scenario_years = years[scenario_start:]            # 11..25
decom_years = years[scenario_start:decom_year + 1] # 11..12

x_obs = np.arange(len(observed_years)) * obs_spacing
x_scen_start = x_obs[-1] + gap
x_scen = x_scen_start + np.arange(len(scenario_years)) * scen_spacing

# Helper to map a year to plotted x-position
def year_to_x(y):
    if y <= observed_end:
        return y * obs_spacing
    else:
        return x_scen_start + (y - scenario_start) * scen_spacing

fig, ax = plt.subplots(figsize=(3.5, 2.2))

# --------------------------------------------------
# Shade observed period
# --------------------------------------------------
ax.axvspan(
    x_obs[0] - 0.35,
    x_obs[-1] + 0.35,
    color="0.9",
    alpha=0.5,
    zorder=0
)

# --------------------------------------------------
# Observed bars
# --------------------------------------------------
ax.bar(
    x_obs,
    do_nothing[:observed_end + 1],
    width=0.38,
    color=colors["Observed"],
    label="_nolegend_",
    zorder=3
)

# --------------------------------------------------
# Scenario grouped bars
# --------------------------------------------------
width = 0.18

ax.bar(
    x_scen - 1.5 * width,
    do_nothing[scenario_start:],
    width=width,
    color=colors["Do nothing"],
    label="Do nothing",
    zorder=3
)

ax.bar(
    x_scen - 0.5 * width,
    repair[scenario_start:],
    width=width,
    color=colors["Repair"],
    label="Repair",
    zorder=3
)

ax.bar(
    x_scen + 1.5 * width,
    repower[scenario_start:],
    width=width,
    color=colors["Repower"],
    label="Repower",
    zorder=3
)

# Decommission only through year 12
x_decom = x_scen[:len(decom_years)]

ax.bar(
    x_decom + 0.5 * width,
    decommission[scenario_start:decom_year + 1],
    width=width,
    color=colors["Decommission"],
    label="Decommission",
    zorder=4
)

# --------------------------------------------------
# Reference lines
# --------------------------------------------------
ax.axhline(
    0,
    color="0.35",
    lw=0.8,
    zorder=2
)

# Boundary between periods
boundary_x = 0.5 * (x_obs[-1] + x_scen[0])
ax.axvline(
    boundary_x,
    color="0.55",
    lw=0.7,
    ls=":",
    zorder=1
)

# --------------------------------------------------
# Axes
# --------------------------------------------------
ax.set_ylabel("Annual cash flow ($M)")
ax.set_xlabel("Year")

ax.set_ylim(-26, 12)
ax.set_xlim(x_obs[0] - 0.5, x_scen[-1] + 0.8)

# Put ticks at real years, mapped to compressed positions
tick_years = [0, 5, 10, 15, 20, 25]
tick_positions = [year_to_x(y) for y in tick_years]
ax.set_xticks(tick_positions)
ax.set_xticklabels([str(y) for y in tick_years])

# --------------------------------------------------
# Grid
# --------------------------------------------------
ax.grid(
    axis="y",
    color="0.85",
    linewidth=0.7,
    zorder=0
)

# --------------------------------------------------
# Period labels
# --------------------------------------------------
ymin, ymax = ax.get_ylim()
y_text = ymin + 0.8

ax.text(
    0.5 * (x_obs[0] + x_obs[-1]),
    y_text,
    "Observed period",
    ha="center",
    va="bottom",
    fontsize=7
)

ax.text(
    0.5 * (x_scen[0] + x_scen[-1]),
    y_text,
    "Scenario period",
    ha="center",
    va="bottom",
    fontsize=7
)

# --------------------------------------------------
# Legend
# --------------------------------------------------
ax.legend(
    frameon=False,
    fontsize=8,
    ncol=2,
    loc="lower center",
    bbox_to_anchor=(0.5, 1.01),
    columnspacing=1.2,
    handlelength=2.0
)

# --------------------------------------------------
# Clean frame
# --------------------------------------------------
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.tight_layout()

# --------------------------------------------------
# Save high quality
# --------------------------------------------------
plt.savefig("annual_cashflow.pdf", bbox_inches="tight")
plt.savefig("annual_cashflow.png", dpi=600, bbox_inches="tight")


fig.savefig("annual_cashflow.pdf", bbox_inches="tight")
fig.savefig("annual_cashflow.png", dpi=600, bbox_inches="tight")
plt.show()


# In[ ]:




