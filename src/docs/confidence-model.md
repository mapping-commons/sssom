# Confidence

SSSOM enables annotating confidence in several ways for individual mappings
records and for mapping sets.

## Confidence with Negated Mappings

In order to express that a subject-predicate-object triple is incorrect, assign
the `Not` value in the `predicate_modifier` column. If the `Not` value is
present, then a confidence of 1.0 means that the creator of the mapping is fully
confidence that the subject-predicate-object triple is not true. A value of 0.0
still means that the creator is unsure whether the mapping is correct or
incorrect.

The following example shows a highly confident negative mapping, because Rocky
Mountain spotted fever (a disease curated in DOID) is not the same as Rocky
mountain spotted fever vaccine (a vaccine curated in UMLS).

The following example shows a medium confidence mapping produced through a
lexical

```tsv
#curie_map:
#  DOID: http://purl.obolibrary.org/obo/DOID_
#  orcid: https://orcid.org/
#  semapv: https://w3id.org/semapv/vocab/
#  skos: http://www.w3.org/2004/02/skos/core#
#  umls: https://uts.nlm.nih.gov/uts/umls/concept/
#mapping_set_id: https://w3id.org/biopragmatics/biomappings/sssom/negative.sssom.tsv
subject_id	subject_label	predicate_id	object_id	object_label	mapping_justification   confidence
DOID:0050052	Rocky Mountain spotted fever	skos:exactMatch	umls:C0035795	Rocky mountain spotted fever vaccine	semapv:LexicalMapping	0.65
```

The following example shows a highly confident negative mapping, because Rocky
Mountain spotted fever (a disease curated in DOID) is not the same as Rocky
mountain spotted fever vaccine (a vaccine curated in UMLS).

```tsv
#curie_map:
#  DOID: http://purl.obolibrary.org/obo/DOID_
#  orcid: https://orcid.org/
#  semapv: https://w3id.org/semapv/vocab/
#  skos: http://www.w3.org/2004/02/skos/core#
#  umls: https://uts.nlm.nih.gov/uts/umls/concept/
#mapping_set_id: https://w3id.org/biopragmatics/biomappings/sssom/negative.sssom.tsv
subject_id	subject_label	predicate_id	predicate_modifier	object_id	object_label	mapping_justification	author_id   confidence
DOID:0050052	Rocky Mountain spotted fever	skos:exactMatch	Not	umls:C0035795	Rocky mountain spotted fever vaccine	semapv:ManualMappingCuration	orcid:0000-0003-4423-4370   1.0
```

## Estimating Overall Confidence in a Mapping Set

There are two places where the confidence in a mapping set can be reported:

1. The creator of the mapping set can report their confidence in the mapping set
   with the `mapping_set_confidence` slot in the mapping set's metadata.
2. The maintainer of a mapping set registry who indexes a mapping set can report
   their own confidence in the mapping set.

In some situations, it may be sufficient to choose a mapping set confidence
based on knowledge about the scope/domain of the mapping set, who the curators
were, etc.

Alternatively, an empirical confidence can be estimated by randomly sampling
semantic mappings from the mapping set, manually reviewing them, then reporting
the percentage that were correct as a decimal value between zero and one. This
estimate becomes more accurate as the size of the sample increases, so it's
suggested to sample a minimum 50-100 semantic mappings.

When not explicitly specified, confidence estimation algorithms should consider
the registry confidence in a mapping set to be 1.0 by default.
