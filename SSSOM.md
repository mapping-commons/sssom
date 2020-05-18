# Simple Standard for Sharing Ontology Mappings (SSSOM)

Development Draft (under construction, do not use), Updated: 15 April 2020

*Editors:*

* Nicolas Matentzoglu (EMBL-EBI)
* Chris Mungall (LBL)
* Ernesto Jimenez-Ruiz (City, University of London)
* John Graybeal (Stanford)
* William Duncan (LBL)
* David Osumi-Sutherland (EMBL-EBI)
* Simon Jupp (SciBite)
* James McLaughlin (EMBL-EBI)

### Abstract

Mappings, or cross-references, are used to link terms across different ontologies. However, there is currently little to no standardisation in how such mappings are represented. While properties such as hasDbXref property are widely used in ontologies such as GO and MONDO, the meaning of such mappings is unclear, and cannot be further described with additional metadata or provenance.

The Simple Standard for Sharing Ontology Mappings (SSSOM) is an initiative to provide a minimal and standard set of elements for the dissemination of 1:1 mappings between ontology terms, to ensure a reliable interpretation of generated mappings and to enable sharing and data integration between people and applications. 

This document introduces the SSSOM catalog of metadata elements, which can be used to attach meta- and provenance data to both mappings and sets of mappings; a controlled vocabulary for the description of match types (SSSOM CV); a definition of both RDF and TSV serialisations of ontology mappings; and a (non-exhaustive) selection of recommended mapping predicates.

### Table of Contents

