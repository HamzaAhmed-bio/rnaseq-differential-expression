# deseq_from_csv.py
# Load counts and metadata from CSV files instead of hardcoding them.

import pandas as pd
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

DATA = "https://raw.githubusercontent.com/owkin/PyDESeq2/main/datasets/synthetic/"

counts = pd.read_csv(DATA + "test_counts.csv", index_col=0)
metadata = pd.read_csv(DATA + "test_metadata.csv", index_col=0)

print("counts shape as loaded:", counts.shape)

counts = counts.T

print("counts shape after transpose:", counts.shape)
print()
print(metadata.head())
print()

dds = DeseqDataSet(
    counts=counts,
    metadata=metadata,
    design="~condition",
    refit_cooks=True,
)
dds.deseq2()

stats = DeseqStats(dds, contrast=["condition", "B", "A"])
stats.summary()

print()
print("RESULTS")
print(stats.results_df)
