# Introduction

## Abstract

Mappings, or cross-references, are used to link terms across different ontologies. However, there is currently little to no standardisation in how such mappings are represented. While properties such as hasDbXref property are widely used in ontologies such as GO and MONDO, the meaning of such mappings is unclear, and cannot be further described with additional metadata or provenance.

The Simple Standard for Sharing Ontology Mappings (SSSOM) is an initiative to provide a minimal and standard set of elements for the dissemination of mappings between ontology terms, to ensure a reliable interpretation of generated mappings and to enable sharing and data integration between people and applications. 

This document introduces the SSSOM catalog of metadata elements, which can be used to attach meta- and provenance data to both mappings and sets of mappings; a controlled vocabulary for the description of match types (SSSOM CV); a definition of both RDF and TSV serialisations of ontology mappings; and a (non-exhaustive) selection of recommended mapping predicates.

## Introduction

Currently, there are three methods typically used to express mappings in OWL: direct logical axioms using owl:equivalentClass; the oboInOwl hasDbXref property; and the SKOS vocabulary for mapping properties.  The first, owl:equivalentClass, is a strong logical equivalence assertion which is not appropriate for more nuanced mappings such as close matches.  The second, hasDbXref, does not assert formal logical equivalence but also has no clearly defined meaning.  Finally, the SKOS vocabulary provides a hierarchy of mapping properties which allow the unambigous specification of exact, close, broad, and narrow matches, but does not provide the means for mappings to be annotated with additional metadata such as confidence scores and provenance.

The Simple Standard for Sharing Ontology Mappings (SSSOM) addresses these problems by defining a catalog of metadata terms to describe mappings.  Both individual mappings and **_sets of_** mappings can be described, enabling provenance and metadata to be captured on multiple levels.  SSSOM interoperates with existing methods for the specification of mappings, allowing any predicate to be used to describe the nature of each mapping including those from OWL and SKOS.

The provenance of mappings - such as whether the mapping was created as the result of a human-curated equivalence match, or a semantic similarity match - is specified using a controlled vocabulary (CV), SSSOM CV.  Combined with the metadata properties provided by SSSOM such as confidence and semantic_similarity_score, this provenance information can be used to capture mapping descriptions in a manner that is explicit and amenable to curation.

