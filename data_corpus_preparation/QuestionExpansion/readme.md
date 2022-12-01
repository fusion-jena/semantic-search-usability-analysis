# Question construction

## Evaluation questions

What data is there for root length?   
What data is there for foraminifera and benthic?
Is there data about the leaf area index and in particular about diversity?
What data is there for Thysanoptera on sunflowers?
Is there data about plant traits influenced by precipitation and grazing?
Where do I find mesopelagic fish of the genus Cyclothone?
How variable is the oxygen concentration (e.g. in unit (mycro)mol/kg) of sea water in the mesopelagic zone(i.e. between 200-1000 m) of the global ocean?
What data exist for invasive grasses, e.g., Poaceae?
What data is in the repository on Ocean acidification and coral bleaching?
What data exist for microbial activities in the groundwater?
What data exist for butterflies on oaks?
What data contains samples from surface water?

## Prerequiste

* local or external terminology service with a SPARQL endpoint, replace the terminology service in 'detectRelations.py'
* python 3.8

## Question expansion

1.) the original annotated questions are typed as annotated keywords combined with AND (+) and OR (|) in "original_questions"

2.) per question create a file with a list of all entities, e.g., query1_entities.txt

<http://purl.obolibrary.org/obo/PPO_0002000>
<http://purl.obolibrary.org/obo/TO_0000387>
<http://purl.obolibrary.org/obo/ENVO_01001363>
<http://purl.obolibrary.org/obo/OBI_0600034>
<http://purl.obolibrary.org/obo/REX_0000182>
<http://purl.obolibrary.org/obo/ECOCORE_00000139>

3.) run 

```
python detectRelations.py -s sparqlDescendantsLabel.sparql -o <pathToExpansionFolder>
```

to obtain all descendants with their labels and synonyms

4.) run

```
python constructQuestionsForEvaluation.py
```

to replace the entities with the descendants and synonyms