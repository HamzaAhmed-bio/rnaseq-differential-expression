# make_counts.py
# Build a small fake RNA-seq counts table so we can see
# the exact shape pydeseq2 expects.

import pandas as pd

counts = pd.DataFrame(
    {
        "geneA": [100, 110, 95, 400, 420, 390],
        "geneB": [50, 55, 48, 52, 49, 51],
        "geneC": [300, 290, 310, 80, 75, 85],
        "geneD": [20, 18, 22, 19, 21, 20],
    },
    index=["control1", "control2", "control3",
           "treated1", "treated2", "treated3"],
)

metadata = pd.DataFrame(
    {"condition": ["control", "control", "control",
                   "treated", "treated", "treated"]},
    index=counts.index,
)

print("COUNTS")
print(counts)
print()
print("METADATA")
print(metadata)
