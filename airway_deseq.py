# airway_deseq.py
# Real RNA-seq: human airway smooth muscle cells, dexamethasone vs untreated.
# Himes et al. 2014, GEO GSE52778.

import pandas as pd
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

BASE = "https://raw.githubusercontent.com/4va/biodatasci/master/data/"

counts = pd.read_csv(BASE + "airway_scaledcounts.csv", index_col=0)
metadata = pd.read_csv(BASE + "airway_metadata.csv", index_col=0)

print("counts as loaded:", counts.shape)
counts = counts.T
print("counts after transpose:", counts.shape)
print()
print(metadata)
print()

# NEW 1: drop genes that are almost never seen
keep = counts.sum(axis=0) >= 10
print("genes before filtering:", counts.shape[1])
counts = counts.loc[:, keep]
print("genes after filtering:", counts.shape[1])
print()

dds = DeseqDataSet(
    counts=counts,
    metadata=metadata,
    design="~dex",
    refit_cooks=True,
)
dds.deseq2()

stats = DeseqStats(dds, contrast=["dex", "treated", "control"])
stats.summary()

res = stats.results_df
res.to_csv("airway_results.csv")

# NEW 2: keep only real hits, sort by strength
hits = res[res["padj"] < 0.05]
hits = hits.sort_values("log2FoldChange", ascending=False)

print()
print("genes tested:", len(res))
print("significant at padj < 0.05:", len(hits))
print()
print("TOP 10 UP")
print(hits.head(10))
print()
print("TOP 10 DOWN")
print(hits.tail(10))
