# rnaseq-differential-expression

Differential gene expression analysis on public RNA-seq count data, from raw counts through filtering, model fitting, and interpretation of results.

Self-directed project, built to learn the differential expression workflow end to end and to practice interpreting results rather than only producing them. Written in Python with PyDESeq2.

## Scripts

make_counts.py builds a small synthetic counts table to show the shape PyDESeq2 expects.

run_deseq.py fits the model on that toy table and reports fold changes and adjusted p-values.

deseq_from_csv.py runs the same workflow on the PyDESeq2 synthetic dataset loaded from CSV, including the transpose that RNA-seq count files need.

airway_deseq.py runs the analysis on real data: human airway smooth muscle cells treated with dexamethasone, from Himes et al. 2014, GEO GSE52778. Filters low-count genes, fits the model, and writes a ranked results table.

add_gene_names.py maps Ensembl gene IDs to human gene symbols through the MyGene.info API.

volcano.py draws a volcano plot of fold change against adjusted p-value.

## Notes

Public datasets only. Result CSV files and figures are not committed.

Results are reported as adjusted p-values. Raw p-values are not used for calling significance.

## Requirements

Python 3.9 or newer, with pydeseq2, pandas, numpy, and matplotlib.
