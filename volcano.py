# volcano.py
# Volcano plot: fold change against significance.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

res = pd.read_csv("airway_results.csv", index_col=0)

print("rows loaded:", len(res))
res = res.dropna(subset=["padj", "log2FoldChange"])
print("rows after dropping missing padj:", len(res))

x = res["log2FoldChange"]
y = -np.log10(res["padj"])

hit = (res["padj"] < 0.05) & (abs(res["log2FoldChange"]) > 1)
print("genes passing both cutoffs:", hit.sum())

plt.figure(figsize=(8, 6))

plt.scatter(x[~hit], y[~hit], s=4, color="lightgrey")
plt.scatter(x[hit], y[hit], s=4, color="crimson")

plt.axhline(-np.log10(0.05), color="black", linewidth=0.6, linestyle="--")
plt.axvline(1, color="black", linewidth=0.6, linestyle="--")
plt.axvline(-1, color="black", linewidth=0.6, linestyle="--")

plt.xlabel("log2 fold change (dexamethasone vs control)")
plt.ylabel("-log10 adjusted p-value")
plt.title("Airway smooth muscle: response to dexamethasone")

plt.savefig("volcano.png", dpi=150, bbox_inches="tight")
print("saved volcano.png")

plt.show()
