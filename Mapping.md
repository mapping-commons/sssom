# Class: Mapping
_Represents an individual mapping between a pair of entities_





URI: [owl:Axiom](http://www.w3.org/2002/07/owl#Axiom)



<!-- no inheritance hierarchy -->



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [subject_id](subject_id.md) | [EntityReference](EntityReference.md) | 1..1 | The ID of the subject of the mapping.  | . |
| [subject_label](subject_label.md) | [string](string.md) | 0..1 _recommended_ | The label of subject of the mapping  | . |
| [subject_category](subject_category.md) | [string](string.md) | 0..1 | The conceptual category to which the subject belongs to. This can be a string denoting the category or a term from a controlled vocabulary.  | . |
| [predicate_id](predicate_id.md) | [EntityReference](EntityReference.md) | 1..1 | The ID of the predicate or relation that relates the subject and object of this match.  | . |
| [predicate_label](predicate_label.md) | [string](string.md) | 0..1 | The label of the predicate/relation of the mapping  | . |
| [predicate_modifier](predicate_modifier.md) | [PredicateModifierEnum](PredicateModifierEnum.md) | 0..1 | A modifier for negating the prediate. See https://github.com/mapping-commons/sssom/issues/40 for discussion  | . |
| [object_id](object_id.md) | [EntityReference](EntityReference.md) | 1..1 | The ID of the object of the mapping.  | . |
| [object_label](object_label.md) | [string](string.md) | 0..1 _recommended_ | The label of object of the mapping  | . |
| [object_category](object_category.md) | [string](string.md) | 0..1 | The conceptual category to which the subject belongs to. This can be a string denoting the category or a term from a controlled vocabulary.  | . |
| [mapping_justification](mapping_justification.md) | [EntityReference](EntityReference.md) | 1..1 | A mapping justification is an action (or the written representation of that action) of showing a mapping to be right or reasonable.  | . |
| [author_id](author_id.md) | [EntityReference](EntityReference.md) | 0..* | Identifies the persons or groups responsible for asserting the mappings. Recommended to be a (pipe-separated) list of ORCIDs or otherwise identifying URLs, but any identifying string (such as name and affiliation) is permissible.  | . |
| [author_label](author_label.md) | [string](string.md) | 0..* | A string identifying the author of this mapping. In the spirit of provenance, consider to use author_id instead.  | . |
| [reviewer_id](reviewer_id.md) | [EntityReference](EntityReference.md) | 0..* | Identifies the persons or groups that reviewed and confirmed the mapping. Recommended to be a (pipe-separated) list of ORCIDs or otherwise identifying URLs, but any identifying string (such as name and affiliation) is permissible.  | . |
| [reviewer_label](reviewer_label.md) | [string](string.md) | 0..* | A string identifying the reviewer of this mapping. In the spirit of provenance, consider to use author_id instead.  | . |
| [creator_id](creator_id.md) | [EntityReference](EntityReference.md) | 0..* | Identifies the persons or groups responsible for the creation of the mapping. The creator is the agent that put the mapping in its published form, which may be different from the author, which is a person that was actively involved in the assertion of the mapping. Recommended to be a (pipe-separated) list of ORCIDs or otherwise identifying URLs, but any identifying string (such as name and affiliation) is permissible.  | . |
| [creator_label](creator_label.md) | [string](string.md) | 0..* | A string identifying the creator of this mapping. In the spirit of provenance, consider to use creator_id instead.  | . |
| [license](license.md) | [uri](uri.md) | 0..1 | A url to the license of the mapping. In absence of a license we assume no license.  | . |
| [subject_type](subject_type.md) | [EntityTypeEnum](EntityTypeEnum.md) | 0..1 | The type of entity that is being mapped.  | . |
| [subject_source](subject_source.md) | [uri](uri.md) | 0..1 | URI of ontology source for the subject.  | . |
| [subject_source_version](subject_source_version.md) | [string](string.md) | 0..1 | Version IRI or version string of the source of the subject term.  | . |
| [object_type](object_type.md) | [EntityTypeEnum](EntityTypeEnum.md) | 0..1 | The type of entity that is being mapped.  | . |
| [object_source](object_source.md) | [uri](uri.md) | 0..1 | IRI of ontology source for the object. Version IRI preferred.  | . |
| [object_source_version](object_source_version.md) | [string](string.md) | 0..1 | Version IRI or version string of the source of the object term.  | . |
| [mapping_provider](mapping_provider.md) | [uri](uri.md) | 0..1 | URL pointing to the source that provided the mapping, for example an ontology that already contains the mappings, or a database from which it was derived.  | . |
| [mapping_cardinality](mapping_cardinality.md) | [MappingCardinalityEnum](MappingCardinalityEnum.md) | 0..1 | A string indicating whether this mapping is from a 1:1 (the subject_id maps to a single object_id), 1:n (the subject maps to more than one object_id), n:1, 1:0, 0:1 or n:n group. Note that this is a convenience field that should be derivable from the mapping set.  | . |
| [mapping_tool](mapping_tool.md) | [string](string.md) | 0..1 | A reference to the tool or algorithm that was used to generate the mapping. Should be a URL pointing to more info about it, but can be free text.  | . |
| [mapping_tool_version](mapping_tool_version.md) | [string](string.md) | 0..1 | Version string that denotes the version of the mapping tool used.  | . |
| [mapping_date](mapping_date.md) | [date](date.md) | 0..1 | The date the mapping was asserted. This is different from the date the mapping was published or compiled in a SSSOM file.  | . |
| [confidence](confidence.md) | [double](double.md) | 0..1 | A score between 0 and 1 to denote the confidence or probability that the match is correct, where 1 denotes total confidence.  | . |
| [subject_match_field](subject_match_field.md) | [EntityReference](EntityReference.md) | 0..* | A tuple of fields (term annotations on the subject) that was used for the match.  | . |
| [object_match_field](object_match_field.md) | [EntityReference](EntityReference.md) | 0..* | A tuple of fields (term annotations on the object) that was used for the match.  | . |
| [match_string](match_string.md) | [string](string.md) | 0..* | Strings that are shared by subj/obj. It is recommended to indicate the fields for the match using the object and subject_match_field slots.  | . |
| [subject_preprocessing](subject_preprocessing.md) | [PreprocessingMethodEnum](PreprocessingMethodEnum.md) | 0..* | Method of preprocessing applied to the fields of the subject. If different preprocessing steps were performed on different fields, it is recommended to store the match in separate rows.  | . |
| [object_preprocessing](object_preprocessing.md) | [PreprocessingMethodEnum](PreprocessingMethodEnum.md) | 0..* | Method of preprocessing applied to the fields of the object. If different preprocessing steps were performed on different fields, it is recommended to store the match in separate rows.  | . |
| [semantic_similarity_score](semantic_similarity_score.md) | [double](double.md) | 0..1 | A score between 0 and 1 to denote the semantic similarity, where 1 denotes equivalence.  | . |
| [semantic_similarity_measure](semantic_similarity_measure.md) | [string](string.md) | 0..1 | The measure used for computing the the semantic similarity score. To make processing this field as unambiguous as possible, we recommend using wikidata identifiers, but wikipedia pages could also be acceptable.  | . |
| [see_also](see_also.md) | [string](string.md) | 0..* | A URL specific for the mapping instance. E.g. for kboom we have a per-mapping image that shows surrounding axioms that drive probability. Could also be a github issue URL that discussed a complicated alignment  | . |
| [other](other.md) | [string](string.md) | 0..1 | Pipe separated list of key value pairs for properties not part of the SSSOM spec. Can be used to encode additional provenance data.  | . |
| [comment](comment.md) | [string](string.md) | 0..1 | Free text field containing either curator notes or text generated by tool providing additional informative information.  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MappingSet](MappingSet.md) | [mappings](mappings.md) | range | mapping |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: mapping
description: Represents an individual mapping between a pair of entities
from_schema: http://w3id.org/sssom/schema/
slots:
- subject_id
- subject_label
- subject_category
- predicate_id
- predicate_label
- predicate_modifier
- object_id
- object_label
- object_category
- mapping_justification
- author_id
- author_label
- reviewer_id
- reviewer_label
- creator_id
- creator_label
- license
- subject_type
- subject_source
- subject_source_version
- object_type
- object_source
- object_source_version
- mapping_provider
- mapping_cardinality
- mapping_tool
- mapping_tool_version
- mapping_date
- confidence
- subject_match_field
- object_match_field
- match_string
- subject_preprocessing
- object_preprocessing
- semantic_similarity_score
- semantic_similarity_measure
- see_also
- other
- comment
class_uri: owl:Axiom

