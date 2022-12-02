# Supplementary material for a usability evaluation of a semantic search for biological datasets

[![DOI](https://zenodo.org/badge/572698150.svg)](https://zenodo.org/badge/latestdoi/572698150)

We conducted a usability evaluation for a semantic dataset search with 20 biodiversity scholars in June and July 2022 in Germany. 
The research aim addressed two objectives:

1. we explored two query inputs (A/B testing) and 
2. we studied two different explanations strategies in the search summary to examine whether users are confused or attracted by presented semantic information such as URIs and ontologies. 

We developed a semantic search over biological datasets with two user interfaces (UI) with different characteristics. The search expands query terms on semantically related terms and allows a search over hierarchy relations. UI 1 (Biodiv 1) provides a category, form-based search input with no information on utilized ontologies. UI 2 (Biodiv 2) offers a classical one input field and in the search summary, it provides links to matched URIs and ontologies. 

Following the TREC guidelines (https://www-nlpir.nist.gov/projects/t9i/spec.html), we setup eight user tasks and surveys with questionnaires to guide users through the evaluation.

* the [analysis](https://github.com/fusion-jena/semantic-search-usability-analysis/tree/main/analysis) folder contains a jupyter notebook to analyse a compiled csv
  * analysis/results16  contains the results for 16 users
  * analysis/results20  contains the results for 20 users
  * scripts to generate the complied csv and further instructions are available under analysis/preprocessing
* [data_corpus_preparation](https://github.com/fusion-jena/semantic-search-usability-analysis/tree/main/data_corpus_preparation) provides various small applications for the preparation and setup of the search index

## Prerequites

Install Python (we developed and tested with version 3.9) and jupyter notebook (https://jupyter.org/). In a command line navigate to the root folder and run

```
jupyter notebook

```

## Data

The survey templates and the original survey results are available at Zenodo: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7388038.svg)](https://doi.org/10.5281/zenodo.7388038)

## License

The code in this project is distributed under the terms of the [GNU LGPL v3.0.](https://www.gnu.org/licenses/lgpl-3.0.en.html)

## Publication
Further information on this study can be obtained from our publication: XXX


