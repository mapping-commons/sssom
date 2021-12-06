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


#### Some notes on the standardisation process:

Note this is a public copy of the editors’ draft. It is provided for discussion only and may change at any moment. Do not cite this document other than as work in progress. SSSOM is community-driven, so all feedback is welcome.

<a name="meta"></a>

## SSSOM Metadata Elements

The SSSOM specification defines a set of SSSOM metadata elements that are used to describe mappings. Apart from the elements themselves, some example usage and a description, **_[the SSSOM spec](https://mapping-commons.github.io/sssom/Mapping/) defines the canonical order for the metadatdata_** in which the elements should appear when serialised. This precludes spurious diffs in a git setting, which is an important concern for the continuous reviewing of mappings by curators and users. 

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
AnnotationAssertion(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:match_type sssom:LexicalEquivalenceMapping) skos:exactMatch <http://purl.obolibrary.org/obo/HP_0009894> <http://purl.obolibrary.org/obo/MP_0000019>)
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
SubClassOf(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:match_type sssom:LexicalEquivalenceMapping) <http://example.org/AA> ObjectSomeValuesFrom(<http://example.org/x> <http://example.org/BB>))
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
ObjectPropertyAssertion(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:match_type sssom:LexicalEquivalenceMapping) <http://www.example.org/x> <http://www.example.org/a> <http://www.example.org/b>)
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
SubClassOf(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:match_type sssom:LexicalEquivalenceMapping) <http://www.example.org/a> <http://www.example.org/b>)
```

### TSV:

All SSSOM metadata elements labelled with L in the metadata table are permissible as column names in the TSV. List elements (such as creator) are "|"-separated. The columns MUST be sorted according to the order as they appear in the [SSSOM metadata](https://mapping-commons.github.io/sssom/Mapping/). For example, the first columns of a mapping set TSV should always be, in that order: subject_id, predicate_id, object_id, match_type, if labels are not included; if they are included, the order should be: subject_id, subject_label, predicate_id, predicate_label, object_id, object_label, match_type. For easier review of diffs, for example git diff or unix diff, we recommend to serialise the TSV by a fixed row order, sorted column by column from left to right.

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
subject_id	predicate_id	object_id	match_type	subject_label	object_label
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
subject_id	predicate_id	object_id	match_type	subject_label	object_label
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
        - `match_type`(s) (Lexical, Logical match, HumanCurated etc)
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
        - For now, if there are _multiple pieces of evidence_ (lexical, logical etc), please emit one row per evidence. If your tool combines multiple pieces of evidence in a complex way, emit yet another row at the end with `match_type` `Complex` and emit ensure you provide the `mapping_tool`.
- _5-Star mappings_ fulfill all the criteria for 4-star mappings and furthermore
    - Are up-to-date with the `subject_source` and `object_source`
    - Have no issue on their issue tracker open for more than 3 months without an interaction
    - Use a _standard_ open license, such as [CC Zero 1.0](https://creativecommons.org/publicdomain/zero/1.0/) or [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
