
# Class: mapping


Represents an individual mapping between a pair of entities

URI: [sssom:Mapping](https://w3id.org/sssom/Mapping)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MappingSet]++-%20mappings%200..*>[Mapping&#124;subject_id:EntityReference;subject_label:string%20%3F;subject_category:string%20%3F;predicate_id:EntityReference;predicate_label:string%20%3F;predicate_modifier:predicate_modifier_enum%20%3F;object_id:EntityReference;object_label:string%20%3F;object_category:string%20%3F;mapping_justification:EntityReference;author_id:EntityReference%20*;author_label:string%20*;reviewer_id:EntityReference%20*;reviewer_label:string%20*;creator_id:EntityReference%20*;creator_label:string%20*;license:uri%20%3F;subject_type:entity_type_enum%20%3F;subject_source:uri%20%3F;subject_source_version:string%20%3F;object_type:entity_type_enum%20%3F;object_source:uri%20%3F;object_source_version:string%20%3F;mapping_provider:uri%20%3F;mapping_cardinality:mapping_cardinality_enum%20%3F;mapping_tool:string%20%3F;mapping_tool_version:string%20%3F;mapping_date:date%20%3F;confidence:double%20%3F;subject_match_field:EntityReference%20*;object_match_field:EntityReference%20*;match_string:string%20*;subject_preprocessing:preprocessing_method_enum%20*;object_preprocessing:preprocessing_method_enum%20*;semantic_similarity_score:double%20%3F;semantic_similarity_measure:string%20%3F;see_also:string%20*;other:string%20%3F;comment:string%20%3F],[MappingSet])](https://yuml.me/diagram/nofunky;dir:TB/class/[MappingSet]++-%20mappings%200..*>[Mapping&#124;subject_id:EntityReference;subject_label:string%20%3F;subject_category:string%20%3F;predicate_id:EntityReference;predicate_label:string%20%3F;predicate_modifier:predicate_modifier_enum%20%3F;object_id:EntityReference;object_label:string%20%3F;object_category:string%20%3F;mapping_justification:EntityReference;author_id:EntityReference%20*;author_label:string%20*;reviewer_id:EntityReference%20*;reviewer_label:string%20*;creator_id:EntityReference%20*;creator_label:string%20*;license:uri%20%3F;subject_type:entity_type_enum%20%3F;subject_source:uri%20%3F;subject_source_version:string%20%3F;object_type:entity_type_enum%20%3F;object_source:uri%20%3F;object_source_version:string%20%3F;mapping_provider:uri%20%3F;mapping_cardinality:mapping_cardinality_enum%20%3F;mapping_tool:string%20%3F;mapping_tool_version:string%20%3F;mapping_date:date%20%3F;confidence:double%20%3F;subject_match_field:EntityReference%20*;object_match_field:EntityReference%20*;match_string:string%20*;subject_preprocessing:preprocessing_method_enum%20*;object_preprocessing:preprocessing_method_enum%20*;semantic_similarity_score:double%20%3F;semantic_similarity_measure:string%20%3F;see_also:string%20*;other:string%20%3F;comment:string%20%3F],[MappingSet])

## Referenced by Class

 *  **None** *[mappings](mappings.md)*  <sub>0..\*</sub>  **[Mapping](Mapping.md)**

## Attributes


### Own

 * [subject_id](subject_id.md)  <sub>1..1</sub>
     * Description: The ID of the subject of the mapping.
     * Range: [EntityReference](types/EntityReference.md)
     * Example: HP:0009894 The CURIE denoting the Human Phenotype Ontology concept of 'Thickened ears'
 * [subject_label](subject_label.md)  <sub>0..1</sub>
     * Description: The label of subject of the mapping
     * Range: [String](types/String.md)
     * Example: Thickened ears None
 * [subject_category](subject_category.md)  <sub>0..1</sub>
     * Description: The conceptual category to which the subject belongs to. This can be a string denoting the category or a term from a controlled vocabulary.
     * Range: [String](types/String.md)
     * Example: UBERON:0001062 (The CURIE of the Uberon term for "anatomical entity".)
     * Example: biolink:Gene (The CURIE of the biolink class for genes.)
 * [predicate_id](predicate_id.md)  <sub>1..1</sub>
     * Description: The ID of the predicate or relation that relates the subject and object of this match.
     * Range: [EntityReference](types/EntityReference.md)
     * Example: skos:exactMatch None
 * [predicate_label](predicate_label.md)  <sub>0..1</sub>
     * Description: The label of the predicate/relation of the mapping
     * Range: [String](types/String.md)
     * Example: owl:sameAs The subject and the object are instances (owl individuals), and the two instances are the same.
     * Example: owl:equivalentClass The subject and the object are classes (owl class), and the two classes are the same.
     * Example: owl:equivalentProperty The subject and the object are properties (owl object, data, annotation properties), and the two properties are the same.
     * Example: rdfs:subClassOf The subject and the object are classes (owl class), and the subject is a subclass of the object.
     * Example: rdfs:subPropertyOf The subject and the object are properties (owl object, data, annotation properties), and the subject is a subproperty of the object.
     * Example: skos:relatedMatch The subject and the object are associated in some unspecified way.
     * Example: skos:closeMatch The subject and the object are sufficiently similar that they can be used interchangeably in some information retrieval applications.
     * Example: skos:exactMatch The subject and the object can, with a high degree of confidence, be used interchangeably across a wide range of information retrieval applications.
     * Example: skos:narrowMatch From the SKOS primer: A triple skos:narrower (and skos:narrowMatch) asserts that , the object of the triple, is a narrower concept than , the subject of the triple.
     * Example: skos:broadMatch From the SKOS primer: A triple skos:broader (and skos:broadMatch) asserts that , the object of the triple, is a broader concept than , the subject of the triple.
     * Example: oio:database_cross_reference Two terms are related in some way. The meaning is frequently consistent across a single set of mappings. Note this property is often overloaded even where the terms are of a different nature (e.g. interpro2go)
     * Example: rdfs:seeAlso The subject and the object are associated in some unspecified way. The object IRI often resolves to a resource on the web that provides additional information.
 * [predicate_modifier](predicate_modifier.md)  <sub>0..1</sub>
     * Description: A modifier for negating the prediate. See https://github.com/mapping-commons/sssom/issues/40 for discussion
     * Range: [predicate_modifier_enum](predicate_modifier_enum.md)
     * Example: Not Negates the predicate, see documentation of predicate_modifier_enum
 * [object_id](object_id.md)  <sub>1..1</sub>
     * Description: The ID of the object of the mapping.
     * Range: [EntityReference](types/EntityReference.md)
     * Example: HP:0009894 The CURIE denoting the Human Phenotype Ontology concept of 'Thickened ears'
 * [object_label](object_label.md)  <sub>0..1</sub>
     * Description: The label of object of the mapping
     * Range: [String](types/String.md)
     * Example: Thickened ears None
 * [object_category](object_category.md)  <sub>0..1</sub>
     * Description: The conceptual category to which the subject belongs to. This can be a string denoting the category or a term from a controlled vocabulary.
     * Range: [String](types/String.md)
     * Example: UBERON:0001062 (The CURIE of the Uberon term for "anatomical entity".)
     * Example: biolink:Gene (The CURIE of the biolink class for genes.)
 * [mapping_justification](mapping_justification.md)  <sub>1..1</sub>
     * Description: A mapping justification is an action (or the written representation of that action) of showing a mapping to be right or reasonable.
     * Range: [EntityReference](types/EntityReference.md)
     * Example: OMAPV:Lexical None
     * Example: OMAPV:HumanCurated None
 * [author_id](author_id.md)  <sub>0..\*</sub>
     * Description: Identifies the persons or groups responsible for asserting the mappings. Recommended to be a (pipe-separated) list of ORCIDs or otherwise identifying URLs, but any identifying string (such as name and affiliation) is permissible.
     * Range: [EntityReference](types/EntityReference.md)
 * [author_label](author_label.md)  <sub>0..\*</sub>
     * Description: A string identifying the author of this mapping. In the spirit of provenance, consider to use author_id instead.
     * Range: [String](types/String.md)
 * [reviewer_id](reviewer_id.md)  <sub>0..\*</sub>
     * Description: Identifies the persons or groups that reviewed and confirmed the mapping. Recommended to be a (pipe-separated) list of ORCIDs or otherwise identifying URLs, but any identifying string (such as name and affiliation) is permissible.
     * Range: [EntityReference](types/EntityReference.md)
 * [reviewer_label](reviewer_label.md)  <sub>0..\*</sub>
     * Description: A string identifying the reviewer of this mapping. In the spirit of provenance, consider to use author_id instead.
     * Range: [String](types/String.md)
 * [creator_id](creator_id.md)  <sub>0..\*</sub>
     * Description: Identifies the persons or groups responsible for the creation of the mapping. The creator is the agent that put the mapping in its published form, which may be different from the author, which is a person that was actively involved in the assertion of the mapping. Recommended to be a (pipe-separated) list of ORCIDs or otherwise identifying URLs, but any identifying string (such as name and affiliation) is permissible.
     * Range: [EntityReference](types/EntityReference.md)
 * [creator_label](creator_label.md)  <sub>0..\*</sub>
     * Description: A string identifying the creator of this mapping. In the spirit of provenance, consider to use creator_id instead.
     * Range: [String](types/String.md)
 * [license](license.md)  <sub>0..1</sub>
     * Description: A url to the license of the mapping. In absence of a license we assume no license.
     * Range: [Uri](types/Uri.md)
 * [subject_type](subject_type.md)  <sub>0..1</sub>
     * Description: The type of entity that is being mapped.
     * Range: [entity_type_enum](entity_type_enum.md)
     * Example: owl:Class None
 * [subject_source](subject_source.md)  <sub>0..1</sub>
     * Description: URI of ontology source for the subject.
     * Range: [Uri](types/Uri.md)
     * Example: http://purl.obolibrary.org/obo/mondo.owl (A persistent IRI pointing to the latest version of the Mondo ontology.)
 * [subject_source_version](subject_source_version.md)  <sub>0..1</sub>
     * Description: Version IRI or version string of the source of the subject term.
     * Range: [String](types/String.md)
     * Example: http://purl.obolibrary.org/obo/mondo/releases/2021-01-30/mondo.owl (A persistent Version IRI pointing to the Mondo version '2021-01-30')
 * [object_type](object_type.md)  <sub>0..1</sub>
     * Description: The type of entity that is being mapped.
     * Range: [entity_type_enum](entity_type_enum.md)
     * Example: owl:Class None
 * [object_source](object_source.md)  <sub>0..1</sub>
     * Description: IRI of ontology source for the object. Version IRI preferred.
     * Range: [Uri](types/Uri.md)
     * Example: http://purl.obolibrary.org/obo/mondo.owl (A persistent IRI pointing to the latest version of the Mondo ontology.)
 * [object_source_version](object_source_version.md)  <sub>0..1</sub>
     * Description: Version IRI or version string of the source of the object term.
     * Range: [String](types/String.md)
     * Example: http://purl.obolibrary.org/obo/mondo/releases/2021-01-30/mondo.owl (A persistent Version IRI pointing to the Mondo version '2021-01-30')
 * [mapping_provider](mapping_provider.md)  <sub>0..1</sub>
     * Description: URL pointing to the source that provided the mapping, for example an ontology that already contains the mappings, or a database from which it was derived.
     * Range: [Uri](types/Uri.md)
 * [mapping_cardinality](mapping_cardinality.md)  <sub>0..1</sub>
     * Description: A string indicating whether this mapping is from a 1:1 (the subject_id maps to a single object_id), 1:n (the subject maps to more than one object_id), n:1, 1:0, 0:1 or n:n group. Note that this is a convenience field that should be derivable from the mapping set.
     * Range: [mapping_cardinality_enum](mapping_cardinality_enum.md)
 * [mapping_tool](mapping_tool.md)  <sub>0..1</sub>
     * Description: A reference to the tool or algorithm that was used to generate the mapping. Should be a URL pointing to more info about it, but can be free text.
     * Range: [String](types/String.md)
     * Example: https://github.com/AgreementMakerLight/AML-Project None
 * [mapping_tool_version](mapping_tool_version.md)  <sub>0..1</sub>
     * Description: Version string that denotes the version of the mapping tool used.
     * Range: [String](types/String.md)
     * Example: v3.2 None
 * [mapping_date](mapping_date.md)  <sub>0..1</sub>
     * Description: The date the mapping was asserted. This is different from the date the mapping was published or compiled in a SSSOM file.
     * Range: [Date](types/Date.md)
 * [confidence](confidence.md)  <sub>0..1</sub>
     * Description: A score between 0 and 1 to denote the confidence or probability that the match is correct, where 1 denotes total confidence.
     * Range: [Double](types/Double.md)
 * [subject_match_field](subject_match_field.md)  <sub>0..\*</sub>
     * Description: A tuple of fields (term annotations on the subject) that was used for the match.
     * Range: [EntityReference](types/EntityReference.md)
 * [object_match_field](object_match_field.md)  <sub>0..\*</sub>
     * Description: A tuple of fields (term annotations on the object) that was used for the match.
     * Range: [EntityReference](types/EntityReference.md)
 * [match_string](match_string.md)  <sub>0..\*</sub>
     * Description: Strings that are shared by subj/obj. It is recommended to indicate the fields for the match using the object and subject_match_field slots.
     * Range: [String](types/String.md)
 * [subject_preprocessing](subject_preprocessing.md)  <sub>0..\*</sub>
     * Description: Method of preprocessing applied to the fields of the subject. If different preprocessing steps were performed on different fields, it is recommended to store the match in separate rows.
     * Range: [preprocessing_method_enum](preprocessing_method_enum.md)
 * [object_preprocessing](object_preprocessing.md)  <sub>0..\*</sub>
     * Description: Method of preprocessing applied to the fields of the object. If different preprocessing steps were performed on different fields, it is recommended to store the match in separate rows.
     * Range: [preprocessing_method_enum](preprocessing_method_enum.md)
 * [semantic_similarity_score](semantic_similarity_score.md)  <sub>0..1</sub>
     * Description: A score between 0 and 1 to denote the semantic similarity, where 1 denotes equivalence.
     * Range: [Double](types/Double.md)
 * [semantic_similarity_measure](semantic_similarity_measure.md)  <sub>0..1</sub>
     * Description: The measure used for computing the the semantic similarity score. To make processing this field as unambiguous as possible, we recommend using wikidata identifiers, but wikipedia pages could also be acceptable.
     * Range: [String](types/String.md)
     * Example: https://www.wikidata.org/wiki/Q865360 (the Wikidata identifier for the Jaccard index measure).
 * [see_also](see_also.md)  <sub>0..\*</sub>
     * Description: A URL specific for the mapping instance. E.g. for kboom we have a per-mapping image that shows surrounding axioms that drive probability. Could also be a github issue URL that discussed a complicated alignment
     * Range: [String](types/String.md)
 * [other](other.md)  <sub>0..1</sub>
     * Description: Pipe separated list of key value pairs for properties not part of the SSSOM spec. Can be used to encode additional provenance data.
     * Range: [String](types/String.md)
 * [comment](comment.md)  <sub>0..1</sub>
     * Description: Free text field containing either curator notes or text generated by tool providing additional informative information.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | owl:Axiom |

