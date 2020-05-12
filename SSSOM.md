# Simple Standard for Sharing Ontology Mappings (SSSOM)

Working Draft, Updated: 15 April 2020

*Editors:*

* Nicolas Matentzoglu (EMBL-EBI)
* Chris Mungall (LBL)
* Ernesto Jimenez-Ruiz (City, University of London)
* John Graybeal (Stanford)
* William Duncan (LBL)
* David Osumi-Sutherland (EMBL-EBI)
* Simon Jupp (SciBite)


### Abstract
The goal of the Simple Standard for Sharing Ontology Mappings (SSSOM) is to provide a minimal and standard set of elements for the dissemination of 1:1 **_mappings between ontology terms_** to ensure a reliable interpretation of generated mappings and enable sharing between people and applications. 

A "term" is defined in a controlled vocabulary / ontology, and usually corresponds to a class, an individual or a property (entity in OWL, concept in SKOS, resource in RDF). The "subject" is the term on the left side of the mapping, and the "object" is the term on the right side of the mapping. A "predicate" relates the subject with the object and is typically an annotation or object property. A "mapping set" is a set of mappings that can be shared using the SSSOM standard.

Apart from a catalog of metadata elements, we will provide (at least) two serialisations for ontology mappings, aimed at different communities: a TSV serialisation which is aimed at the wider bioinformatics community, and an RDF/OWL serialisation that is aimed at the Knowledge Graph/Semantic Web community. Apart from the format, the main difference between the two serialisations is that we use [CURIE](https://www.w3.org/TR/curie/) syntax to denote entities in the TSV, and IRIs in the RDF based serialisation. Apart from the mappings themselves, we also provide a way to attach meta- and provenance data to **_a set_** of mappings. We will define an unambiguous translation between the TSV and RDF/OWL serialisations as part of this document. 

This document contains:

* A definition of the SSSOM metadata elements
* A controlled vocabulary for the description of match types (SSSOM CV)
* A definition of the two primary serialisations of ontology mappings
* A (non-exhaustive) selection recommended mapping predicates

### Some notes on the standardisation process:

Note this is a public copy of the editors’ draft. It is provided for discussion only and may change at any moment. Do not cite this document other than as work in progress. SSSOM is community-driven, so all feedback is welcome.

### Table of Content

* [SSSOM Metadata Elements](#meta)
* [SSSOM Controlled Vocabulary](#vocab)
* [SSSOM Common Predicates](#predicates)
* [SSSOM Serialisation](#serialisation)
* [SSSOM Use Cases](#usecase)

<a name="meta"/>

# SSSOM Metadata Elements

The following table defines all the SSSOM metadata elements. Elements shaded in grey are required, i.e, should be present for every mapping. Apart from the elements, **_this tables defines the canonical order_** in which the elements should appear when serialised. This precludes spurious diffs in a git setting, which is an important concern for the continuous reviewing of mappings by curators and users. 

*G: The element is global, i.e. pertains to a set of mappings, or local, i.e. pertaining to a single mapping

<table>
  <tr>
    <td>Element ID</td>
    <td>Description</td>
    <td>Example</td>
    <td>G*</td>
  </tr>
  <tr>
    <td>subject_id</td>
    <td>The ID of the subject of the mapping.</td>
    <td>HP:0009894, http://purl.obolibrary.org/obo/HP_0009894</td>
    <td>L</td>
  </tr>
  <tr>
    <td>predicate_id</td>
    <td>The ID of the predicate or relation that relates the subject and object of this match.</td>
    <td>owl:equivalentClass</td>
    <td>L</td>
  </tr>
  <tr>
    <td>object_id</td>
    <td>The ID of the object of the mapping.</td>
    <td>MP:0000019, http://purl.obolibrary.org/obo/MP_0000019</td>
    <td>L</td>
  </tr>
  <tr>
    <td>match_type</td>
    <td>ID from Match type (SSSOM:MatchType) branch of the SSSSOM Vocabulary. In the case of multiple match types for a single subject, predicate, object triplet, two seperate mappings must be specified.</td>
    <td>SSSOM:LexicalEquivalenceMatch</td>
    <td>L</td>
  </tr>
  <tr>
    <td>creator_id</td>
    <td>Identifies the persons or groups responsible for the creation of the mapping. Recommended to be a (pipe-separated) list of ORCIDs or otherwise identifying URLs, but any identifying string (such as name and affiliation) is permissible.</td>
    <td>https://orcid.org/0000-0002-7356-1779</td>
    <td>G/L</td>
  </tr>
  <tr>
    <td>creator_label</td>
    <td>A string identifying the creator of this mapping. In the spirit of provenance, consider to use creator_id instead.</td>
    <td>Lebron James, LA Lakers</td>
    <td>G/L</td>
  </tr>
  <tr>
    <td>license</td>
    <td>A url to the license of the mapping. In absence of a license we assume no license.</td>
    <td>https://creativecommons.org/licenses/by/3.0/</td>
    <td>G/L</td>
  </tr>
  <tr>
    <td>subject_label</td>
    <td>The label of subject of the mapping</td>
    <td>Thickened ears</td>
    <td>L</td>
  </tr>
  <tr>
    <td>object_label</td>
    <td>The label of object of the mapping</td>
    <td>thick ears</td>
    <td>L</td>
  </tr>
  <tr>
    <td>predicate_label</td>
    <td>The label of the predicate/relation of the mapping</td>
    <td>equivalent to</td>
    <td>L</td>
  </tr>
  <tr>
    <td>subject_source</td>
    <td>IRI of ontology source for the subject. Version IRI preferred.</td>
    <td>http://purl.obolibrary.org/obo/hp.owl</td>
    <td>G/L</td>
  </tr>
  <tr>
    <td>object_source</td>
    <td>IRI of ontology source for the object. Version IRI preferred.</td>
    <td>http://purl.obolibrary.org/obo/mp.owl</td>
    <td>G/L</td>
  </tr>
  <tr>
    <td>subject_source_version</td>
    <td>Version IRI of the source of the subject term.</td>
    <td>http://purl.obolibrary.org/obo/hp/releases/2020-03-27/hp-base.owl</td>
    <td>G/L</td>
  </tr>
  <tr>
    <td>object_source_version</td>
    <td>Version IRI of the source of the object term.</td>
    <td>http://purl.obolibrary.org/obo/mp/releases/2020-04-14/mp-base.owl</td>
    <td>G/L</td>
  </tr>
  <tr>
    <td>mapping_provider</td>
    <td>URL pointing to the source that provided the mapping, for example an ontology that already contains the mappings.</td>
    <td>http://www.ebi.ac.uk/efo/efo.owl</td>
    <td>G/L</td>
  </tr>
  <tr>
    <td>mapping_tool</td>
    <td>A reference to the tool or algorithm that was used to generate the mapping. Should be a URL pointing to more info about it, but can be free text.</td>
    <td>https://github.com/ernestojimenezruiz/logmap-matcher</td>
    <td>G/L</td>
  </tr>
  <tr>
    <td>mapping_date</td>
    <td>The date the mapping was computed</td>
    <td>2020-02-29</td>
    <td>G/L</td>
  </tr>
  <tr>
    <td>confidence</td>
    <td>A score between 0 and 1 to denote the confidence or probability that the match is correct, where 1 denotes total confidence.</td>
    <td>0.3</td>
    <td>L</td>
  </tr>
  <tr>
    <td>subject_match_field</td>
    <td>A tuple of fields (term annotations on the subject) that was used for the match. Should be used in conjunction with lexical and complexes matches, see SSSOM match types below.</td>
    <td>oio:hasExactSynonym|rdfs:label</td>
    <td>G/L</td>
  </tr>
  <tr>
    <td>object_match_field</td>
    <td>A tuple of fields (term annotations on the object) that was used for the match. Should be used in conjunction with lexical and complexes matches, see SSSOM match types below.</td>
    <td>oio:hasExactSynonym|rdfs:label</td>
    <td>G/L</td>
  </tr>
  <tr>
    <td>match_string</td>
    <td>String that is shared by subj/obj</td>
    <td>Thick ear</td>
    <td>L</td>
  </tr>
  <tr>
    <td>subject_preprocessing</td>
    <td>Method of preprocessing applied to the fields of the subject. Tuple of IDs from "Pre-processing method" (SSSOM:PreprocessingMethod) branch of the SSSSOM Vocabulary.</td>
    <td>SSSOM:Stemming</td>
    <td>G/L</td>
  </tr>
  <tr>
    <td>object_preprocessing</td>
    <td>Method of preprocessing applied to the fields of the object. Tuple of IDs from “Pre-processing method” (SSSOM:PreprocessingMethod) branch of the SSSSOM Vocabulary.</td>
    <td>SSSOM:Stemming</td>
    <td>G/L</td>
  </tr>
  <tr>
    <td>match_term_type</td>
    <td>Specifies what type of terms are being matched (class, property, or individual). Value should be ID from Term Match (SSSOM:TermMatch) branch of the SSSSOM Vocabulary. </td>
    <td>SSSOM:ClassMatch</td>
    <td>G/L</td>
  </tr>
  <tr>
    <td>semantic_similarity_score</td>
    <td>A score between 0 and 1 to denote the semantic similarity, where 1 denotes equivalence.</td>
    <td>0.8</td>
    <td>L</td>
  </tr>
  <tr>
    <td>information_content_mica_score</td>
    <td>A score between 0 and 1 to denote the information content of the most informative common ancestor, where 1 denotes the maximum level of informativeness.</td>
    <td>0.3</td>
    <td>L</td>
  </tr>
  <tr>
    <td>see_also</td>
    <td>A URL specific for the mapping instance. E.g. for kboom we have a per-mapping image that shows surrounding axioms that drive probability. Could also be a github issue URL that discussed a complicated alignment</td>
    <td>https://user-images.githubusercontent.com/6722114/29056483-25e371e0-7bb8-11e7-8d27-5b4c3b1843fd.png</td>
    <td>G/L</td>
  </tr>
  <tr>
    <td>other</td>
    <td>Pipe separated list of key value pairs for properties not part of the SSSOM spec. Can be used to encode additional provenance data.</td>
    <td>subject_information_content: 0.1|object_information_content: 0.3|github_issue: http://issue.org</td>
    <td>G/L</td>
  </tr>
  <tr>
    <td>comment</td>
    <td>Free text field containing either curator notes or text generated by tool providing additional informative information. </td>
    <td>“Match should be reviewed manually.”</td>
    <td>G/L</td>
  </tr>
</table>

<a name="vocab"/>

# The SSSOM Controlled Vocabulary

The SSSOM Vocabulary is a Controlled Vocabulary (CV) for representing the method by which a mapping was produced. **The following excerpt only gives a sense of the vocabulary (i.e. is incomplete and unstructured)** - the actual implementation will be done in the usual way as a linked data vocabulary in rdf. In the OWL/RDF serialisation, matches are connected to match types using dc:type.

The vocabulary (http://purl.org/sssom/sssom.owl) is managed here:

* Robot [template](sssom_vocab.tsv)
* [Vocab](sssom_vocab.tsv) (OWL)

<a name="predicates"/>

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

<a name="serialisation"/>

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

For example, sssomMeta could be:

```
sssom:creator orcid:001
sssom:match_type: SSSOM:LexicalEquivalenceMapping
```

Which would materialise as:
AnnotationAssertion(Annotation(sssom:creator,orcid:001) Annotation(sssom:match_type, SSSOM:LexicalEquivalenceMapping) P, S, O)

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

Case 2: Object and Subject are individuals

The Mapping <S,P,O> gets translated into an object property assertion: 

```
ObjectPropertyAssertion(P, A, O)
```

All metadata elements are added as OWLAnnotation objects and added to ObjectPropertyAssertion axiom as axiom annotations:

```
ObjectPropertyAssertion(sssomMetadata, P, A, O)
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


### SSSOM Metadata Element Mapping to common properties

Some SSSOM metadata elements have known equivalent properties which will be used in the OWL serialisation. 

TBD: These mappings could be specified in the default JSON-LD context.

<table>
  <tr>
    <td>Element ID</td>
    <td>Mapped to</td>
  </tr>
  <tr>
    <td>creator</td>
    <td>dc:creator</td>
  </tr>
  <tr>
    <td>license</td>
    <td>dce:license</td>
  </tr>
  <tr>
    <td>date_mapping</td>
    <td>dc:date</td>
  </tr>
  <tr>
    <td>see_also</td>
    <td>rdfs:seeAlso</td>
  </tr>
</table>


## TSV:

All SSSOM metadata elements labelled with L in the metadata table are permissible as column names in the TSV. List elements (such as creator) are "|"-separated. The columns MUST be sorted according to the order as they appear in the SSSOM metadata table. For example, the first four columns should always be, in that order: subject_id, predicate_id, object_id, match_type. For easier review of diffs, for example git diff or unix diff, we recommend to serialise the TSV by a fixed row order, sorted column by column from left to right.

Metadata about a set of mappings can be supplied as part of the mappings (embedded mode) and as a simple JSON LD. Note that for the TSV, it will be required to supply a valid curie map that allows the unambiguous interpretation of CURIEs. A curie map is supplied after a curie_map: parameter in the JSON LD file. The value can be either a dictionary of CURIE->URLPREFIX pairs or a link to a valid curie map of the same shape.

Note that only metadata elements permissible in a global context (G*) can be used in the metadatafile:

```
SSSOMELEMENT: VALUE
```


SSSOMELEMENT: any element from the SSSOM set of metadata elements.

VALUE: the literal value permissible according to the SSSOM set of metadata elements specification.

Example:

```
"creator": "orcid:01"	
"date":	“2020-09-2020"	
"source": https://www.ebi.ac.uk/ols/index"	
"curie_map": 
 {
  “BRO”: “http://bioontology.org/ontologies/BiomedicalResourceOntology.owl#"
  “HP”: “http://purl.obolibrary.org/HP_"
}
```

### External mode 

In external mode, the mapping set metadata is supplied by a separate JSON LD file having the same base-name of the mapping file, with the extension -metadata.yml. The a resolvable link to the mapping file should be included in the form of a comment:

```
# "metadata": “http://example.org/mapping/hp-mp-mapping.json”
subject	predicate	object	match_type
HP:0009124	oio:database_cross_reference	MP:0000003	SSSOM:0000101
HP:0008551	oio:database_cross_reference	MP:0000018	SSSOM:0000101
HP:0000411	oio:database_cross_reference	MP:0000021	SSSOM:0000101
```


### Embedded mode

In the embedded mode, we allow the integration of mapping set level metadata as **_commented JSON LD_**. Apart from being commented, the JSON LD follows the exact same spec as the *JSON LD specified by the external mode*. Heavily used tools in bioinformatics such as pandas allow to [specify comment characters](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) when reading CSV files, which makes this option the most user friendly for this community. Additionally, it is a simple unix-level or language-level operation to filter these as a pre-processing in a robust fashion.

Example:

```
# "creator": “orcid:01”	
# “date”: “2020-09-2020”	
# “source: https://www.ebi.ac.uk/ols/index”	
# “curie_map”: 
# {
#  “BRO”: “http://bioontology.org/ontologies/BiomedicalResourceOntology.owl#”
#  “HP”: “http://purl.obolibrary.org/HP_”
# }
subject	predicate	object	match_type
HP:0009124	oio:database_cross_reference	MP:0000003	SSSOM:0000101
HP:0008551	oio:database_cross_reference	MP:0000018	SSSOM:0000101
HP:0000411	oio:database_cross_reference	MP:0000021	SSSOM:0000101
```


*Notes:*

* ROBOT implementation: [https://github.com/ontodev/robot/issues/312](https://github.com/ontodev/robot/issues/312)

## JSON:

* TBD in the future
* JSON-LD vs JSON
* Ernesto showed interest

<a name="usecase"/>

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

