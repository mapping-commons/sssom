
# Class: mapping set


Represents a set of mappings

URI: [sssom:MappingSet](https://w3id.org/sssom/MappingSet)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Mapping]<mappings%200..*-++[MappingSet&#124;mapping_set_id:uri;mapping_set_version:string%20%3F;mapping_set_source:EntityReference%20*;mapping_set_description:string%20%3F;creator_id:EntityReference%20*;creator_label:string%20*;license:uri;subject_type:entity_type_enum%20%3F;subject_source:uri%20%3F;subject_source_version:string%20%3F;object_type:entity_type_enum%20%3F;object_source:uri%20%3F;object_source_version:string%20%3F;mapping_provider:uri%20%3F;mapping_tool:string%20%3F;mapping_date:date%20%3F;subject_match_field:EntityReference%20*;object_match_field:EntityReference%20*;subject_preprocessing:preprocessing_method_enum%20*;object_preprocessing:preprocessing_method_enum%20*;see_also:string%20*;other:string%20%3F;comment:string%20%3F],[Mapping])](https://yuml.me/diagram/nofunky;dir:TB/class/[Mapping]<mappings%200..*-++[MappingSet&#124;mapping_set_id:uri;mapping_set_version:string%20%3F;mapping_set_source:EntityReference%20*;mapping_set_description:string%20%3F;creator_id:EntityReference%20*;creator_label:string%20*;license:uri;subject_type:entity_type_enum%20%3F;subject_source:uri%20%3F;subject_source_version:string%20%3F;object_type:entity_type_enum%20%3F;object_source:uri%20%3F;object_source_version:string%20%3F;mapping_provider:uri%20%3F;mapping_tool:string%20%3F;mapping_date:date%20%3F;subject_match_field:EntityReference%20*;object_match_field:EntityReference%20*;subject_preprocessing:preprocessing_method_enum%20*;object_preprocessing:preprocessing_method_enum%20*;see_also:string%20*;other:string%20%3F;comment:string%20%3F],[Mapping])

## Referenced by Class


## Attributes


### Own

 * [mappings](mappings.md)  <sub>0..\*</sub>
     * Description: Contains a list of mapping objects
     * Range: [Mapping](Mapping.md)
 * [mapping_set_id](mapping_set_id.md)  <sub>1..1</sub>
     * Description: A globally unique identifier for the mapping set (not each individual mapping). Should be IRI, ideally resolvable.
     * Range: [Uri](types/Uri.md)
     * Example: http://purl.obolibrary.org/obo/mondo/mappings/mondo_exactmatch_ncit.sssom.tsv (A persistent URI pointing to the latest version of the Mondo - NCIT mapping in the Mondo namespace.)
 * [mapping_set_version](mapping_set_version.md)  <sub>0..1</sub>
     * Description: A version string for the mapping.
     * Range: [String](types/String.md)
     * Example: 2020-01-01 (A date-based version that indicates that the mapping was published on the 1st January in 2021.)
     * Example: 1.2.1 (A semantic version tag that indicates that this is the 1st major, 2nd minor version, patch 1 (https://semver.org/).)
 * [mapping_set_source](mapping_set_source.md)  <sub>0..\*</sub>
     * Description: A mapping set or set of mapping set that was used to derive the mapping set.
     * Range: [EntityReference](types/EntityReference.md)
     * Example: MONDO_MAPPINGS:mondo_exactmatch_ncit.sssom.tsv None
     * Example: MONDO_MAPPINGS:mondo_exactmatch_ncit.sssom.tsv|MONDO_MAPPINGS:mondo_exactmatch_omim.sssom.tsv (multivalued example in TSV)
 * [mapping_set_description](mapping_set_description.md)  <sub>0..1</sub>
     * Description: A description of the mapping set.
     * Range: [String](types/String.md)
     * Example: This mapping set was produced to integrate human and mouse phenotype data at the IMPC. It is primarily used for making mouse phenotypes searchable by human synonyms at https://mousephenotype.org/. None
 * [creator_id](creator_id.md)  <sub>0..\*</sub>
     * Description: Identifies the persons or groups responsible for the creation of the mapping. The creator is the agent that put the mapping in its published form, which may be different from the author, which is a person that was actively involved in the assertion of the mapping. Recommended to be a (pipe-separated) list of ORCIDs or otherwise identifying URLs, but any identifying string (such as name and affiliation) is permissible.
     * Range: [EntityReference](types/EntityReference.md)
 * [creator_label](creator_label.md)  <sub>0..\*</sub>
     * Description: A string identifying the creator of this mapping. In the spirit of provenance, consider to use creator_id instead.
     * Range: [String](types/String.md)
 * [mapping set➞license](mapping_set_license.md)  <sub>1..1</sub>
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
 * [mapping_tool](mapping_tool.md)  <sub>0..1</sub>
     * Description: A reference to the tool or algorithm that was used to generate the mapping. Should be a URL pointing to more info about it, but can be free text.
     * Range: [String](types/String.md)
     * Example: https://github.com/AgreementMakerLight/AML-Project None
 * [mapping_date](mapping_date.md)  <sub>0..1</sub>
     * Description: The date the mapping was asserted. This is different from the date the mapping was published or compiled in a SSSOM file.
     * Range: [Date](types/Date.md)
 * [subject_match_field](subject_match_field.md)  <sub>0..\*</sub>
     * Description: A tuple of fields (term annotations on the subject) that was used for the match.
     * Range: [EntityReference](types/EntityReference.md)
 * [object_match_field](object_match_field.md)  <sub>0..\*</sub>
     * Description: A tuple of fields (term annotations on the object) that was used for the match.
     * Range: [EntityReference](types/EntityReference.md)
 * [subject_preprocessing](subject_preprocessing.md)  <sub>0..\*</sub>
     * Description: Method of preprocessing applied to the fields of the subject. If different preprocessing steps were performed on different fields, it is recommended to store the match in separate rows.
     * Range: [preprocessing_method_enum](preprocessing_method_enum.md)
 * [object_preprocessing](object_preprocessing.md)  <sub>0..\*</sub>
     * Description: Method of preprocessing applied to the fields of the object. If different preprocessing steps were performed on different fields, it is recommended to store the match in separate rows.
     * Range: [preprocessing_method_enum](preprocessing_method_enum.md)
 * [see_also](see_also.md)  <sub>0..\*</sub>
     * Description: A URL specific for the mapping instance. E.g. for kboom we have a per-mapping image that shows surrounding axioms that drive probability. Could also be a github issue URL that discussed a complicated alignment
     * Range: [String](types/String.md)
 * [other](other.md)  <sub>0..1</sub>
     * Description: Pipe separated list of key value pairs for properties not part of the SSSOM spec. Can be used to encode additional provenance data.
     * Range: [String](types/String.md)
 * [comment](comment.md)  <sub>0..1</sub>
     * Description: Free text field containing either curator notes or text generated by tool providing additional informative information.
     * Range: [String](types/String.md)
