# sssom

Datamodel for Simple Standard for Sharing Ontology Mappings (SSSOM)

URI: http://w3id.org/sssom/schema/

## Classes

| Class | Description |
| --- | --- |
| [MappingSet](MappingSet.md) | Represents a set of mappings | 
| [Mapping](Mapping.md) | Represents an individual mapping between a pair of entities | 


## Slots

| Slot | Description |
| --- | --- |
| [mappings](mappings.md) | Contains a list of mapping objects | 
| [subject_id](subject_id.md) | The ID of the subject of the mapping. | 
| [subject_label](subject_label.md) | The label of subject of the mapping | 
| [subject_category](subject_category.md) | The conceptual category to which the subject belongs to. This can be a string denoting the category or a term from a controlled vocabulary. | 
| [subject_type](subject_type.md) | The type of entity that is being mapped. | 
| [predicate_id](predicate_id.md) | The ID of the predicate or relation that relates the subject and object of this match. | 
| [predicate_modifier](predicate_modifier.md) | A modifier for negating the prediate. See https://github.com/mapping-commons/sssom/issues/40 for discussion | 
| [predicate_label](predicate_label.md) | The label of the predicate/relation of the mapping | 
| [predicate_type](predicate_type.md) | The type of entity that is being mapped. | 
| [object_id](object_id.md) | The ID of the object of the mapping. | 
| [object_label](object_label.md) | The label of object of the mapping | 
| [object_category](object_category.md) | The conceptual category to which the subject belongs to. This can be a string denoting the category or a term from a controlled vocabulary. | 
| [mapping_justification](mapping_justification.md) | A mapping justification is an action (or the written representation of that action) of showing a mapping to be right or reasonable. | 
| [object_type](object_type.md) | The type of entity that is being mapped. | 
| [mapping_set_id](mapping_set_id.md) | A globally unique identifier for the mapping set (not each individual mapping). Should be IRI, ideally resolvable. | 
| [mapping_set_version](mapping_set_version.md) | A version string for the mapping. | 
| [mapping_set_description](mapping_set_description.md) | A description of the mapping set. | 
| [creator_id](creator_id.md) | Identifies the persons or groups responsible for the creation of the mapping. The creator is the agent that put the mapping in its published form, which may be different from the author, which is a person that was actively involved in the assertion of the mapping. Recommended to be a (pipe-separated) list of ORCIDs or otherwise identifying URLs, but any identifying string (such as name and affiliation) is permissible. | 
| [creator_label](creator_label.md) | A string identifying the creator of this mapping. In the spirit of provenance, consider to use creator_id instead. | 
| [author_id](author_id.md) | Identifies the persons or groups responsible for asserting the mappings. Recommended to be a (pipe-separated) list of ORCIDs or otherwise identifying URLs, but any identifying string (such as name and affiliation) is permissible. | 
| [author_label](author_label.md) | A string identifying the author of this mapping. In the spirit of provenance, consider to use author_id instead. | 
| [reviewer_id](reviewer_id.md) | Identifies the persons or groups that reviewed and confirmed the mapping. Recommended to be a (pipe-separated) list of ORCIDs or otherwise identifying URLs, but any identifying string (such as name and affiliation) is permissible. | 
| [reviewer_label](reviewer_label.md) | A string identifying the reviewer of this mapping. In the spirit of provenance, consider to use author_id instead. | 
| [license](license.md) | A url to the license of the mapping. In absence of a license we assume no license. | 
| [subject_source](subject_source.md) | URI of ontology source for the subject. | 
| [subject_source_version](subject_source_version.md) | Version IRI or version string of the source of the subject term. | 
| [object_source](object_source.md) | IRI of ontology source for the object. Version IRI preferred. | 
| [object_source_version](object_source_version.md) | Version IRI or version string of the source of the object term. | 
| [mapping_provider](mapping_provider.md) | URL pointing to the source that provided the mapping, for example an ontology that already contains the mappings, or a database from which it was derived. | 
| [mapping_set_source](mapping_set_source.md) | A mapping set or set of mapping set that was used to derive the mapping set. | 
| [mapping_source](mapping_source.md) | The mapping set this mapping was originally defined in. mapping_source is used for example when merging multiple mapping sets or deriving one mapping set from another. | 
| [mapping_cardinality](mapping_cardinality.md) | A string indicating whether this mapping is from a 1:1 (the subject_id maps to a single object_id), 1:n (the subject maps to more than one object_id), n:1, 1:0, 0:1 or n:n group. Note that this is a convenience field that should be derivable from the mapping set. | 
| [mapping_tool](mapping_tool.md) | A reference to the tool or algorithm that was used to generate the mapping. Should be a URL pointing to more info about it, but can be free text. | 
| [mapping_tool_version](mapping_tool_version.md) | Version string that denotes the version of the mapping tool used. | 
| [mapping_date](mapping_date.md) | The date the mapping was asserted. This is different from the date the mapping was published or compiled in a SSSOM file. | 
| [publication_date](publication_date.md) | The date the mapping was published. This is different from the date the mapping was asserted. | 
| [confidence](confidence.md) | A score between 0 and 1 to denote the confidence or probability that the match is correct, where 1 denotes total confidence. | 
| [subject_match_field](subject_match_field.md) | A tuple of fields (term annotations on the subject) that was used for the match. | 
| [object_match_field](object_match_field.md) | A tuple of fields (term annotations on the object) that was used for the match. | 
| [match_string](match_string.md) | Strings that are shared by subj/obj. It is recommended to indicate the fields for the match using the object and subject_match_field slots. | 
| [subject_preprocessing](subject_preprocessing.md) | Method of preprocessing applied to the fields of the subject. If different preprocessing steps were performed on different fields, it is recommended to store the match in separate rows. | 
| [object_preprocessing](object_preprocessing.md) | Method of preprocessing applied to the fields of the object. If different preprocessing steps were performed on different fields, it is recommended to store the match in separate rows. | 
| [semantic_similarity_score](semantic_similarity_score.md) | A score between 0 and 1 to denote the semantic similarity, where 1 denotes equivalence. | 
| [semantic_similarity_measure](semantic_similarity_measure.md) | The measure used for computing the the semantic similarity score. To make processing this field as unambiguous as possible, we recommend using wikidata identifiers, but wikipedia pages could also be acceptable. | 
| [see_also](see_also.md) | A URL specific for the mapping instance. E.g. for kboom we have a per-mapping image that shows surrounding axioms that drive probability. Could also be a github issue URL that discussed a complicated alignment | 
| [other](other.md) | Pipe separated list of key value pairs for properties not part of the SSSOM spec. Can be used to encode additional provenance data. | 
| [comment](comment.md) | Free text field containing either curator notes or text generated by tool providing additional informative information. | 
| [metadata_element](metadata_element.md) | All legal SSSOM metadata elements are subproperties of this. | 
| [scope](scope.md) | Indicates whether the metadata element has local, global or local-global scope. | 
| [rdf_example](rdf_example.md) | An example value of the a SSSOM element in the TSV file. | 
| [tsv_example](tsv_example.md) | An example value of the a SSSOM element in RDF. | 
| [equivalent_property](equivalent_property.md) | SSSOM property should be mapped to: | 


## Enums

| Enums | Description |
| --- | --- |
| [EntityTypeEnum](EntityTypeEnum.md) | None | 
| [PredicateModifierEnum](PredicateModifierEnum.md) | None | 
| [MappingCardinalityEnum](MappingCardinalityEnum.md) | None | 
| [PreprocessingMethodEnum](PreprocessingMethodEnum.md) | None | 