```
</details>

### Induced

<details>
```yaml
name: mapping
description: Represents an individual mapping between a pair of entities
from_schema: http://w3id.org/sssom/schema/
attributes:
  subject_id:
    name: subject_id
    description: The ID of the subject of the mapping.
    examples:
    - value: HP:0009894
      description: The CURIE denoting the Human Phenotype Ontology concept of 'Thickened
        ears'
    from_schema: http://w3id.org/sssom/schema/
    mappings:
    - owl:annotatedSource
    slot_uri: owl:annotatedSource
    alias: subject_id
    owner: mapping
    range: EntityReference
    required: true
  subject_label:
    name: subject_label
    description: The label of subject of the mapping
    examples:
    - value: Thickened ears
    from_schema: http://w3id.org/sssom/schema/
    alias: subject_label
    owner: mapping
    range: string
    recommended: true
  subject_category:
    name: subject_category
    description: The conceptual category to which the subject belongs to. This can
      be a string denoting the category or a term from a controlled vocabulary.
    examples:
    - value: UBERON:0001062
      description: (The CURIE of the Uberon term for "anatomical entity".)
    - value: biolink:Gene
      description: (The CURIE of the biolink class for genes.)
    from_schema: http://w3id.org/sssom/schema/
    alias: subject_category
    owner: mapping
    range: string
  predicate_id:
    name: predicate_id
    description: The ID of the predicate or relation that relates the subject and
      object of this match.
    examples:
    - value: skos:exactMatch
    from_schema: http://w3id.org/sssom/schema/
    mappings:
    - owl:annotatedProperty
    slot_uri: owl:annotatedProperty
    alias: predicate_id
    owner: mapping
    range: EntityReference
    required: true
  predicate_label:
    name: predicate_label
    description: The label of the predicate/relation of the mapping
    examples:
    - value: owl:sameAs
      description: The subject and the object are instances (owl individuals), and
        the two instances are the same.
    - value: owl:equivalentClass
      description: The subject and the object are classes (owl class), and the two
        classes are the same.
    - value: owl:equivalentProperty
      description: The subject and the object are properties (owl object, data, annotation
        properties), and the two properties are the same.
    - value: rdfs:subClassOf
      description: The subject and the object are classes (owl class), and the subject
        is a subclass of the object.
    - value: rdfs:subPropertyOf
      description: The subject and the object are properties (owl object, data, annotation
        properties), and the subject is a subproperty of the object.
    - value: skos:relatedMatch
      description: The subject and the object are associated in some unspecified way.
    - value: skos:closeMatch
      description: The subject and the object are sufficiently similar that they can
        be used interchangeably in some information retrieval applications.
    - value: skos:exactMatch
      description: The subject and the object can, with a high degree of confidence,
        be used interchangeably across a wide range of information retrieval applications.
    - value: skos:narrowMatch
      description: 'From the SKOS primer: A triple skos:narrower (and skos:narrowMatch)
        asserts that , the object of the triple, is a narrower concept than , the
        subject of the triple.'
    - value: skos:broadMatch
      description: 'From the SKOS primer: A triple skos:broader (and skos:broadMatch)
        asserts that , the object of the triple, is a broader concept than , the subject
        of the triple.'
    - value: oio:database_cross_reference
      description: Two terms are related in some way. The meaning is frequently consistent
        across a single set of mappings. Note this property is often overloaded even
        where the terms are of a different nature (e.g. interpro2go)
    - value: rdfs:seeAlso
      description: The subject and the object are associated in some unspecified way.
        The object IRI often resolves to a resource on the web that provides additional
        information.
    from_schema: http://w3id.org/sssom/schema/
    alias: predicate_label
    owner: mapping
    range: string
  predicate_modifier:
    name: predicate_modifier
    description: A modifier for negating the prediate. See https://github.com/mapping-commons/sssom/issues/40
      for discussion
    examples:
    - value: Not
      description: Negates the predicate, see documentation of predicate_modifier_enum
    from_schema: http://w3id.org/sssom/schema/
    alias: predicate_modifier
    owner: mapping
    range: predicate_modifier_enum
  object_id:
    name: object_id
    description: The ID of the object of the mapping.
    examples:
    - value: HP:0009894
      description: The CURIE denoting the Human Phenotype Ontology concept of 'Thickened
        ears'
    from_schema: http://w3id.org/sssom/schema/
    mappings:
    - owl:annotatedTarget
    slot_uri: owl:annotatedTarget
    alias: object_id
    owner: mapping
    range: EntityReference
    required: true
  object_label:
    name: object_label
    description: The label of object of the mapping
    examples:
    - value: Thickened ears
    from_schema: http://w3id.org/sssom/schema/
    alias: object_label
    owner: mapping
    range: string
    recommended: true
  object_category:
    name: object_category
    description: The conceptual category to which the subject belongs to. This can
      be a string denoting the category or a term from a controlled vocabulary.
    examples:
    - value: UBERON:0001062
      description: (The CURIE of the Uberon term for "anatomical entity".)
    - value: biolink:Gene
      description: (The CURIE of the biolink class for genes.)
    from_schema: http://w3id.org/sssom/schema/
    alias: object_category
    owner: mapping
    range: string
  mapping_justification:
    name: mapping_justification
    description: A mapping justification is an action (or the written representation
      of that action) of showing a mapping to be right or reasonable.
    examples:
    - value: OMAPV:Lexical
    - value: OMAPV:HumanCurated
    from_schema: http://w3id.org/sssom/schema/
    alias: mapping_justification
    owner: mapping
    range: EntityReference
    required: true
  author_id:
    name: author_id
    description: Identifies the persons or groups responsible for asserting the mappings.
      Recommended to be a (pipe-separated) list of ORCIDs or otherwise identifying
      URLs, but any identifying string (such as name and affiliation) is permissible.
    from_schema: http://w3id.org/sssom/schema/
    slot_uri: pav:authoredBy
    multivalued: true
    alias: author_id
    owner: mapping
    range: EntityReference
  author_label:
    name: author_label
    description: A string identifying the author of this mapping. In the spirit of
      provenance, consider to use author_id instead.
    from_schema: http://w3id.org/sssom/schema/
    multivalued: true
    alias: author_label
    owner: mapping
    range: string
  reviewer_id:
    name: reviewer_id
    description: Identifies the persons or groups that reviewed and confirmed the
      mapping. Recommended to be a (pipe-separated) list of ORCIDs or otherwise identifying
      URLs, but any identifying string (such as name and affiliation) is permissible.
    from_schema: http://w3id.org/sssom/schema/
    multivalued: true
    alias: reviewer_id
    owner: mapping
    range: EntityReference
  reviewer_label:
    name: reviewer_label
    description: A string identifying the reviewer of this mapping. In the spirit
      of provenance, consider to use author_id instead.
    from_schema: http://w3id.org/sssom/schema/
    multivalued: true
    alias: reviewer_label
    owner: mapping
    range: string
  creator_id:
    name: creator_id
    description: Identifies the persons or groups responsible for the creation of
      the mapping. The creator is the agent that put the mapping in its published
      form, which may be different from the author, which is a person that was actively
      involved in the assertion of the mapping. Recommended to be a (pipe-separated)
      list of ORCIDs or otherwise identifying URLs, but any identifying string (such
      as name and affiliation) is permissible.
    from_schema: http://w3id.org/sssom/schema/
    slot_uri: dc:creator
    multivalued: true
    alias: creator_id
    owner: mapping
    range: EntityReference
  creator_label:
    name: creator_label
    description: A string identifying the creator of this mapping. In the spirit of
      provenance, consider to use creator_id instead.
    from_schema: http://w3id.org/sssom/schema/
    multivalued: true
    alias: creator_label
    owner: mapping
    range: string
  license:
    name: license
    description: A url to the license of the mapping. In absence of a license we assume
      no license.
    from_schema: http://w3id.org/sssom/schema/
    slot_uri: dcterms:license
    alias: license
    owner: mapping
    range: uri
  subject_type:
    name: subject_type
    description: The type of entity that is being mapped.
    examples:
    - value: owl:Class
    from_schema: http://w3id.org/sssom/schema/
    alias: subject_type
    owner: mapping
    range: entity_type_enum
  subject_source:
    name: subject_source
    description: URI of ontology source for the subject.
    examples:
    - value: http://purl.obolibrary.org/obo/mondo.owl
      description: (A persistent IRI pointing to the latest version of the Mondo ontology.)
    from_schema: http://w3id.org/sssom/schema/
    alias: subject_source
    owner: mapping
    range: uri
  subject_source_version:
    name: subject_source_version
    description: Version IRI or version string of the source of the subject term.
    examples:
    - value: http://purl.obolibrary.org/obo/mondo/releases/2021-01-30/mondo.owl
      description: (A persistent Version IRI pointing to the Mondo version '2021-01-30')
    from_schema: http://w3id.org/sssom/schema/
    alias: subject_source_version
    owner: mapping
    range: string
  object_type:
    name: object_type
    description: The type of entity that is being mapped.
    examples:
    - value: owl:Class
    from_schema: http://w3id.org/sssom/schema/
    alias: object_type
    owner: mapping
    range: entity_type_enum
  object_source:
    name: object_source
    description: IRI of ontology source for the object. Version IRI preferred.
    examples:
    - value: http://purl.obolibrary.org/obo/mondo.owl
      description: (A persistent IRI pointing to the latest version of the Mondo ontology.)
    from_schema: http://w3id.org/sssom/schema/
    alias: object_source
    owner: mapping
    range: uri
  object_source_version:
    name: object_source_version
    description: Version IRI or version string of the source of the object term.
    examples:
    - value: http://purl.obolibrary.org/obo/mondo/releases/2021-01-30/mondo.owl
      description: (A persistent Version IRI pointing to the Mondo version '2021-01-30')
    from_schema: http://w3id.org/sssom/schema/
    alias: object_source_version
    owner: mapping
    range: string
  mapping_provider:
    name: mapping_provider
    description: URL pointing to the source that provided the mapping, for example
      an ontology that already contains the mappings, or a database from which it
      was derived.
    from_schema: http://w3id.org/sssom/schema/
    alias: mapping_provider
    owner: mapping
    range: uri
  mapping_cardinality:
    name: mapping_cardinality
    description: A string indicating whether this mapping is from a 1:1 (the subject_id
      maps to a single object_id), 1:n (the subject maps to more than one object_id),
      n:1, 1:0, 0:1 or n:n group. Note that this is a convenience field that should
      be derivable from the mapping set.
    from_schema: http://w3id.org/sssom/schema/
    alias: mapping_cardinality
    owner: mapping
    range: mapping_cardinality_enum
  mapping_tool:
    name: mapping_tool
    description: A reference to the tool or algorithm that was used to generate the
      mapping. Should be a URL pointing to more info about it, but can be free text.
    examples:
    - value: https://github.com/AgreementMakerLight/AML-Project
    from_schema: http://w3id.org/sssom/schema/
    alias: mapping_tool
    owner: mapping
    range: string
  mapping_tool_version:
    name: mapping_tool_version
    description: Version string that denotes the version of the mapping tool used.
    examples:
    - value: v3.2
    from_schema: http://w3id.org/sssom/schema/
    alias: mapping_tool_version
    owner: mapping
    range: string
  mapping_date:
    name: mapping_date
    description: The date the mapping was asserted. This is different from the date
      the mapping was published or compiled in a SSSOM file.
    from_schema: http://w3id.org/sssom/schema/
    slot_uri: pav:authoredOn
    alias: mapping_date
    owner: mapping
    range: date
  confidence:
    name: confidence
    description: A score between 0 and 1 to denote the confidence or probability that
      the match is correct, where 1 denotes total confidence.
    from_schema: http://w3id.org/sssom/schema/
    alias: confidence
    owner: mapping
    range: double
  subject_match_field:
    name: subject_match_field
    description: A tuple of fields (term annotations on the subject) that was used
      for the match.
    from_schema: http://w3id.org/sssom/schema/
    multivalued: true
    alias: subject_match_field
    owner: mapping
    range: EntityReference
  object_match_field:
    name: object_match_field
    description: A tuple of fields (term annotations on the object) that was used
      for the match.
    from_schema: http://w3id.org/sssom/schema/
    multivalued: true
    alias: object_match_field
    owner: mapping
    range: EntityReference
  match_string:
    name: match_string
    description: Strings that are shared by subj/obj. It is recommended to indicate
      the fields for the match using the object and subject_match_field slots.
    from_schema: http://w3id.org/sssom/schema/
    multivalued: true
    alias: match_string
    owner: mapping
    range: string
  subject_preprocessing:
    name: subject_preprocessing
    description: Method of preprocessing applied to the fields of the subject. If
      different preprocessing steps were performed on different fields, it is recommended
      to store the match in separate rows.
    from_schema: http://w3id.org/sssom/schema/
    multivalued: true
    alias: subject_preprocessing
    owner: mapping
    range: preprocessing_method_enum
  object_preprocessing:
    name: object_preprocessing
    description: Method of preprocessing applied to the fields of the object. If different
      preprocessing steps were performed on different fields, it is recommended to
      store the match in separate rows.
    from_schema: http://w3id.org/sssom/schema/
    multivalued: true
    alias: object_preprocessing
    owner: mapping
    range: preprocessing_method_enum
  semantic_similarity_score:
    name: semantic_similarity_score
    description: A score between 0 and 1 to denote the semantic similarity, where
      1 denotes equivalence.
    from_schema: http://w3id.org/sssom/schema/
    alias: semantic_similarity_score
    owner: mapping
    range: double
  semantic_similarity_measure:
    name: semantic_similarity_measure
    description: The measure used for computing the the semantic similarity score.
      To make processing this field as unambiguous as possible, we recommend using
      wikidata identifiers, but wikipedia pages could also be acceptable.
    examples:
    - value: https://www.wikidata.org/wiki/Q865360
      description: (the Wikidata identifier for the Jaccard index measure).
    from_schema: http://w3id.org/sssom/schema/
    alias: semantic_similarity_measure
    owner: mapping
    range: string
  see_also:
    name: see_also
    description: A URL specific for the mapping instance. E.g. for kboom we have a
      per-mapping image that shows surrounding axioms that drive probability. Could
      also be a github issue URL that discussed a complicated alignment
    from_schema: http://w3id.org/sssom/schema/
    slot_uri: rdfs:seeAlso
    multivalued: true
    alias: see_also
    owner: mapping
    range: string
  other:
    name: other
    description: Pipe separated list of key value pairs for properties not part of
      the SSSOM spec. Can be used to encode additional provenance data.
    from_schema: http://w3id.org/sssom/schema/
    alias: other
    owner: mapping
    range: string
  comment:
    name: comment
    description: Free text field containing either curator notes or text generated
      by tool providing additional informative information.
    from_schema: http://w3id.org/sssom/schema/
    slot_uri: rdfs:comment
    alias: comment
    owner: mapping
    range: string
class_uri: owl:Axiom

```
</details>