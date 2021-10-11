# Tutorials



## How to create an SSSOM mapping set from scratch

SSSOM mapping sets can be created as part of automated processes, like ontology matchers, or manually by ontology curators. While there is overlap, it makes sense to look at both cases separately. To remind yourself why you should build SSSOM mapping sets in the first place, please refer to [the FAQ](faq.md#why).

### Manually curating mapping sets

Manually curating mappings is often done in a collaborative fashion. We recommend tools like Google Sheets for organising collaborative workflows to edit mapping sets.

To get a good sense of the most important metadata to consider for your project, refer to [SSSOM 5-Star recommendation for mappings](spec.md#minimum)

For the sake of this tutorial, we will focus on producing a solid 3-Star mapping set with the following metadata:

Core:

- `subject_id`: The ID of the subject of the mapping
- `predicate_id`
- `object_id`

Provenance:

- `match_type`(s) (Lexical, Logical match, HumanCurated etc)
- `date` of the mapping
- `creator_id`
- `subject_source`
- `subject_source_version`
- `object_source`
- `object_source_version`

