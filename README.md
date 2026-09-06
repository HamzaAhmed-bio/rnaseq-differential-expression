# rnaseq-differential-expression

Differential gene expression analysis on public RNA-seq count data.

The workflow covers the full path from a raw count matrix through low-count filtering, model fitting, multiple-testing correction, and visualization of results. It runs first on synthetic data for validation, then on a published dataset of human airway smooth muscle cells treated with dexamethasone.

Built to understand each stage of the analysis and the interpretation of its output, rather than to produce results alone.

## Usage

The scripts progress from a small synthetic count table to the published dataset. Result tables and figures are generated locally and are not committed.

## Requirements

Python 3.9 or newer, with pydeseq2, pandas, numpy, and matplotlib.
