# Simple Standard for Sharing Ontology Mappings (SSSOM)

Development Draft (under construction: some metadata fields may be subject to change)

*Editors:*

* Nicolas Matentzoglu (EMBL-EBI)
* Chris Mungall (LBL)
* Ernesto Jimenez-Ruiz (City, University of London)
* John Graybeal (Stanford)
* William Duncan (LBL)
* David Osumi-Sutherland (EMBL-EBI)
* Simon Jupp (SciBite)
* James McLaughlin (EMBL-EBI)
* Henriette Harmse (EMBL-EBI)
* Tiffany Callahan (@callahantiff)
* Charlie Hoyt (Harvard Medical School; [@cthoyt](https://github.com/cthoyt))
* Thomas Liener (Pistoia Alliance)
* Harshad Hegde (LBL)

Contributors:
* Balhoff, James P.
* Chute, Christopher
* Dahzi, Jiao
* Gabriel, Davera
* Haendel, Melissa
* Harold, Solbrig
* Harris, Nomi
* Kim, Hyeongsik
* Koehler, Sebastian
* Malone, James
* Munoz-Torres, Monica
* Overton, James
* Thessen, Anne
* Vasilevsky, Nicole


### Abstract

Mappings, or cross-references, are used to link terms across different ontologies. However, there is currently little to no standardisation in how such mappings are represented. While properties such as hasDbXref property are widely used in ontologies such as GO and MONDO, the meaning of such mappings is unclear, and cannot be further described with additional metadata or provenance.

The Simple Standard for Sharing Ontology Mappings (SSSOM) is an initiative to provide a minimal and standard set of elements for the dissemination of mappings between ontology terms, to ensure a reliable interpretation of generated mappings and to enable sharing and data integration between people and applications. 

This document introduces the SSSOM catalog of metadata elements, which can be used to attach meta- and provenance data to both mappings and sets of mappings; a controlled vocabulary for the description of match types (SSSOM CV); a definition of both RDF and TSV serialisations of ontology mappings; and a (non-exhaustive) selection of recommended mapping predicates.

### Table of Contents

* [Introduction](#intro)
* [SSSOM Metadata Elements](#meta)
* [SSSOM Controlled Vocabulary](#vocab)
* [SSSOM Common Predicates](#predicates)
* [SSSOM Serialisation](#serialisation)
* [SSSOM Use Cases](#usecase)
* [Minimum Metadata Recommendation](#minimum)

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

## Metadata Element Table

Element ID | Description | TSV Example | RDF example | scope | req.
-- | -- | -- | -- | -- | --
subject_id | The ID of the subject of the mapping. | HP:0009894 | http://purl.obolibrary.org/obo/HP_0009894 | L | 1
subject_label | The label of subject of the mapping | Thickened ears | Thickened ears | L | 0
subject_category | The conceptual category to which the subject belongs to. This can be a string denoting the category or a term from a controlled vocabulary. | COB:0000022 | http://purl.obolibrary.org/obo/COB_0000022 | L | 0
predicate_id | The ID of the predicate or relation that relates the subject and object of this match. | owl:equivalentClass | owl:equivalentClass | L | 1
predicate_label | The label of the predicate/relation of the mapping | equivalent to | equivalent to | L | 0
object_id | The ID of the object of the mapping. | MP:0000019 | http://purl.obolibrary.org/obo/MP_0000019 | L | 1
object_label | The label of object of the mapping | thick ears | thick ears | L | 0
object_category | The conceptual category to which the object belongs to. This can be a string denoting the category or a term from a controlled vocabulary. | COB:0000022 | http://purl.obolibrary.org/obo/COB_0000022 | L | 0
match_type | ID from Match type (SSSOM:MatchType) branch of the SSSSOM Vocabulary. In the case of multiple match types for a single subject, predicate, object triplet, two seperate mappings must be specified. | SSSOM:LexicalEquivalenceMatch | http://purl.org/sssom/type/LexicalEquivalenceMatch | L | 1
mapping_set_id | A globally unique identifier for the mapping set (not each individual mapping). Should be IRI, ideally resolvable. | http://purl.obolibrary.org/obo/upheno/mapping/mp-hp | http://purl.obolibrary.org/obo/upheno/mapping/mp-hp | G | 0
mapping_set_description | A description of the mapping set. | The official Pistoia MP-HP mappings, generated by Paxo. | The official Pistoia MP-HP mappings, generated by Paxo. | G | 0
mapping_set_version | A version string for the mapping. | 2.3 | 2.3 | G | 0
creator_id | Identifies the persons or groups responsible for the creation of the mapping. Recommended to be a (pipe-separated) list of ORCIDs or otherwise identifying URLs, but any identifying string (such as name and affiliation) is permissible. | https://orcid.org/0000-0002-7356-1779\|https://orcid.org/0000-0002-7356-XXXX | https://orcid.org/0000-0002-7356-1779 | G/L | 0
creator_label | A string identifying the creator of this mapping. In the spirit of provenance, consider to use creator_id instead. | Lebron James, LA Lakers | Lebron James, LA Lakers | G/L | 0
license | A url to the license of the mapping. In absence of a license we assume no license. | https://creativecommons.org/licenses/by/3.0/ | https://creativecommons.org/licenses/by/3.0/ | G/L | 0
subject_source | IRI of ontology source for the subject. Version IRI preferred. | http://purl.obolibrary.org/obo/hp.owl | http://purl.obolibrary.org/obo/hp.owl | G/L | 0
subject_source_version | Version IRI of the source of the subject term. | http://purl.obolibrary.org/obo/hp/releases/2020-03-27/hp-base.owl | http://purl.obolibrary.org/obo/hp/releases/2020-03-27/hp-base.owl | G/L | 0
object_source | IRI of ontology source for the object. Version IRI preferred. | http://purl.obolibrary.org/obo/mp.owl | http://purl.obolibrary.org/obo/mp.owl | G/L | 0
object_source_version | Version IRI of the source of the object term. | http://purl.obolibrary.org/obo/mp/releases/2020-04-14/mp-base.owl | http://purl.obolibrary.org/obo/mp/releases/2020-04-14/mp-base.owl | G/L | 0
mapping_provider | URL pointing to the source that provided the mapping, for example an ontology that already contains the mappings. | http://www.ebi.ac.uk/efo/efo.owl | http://www.ebi.ac.uk/efo/efo.owl | G/L | 0
mapping_tool | A reference to the tool or algorithm that was used to generate the mapping. Should be a URL pointing to more info about it, but can be free text. | https://github.com/ernestojimenezruiz/logmap-matcher | https://github.com/ernestojimenezruiz/logmap-matcher | G/L | 0
mapping_date | The date the mapping was computed | 29/02/2020 | 29/02/2020 | G/L | 0
mapping_cardinality | A string indicating whether this mapping is from a 1:1 (the subject_id maps to a single object_id), 1:n (the subject maps to more than one object_id), n:1, 1:0, 0:1 or n:n group. Note that this is a convenience field that should be derivable from the mapping set. | 1:1 | 1:1 | L | 0
confidence | A score between 0 and 1 to denote the confidence or probability that the match is correct, where 1 denotes total confidence. | 0.3 | 0.3 | L | 0
subject_match_field | A tuple of fields (term annotations on the subject) that was used for the match. Should be used in conjunction with lexical and complexes matches, see SSSOM match types below. | oio:hasExactSynonym\|rdfs:label | oio:hasExactSynonym\|rdfs:label | G/L | 0
object_match_field | A tuple of fields (term annotations on the object) that was used for the match. Should be used in conjunction with lexical and complexes matches, see SSSOM match types below. | oio:hasExactSynonym\|rdfs:label | oio:hasExactSynonym\|rdfs:label | G/L | 0
match_string | String that is shared by subj/obj | Thick ear | Thick ear | L | 0
subject_preprocessing | Method of preprocessing applied to the fields of the subject. Tuple of IDs from "Pre-processing method" (SSSOM:PreprocessingMethod) branch of the SSSSOM Vocabulary. | SSSOM:Stemming | http://purl.org/sssom/type/Stemming | G/L | 0
object_preprocessing | Method of preprocessing applied to the fields of the object. Tuple of IDs from “Pre-processing method” (SSSOM:PreprocessingMethod) branch of the SSSSOM Vocabulary. | SSSOM:Stemming | http://purl.org/sssom/type/Stemming | G/L | 0
match_term_type | Specifies what type of terms are being matched (class, property, or individual). Value should be ID from Term Match (SSSOM:TermMatch) branch of the SSSSOM Vocabulary. | SSSOM:ClassMatch | http://purl.org/sssom/type/ClassMatch | G/L | 0
semantic_similarity_score | A score between 0 and 1 to denote the semantic similarity, where 1 denotes equivalence. | 0.8 | 0.8 | L | 0
information_content_mica_score | A score between 0 and 1 to denote the information content of the most informative common ancestor, where 1 denotes the maximum level of informativeness. | 0.3 | 0.3 | L | 0
see_also | A URL specific for the mapping instance. E.g. for kboom we have a per-mapping image that shows surrounding axioms that drive probability. Could also be a github issue URL that discussed a complicated alignment | https://user-images.githubusercontent.com/6722114/29056483-25e371e0-7bb8-11e7-8d27-5b4c3b1843fd.png | https://user-images.githubusercontent.com/6722114/29056483-25e371e0-7bb8-11e7-8d27-5b4c3b1843fd.png | G/L | 0
other | Pipe separated list of key value pairs for properties not part of the SSSOM spec. Can be used to encode additional provenance data. | subject_information_content: 0.1\|object_information_content: 0.3\|github_issue: http://issue.org | subject_information_content: 0.1\|object_information_content: 0.3\|github_issue: http://issue.org | G/L | 0
comment | Free text field containing either curator notes or text generated by tool providing additional informative information. | Match should be reviewed manually | Match should be reviewed manually | G/L | 0

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

Metadata about a set of mappings can be supplied as part of the mappings (embedded mode) and as a simple yaml file alongside the primary mapping file. Note that for the TSV, it will be required to supply a valid curie map that allows the unambiguous interpretation of CURIEs. A curie map is supplied after a `curie_map:` parameter in the yaml file. The value can be either a dictionary of CURIE->URLPREFIX pairs or a link to a valid curie map of the same shape. The metadata and mapping set are implicitly to connected to the [SSSOM jsonld context](context.jsonld).

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

### External mode 

In external mode, the mapping set metadata is supplied by a separate YAML file having the same base-name of the mapping file, with the extension `-meta.yml`. By default, tools will look for the file of that name in the same directory as the the mapping set table.

Example ([download](https://raw.githubusercontent.com/matentzn/SSSOM/master/examples/external/mp-hp-exact-0.0.1.sssom.tsv)):

```
subject_id	predicate_id	object_id	match_type	subject_label	object_label
HP:0009124	skos:exactMatch	MP:0000003	Lexical	Abnormal adipose tissue morphology	abnormal adipose tissue morphology
HP:0008551	skos:exactMatch	MP:0000018	Lexical	Microtia	small ears
HP:0000411	skos:exactMatch	MP:0000021	Lexical	Protruding ear	prominent ears
```

### Embedded mode (default)

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

<a name="minimum"></a>

### Minimum Metadata Recommendation

Current mappings are extremely hard to use for data integration, because they are:

- non-transparently imprecise
- non-transparently incomplete
- inaccurate
- unFAIR

In principle, to reach full integration through mappings, you will have to cross-map all ontologies, or semantic
spaces, which means if you have N "spaces", you have N x N (-1) mappings. To mitigate the explosion
of mappings, we have to be able to cross-walk:
- multi-hop forward walks `{ O1:A->O2:A, O2:A->O3:A } --> {O1:A->O3:A}`
- walk-backs `{ O1:A->O2:A } --> {O2:A->O1:A}`
- combinations `{ O1:A->O2:A, O2:A->O3:A, O4:A->O3:A } --> {O1:A->O4:A}`

To enable cross-walking, we propose the following 5 star system for mapping metadata. 

1. _1-star mappings_ fulfill the following criteria:
   - record subject id, object id and mapping precision
   - using qualified names (either URIs or CURIEs + curie maps) for subject id and object id
   - using a standard file format (JSON, XML, CSV, TSV)
   - made available in a public space
   - _optional_: record the subject and object labels to make it easier for humans to read the file
2. _2-star mappings_ fulfill all the criteria for 1-star mappings and furthermore
   - made available in a public version control system with an issue tracker
   - record the semantic predicate explicitly
   - using qualified names for the semantic predicate (i.e. owl:equivalentClass, skos:exactMatch)
   - record a confidence value for the mapping between 0 and 1.
   - record an open license for the use of the mapping set
3. _3-star mappings_ fulfill all the criteria for 2-star mappings and furthermore 
   - are stored in SSSOM format
   - record the following additional metadata: 
     - `match_type`(s) (Lexical, Logical match, HumanCurated etc)
     - `date` of the mapping
     - `creator_id`
     - `subject_source`
     - `object_source`
     - `subject_source_version`
     - `object_source_version`
     - `mapping_tool` if the mapping was automatically computed using a tool
4. _4-star mappings_ fulfill all the criteria for 3-star mappings and furthermore
   - Register the mapping at a mapping commons
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
     - if the mapping is `Logical`, the mapping should be derivable by a reasoner from
      a combination of the `object_source` and `subject_source`. If more is needed then please 
      leave a `comment` with details.
     - if the mapping is `HumanCurated`.. (this needs to be [fleshed out](https://github.com/mapping-commons/SSSOM/issues/57). 
       For now, leave a `comment` indicating what you did to arrive at your conclusion, i.e. wether you compared the definitions, 
       looked up the "labels" in a database, ran a tool and decided to trust it etc.)
     - if the mapping is `SemanticSimilarity` (graph similarity, neighbourhood, cosine similarity), you should provide:
       - `semantic_similarity_score`
       - `semantic_similarity_measure`
     - For now, if there are _multiple pieces of evidence_ (lexical, logical etc), please emit one row per evidence. 
       If your tool combines multiple pieces of evidence in a complex way, emit yet another row at the end with
       `match_type` `Complex` and emit ensure you provide the `mapping_tool`.
5. _5-star mappings_ fulfill all the criteria for 4-star mappings and furthermore
   - Are up-to-date with the `subject_source` and `object_source`
   - Have no issue on their issue tracker open for more than 3 months without an interaction
   - Use a _standard_ open license, such as [CC Zero 1.0](https://creativecommons.org/publicdomain/zero/1.0/) or [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).

      
