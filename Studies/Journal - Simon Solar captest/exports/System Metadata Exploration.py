#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import re
from collections import defaultdict

myfile = r'C:\Users\sayala\Desktop\delete_9069_system_metadata.json'
with open(myfile, "r") as f:
    data = json.load(f)

metrics = data["Metrics"]

combiner_strings = defaultdict(set)

for key, sensor in metrics.items():

    sensor_name = sensor.get("sensor_name", "")

    match = re.search(
        r"Combiner DC Input_(\d+)\.(\d+)\.(\d+)_DC CURRENT STRING (\d+)",
        sensor_name
    )

    if match:
        group = int(match.group(1))
        combiner = int(match.group(2))
        string = int(match.group(3))

        combiner_id = (group, combiner)

        combiner_strings[combiner_id].add(string)


print("Number of combiner boxes:", len(combiner_strings))

print("\nStrings per combiner:")

for (group, combiner), strings in sorted(combiner_strings.items()):

    strings = sorted(strings)

    print(
        f"{group:02d}.{combiner:02d}: "
        f"{len(strings)} strings "
        f"(strings {min(strings):02d}-{max(strings):02d})"
    )


# In[2]:


all_strings = set()

for key, sensor in metrics.items():

    sensor_name = sensor.get("sensor_name", "")

    match = re.search(
        r"Combiner DC Input_(\d+)\.(\d+)\.(\d+)_DC CURRENT STRING",
        sensor_name
    )

    if match:
        group = int(match.group(1))
        combiner = int(match.group(2))
        string = int(match.group(3))

        # Full identifier uniquely identifies a physical string
        all_strings.add((group, combiner, string))

print("Total number of strings:", len(all_strings))


# In[3]:


# Collect combiner/string information
by_inverter = defaultdict(lambda: {
    "combiners": set(),
    "strings": set()
})

pattern = re.compile(
    r"Combiner DC Input_(\d+)\.(\d+)\.(\d+)_DC CURRENT STRING"
)

for sensor in data["Metrics"].values():

    name = sensor.get("sensor_name", "")
    match = pattern.search(name)

    if match:
        inverter = int(match.group(1))
        combiner = int(match.group(2))
        string = int(match.group(3))

        by_inverter[inverter]["combiners"].add(combiner)
        by_inverter[inverter]["strings"].add((combiner, string))


# Print comparison
print(
    f"{'Inv':>4} {'Combiners':>10} {'Measured strings':>18} "
    f"{'Metadata strings':>17}"
)
print("-" * 55)

for inverter_num in sorted(by_inverter):

    # 01 corresponds to "Inverter 0", 02 to "Inverter 1", etc.
    inverter_metadata = data["Inverters"].get(
        f"Inverter {inverter_num - 1}", {}
    )

    metadata_strings = inverter_metadata.get("num_strings", "NA")

    n_combiners = len(by_inverter[inverter_num]["combiners"])
    n_strings = len(by_inverter[inverter_num]["strings"])

    print(
        f"{inverter_num:>4} "
        f"{n_combiners:>10} "
        f"{n_strings:>18} "
        f"{metadata_strings:>17}"
    )


# In[4]:


for inverter_name, inverter in data["Inverters"].items():
    if "AC capacity(kW)" in inverter:
        print(
            inverter_name,
            inverter.get("name"),
            inverter["AC capacity(kW)"]
        )


# In[5]:


for inverter_name, inverter in data["Inverters"].items():
    print("\n", inverter_name)
    for key, value in inverter.items():
        print(f"  {key}: {value}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