Two serialisations for SSSOM mappings are provided in this document, aimed at different communities: an RDF/OWL serialisation using IRIs that is aimed at the Knowledge Graph/Semantic Web community, and a TSV serialisation using [CURIE](https://www.w3.org/TR/curie/) syntax which is aimed at the wider bioinformatics community.  An unambiguous translation between these serialisations is provided.

## Challenges for exchange and use of mappings
Despite their importance for data integration, term mappings are typically neglected as data artefacts (57). A mapping in this context is a correspondence between two terms, referred to here as "subject" and "object" terms. A "predicate" defines the type of relationship between the subject and the object, such as skos:exactMatch, or owl:equivalentClass. A mapping, or "match", does not have to be exact: it can be broad, e.g. between a conceptually narrow term such as "Red Delicious" and a conceptually broader term such as "Apple". To our knowledge, no formal review has been published that analyzes the representation and formats used for collections of term mappings (mapping sets, or alignments), but in our experience, most mapping sets are represented as tables using an ad-hoc "schema", often merely a simple two-column format that lists matching terms in two naming schemes. An example of such a table can be seen in the following Table.


Subject | Object
--- | ---
UBERON:0002101 | FMA:24875
UBERON:0000019 | FMA:54448

```
Table 1: An example of a typical mapping table one might find on the web.
```

This type of table lacks clear semantics and is therefore very difficult to use and re-use either by humans or by machines. We will discuss a few of the most critical problems in the sections that follow.

_Non-transparent imprecision_. Mapping precision describes, usually qualitatively, whether a mapping between a subject and an object is exact, broad, narrow, close or related. An exact mapping means that the subject term can be replaced with the object term and vice versa, i.e. they refer to the exact same real-world entity. A broad mapping links a subject term to a more general term, for example, the term "leg" to the term "hindlimb" (if the ontology defines leg as the parts of the hindlimb that exclude the foot). A narrow mapping links a subject term to a more specific term. For example, "long QT syndrome" in the Mondo Disease Ontology is a narrow match to "Romano-Ward long QT syndrome" in Orphanet. A close mapping relates two terms that are neither exact, broad or narrow, but belong to the same category of things and are semantically similar, such as "apple" to "pear", or "paw" to "hand". Due to its subjective nature ("what is close?"), this is a problematic category of mapping, but it is widely used, for example for relating similar anatomical terms across species. Related mappings are mappings across categories of things, such as the mapping between a phenotype "enlarged liver" and the anatomical entity "liver". In practice, it is rare that mapping tables such as the one presented in Table 1 constitute a set of purely "exact" matches. 

Different use cases may require different levels of mapping precision. For example, for entity merging (defined as the process of merging two entities from different sources into one) or data translation (defined as the process of moving annotations from using one ontology to another), exact mappings may be required, while for data grouping broad matches are often sufficient (ensuring that the subject is classified under the object term). For many machine learning use cases, close and related matches will be extremely useful regardless of their lack of semantic precision (though semantic precision is likely to improve predictive power). In practice, many mappings are to varying degrees imprecise but do not specify the mapping precision. This makes it impossible to reliably apply them to use cases such as entity merging or data translation.

_Non-transparent accuracy, confidence, and provenance_. To scale to real-world use cases, automated tools are critical for matching terms across databases, terminologies and ontologies. Such tools typically implement mapping rules that determine whether a given pair of terms constitutes a match. For example, label matching rules might include "match if subject and object labels match", "match if subject label matches with an exact synonym of the object" and "match if subject and object exhibit a very high degree of semantic similarity". Depending on the rules, tools will have more or less confidence that a match constitutes a mapping. Even human curators often have different levels of confidence about the accuracy of any given mapping, especially if the process of determining whether a mapping is accurate involves the review of (often complex) descriptions and term definitions. 

Different use cases will profit from different degrees of accuracy. For example, if we seek to integrate data from various medical terminologies to inform medical diagnosis, we may require not only a very high degree of confidence about the mapping but also ensure that the mapping is "explainable" to users. To ensure that diagnostic decisions that require bridging of data silos through mappings are explainable, we furthermore need provenance (documentation of where a piece of data comes from and how it was produced), such as an explicit statement of the mapping rules by which the match was originally determined (for example, the labels of both terms could have been the same). Thanks to efforts by initiatives such as the Ontology Alignment Evaluation Initiative (OAEI), many mapping tables on the web include at least a confidence score. However, in our experience, mapping rules are rarely stated explicitly as part of the mappings or mapping set metadata. Many mappings in the wild are to varying degrees inaccurate, but without a confidence score and explicit mapping rules, this inaccuracy will not be transparent.

_Non-transparent incompleteness_. Mapping sets can be incomplete for (at least) three major reasons: (1) they are out of date, i.e. a term in one ontology was removed (deprecated) in a later version of the ontology or a term with a more precise mapping was introduced; (2) they are deliberately partial, i.e. covering only a subset of terms, which were mapped for a specific purpose (for example a manual effort to map all COVID-19-relevant  phenotypes from the Human Phenotype Ontology to the Mammalian Phenotype Ontology); or (3) they accidentally omit certain correct mappings, as the automated approaches that were used did not detect them (false negatives). We cannot determine whether a mapping set such as the one given in Table X1 is up-to-date, deliberately partial or accidentally incomplete without sufficient metadata about the purpose of the mappings, the tools used and the version of the source data used for the matching process.

_UnFAIRness_. The FAIR principles are a set of community-developed guidelines to ensure that data or any digital object are Findable, Accessible, Interoperable and Reusable. Unlike many of the widely used controlled vocabularies, ontologies and data schemas, mappings are rarely published using standard formats and metadata vocabularies and can therefore be considered second class citizens in the world of FAIR semantics. 
While some tools exist to browse mappings (the F and A in FAIR, findable and accessible), such as OxO and BioPortal, they lack access to at least some of the metadata required to determine their applicability for a use case: Are mappings likely to be correct? Are they precise enough? Have they been updated recently? Can I trust the authority that generated the mappings? While some minimum level of interoperability (the I in FAIR) is achieved simply by publishing the mappings as RDF triples (which rarely happens in practice), most mappings are best captured in the form of simple tables (in our experience the preferred format for both mapping curators and data engineers). Furthermore, the predicates or relations used in the mappings are far from standardized. Different relations have different semantics, ranging from strong logical relations such as owl:sameAs or owl:equivalentClass to predicates with no formally specified semantics such as oboInOwl:hasDbXref. 

In our experience, reusability (the R in FAIR) is a significant obstacle to FAIRness. It is infeasible to simply reuse existing mappings without the metadata required to make imprecision, inaccuracy and incompleteness explicit. Repositories such as OxO and BioPortal cannot make mappings more accessible, because the metadata required to do so simply does not exist. In order to gradually improve our mappings and make them FAIRer, we need to be able to share, review, fix and maintain our mappings in much the same way as our ontologies themselves - using standard formats and rich metadata.
FAIRifying data is an effort that aims to supply practical solutions for the use of the FAIR guiding principles throughout the research data life cycle. It recommends technologies that support semantic interoperability in a sustainable way, and practices that support FAIRness. The FAIRSemantics effort is currently discussing how to incorporate semantic mappings, and we reached out to them to consider SSSOM for this purpose.

## Background about mappings

A mapping can be defined as a triple _s, p, o_, where s is the subject of the mapping, p is the mapping predicate (or relation) and o is the object. There are many different mapping predicates used in practice, but they are not always standardized. The Semantic Web community uses a number of standard mapping predicates, such as owl:sameAs or owl:equivalentClass (logical mapping predicates) and skos:exactMatch or skos:broadMatch (terminological mapping predicates). We refer to mapping subjects and objects as "terms", which we will loosely define here as a set of symbols that define some entity in the real world. Usually, a term can be referred to by an identifier that uniquely identifies some entity in a certain context. For example, UBERON:0002101 is the identifier for a term that refers to the anatomical entity "limb". 
Putting it all together, the mapping <UBERON:0002101, skos:exactMatch, FMA:24875> describes a correspondence in which the term with the id UBERON:0002101 constitutes a terminological exact match to the term with the identifier FMA:24875. Mappings between data model elements, databases and other representations can be described similarly. Note that we generally use the terms "matching" and "mapping" interchangeably. Occasionally we refer to "matching" as the process to determine a mapping candidate (lexical matching, logical matching etc), a "match" as the result of the matching process, and a "mapping" the process and result of the process that deduces a true correspondence from a (set of) matches. For SSSOM, this distinction is a bit academic, but useful to keep in mind when talking about the interplay of automated approaches (which result in "matches") and manual approaches (which typically result in the final mappings). Ontology alignment is the task of determining corresponding terms shared between two or more ontologies, i.e. mappings. Sometimes "ontology alignment" refers to the output of the alignment process.

Mapping sets can be "partial", i.e. covering only a subset of terms in the subject or object source (ontology, database, etc), "derived", i.e. one mapping set can be obtained from one or more others (for example, a XAO to MeSH mapping can be obtained by combining a XAO-Uberon mapping with a Uberon-MeSH mapping), or "complete". We refer to a "complete" mapping, i.e. the set of all correspondences between two resources (ontologies, databases), as an "alignment".

The identifier of a term has three parts: a namespace that describes in which database or ontology the identifier is defined, a local identifier that unambiguously identifies an entity within that namespace, and optionally a separator that can be used to separate the namespace from the local identifier to make them easier to process. UBERON:0002101, for example, comprises the namespace "UBERON", the separator ":" and the local identifier "0002101". There are various syntaxes for denoting identifiers; the UBERON:0002101 notation is called compact URI (CURIE) syntax, which is used widely across the database and ontology worlds. The problem with this syntax is that UBERON may not be a globally unique prefix, so files making use of such CURIEs must come with a prefix map that ensures that UBERON (in the CURIE syntax referred to as "prefix") is globally unique by mapping it to the persistent International Resource Identifier (IRI) prefix http://purl.obolibrary.org/obo/UBERON_. This may not be a major problem for a fairly unique prefix such as "UBERON", but it is for prefixes such as "ICD", which can refer to many different name spaces, such as ICD9, ICD10, ICD11 and more, all of which correspond to entirely different terminologies.

_Approaches to mapping_. There are many different techniques that can be employed to generate term mappings. Automated matching techniques include ontology matching, entity resolution (the task of determining whether two database records correspond to the same entity), semantic similarity or automated reasoning. Recent approaches based on machine learning and graph embeddings show promise for working with messier inputs. No single tool will perform equally well on all inputs: some of the semantics-aware tools like LogMap and Agreement Maker Light (AML) can exploit the ontology structure to determine high-quality matches but will have problems with the large-scale data linking tasks required by modern big-data applications. 

Purely automated approaches to mapping are often insufficient for real world use cases that require a high degree of accuracy, such as medical diagnostics. They often need to be refined by hand or using sophisticated mapping reconciliation approaches independent of the actual matching. Determining a mapping is often complex, due to the high degree of terminological variability: different communities may use very different names for the same real world entities . For example, for example, the condition referred to in the Human Phenotype Ontology (HPO) as "Hyperchloriduria" is called "increased urine chloride ion level" in the Mammalian Phenotype Ontology (MP), which is used by the model organism community.

_Mapping rules - capturing the conditions under which a match is established_.
Mapping rules define the conditions under which we determine a match between two terms. For example, the condition for a mapping rule could be "if the subject label and object label match exactly". In practice, mapping rules can be very simple (e.g., "exact match of term labels"),  more complex ("exact match between label of subject and exact synonym of object after they are pre-processed using stemming"), or even more exacting ("complex match determined by a human curator that carefully reviewed the descriptions and definitions of both terms and concluded they mean the same thing"). One problem for both manually curated mappings and automated approaches is that these mapping rules are often hidden deeply in the code or are not documented at all. Exposing mapping rules along with confidence scores would be very valuable for reviewing mappings and explaining them to users. Our reference implementation for SSSOM is rdf-matcher, which makes these mapping rules explicit, but other approaches such as OMOP2OBO also capture mapping rules as part of the mapping metadata.