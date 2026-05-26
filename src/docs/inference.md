# Inference

There are several mechanisms for inference:

- Inference via chaining (see [chaining rules](chaining-rules.md)), which should
  be tagged with `semapv:MappingChaining` as a justification
- Inference via mapping inversion, which should be tagged with
  `semapv:MappingInversion` as a justification
- Inference via prior knowledge, which should be tagged with
  `semapv:BackgroundKnowledgeBasedMatching` as a justification

## Background on Mapping Triples, Quadruples, and Records

This section provides a brief background on different ways of referencing a
mapping appearing in SSSOM.

A mapping triple has a subject, predicate, and object as in (`mesh:C000089`,
`skos:exactMatch`, `CHEBI:28646`). A mapping triple does not clarify the
judgment on whether a triple is true or false, nor how the mapping was created.

A mapping quadruple has a subject, predicate, object, and predicate modifier.
The addition of the predicate modifier allows a mapping quadruple to explicitly
denote the judgment on whether a triple is true or false. For example,
(`mesh:C000089`, `skos:exactMatch`, `CHEBI:28646`, True) explicitly represents
that the above subject, predicate, object triple is true, while (`CHEBI:10057`,
`skos:exactMatch`, `mesh:C002563`, False) is false because `CHEBI:10057` refers
to 9H-xanthene, a small molecule, and `mesh:C002563` refers to xanthan gum, a
polysaccharide. By convention, mapping triples are implicitly considered to
refer to the "true" mapping quadruple.

A mapping record refers to the subject, predicate, object, predicate modifier,
and all other fields in the SSSOM data model (except where otherwise stated in
["Hashing a SSSOM mapping record"](spec-support-hashing.md), such as the
`record_id`).

## Referring to Evidence

The `derived_from` field was introduced in
[#537](https://github.com/mapping-commons/sssom/issues/537) in order to
reference the original subject-predicate-object-predicate modifier quadruple
from which new mappings are inferred/derived.

The following example demonstrates how the `derived_from` field can be leveraged
in two scenarios:

1. mapping chaining. the table contains a SKOS exact match from `mesh:C000089`
   to `CHEBI:28646` and from `CHEBI:28646` to `cas:645-92-1`. The third row of
   the table contains a SKOS exact match from `mesh:C000089` to `cas:645-92-1`
   produced through mapping chaining. The `derived_from` column in this row
   contains CURIEs referring to the
   `mesh:C000089`-`skos:exactMatch`-`CHEBI:28646`-True and
   `CHEBI:28646`-`skos:exactMatch`-`cas:645-92-1`-True mapping quadruples,
   concatenated with a pipe
2. mapping inversion. the fourth row of the table contains a SKOS exact match
   from `CHEBI:28646` to `mesh:C000089` produced through mapping inversion of
   the first row of the table. The `derived_from` column in this row contains
   the CURIE referring to the
   `mesh:C000089`-`skos:exactMatch`-`CHEBI:28646`-True quad.

```
# curie_map:
#   cas:  	https://commonchemistry.cas.org/detail?cas_rn=
#   CHEBI: http://purl.obolibrary.org/obo/CHEBI_
#   mesh: http://id.nlm.nih.gov/mesh/
#   orcid: https://orcid.org/
#   semapv: https://w3id.org/semapv/vocab/
#   skos: http://www.w3.org/2004/02/skos/core#
#   mapping: https://example.com/mapping/
# license: https://creativecommons.org/publicdomain/zero/1.0/
# mapping_set_id: https://github.com/mapping-commons/sssom/blob/master/examples/schema/derived_from.sssom.tsv
# creator_id:
#  - orcid:0000-0003-4423-4370
```

| subject_id   | subject_label | predicate_id    | object_id    | object_label | mapping_justification        | derived_from                                                                                                                                       | comment                                                                                                |
| ------------ | ------------- | --------------- | ------------ | ------------ | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| mesh:C000089 | ammeline      | skos:exactMatch | CHEBI:28646  | ammeline     | semapv:ManualMappingCuration |                                                                                                                                                    |                                                                                                        |
| CHEBI:28646  | ammeline      | skos:exactMatch | cas:645-92-1 | Ammeline     | semapv:ManualMappingCuration |                                                                                                                                                    |                                                                                                        |
| mesh:C000089 | ammeline      | skos:exactMatch | cas:645-92-1 | Ammeline     | semapv:MappingChaining       | mapping:36a1f9244ea7641a90987c82f33c25c0c13712ee8f48207b2a0825f8a4e4e26a\|mapping:bb768f0b1e1643298f4df1a381001f6ed68fcc8fff49b371f0235b51dbab9e1e | this example needs to refer to the first two mappings in this table by mapping sameness identifier     |
| CHEBI:28646  | ammeline      | skos:exactMatch | mesh:C000089 | Ammeline     | semapv:MappingInversion      | mapping:36a1f9244ea7641a90987c82f33c25c0c13712ee8f48207b2a0825f8a4e4e26a                                                                           | this example just needs to refer to the first mapping in this table by the mapping sameness identifier |

For the purposes of inference, the mapping quadruple should be used:

1. Mapping triples are insufficient: without the judgment of whether a mapping
   is true or false, then an algorithm could accidentally conclude from
   `A skos:exactMatch B` and `B (not) skos:exactMatch C` that
   `A skos:exactMatch C`. This is why mapping triples are insufficient
2. Full mapping records are inflexible: the SSSOM data should be flexible so if
   additional evidence (i.e., records) for a given mapping quadruple are found,
   then the confidence in the inferred/derived mapping (e.g., chained or
   inverted)can be adjusted accordingly. This is possible because most chaining
   and inversion algorithms logically operate on mapping quadruples, and not on
   records.

Note: the local unique identifiers used for mappings in this example are related
to the proposal in https://github.com/ts4nfdi/mapping-sameness-identifier (which
currently is under review). For now, the SSSOM specification isn't prescribing
how to assign identifiers to mapping quadruples.

