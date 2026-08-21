# rnaseq-differential-expression

An R/Bioconductor workflow for differential gene-expression analysis on publicly available RNA-seq count data — from raw counts through normalization, differential testing, and visualization.

Built to learn the standard Bioconductor analysis path end to end and to practice interpreting expression results, not just producing them.

## What it does

1. Loads a public count matrix and sample metadata
2. Filters low-count genes
3. Normalizes and fits the differential expression model
4. Tests for differentially expressed genes between conditions, with multiple-testing correction
5. Visualizes results — PCA, MA plot, volcano plot, heatmap of top genes
6. Exports a ranked results table

## Requirements

R 4.2+ with `DESeq2`, `SummarizedExperiment`, `ggplot2`, `pheatmap`, `dplyr`.

## Notes

Uses publicly available datasets only.
