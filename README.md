# A Simple Standard for Sharing Ontology Mappings (SSSOM)

SSSOM is a Simple Standard for Sharing Ontology Mappings, providing 

1. a TSV-based representation for ontology term mappings
1. a comprehensive set of standard metadata elements to describe mappings and 
1. a standard translation between the TSV and the Web Ontology Language (OWL). 

The SSSOM TSV format in particular is geared towards the needs of the wider bioinformatics community as a way to safely exchange mappings in a easily readable yet semantically well-specified manner. Consider this example of a simple mapping file:

| subject_id	| predicate_id	| object_id	| match_type	| subject_label	| object_label |
| --- | --- | --- | --- | --- | --- |
| HP:0009124	| skos:exactMatch	| MP:0000003	| Lexical	| Abnormal adipose tissue morphology	| abnormal adipose tissue morphology |
| HP:0008551	| skos:exactMatch	| MP:0000018	| Lexical	| Microtia	| small ears |
| HP:0000411	| skos:exactMatch	| MP:0000021	| Lexical	| Protruding ear	| prominent ears |

SSSOM specifies all its metadata elements:

- subject_id
- predicate_id
- object_id
- match_type
- subject_label
- object_label

including definitions, examples of use and controlled vocabulary where necessary, along with 30 other optional metadata elements to provide additional provenance.


SSSOM further provides a standard way to 
- augment the TSV file with mapping set - level metadata, such as creator_id, mapping_date or license and
- translate a SSSOM compliant TSV files into _OWL reified axioms_. This will allow the easy loading, and merging of SSSOM mapping tables into existing ontologies using standard tools such as ROBOT (under development).


Note that SSSOM is currently under development and subject to change. Please leave us a comment on the [issue tracker](https://github.com/OBOFoundry/SSSOM/issues) if you want to be involved. The full specification can be found [here](SSSOM.md).

