# rnaseq-differential-expression

Differential gene expression analysis on public RNA-seq count data, from raw counts through filtering, model fitting, and interpretation of results.

Self-directed project, built to learn the differential expression workflow end to end and to practice interpreting results rather than only producing them.

## Status

Work in progress. The analysis scripts are being cleaned up and added to this repository.

## Scope

Load a public count matrix and its sample metadata.

Filter low-count genes.

Fit the differential expression model and test between conditions with multiple-testing correction.

Export a ranked results table.

## Requirements

Python 3.9 or newer, with PyDESeq2, pandas, and NumPy.

## Notes

Public datasets only.
