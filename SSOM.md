# Simple Standard for Sharing Ontology Mappings (SSSOM)

Working Draft, Updated: 15 April 2020

Feedback: [Issue tracker](issues)

_Editors:_

- TBD
​
_Contributors:_

- Nicolas Matentzoglu (EMBL-EBI)
- Chris Mungall (LBL)
- Ernesto Jimenez-Ruiz (City, University of London)
- John Graybeal (Stanford)


## Abstract
The goal of the Simple Standard for Sharing Ontology Mappings (SSSOM) is to provide a minimal and standard set of elements for the dissemination of mappings between ontology terms to ensure a reliable interpretation of generated mappings and enable sharing between people and applications. We will provide two serialisations, aimed at different communities: a TSV serialisation which is aimed at the wider bioinformatics community, and an RDF serialisation that is aimed at the Knowledge Graph/Semantic Web community. We will define and unambiguous translation between the two, which enables, for example, the use of shape validation also for the TSV format. Apart from the format, the main difference between the two serialisation is that we use CURIE syntax [CURIE](https://www.w3.org/TR/curie/) to denote entities in the TSV, and IRIs in the RDF based serialisation.

## Some notes on the standardisation process

There are a few hurdles towards a standard approach, including:

1. Using IRIs vs CURIEs to denote mapped terms. This is essentially a question of the target user group.
2. Using controlled vocabularies for the mapping types
3. Versioning - source versioning vs versioning of mappings
4. Serialisation (CSV, TSV, RDF, JSON) 

Some opinions will probably not be reconciled, but we will do the best we can to make SSSOM useful to a wide community. Note this is a public copy of the editors’ draft. It is provided for discussion only and may change at any moment. Do not cite this document other than as work in progress.

## Table of Content

* The SSSOM Method Vocabulary
* Common Mapping Predicates
* SSSOM Metadata Elements
  * Data Dictionary of Required Elements (SSSOM Core)
  * Data Dictionary of Optional Elements (SSSOM Extended)
* Serialisation 
  * CSV
	* RDF

## The SSSOM Match Type Vocabulary

The SSSOM Vocabulary is a Controlled Vocabulary (CV) for representing the method by which a mapping was produced.

| Term | Label | Description | Parent |
| ---- | ----- | ----------- | ------ |
| *SSSOM:0000001* | SSSOM Code | Root level term that groups all OMTs. Should not be used for annotation. | |
| *SSSOM:0000002* | Match Type | A mapping that fully or partially relies on matching lexical data such as labels or synonyms. | SSSOM:0000001 |
| *SSSOM:0000003* | Equivalence Match | A mapping that fully or partially relies on matching lexical data such as labels or synonyms. | SSSOM:0000001 |
| *SSSOM:0000021* | Label Exact Match | Exact match on the label of the terms. | SSSOM:0000002 |
| *SSSOM:0000021* | Label-Exact Synonym Exact Match | Exact match on the label of the terms. | SSSOM:0000002 |
| *SSSOM:0000021* | Exact Synonym-Label Exact Match | Exact match on the label of the terms. | SSSOM:0000002 |
| *SSSOM:0000022* | Exact Synonym Exact Match | Exact match on the exact synonym property of a term. | SSSOM:0000002 |
| *SSSOM:0000023* | Logical Equivalence Match | Exact match on the logical definition of a term. | SSSOM:0000002 |
| *SSSOM:0000025* | Human Curated Equivalence Match | Exact match based on human curation. |  SSSOM:0000002 |
| *SSSOM:0000026* | Complex Equivalence Match | Exact match based on the use of a tool that combines multiple techniques for matching. | SSSOM:0000002 |
| *SSSOM:0000007* | Related Match | A mapping that fully or partially relies on matching lexical data such as labels or synonyms. |  SSSOM:0000001 |
| *SSSOM:0000008* | Logical Similarity Match | Related match on the semantic similarity between two terms. |  SSSOM:0000007 |
| *SSSOM:0000009* | Complex Related Match | Related match based on the use of a tool that combines multiple techniques for matching. |   SSSOM:0000007 |
| *SSSOM:0000010* | Term Match | | SSSOM:0000001 |
| *SSSOM:0000011* | Class Match | | SSSOM:0000010 |
| *SSSOM:0000012* | Object Property Match | | SSSOM:0000010 |
| *SSSOM:0000013* | Individual Match | | SSSOM:0000010 |
| *SSSOM:0000020* | Transformation | | SSSOM:0000001 |
| *SSSOM:0000020* | Stemming | | SSSOM:0000001 |


## Common Mapping Predicates

The use of predicates is not restricted by SSSOM, but for maximum re-use, we recommend the relationships below

_Sources:_

- https://www.bioontology.org/wiki/BioPortal_Mappings
- TBD

| Predicate | Description | Example |
| ---------- | ----------- | ------- |
| owl:sameAs | Two instances are the same.  |  |
| owl:equivalentTo | Two classes are the same. |  |
| skos:relatedMatch | Two terms are related in some |  |
| skos:closeMatch |  |  |
| skos:exactMatch |  |  |
| oio:database_cross_reference |  |  |
| rdfs:seeAlso |  |  |
| RO:? | Any Relation in the Relation Ontology (RO). | BFO:0000050 |

## SSSOM Metadata Elements

### Data Dictionary of Required Elements (SSSOM Core)

Note that there is disagreement whether the primary id should be a curie or an IRI (CURIE camp: CJM, IRI camp:JG, Undecided: NM).

| Element ID | Description | Example |
| ---------- | ----------- | ------- |
| x_id | The ID of subject of the mapping in [CURIE](https://www.w3.org/TR/curie/) syntax | HP:0009894 |
| predicate | The ID of the predicate or relation that relates the subject and object of this match in [CURIE](https://www.w3.org/TR/curie/) syntax | owl:EquivalentTo |
| y_id | The ID of object of the mapping in [CURIE](https://www.w3.org/TR/curie/) syntax | MP:0000019 |
| x_source | Version IRI of ontology source for the x term | http://purl.obolibrary.org/obo/hp/releases/2020-03-27/hp-base.owl |
| y_source | Version IRI of ontology source for the y term | http://purl.obolibrary.org/obo/mp/releases/2020-04-14/mp-base.owl |
| match_type | Tuple of IDs from  SSSOM Vocabulary | SSSOM:0000004, SSSOM:0000011 |
| creator | IRI of person or group responsible for the mapping. | https://orcid.org/0000-0002-7356-1779 |

### Data Dictionary of Optional Elements (SSSOM Extended)

| Element ID | Description | Example |
| ---------- | ----------- | ------- |
| x_label | The label of subject of the mapping | Thickened ears |
| y_label | The label of subject of the mapping | thick ears |
| predicate_label | The label of the predicate/relation of the mapping | EquivalentTo |
| tool | A reference to the tool that was used to generated the mapping | https://github.com/ernestojimenezruiz/logmap-matcher |
| date | The date the mapping was computed | 2020-02-29 | 
| confidence | A score between 0 and 1 to denote the confidence that the match is of type 'method' | 0.3 |

### Not included yet

- source_type
- source_subtype
- x_definition / y_definition

## Serialisation

### CSV:

_Notes:_

- No prescribed column order
- ROBOT implementation: https://github.com/ontodev/robot/issues/312
- Check http://alignapi.gforge.inria.fr/format.html