* [Introduction](#intro)
* [SSSOM Metadata Elements](#meta)
* [SSSOM Controlled Vocabulary](#vocab)
* [SSSOM Common Predicates](#predicates)
* [SSSOM Serialisation](#serialisation)
* [SSSOM Use Cases](#usecase)

<a name="intro"></a>

### Introduction

Currently, there are three methods typically used to express mappings in OWL: direct logical axioms using owl:equivalentClass; the oboInOwl hasDbXref property; and the SKOS vocabulary for mapping properties.  The first, owl:equivalentClass, is a strong logical equivalence assertion which is not appropriate for more nuanced mappings such as close matches.  The second, hasDbXref, does not assert formal logical equivalence but also has no clearly defined meaning.  Finally, the SKOS vocabulary provides a hierarchy of mapping properties which allow the unambigous specification of exact, close, broad, and narrow matches, but does not provide the means for mappings to be annotated with additional metadata such as confidence scores and provenance.

The Simple Standard for Sharing Ontology Mappings (SSSOM) addresses these problems by defining a catalog of metadata terms to describe mappings.  Both individual mappings and **_sets of_** mappings can be described, enabling provenance and metadata to be captured on multiple levels.  SSSOM interoperates with existing methods for the specification of mappings, allowing any predicate to be used to describe the nature of each mapping including those from OWL and SKOS.

The provenance of mappings - such as whether the mapping was created as the result of a human-curated equivalence match, or a semantic similarity match - is specified using a controlled vocabulary (CV), SSSOM CV.  Combined with the metadata properties provided by SSSOM such as confidence and semantic_similarity_score, this provenance information can be used to capture mapping descriptions in a manner that is explicit and amenable to curation.

Two serialisations for SSSOM mappings are provided in this document, aimed at different communities: an RDF/OWL serialisation using IRIs that is aimed at the Knowledge Graph/Semantic Web community, and a TSV serialisation using [CURIE](https://www.w3.org/TR/curie/) syntax which is aimed at the wider bioinformatics community.  An unambiguous translation between these serialisations is provided.


### Some notes on the standardisation process:

Note this is a public copy of the editors’ draft. It is provided for discussion only and may change at any moment. Do not cite this document other than as work in progress. SSSOM is community-driven, so all feedback is welcome.

<a name="meta"></a>

# SSSOM Metadata Elements

The SSSOM specification defines a set of SSSOM metadata elements that are used to describe mappings. Apart from the elements themselves, some example usage and status like 'required', **_[the metadata element table](sssom_metadata.tsv) defines the canonical order_** in which the elements should appear when serialised. This precludes spurious diffs in a git setting, which is an important concern for the continuous reviewing of mappings by curators and users. 

A "term" is defined in a controlled vocabulary / ontology, and usually corresponds to a class, an individual or a property (entity in OWL, concept in SKOS, resource in RDF). The "subject" is the term on the left side of the mapping, and the "object" is the term on the right side of the mapping. A "predicate" relates the subject with the object and is typically an annotation or object property. A "mapping set" is a set of mappings that can be shared using the SSSOM standard.

Some elements are global (annotated with "G" using `sssom:scope`), i.e. pertains to a set of mappings, or local (annotated with "L" using `sssom:scope`), i.e. pertaining to a single mapping. Most elements can be used both as global and local; global elements should be interpreted to applying to all mappings in the mapping set. 

Note that some SSSOM metadata elements have known equivalent properties which will be used in the OWL serialisation.
These are declared as equivalent as part of the metadata vocabulary.

The metadata vocabulary is managed here:

* Robot [template](sssom_metadata.tsv)
* [Vocab](sssom_metadata.owl) (OWL)

<a name="vocab"></a>

# The SSSOM Controlled Vocabulary

The SSSOM Vocabulary is a Controlled Vocabulary (CV) for representing the method by which a mapping was produced. **The following excerpt only gives a sense of the vocabulary (i.e. is incomplete and unstructured)** - the actual implementation will be done in the usual way as a linked data vocabulary in rdf. In the OWL/RDF serialisation, matches are connected to match types using dc:type.

The vocabulary (http://purl.org/sssom/sssom.owl) is managed here:

* Robot [template](sssom_vocab.tsv)
* [Vocab](sssom_vocab.owl) (OWL)

<a name="predicates"></a>

# Common Mapping Predicates

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
    <td>The subject is taxonomically narrower than the object.</td>
  </tr>
  <tr>
    <td>skos:broadMatch</td>
    <td>The subject is taxonomically broader than the object.</td>
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

# Serialisation

## RDF/XML serialised re-ified OWL axioms:

The default RDFXML serialisation of the mappings will be realised as *reified OWL axioms*. This has the advantage that any mapping set can be simply merged with an ontology in the usual way, for example using [ROBOT merge](http://robot.obolibrary.org/merge). We will deal with three types of reified OWL-axioms, and a few sub-types:

1. Predicate is an annotation property
2. Predicate is an object property and
   1. Object/Subject are classes
   2. Object/Subject are individuals
3. Predicate is language relational construct of RDFS or OWL (rdfs:subClassOf, owl:equivalentClass)

### Predicate is an annotation property:

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
AnnotationAssertion(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:match_type SSSOMC:LexicalEquivalenceMapping) skos:exactMatch <http://purl.obolibrary.org/obo/HP_0009894> <http://purl.obolibrary.org/obo/MP_0000019>)
```

Mapping set level annotations are manifested as Ontology annotation in the usual way, according to the [OWL 2 Structural Specification](https://www.w3.org/TR/owl2-syntax/#Annotations).

### Predicate is an object property

#### Case 1: Object and Subject are classes.

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
SubClassOf(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:match_type SSSOMC:LexicalEquivalenceMapping) <http://example.org/AA> ObjectSomeValuesFrom(<http://example.org/x> <http://example.org/BB>))
```

#### Case 2: Object and Subject are individuals

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
ObjectPropertyAssertion(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:match_type SSSOMC:LexicalEquivalenceMapping) <http://www.example.org/x> <http://www.example.org/a> <http://www.example.org/b>)
```

### Predicate is language relational construct of RDFS or OWL

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
SubClassOf(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:match_type SSSOMC:LexicalEquivalenceMapping) <http://www.example.org/a> <http://www.example.org/b>)
```

## TSV:

All SSSOM metadata elements labelled with L in the metadata table are permissible as column names in the TSV. List elements (such as creator) are "|"-separated. The columns MUST be sorted according to the order as they appear in the SSSOM metadata [table](sssom_metadata.tsv). For example, the first columns of a mapping set TSV should always be, in that order: subject_id, predicate_id, object_id, match_type, if labels are not included; if they are included, the order should be: subject_id, subject_label, predicate_id, predicate_label, object_id, object_label, match_type. For easier review of diffs, for example git diff or unix diff, we recommend to serialise the TSV by a fixed row order, sorted column by column from left to right.

Metadata about a set of mappings can be supplied as part of the mappings (embedded mode) and as a simple yaml file alongside the primary mapping file. Note that for the TSV, it will be required to supply a valid curie map that allows the unambiguous interpretation of CURIEs. A curie map is supplied after a `curie_map:` parameter in the yaml file. The value can be either a dictionary of CURIE->URLPREFIX pairs or a link to a valid curie map of the same shape.

Note that only metadata elements permissible in a global context (G, or L/G) can be used in the external metadata-file.

Example ([download](https://raw.githubusercontent.com/matentzn/SSSOM/master/examples/external/mp-hp-exact-0.0.1-meta.yml)):

```
creator_id: "https://orcid.org/0000-0002-7356-1779"
curie_map: 
  HP: "http://purl.obolibrary.org/obo/HP_"
  MP: "http://purl.obolibrary.org/obo/MP_"
  skos: "http://www.w3.org/2004/02/skos/core"
license: "https://creativecommons.org/publicdomain/zero/1.0/"
mapping_provider: "http://purl.obolibrary.org/obo/upheno.owl"
```

### External mode 

In external mode, the mapping set metadata is supplied by a separate YAML file having the same base-name of the mapping file, with the extension `-meta.yml`. By default, tools will look for the file of that name in the same directory as the the mapping set table.

Example ([download](https://raw.githubusercontent.com/matentzn/SSSOM/master/examples/external/mp-hp-exact-0.0.1.tsv)):

```
subject_id	predicate_id	object_id	match_type	subject_label	object_label
HP:0009124	skos:exactMatch	MP:0000003	Lexical	Abnormal adipose tissue morphology	abnormal adipose tissue morphology
HP:0008551	skos:exactMatch	MP:0000018	Lexical	Microtia	small ears
HP:0000411	skos:exactMatch	MP:0000021	Lexical	Protruding ear	prominent ears
```

### Embedded mode

In the embedded mode, we allow the integration of mapping set level metadata as **_commented YAML_**. Apart from being commented, the YAML follows the exact same spec as the *YAML specified by the external mode*. Heavily used tools in bioinformatics such as pandas allow to [specify comment characters](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) when reading CSV files, which makes this option the most user friendly for this community. Additionally, it is a simple unix-level or language-level operation to filter these as a pre-processing in a robust fashion.

Example ([download](https://raw.githubusercontent.com/matentzn/SSSOM/master/examples/embedded/mp-hp-exact-0.0.1.tsv)):

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

## JSON:

* TBD in the future
* JSON-LD vs JSON
* Ernesto showed interest

<a name="usecase"></a>

# Use Cases:

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

<hr>
<hr>

Not part of spec, clean up.

# Notes:

* Mapping notes SNOMED-ORPHANET (codes)

    * [https://confluence.ihtsdotools.org/download/attachments/14746117/IHTSDO%20INSERM%20SNOMED%20CT%20EXPO%202015%201.0.pdf?version=1&modificationDate=1446570840000&api=v2](https://confluence.ihtsdotools.org/download/attachments/14746117/IHTSDO%20INSERM%20SNOMED%20CT%20EXPO%202015%201.0.pdf?version=1&modificationDate=1446570840000&api=v2)

    * Codes:

        * E exact mapping (the terms and the concepts are equivalent)

        * NTBT narrower term maps to a broader term

        * BTNT broader term maps to a narrower term

        * W incorrect mapping (two different concepts)

        * NTBT/E narrower term maps to a broader term because of an exact mapping with a synonym in the target terminology

        * BTNT/E broader term maps to a narrower term because of an exact mapping with a synonym

        * in the target terminology

        * W/E incorrect mapping (two different concepts) but syntactically exact mapping to a synonym or a preferred term in the target terminology

        * ND not yet decided/unable to decide

* SNOMED mapping categories:

    * [https://browser.ihtsdotools.org/?perspective=full&conceptId1=447634004&edition=MAIN/2020-03-09&release=&languages=en](https://browser.ihtsdotools.org/?perspective=full&conceptId1=447634004&edition=MAIN/2020-03-09&release=&languages=en)

* Possibility of complex mappings (mappings between tuples of terms, connected by patterns)

* Ernesto: In the Ontology Matching community we use RDF alignment format (http://alignapi.gforge.inria.fr/format.html). It is very limited but also simple for the OAEI evaluation. We could think in some sort of extension of this format.

* Many SSSOM metadata elements can be mapped to directly to standard properties

* Check [http://alignapi.gforge.inria.fr/format.html](http://alignapi.gforge.inria.fr/format.html)
* How to we determine the type of the predicate (annotation or object property) at conversion time? Is this extra information that needs to be provided? Lookup in some ontology?
* Sometimes annotations reference IRIs. We may need to consider if we want to distinguish between a literal value and an IRI.
* Can we have more complex logical mappings? A common use case is a taxon-specific anatomy ontology (taxon X). We want to map A to B, but say that B is not equivalent to A, rather it is equivalent to an OWL expression based on A (A and 'in taxon' some X). But there are plenty of arbitrary expressions that could be supported. A while back I looked at some SNOMED to Uberon mappings; it seemed like a lot of the SNOMED terms would better be ('part of' some UBERON:X) rather than directly equivalent to X.
*  explicitly declare the metadata elements as equivalent to properties?
* What about mapping to Literals in general? Is this in-spec?
