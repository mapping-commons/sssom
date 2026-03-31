# Confidence

SSSOM enables annotating confidence in several ways for individual mappings
records and for mapping sets.

## Confidence in Positive Semantic Mappings

The following example shows a high confidence (0.99) manually curated semantic
mapping, between two disease resources.

```tsv
#curie_map:
#  mesh: https://meshb.nlm.nih.gov/record/ui?ui=
#  MONDO: http://purl.obolibrary.org/obo/MONDO_
#  oboinowl: http://www.geneontology.org/formats/oboInOwl#
#  orcid: https://orcid.org/
#  semapv: https://w3id.org/semapv/vocab/
#  skos: http://www.w3.org/2004/02/skos/core#
#mapping_set_id: https://w3id.org/biopragmatics/biomappings/sssom/positive.sssom.tsv
subject_id	subject_label	predicate_id	object_id	object_label	mapping_justification	author_id	confidence
MONDO:0000455	cone dystrophy	skos:exactMatch	mesh:D000077765	Cone Dystrophy	semapv:ManualMappingCuration	orcid:0000-0001-9439-5346 .99
```

The following example shows a medium-confidence semantic mapping produced
through a lexical matching process. While this semantic mapping is actually
incorrect, the lexical matching process assigned it a confidence of 0.65.

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

When not explicitly specified, confidence estimation algorithms should consider
the confidence of a semantic mapping to be 1.0 by default.

## Confidence with Negated Semantic Mappings

SSSOM has explicit support for curating negative semantic mappings (i.e.,
subject-predicate-object triples known to be false) by using the
`predicate_modifier` column.

The following example shows a highly confident negative semantic mapping,
because _Rocky Mountain spotted fever_ (a disease curated in DOID) is not the
same as _Rocky mountain spotted fever vaccine_ (a vaccine curated in UMLS).

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

It's also possible to curate a negative semantic mapping with low confidence,
but this is done less commonly in practice. Both human curators and semantic
mapping prediction workflows typically focus on the production of _positive_
knowledge.

Similarly, there are a large number of trivial negative semantic mappings that
are typically ignored by curators and algorithms that consume semantic mappings.

When not explicitly specified, confidence estimation algorithms should consider
the confidence of a negative semantic mapping to be 1.0 by default.

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
