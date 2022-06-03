# Simple Standard for Sharing Ontology Mappings (SSSOM)

Development Draft (under construction: some metadata fields may be subject to change)

*Editors:*

* [Nicolas Matentzoglu](https://orcid.org/0000-0002-7356-1779) (Semanticly Ltd; [@matentzn](https://github.com/matentzn))
* [Chris Mungall](https://orcid.org/0000-0002-6601-2165) (LBL)
* [Ernesto Jimenez-Ruiz](https://orcid.org/0000-0002-9083-4599) (City, University of London)
* [John Graybeal](https://orcid.org/0000-0001-6875-5360) (Stanford)
* [William Duncan](https://orcid.org/0000-0001-9625-1899) (LBL)
* [David Osumi-Sutherland](https://orcid.org/0000-0002-7073-9172) (EMBL-EBI)
* [Simon Jupp](https://orcid.org/0000-0002-0643-3144) (SciBite)
* [James McLaughlin](https://orcid.org/0000-0002-8361-2795) (EMBL-EBI)
* [Henriette Harmse](https://orcid.org/0000-0001-7251-9504) (EMBL-EBI)
* [Tiffany Callahan](https://orcid.org/0000-0002-8169-9049) ([@callahantiff](https://github.com/callahantiff))
* [Charlie Hoyt](https://orcid.org/0000-0003-4423-4370) (Harvard Medical School; [@cthoyt](https://github.com/cthoyt))
* [Thomas Liener](https://orcid.org/0000-0003-3257-9937) (Pistoia Alliance)
* [Harshad Hegde](https://orcid.org/0000-0002-2411-565X) (LBL)

*Contributors:*

* [Alasdair Gray](https://orcid.org/0000-0002-5711-4872)
* [Alex Wagner](https://orcid.org/0000-0002-2502-8961)
* [Amelia L. Hoyt](https://orcid.org/0000-0003-1307-2508)
* [Andrew Williams](https://orcid.org/0000-0002-0692-412X)
* [Anne Thessen](https://orcid.org/0000-0002-2908-3327)
* [Benjamin M. Gyori](https://orcid.org/0000-0001-9439-5346)
* [Bill Baumgartner](https://orcid.org/0000-0001-6717-5313)
* [Christopher Chute](https://orcid.org/0000-0001-5437-2545)
* [Chris T. Evelo](https://orcid.org/0000-0002-5301-3142)
* [Damion Dooley](https://orcid.org/0000-0002-8844-9165)
* [Davera Gabriel](https://orcid.org/0000-0001-9041-4597)
* [Harold Solbrig](https://www.wikidata.org/wiki/Q44607574)
* [HyeongSik Kim](https://orcid.org/0000-0002-3002-9838)
* [Ian Harrow](https://orcid.org/0000-0003-0109-0522)
* [James Malone](https://orcid.org/0000-0002-1615-2899)
* [James Overton](https://orcid.org/0000-0001-5139-5557)
* [James P. Balhoff](https://orcid.org/0000-0002-8688-6599)
* [James Stevenson](https://orcid.org/0000-0002-2568-6163)
* [Jiao Dahzi](https://orcid.org/0000-0001-5052-3836)
* [Joe Flack](https://orcid.org/0000-0002-2906-7319)
* [Jooho Lee](https://orcid.org/0000-0002-2955-3405)
* [Julie McMurry](https://orcid.org/0000-0002-9353-5498)
* [Kori Kuzma](https://orcid.org/0000-0002-9954-7449)
* [Kristin Kostka](https://orcid.org/0000-0003-2595-8736)
* [Lauren Chan](https://orcid.org/0000-0002-7463-6306)
* [Melissa Haendel](https://orcid.org/0000-0001-9114-8737)
* [Monica Munoz-Torres](https://orcid.org/0000-0001-8430-6039)
* [Nicole Vasilevsky](https://orcid.org/0000-0001-5208-3432)
* [Nomi Harris](https://orcid.org/0000-0001-6315-3707)
* [Núria Queralt-Rosinach](https://orcid.org/0000-0003-0169-8159)
* [Sabrina Toro](https://orcid.org/0000-0002-4142-7153)
* [Sebastian Koehler](https://orcid.org/0000-0002-5316-1399)
* [Shahim Essaid](https://orcid.org/0000-0003-2338-2550)
* [Sierra Moxon](https://orcid.org/0000-0002-8719-7760)
* [Sue Bello](https://orcid.org/0000-0003-4606-0597)
* [Tim Putman](https://orcid.org/0000-0002-4291-0737)

*Quick links*: 

- [SSSOM on Wikidata](https://www.wikidata.org/wiki/Q108394480)
- [SSSOM Python toolkit on Wikidata](https://www.wikidata.org/wiki/Q108394654)
- [SSSOM Python toolkit: Official Documentation](https://mapping-commons.github.io/sssom-py)
- [Presentations](presentations.md)

## Abstract

Mappings, or cross-references, are used to link terms across different ontologies. However, there is currently little to no standardisation in how such mappings are represented. While properties such as hasDbXref property are widely used in ontologies such as GO and MONDO, the meaning of such mappings is unclear, and cannot be further described with additional metadata or provenance.

The Simple Standard for Sharing Ontology Mappings (SSSOM) is an initiative to provide a minimal and standard set of elements for the dissemination of mappings between ontology terms, to ensure a reliable interpretation of generated mappings and to enable sharing and data integration between people and applications. 

This document introduces the SSSOM catalog of metadata elements, which can be used to attach meta- and provenance data to both mappings and sets of mappings; a controlled vocabulary for the description of match types (SSSOM CV); a definition of both RDF and TSV serialisations of ontology mappings; and a (non-exhaustive) selection of recommended mapping predicates.

## Table of Contents

* [Introduction](#intro)
* [SSSOM Metadata Elements](#meta)
* [SSSOM Common Predicates](#predicates)
* [SSSOM Serialisation](#serialisation)
* [SSSOM Use Cases](#usecase)
* [SSSOM 5-Star recommendation for mappings](#minimum)

<a name="intro"></a>

## Introduction

Currently, there are three methods typically used to express mappings in OWL: direct logical axioms using owl:equivalentClass; the oboInOwl hasDbXref property; and the SKOS vocabulary for mapping properties.  The first, owl:equivalentClass, is a strong logical equivalence assertion which is not appropriate for more nuanced mappings such as close matches.  The second, hasDbXref, does not assert formal logical equivalence but also has no clearly defined meaning.  Finally, the SKOS vocabulary provides a hierarchy of mapping properties which allow the unambigous specification of exact, close, broad, and narrow matches, but does not provide the means for mappings to be annotated with additional metadata such as confidence scores and provenance.

The Simple Standard for Sharing Ontology Mappings (SSSOM) addresses these problems by defining a catalog of metadata terms to describe mappings.  Both individual mappings and **_sets of_** mappings can be described, enabling provenance and metadata to be captured on multiple levels.  SSSOM interoperates with existing methods for the specification of mappings, allowing any predicate to be used to describe the nature of each mapping including those from OWL and SKOS.

The provenance of mappings - such as whether the mapping was created as the result of a human-curated equivalence match, or a semantic similarity match - is specified using a controlled vocabulary (CV), SSSOM CV.  Combined with the metadata properties provided by SSSOM such as confidence and semantic_similarity_score, this provenance information can be used to capture mapping descriptions in a manner that is explicit and amenable to curation.

Two serialisations for SSSOM mappings are provided in this document, aimed at different communities: an RDF/OWL serialisation using IRIs that is aimed at the Knowledge Graph/Semantic Web community, and a TSV serialisation using [CURIE](https://www.w3.org/TR/curie/) syntax which is aimed at the wider bioinformatics community.  An unambiguous translation between these serialisations is provided.

### Challenges for exchange and use of mappings
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

### Background about mappings

A mapping can be defined as a triple <s, p, o>, where s is the subject of the mapping, p is the mapping predicate (or relation) and o is the object. There are many different mapping predicates used in practice, but they are not always standardized. The Semantic Web community uses a number of standard mapping predicates, such as owl:sameAs or owl:equivalentClass (logical mapping predicates) and skos:exactMatch or skos:broadMatch (terminological mapping predicates). We refer to mapping subjects and objects as "terms", which we will loosely define here as a set of symbols that define some entity in the real world. Usually, a term can be referred to by an identifier that uniquely identifies some entity in a certain context. For example, UBERON:0002101 is the identifier for a term that refers to the anatomical entity "limb". 
Putting it all together, the mapping <UBERON:0002101, skos:exactMatch, FMA:24875> describes a correspondence in which the term with the id UBERON:0002101 constitutes a terminological exact match to the term with the identifier FMA:24875. Mappings between data model elements, databases and other representations can be described similarly. Note that we generally use the terms "matching" and "mapping" interchangeably. Occasionally we refer to "matching" as the process to determine a mapping candidate (lexical matching, logical matching etc), a "match" as the result of the matching process, and a "mapping" the process and result of the process that deduces a true correspondence from a (set of) matches. For SSSOM, this distinction is a bit academic, but useful to keep in mind when talking about the interplay of automated approaches (which result in "matches") and manual approaches (which typically result in the final mappings). Ontology alignment is the task of determining corresponding terms shared between two or more ontologies, i.e. mappings. Sometimes "ontology alignment" refers to the output of the alignment process.

Mapping sets can be "partial", i.e. covering only a subset of terms in the subject or object source (ontology, database, etc), "derived", i.e. one mapping set can be obtained from one or more others (for example, a XAO to MeSH mapping can be obtained by combining a XAO-Uberon mapping with a Uberon-MeSH mapping), or "complete". We refer to a "complete" mapping, i.e. the set of all correspondences between two resources (ontologies, databases), as an "alignment".

The identifier of a term has three parts: a namespace that describes in which database or ontology the identifier is defined, a local identifier that unambiguously identifies an entity within that namespace, and optionally a separator that can be used to separate the namespace from the local identifier to make them easier to process. UBERON:0002101, for example, comprises the namespace "UBERON", the separator ":" and the local identifier "0002101". There are various syntaxes for denoting identifiers; the UBERON:0002101 notation is called compact URI (CURIE) syntax, which is used widely across the database and ontology worlds. The problem with this syntax is that UBERON may not be a globally unique prefix, so files making use of such CURIEs must come with a prefix map that ensures that UBERON (in the CURIE syntax referred to as "prefix") is globally unique by mapping it to the persistent International Resource Identifier (IRI) prefix http://purl.obolibrary.org/obo/UBERON_. This may not be a major problem for a fairly unique prefix such as "UBERON", but it is for prefixes such as "ICD", which can refer to many different name spaces, such as ICD9, ICD10, ICD11 and more, all of which correspond to entirely different terminologies.

_Approaches to mapping_. There are many different techniques that can be employed to generate term mappings. Automated matching techniques include ontology matching, entity resolution (the task of determining whether two database records correspond to the same entity), semantic similarity or automated reasoning. Recent approaches based on machine learning and graph embeddings show promise for working with messier inputs. No single tool will perform equally well on all inputs: some of the semantics-aware tools like LogMap and Agreement Maker Light (AML) can exploit the ontology structure to determine high-quality matches but will have problems with the large-scale data linking tasks required by modern big-data applications. 

Purely automated approaches to mapping are often insufficient for real world use cases that require a high degree of accuracy, such as medical diagnostics. They often need to be refined by hand or using sophisticated mapping reconciliation approaches independent of the actual matching. Determining a mapping is often complex, due to the high degree of terminological variability: different communities may use very different names for the same real world entities . For example, for example, the condition referred to in the Human Phenotype Ontology (HPO) as "Hyperchloriduria" is called "increased urine chloride ion level" in the Mammalian Phenotype Ontology (MP), which is used by the model organism community.

_Mapping rules - capturing the conditions under which a match is established_.
Mapping rules define the conditions under which we determine a match between two terms. For example, the condition for a mapping rule could be "if the subject label and object label match exactly". In practice, mapping rules can be very simple (e.g., "exact match of term labels"),  more complex ("exact match between label of subject and exact synonym of object after they are pre-processed using stemming"), or even more exacting ("complex match determined by a human curator that carefully reviewed the descriptions and definitions of both terms and concluded they mean the same thing"). One problem for both manually curated mappings and automated approaches is that these mapping rules are often hidden deeply in the code or are not documented at all. Exposing mapping rules along with confidence scores would be very valuable for reviewing mappings and explaining them to users. Our reference implementation for SSSOM is rdf-matcher, which makes these mapping rules explicit, but other approaches such as OMOP2OBO also capture mapping rules as part of the mapping metadata.


### Some notes on the standardisation process:

Note this is a public copy of the editors’ draft. It is provided for discussion only and may change at any moment. Do not cite this document other than as work in progress. SSSOM is community-driven, so all feedback is welcome.

<a name="meta"></a>

## SSSOM Metadata Elements

The SSSOM specification defines a set of SSSOM metadata elements that are used to describe mappings. Apart from the elements themselves, some example usage and a description, **_[the SSSOM spec](https://mapping-commons.github.io/sssom/Mapping/) defines the canonical order for the metadata_** in which the elements should appear when serialised. This precludes spurious diffs in a git setting, which is an important concern for the continuous reviewing of mappings by curators and users. 

A "term" is defined in a controlled vocabulary / ontology, and usually corresponds to a class, an individual or a property (entity in OWL, concept in SKOS, resource in RDF). The "subject" is the term on the left side of the mapping, and the "object" is the term on the right side of the mapping. A "predicate" relates the subject with the object and is typically an annotation or object property. A "mapping set" is a set of mappings that can be shared using the SSSOM standard.

The conceptual model of SSSOM has two main elements: 

- a [Mapping](https://mapping-commons.github.io/sssom/Mapping/) and
- a [MappingSet](https://mapping-commons.github.io/sssom/MappingSet/).

Some SSSOM metadata elements apply only to one element or the other, but many can be applied to both.

Note that some SSSOM metadata elements have known equivalent properties which will be used in the RDF serialisation, for example `see_also` is mapped to `rdfs:seeAlso`.

All metadata elements and their mappings are declared and managed in the [SSSOM schema](https://github.com/mapping-commons/sssom/blob/master/model/schema/sssom.yaml).

### Metadata Elements

The latest version of the metadata elements are:

- [Mapping](https://mapping-commons.github.io/sssom/Mapping/)
- [MappingSet](https://mapping-commons.github.io/sssom/MappingSet/) 

<a name="predicates"></a>

## Common Mapping Predicates

The use of predicates is not restricted by SSSOM, but for maximum re-use, the following predicates are strongly encouraged.

*Sources:*

* [https://www.bioontology.org/wiki/BioPortal_Mappings](https://www.bioontology.org/wiki/BioPortal_Mappings)

<table>
  <tr>
    <td>Predicate</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>owl:sameAs</td>
    <td>The subject and the object are instances (owl individuals), and the two instances are the same.</td>
  </tr>
  <tr>
    <td>owl:equivalentClass</td>
    <td>The subject and the object are classes (owl class), and the two classes are the same.</td>
  </tr>
  <tr>
    <td>owl:equivalentProperty</td>
    <td>The subject and the object are properties (owl object, data, annotation properties), and the two properties are the same.</td>
  </tr>
  <tr>
    <td> rdfs:subClassOf</td>
    <td>The subject and the object are classes (owl class), and the subject is a subclass of the object.</td>
  </tr>
  <tr>
    <td>rdfs:subPropertyOf</td>
    <td>The subject and the object are properties (owl object, data, annotation properties), and the subject is a subproperty of the object.</td>
  </tr>
  <tr>
    <td>skos:relatedMatch</td>
    <td>The subject and the object are associated in some unspecified way.</td>
  </tr>
  <tr>
    <td>skos:closeMatch</td>
    <td>The subject and the object are sufficiently similar that they can be used interchangeably in some information retrieval applications.</td>
  </tr>
  <tr>
    <td>skos:exactMatch</td>
    <td>The subject and the object can, with a high degree of confidence, be used interchangeably across a wide range of information retrieval applications.</td>
  </tr>
  <tr>
    <td>skos:narrowMatch</td>
    <td>From the SKOS primer: A triple <A> skos:narrower (and skos:narrowMatch) <B> asserts that <B>, the object of the triple, is a narrower concept than <A>, the subject of the triple.</td>
  </tr>
  <tr>
    <td>skos:broadMatch</td>
    <td>From the SKOS primer: A triple <A> skos:broader (and skos:broadMatch) <B> asserts that <B>, the object of the triple, is a broader concept than <A>, the subject of the triple.</td>
  </tr>
  <tr>
    <td>oio:database_cross_reference</td>
    <td>Two terms are related in some way. The meaning is frequently consistent across a single set of mappings. Note this property is often overloaded even where the terms are of a different nature (e.g. interpro2go)</td>
  </tr>
  <tr>
    <td>rdfs:seeAlso</td>
    <td>The subject and the object are associated in some unspecified way. The object IRI often resolves to a resource on the web that provides additional information.</td>
  </tr>
  <tr>
    <td>RO:?</td>
    <td>Any Relation in the Relation Ontology (RO).</td>
  </tr>
</table>

<a name="serialisation"></a>

## Serialisation

### RDF/XML serialised re-ified OWL axioms:

The default RDFXML serialisation of the mappings will be realised as *reified OWL axioms*. This has the advantage that any mapping set can be simply merged with an ontology in the usual way, for example using [ROBOT merge](http://robot.obolibrary.org/merge). We will deal with three types of reified OWL-axioms, and a few sub-types:

1. Predicate is an annotation property
2. Predicate is an object property and
   1. Object/Subject are classes
   2. Object/Subject are individuals
3. Predicate is language relational construct of RDFS or OWL (rdfs:subClassOf, owl:equivalentClass)

#### Predicate is an annotation property:

If the predicate corresponds to an annotation property, the mapping <S,P,O, sssomMetadata> gets converted to an OWLAnnotationAssertion axiom: `OWLAnnotationAssertion(P,S,O)`. All mapping level metadata (`sssomMetadata`) gets converted into OWLAnnotation objects which are materialised as axiom annotations on the mapping annotation assertion, see [OWL 2 Structural Specification](https://www.w3.org/TR/owl2-syntax/#Annotations):

```
AnnotationAssertion(sssomMetadata P, S, O)
```

Where `sssomMetadata` is a sequence of OWL Annotations objects like:

```	
Annotation(Q1,V1) Annotation(Q2,V2) ... Annotation(Qn,Vn)
```

where Qi is a SSSOM metadata element and Vi is an annotation value.

Note that if a SSSOM metadata element value is a list L (i.e. can have multiple elements, such as creator and others), individual annotations are created for each of them:

```
Annotation(Q,V) for all V in L.
```

Example:

```
AnnotationAssertion(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:mapping_justification semapv:LexicalEquivalenceMatch) skos:exactMatch <http://purl.obolibrary.org/obo/HP_0009894> <http://purl.obolibrary.org/obo/MP_0000019>)
```

Mapping set level annotations are manifested as Ontology annotation in the usual way, according to the [OWL 2 Structural Specification](https://www.w3.org/TR/owl2-syntax/#Annotations).

#### Predicate is an object property

##### Case 1: Object and Subject are classes.

The Mapping <S,P,O> gets translated into an existential restriction: 

```
SubclassOf(A, P some O)
```

All metadata elements are added as OWLAnnotation objects and added to SubclassOf axiom as axiom annotations:

```
SubclassOf(sssomMetadata, A, P some O)
```

Example:

```
SubClassOf(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:mapping_justification semapv:LexicalEquivalenceMatch) <http://example.org/AA> ObjectSomeValuesFrom(<http://example.org/x> <http://example.org/BB>))
```

##### Case 2: Object and Subject are individuals

The Mapping <S,P,O> gets translated into an object property assertion: 

```
ObjectPropertyAssertion(P, A, O)
```

All metadata elements are added as OWLAnnotation objects and added to ObjectPropertyAssertion axiom as axiom annotations:

```
ObjectPropertyAssertion(sssomMetadata, P, A, O)
```

Example:

```
ObjectPropertyAssertion(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:mapping_justification semapv:LexicalEquivalenceMatch) <http://www.example.org/x> <http://www.example.org/a> <http://www.example.org/b>)
```

#### Predicate is language relational construct of RDFS or OWL

The mapping <S,P,O> gets translated into an annotated axiom that corresponds to the construct used. By default, SSSOM will support:

<table>
  <tr>
    <td>owl:EquivalentClass</td>
    <td>EquivalentClass(sssomMetadata,A,O)</td>
  </tr>
  <tr>
    <td>rdfs:subClassOf</td>
    <td>SubClassOf(sssomMetadata, A,O)</td>
  </tr>
</table>

Example:

```
SubClassOf(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:mapping_justification semapv:LexicalEquivalenceMatch) <http://www.example.org/a> <http://www.example.org/b>)
```

### TSV:

All SSSOM metadata elements labelled with L in the metadata table are permissible as column names in the TSV. List elements (such as creator) are "|"-separated. The columns MUST be sorted according to the order as they appear in the [SSSOM metadata](https://mapping-commons.github.io/sssom/Mapping/). For example, the first columns of a mapping set TSV should always be, in that order: subject_id, predicate_id, object_id, mapping_justification, if labels are not included; if they are included, the order should be: subject_id, subject_label, predicate_id, predicate_label, object_id, object_label, mapping_justification. For easier review of diffs, for example git diff or unix diff, we recommend to serialise the TSV by a fixed row order, sorted column by column from left to right.

Metadata about a set of mappings can be supplied as part of the mappings (embedded mode) and as a simple yaml file alongside the primary mapping file. Note that for the TSV, it will be required to supply a valid curie map that allows the unambiguous interpretation of CURIEs. A curie map is supplied after a `curie_map:` parameter in the yaml file. The value can be either a dictionary of CURIE->URLPREFIX pairs or a link to a valid curie map of the same shape.

Note that only metadata elements permissible in a global context (G, or L/G) can be used in the metadata-file.

We recommend to use the following *filename conventions* for SSSOM metadatafiles:

- TSV files should have the extension `.sssom.tsv`, for example: `mp-hp-exact-0.0.1.sssom.tsv`.
- External yaml metadata files should have the extension `.sssom.yml`, for example `mp-hp-exact-0.0.1.sssom.tsv`

Example ([download](https://raw.githubusercontent.com/matentzn/SSSOM/master/examples/external/mp-hp-exact-0.0.1.sssom.yml)):

```
creator_id: "https://orcid.org/0000-0002-7356-1779"
curie_map: 
  HP: "http://purl.obolibrary.org/obo/HP_"
  MP: "http://purl.obolibrary.org/obo/MP_"
  skos: "http://www.w3.org/2004/02/skos/core"
license: "https://creativecommons.org/publicdomain/zero/1.0/"
mapping_provider: "http://purl.obolibrary.org/obo/upheno.owl"
```

#### External mode 

In external mode, the mapping set metadata is supplied by a separate YAML file having the same base-name of the mapping file, with the extension `-meta.yml`. By default, tools will look for the file of that name in the same directory as the the mapping set table.

Example ([download](https://raw.githubusercontent.com/matentzn/SSSOM/master/examples/external/mp-hp-exact-0.0.1.sssom.tsv)):

```
subject_id	predicate_id	object_id	mapping_justification	subject_label	object_label
HP:0009124	skos:exactMatch	MP:0000003	Lexical	Abnormal adipose tissue morphology	abnormal adipose tissue morphology
HP:0008551	skos:exactMatch	MP:0000018	Lexical	Microtia	small ears
HP:0000411	skos:exactMatch	MP:0000021	Lexical	Protruding ear	prominent ears
```

#### Embedded mode (default)

In the embedded mode, we allow the integration of mapping set level metadata as **_commented YAML_**. Apart from being commented, the YAML follows the exact same spec as the *YAML specified by the external mode*. Heavily used tools in bioinformatics such as pandas allow to [specify comment characters](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) when reading CSV files, which makes this option the most user friendly for this community. Additionally, it is a simple unix-level or language-level operation to filter these as a pre-processing in a robust fashion.

Note: the mapping set level metadata _must be included as a continuous block at the beginning of the file_. This means in particular: 
- No comments can be included that are not part of the metadata data. For example, this is not allowed:

Illegal case 1:
```
#creator_id: "https://orcid.org/0000-0002-7356-1779"
# This is a comment that does not belong here
#curie_map: 
#  HP: "http://purl.obolibrary.org/obo/HP_"
#  MP: "http://purl.obolibrary.org/obo/MP_"
```

Illegal case 2:
```
# This is a comment that does not belong here
#creator_id: "https://orcid.org/0000-0002-7356-1779"
#curie_map: 
#  HP: "http://purl.obolibrary.org/obo/HP_"
#  MP: "http://purl.obolibrary.org/obo/MP_"
```

- There should be no empty rows: the commented yaml files _must_ be directly followed by the column headers. For example, this is not allowed:

Illegal case 3:
```

#creator_id: "https://orcid.org/0000-0002-7356-1779"

#curie_map: 
#  HP: "http://purl.obolibrary.org/obo/HP_"
#  MP: "http://purl.obolibrary.org/obo/MP_"
```

- The can be only a single # in the beginning of each row, followed immediately by the yaml.
- When the leading hash-symbol is stripped from the header block, the resulting string is:
  1. a valid yaml file
  2. conforms to SSSOM mapping set specification (only `curie_map` or a metadata elements that are allowed on `mapping_set` level, i.e. `global`).
- After the table header, no further row should be commented out.

Example ([download](https://raw.githubusercontent.com/matentzn/SSSOM/master/examples/embedded/mp-hp-exact-0.0.1.sssom.tsv)):

```
#creator_id: "https://orcid.org/0000-0002-7356-1779"
#curie_map: 
#  HP: "http://purl.obolibrary.org/obo/HP_"
#  MP: "http://purl.obolibrary.org/obo/MP_"
#  skos: "http://www.w3.org/2004/02/skos/core"
#license: "https://creativecommons.org/publicdomain/zero/1.0/"
#mapping_provider: "http://purl.obolibrary.org/obo/upheno.owl"
subject_id	predicate_id	object_id	mapping_justification	subject_label	object_label
HP:0009124	skos:exactMatch	MP:0000003	Lexical	Abnormal adipose tissue morphology	abnormal adipose tissue morphology
HP:0008551	skos:exactMatch	MP:0000018	Lexical	Microtia	small ears
HP:0000411	skos:exactMatch	MP:0000021	Lexical	Protruding ear	prominent ears
```

*Notes:*

* ROBOT implementation: [https://github.com/ontodev/robot/issues/312](https://github.com/ontodev/robot/issues/312)

### JSON:

JSON translation is fully managed by [LinkML dumper classes](https://linkml.io/linkml/code.html#loaders-and-dumpers).

<a name="usecase"></a>

## Use Cases:

* Consumers:
  * OxO
  * Analysis in R/Python using dataframes/pandas
  * Visual inspection by curators to spot-check errors
  * Machine Learning (e.g. predict predicate based on SSSOM columns)

* Maintainers:
  * Maintain mappings in google sheets
  * Is the format optimized for google refine?
  * Maintain mappings in github/tsvs
    * Rendering
    * Drive-by PRs

* Providers
  * Autogenerate pages like 
    * [http://geneontology.org/docs/download-mappings/](http://geneontology.org/docs/download-mappings/)
    * [http://uberon.github.io/downloads.html#bridge](http://uberon.github.io/downloads.html#bridge)
   * OxO

<a name="minimum"></a>
     
## The SSSOM 5-Star System For Mappings

Current mappings are extremely hard to use for data integration, because they are:

- *non-transparently imprecise*: we do not know whether they are between equivalent terms, or wether one term is broader than the other.
- *non-transparently incomplete*: we do not know whether the absence of a mapping means there is none.
- *inaccurate*: there are many mappings generated by automated tools that have a low mapping confidence - but still included in mapping sets.
- *unFAIR*: there is insufficient metadata attached to mappings and mapping sets to trace their provenance, attribute trust or combine them to exploit cross-walks.

In principle, to reach full integration through mappings, you will have to cross-map all ontologies, or semantic
spaces (e.g. controlled vocabularies, semantic databases), which means if you have N "spaces", you have `N x (N - 1)` mappings (because A -> B is often different from B -> A). It makes sense to consider mappings as a directed graph from which you can infer other mappings using graph walking or [graph traversals](https://en.wikipedia.org/wiki/Graph_traversal). To mitigate the explosion of mappings, we have to be able to cross-walk. While some typical mapping predicates such as owl:equivalentClass or skos:exactMatch are symetric (which means that if A -> B then you can infer B -> A, which we will call a "walk-back"), other are not (skos:narrowMatch), but maybe have `inverse` predicates (A --[skos:narrowMatch]--> B implies B --[skos:broadMatch]--> A). Apart from walk backs, you can infer additional mappings through a chain of subsequent mappings (multi-hop forward walks), for example:
- multi-hop forward walks `{ PR:000050277 -> ncbiprotein:YP_009725304, ncbiprotein:YP_009725304-> uniprot.chain:PRO_0000449627 } --> {PR:000050277 -> uniprot.chain:PRO_0000449627}`
) 
- walk-backs `{ PR:000050277 -> ncbiprotein:YP_009725304 } --> {ncbiprotein:YP_009725304 -> PR:000050277}`
- combinations `{ PR:000050277 -> ncbiprotein:YP_009725304, ncbiprotein:YP_009725304-> uniprot.chain:PRO_0000449627, MY:NSP8-> uniprot.chain:PRO_0000449627 } --> { PR:000050277 -> MY:NSP8 }`

To enable cross-walking, we propose the following **Five-Star system** for mapping sets. 

- _1-Star mappings_ fulfill the following criteria:
    - record subject id, object id and mapping precision (exact, broad, narrow, close, related)
    - using qualified names (either URIs or CURIEs + curie maps) for subject id and object id
    - using a standard file format (JSON, XML, CSV, TSV)
    - made available in a public space
    - _optional_: record the subject and object labels to make it easier for humans to read the file
- _2-Star mappings_ fulfill all the criteria for 1-star mappings and furthermore
    - made available in a public version control system with an issue tracker
    - record the semantic predicate explicitly and using qualified names for the semantic predicate (i.e. owl:equivalentClass, skos:exactMatch)
    - record a confidence value for the mapping between 0 and 1 (0 no confidence, 1 100% confidence).
    - record an open license for the use of the mapping set
- _3-Star mappings_ fulfill all the criteria for 2-star mappings and furthermore 
    - are exported in SSSOM format
    - record the following additional metadata: 
        - `mapping_justification`(s) (Lexical, Logical match, HumanCurated etc)
        - `date` of the mapping
        - `creator_id`
        - `subject_source`
        - `object_source`
        - `subject_source_version`
        - `object_source_version`
        - `mapping_tool` if the mapping was automatically computed using a tool
- _4-Star mappings_ fulfill all the criteria for 3-star mappings and furthermore
    - register the mapping at a mapping commons
    - record the following additional metadata:
         - `mapping_set_id`
         - `mapping_set_description`
         - `mapping_set_version`
         - `mapping_provider` (if the mapping is not original, i.e. it is not derived from another source)
    - provide a completely executable curation_rule:
        - if the mapping is `Lexical`, provide:
            - `subject_preprocessing`, `object_preprocessing`
            - `subject_match_field`, `object_match_field`
            - `match_string`
        - if the mapping is `Logical`, the mapping should be derivable by a reasoner from a combination of the `object_source` and `subject_source`. If more is needed then please leave a `comment` with details.
        - if the mapping is `HumanCurated`.. (this needs to be [fleshed out](https://github.com/mapping-commons/SSSOM/issues/57). For now, leave a `comment` indicating what you did to arrive at your conclusion, i.e. wether you compared the definitions, looked up the "labels" in a database, ran a tool and decided to trust it etc.)
        - if the mapping is `SemanticSimilarity` (graph similarity, neighbourhood, cosine similarity), you should provide:
            - `semantic_similarity_score`
            - `semantic_similarity_measure`
        - For now, if there are _multiple pieces of evidence_ (lexical, logical etc), please emit one row per evidence. If your tool combines multiple pieces of evidence in a complex way, emit yet another row at the end with `mapping_justification` `Complex` and emit ensure you provide the `mapping_tool`.
- _5-Star mappings_ fulfill all the criteria for 4-star mappings and furthermore
    - Are up-to-date with the `subject_source` and `object_source`
    - Have no issue on their issue tracker open for more than 3 months without an interaction
    - Use a _standard_ open license, such as [CC Zero 1.0](https://creativecommons.org/publicdomain/zero/1.0/) or [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
