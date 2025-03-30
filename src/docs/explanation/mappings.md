# What is a mapping?

The word "mapping" is pretty
overloaded in practice: for some people, it simply means "a correspondence of one term 
to another equivalent or near equivalent term." 
But even here, there is little understanding to what a "term" is in this sentence, 
or what "almost equivalent" means - and, there are many different kinds of mappings used in practice that are not "equivalent" at all. In its very essence, an individual mapping maps one information entity, i.e. a _representation of a real world entity_, to another information entity - how, and what these strings could be, will be the subject of the following section.

In the following, we consider an **information entity** a *sequence of characters which has a well defined relationship to some thing in the real world*, for example:
- an ontology id like HP:0004934 corresponds to the concept of "Vascular calcification" in the real world. Note that HP:0004934 is annotated with the `rdfs:label` "Vascular calcification". 
The label itself is not necessarily a term - it could change, for example to "Abnormal calcification of the vasculature", and still retain the same meaning.
- "Vascular calcification" may be a term in my controlled vocabulary which I understand to correspond to that respective disease (not all controlled vocabularies have IDs for their terms). 
This happens for example in clinical data models that do not use formal identifiers to refer to the values of slots in their data model, like "MARRIED" in /datamodel/marital_status.
- Examples of terms: 
  - IDs of classes in an ontology
  - elements of a clinical value set
  - codes of clinical terminologies such as [Z63.1](https://www.icd10data.com/ICD10CM/Codes/Z00-Z99/Z55-Z65/Z63-/Z63.1)
- TLDR: terms correspond to things in the world and that correspondence is not subject to change. 
Labels can change without changing the meaning of a term.

## An attempt at a practical categorisation

In our experience, there are roughly four kinds of mappings:

- _string-string_: Relating one string, or label, to another string, or label. Understanding such mappings is fundamental to understanding all the other kinds of mappings.
- _string-term_: Relating a specific string or "label" to their corresponding term in a terminology or ontology. We usually refer to these as synonyms, but there may be other words used in this case.
- _term-term_: Relating a term, for example a class in an ontology, to another term. This is what most people in the ontology domain would understand when thy hear "ontology mappings".
- _complex mappings_: Relating two sets of terms. These are the rarest and most complicated kinds of mappings, as they related for example two phenotypic profiles (sets of phenotypes) with each other. We will discuss some more examples in a future lesson.

In some ways, these four kinds of mappings can be very different. We do believe, however, that there are enough important commonalities such as common features, widely overlapping use cases and overlapping toolkits to consider them together. In the following, we will discuss these in more detail, including important features of mappings and useful tools.

### Important features of mappings

Mappings have historically been neglected as second-class citizens in the medical terminology and ontology worlds -
the metadata is insufficient to allow for precise analyses and clinical decision support, they are frequently stale and out of date, etc. The question "Where can I find the canonical mappings between X and Y"? is often shrugged off and developers are pointed to aggregators such as [OxO](https://www.ebi.ac.uk/spot/oxo/) or [UMLS](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/mapping_projects/index.html) which combine manually curated mappings with automated ones causing ["mapping hairballs"](#How-to-solve-the-problem-of-mapping-hairballs).

There are many important metadata elements to consider, but the ones that are by far the most important to consider one way or another are:

- _Precision_: Is the mapping exact, broad or merely closely related?
- _Confidence_: Do I trust the mapping? Was is done manually by an expert in my domain, or by an algorithm?
- _Source version_: Which version of the term (or its corresponding ontology) was mapped? Is there a newer mapping which has a more suitable match for my term?

Whenever you handle mappings (either create, or reuse), make sure you are keenly aware of at least these three metrics, and capture them. You may even want to consider using a proper mapping model like the [Simple Shared Standard for Ontology Mappings (SSSOM)](https://github.com/mapping-commons/SSSOM/blob/master/SSSOM.md) which will make your mappings FAIR and reusable.

### String-string mappings
String-string mappings are mappings that relate two strings. The task of matching two strings is ubiquitous for example in database search fields (where a user search string needs to be mapped to some strings in a database). Most, if not all effective ontology matching techniques will employ some form of string-string matching. For example, to match simple variations of labels such as "abnormal heart" and "heart abnormality", various techniques such as [Stemming](https://en.wikipedia.org/wiki/Stemming) and [bag of words](https://en.wikipedia.org/wiki/Bag-of-words_model#:~:text=The%20bag%2Dof%2Dwords%20model,word%20order%20but%20keeping%20multiplicity.) can be employed effectively. Other techniques such as edit-distance or Levenshtein can be used to quantify the similarity of two strings, which can provide useful insights into mapping candidates.

### String-term mappings / synonyms
String-term mappings relate a specific string or "label" to their corresponding term in a terminology or ontology. Here, we refer to these as "synonyms", but there may be other cases for string-term mappings beyond synonymy.

There are a lot of use cases for synonyms so we will name just a few here that are relevant to typical workflows of Semantic Engineers in the life sciences. 

[Thesauri](https://en.wikipedia.org/wiki/Thesaurus) are reference tools for finding synonyms of terms. Modern ontologies often include very rich thesauri, with some ontologies like Mondo capturing more than 70,000 exact and 35,000 related synonyms. They can provide a huge boost to traditional NLP pipelines by providing synonyms that can be used for both Named Entity Recognition and Entity Resolution. Some insight on how, for example, Uberon was used to boost text mining can be found [here](https://github.com/obophenotype/uberon/wiki/Using-uberon-for-text-mining).

### Term-term mappings / ontology mappings
Term-term mappings relate a term, for example a class in an ontology, to another term, usually from another ontology or database. The term-term case of mappings is what most people in the ontology domain would understand when they hear "ontology mappings". This is also what most people understand when they here "Entity Resolution" in the database world - the task of determining whether, in essence, two rows in a database correspond to the same thing (as an example of a tool doing ER see [deepmatcher](https://github.com/anhaidgroup/deepmatcher), or [py-entitymatcher](https://pypi.org/project/py-entitymatching/)). For a list standard entity matching toolkit outside the ontology sphere see [here](https://www.biggorilla.org/software_cat/entity-matching/index.html). 

### Further reading
- A great overview can be found in ["Tackling the challenges of matching biomedical ontologies" (Faria et al 2018)](https://jbiomedsem.biomedcentral.com/articles/10.1186/s13326-017-0170-9)
- A yearly competition of ontology matching systems is held by the [Ontology Alignment Evaluation Initiative (OAEI)](https://oaei.ontologymatching.org/). The challenge [results](http://oaei.ontologymatching.org/2020/results/) are a useful guide to identifying systems for matching you may want to try.


## Some examples of domain-specific mapping of importance to the biomedical domain

### Phenotype ontology mappings
Mapping phenotypes across species holds great promise for leveraging the knowledge generated by Model Organism Database communities (MODs) for understanding human disease. There is a lot of work happening at the moment (2021) to provide standard mappings between species specific phenotype ontologies to drive translational research ([example](https://github.com/mapping-commons/mh_mapping_initiative/tree/master/mappings)). Tools such as [Exomiser](https://github.com/exomiser/Exomiser) leverage such mappings to perform clinical diagnostic tasks such as variant prioritisation. Another app you can try out that leverages cross-species mappings is the Monarch Initiatives [Phenotype Profile Search](https://monarchinitiative.org/analyze/phenotypes).

### Disease ontology mappings
Medical terminology and ontology mapping is a huge deal in medical informatics ([example](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/mapping_projects/index.html)). [Mondo](https://github.com/monarch-initiative/mondo) is a particularly rich source of well provenanced disease ontology mappings.

## How should you map your data to ontologies?

There are no one size fits all strategies for mapping your data to ontologies. There
are many research areas that have something to give in this process. Here, we outline some ideas 
on how to think about the problem.

### Case 1: Mapping internal controlled vocabularies

### Case 2: Mappings from free text

Examples: 
- [Monarch Text Annotator](https://monarchinitiative.org/tools/text-annotate)

### Case 3: Mappings between public controlled vocabularies and ontologies

## How to solve the problem of mapping hairballs
  
String-term mappings

Overview of automated approaches
  - Simple matches (string, string pre-pro, fuzzy string)
  - Graph-based matches (incl. semantic similarity)
  - NLP/Machine Learning

Practical:
  - Try to get the same mappings as before using techniques
  - Exact
  - Simple preprocessing
  - Levenshtein
  - Jaccard similarity
  - Embedding similarity (?)  