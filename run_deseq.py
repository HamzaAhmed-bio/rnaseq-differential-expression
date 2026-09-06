# run_deseq.py
# Feed the counts and metadata into pydeseq2 and get
# fold changes and adjusted p-values for every gene.

import pandas as pd
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

counts = pd.DataFrame(
    {
        "geneA": [60, 110, 135, 250, 420, 540],
        "geneB": [50, 55, 48, 52, 49, 51],
        "geneC": [180, 290, 430, 40, 75, 125],
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

dds = DeseqDataSet(
    counts=counts,
    metadata=metadata,
    design="~condition",
    refit_cooks=True,
)

dds.deseq2()

stats = DeseqStats(dds, contrast=["condition", "treated", "control"])
stats.summary()

print()
print("RESULTS")
print(stats.results_df)
