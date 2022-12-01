
# Data corpus preparation

For our evaluation, we utilized various applications and scripts for the download and preparation of the [GFBio](https://www.gfbio.org) metadata corpus.

1.) Metadata files have been downloaded with the code provided in https://github.com/fusion-jena/GFBioMetadata
2.) For the query preparation, we expanded the original search tasks with scripts and instruction provided in the QuestionExpansion folder, a test corpus is provided in GFBioTestCorpus
3.) We utilized the [Biodivtagger](https://github.com/fusion-jena/BiodivTagger) and [OrganismTagger](https://www.semanticsoftware.info/organism-tagger) pipelines based on the [GATE framework](https://github.com/GateNLP) to annotate these metadata files. In order to properly load GFBio metadata files into GATE, a plugin is necessary provided in GFBioDocumentFormat.
4.) For faster annotation and indexing, small thread pipelines are provided in AnnotateGFBioCorpus and ParallelIndexing.
5.) Folder SearchIndex contains the index file for a [GATE Mìmir index](https://github.com/GateNLP/mimir)

## Prerequisites

All JAVA code has been implemented with JAVA 1.8. All Python scripts were developed with Python 3.8