### Example with Negative Mappings

The following example uses mapping chaining combine with negated mappings to
infer a non-trivial negative mapping. This illustrates why mapping quadruples
(i.e., subject-predicate-object-predicate modifier) are required over mapping triples
(i.e., subject-predicate-object).

```
# curie_map:
#   cas:  	https://commonchemistry.cas.org/detail?cas_rn=
#   CHEBI: http://purl.obolibrary.org/obo/CHEBI_
#   mesh: http://id.nlm.nih.gov/mesh/
#   orcid: https://orcid.org/
#   semapv: https://w3id.org/semapv/vocab/
#   skos: http://www.w3.org/2004/02/skos/core#
#   mapping: https://example.com/mapping/
# license: https://creativecommons.org/publicdomain/zero/1.0/
# creator_id:
#  - orcid:0000-0003-4423-4370
```

| subject_id  | subject_label | predicate_id    | predicate_modifier | object_id    | object_label | mapping_justification        | derived_from                                                                                                                                        | comment                                                                                                                    |
| ----------- | ------------- | --------------- | ------------------ | ------------ | ------------ | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| CHEBI:10057 | 9H-xanthene   | skos:exactMatch | Not                | mesh:C002563 | xanthan gum  | semapv:ManualMappingCuration |                                                                                                                                                     |                                                                                                                            |
| CAS:92-83-1 | Xanthane      | skos:exactMatch |                    | CHEBI:10057  | 9H-xanthene  | semapv:ManualMappingCuration |                                                                                                                                                     |                                                                                                                            |
| CAS:92-83-1 | Xanthene      | skos:exactMatch | Not                | mesh:C002563 | xanthan gum  | semapv:MappingChaining       | mapping:58f24ccfaf71431276da873c9e7b77ea61a2425e4e8b283b943542290deb292b~\|mapping:bb1162fb2afb1c519c0aa8be98c352061720af220e2d052c571a1fecabff9800 | this example uses the first two mappings in the table, importantly, incorporating the negative modifier in the identifiers |
