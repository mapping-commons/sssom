# Inference

There are several mechanisms for inference:

- Inference via chaining (see [chaining rules](chaining-rules.md)), which should
  be tagged with `semapv:MappingChaining` as a justification
- Inference via mapping inversion, which should be tagged with
  `semapv:MappingInversion` as a justification
- Inference via prior knowledge, which should be tagged with
  `semapv:BackgroundKnowledgeBasedMatching` as a justification

## Referring to Evidence

The `derived_from` field was introduced in
[#537](https://github.com/mapping-commons/sssom/issues/537) in order to
reference the original subject-predicate-object-predicate modifier quadruple
from which new mappings are inferred/derived.

The following example demonstrates how the `derived_from` field can be leveraged when doing both
mapping chaining (i.e., using multiple mappings to infer a new one) and mapping
inversion. The local unique identifiers used for mappings in this example are
related to the proposal in
https://github.com/ts4nfdi/mapping-sameness-identifier (which currently is under
finalization). For now, the SSSOM specification isn't currently prescribing how
to assign CURIEs to mapping quads.

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

| subject_id   | subject_label | predicate_id    | object_id    | object_label | mapping_justification        | derived_from                                                                                                                                       | comment                                                                                               |
| ------------ | ------------- | --------------- | ------------ | ------------ | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| mesh:C000089 | ammeline      | skos:exactMatch | CHEBI:28646  | ammeline     | semapv:ManualMappingCuration |                                                                                                                                                    |                                                                                                       |
| CHEBI:28646  | ammeline      | skos:exactMatch | cas:645-92-1 | Ammeline     | semapv:ManualMappingCuration |                                                                                                                                                    |                                                                                                       |
| mesh:C000089 | ammeline      | skos:exactMatch | cas:645-92-1 | Ammeline     | semapv:MappingChaining       | mapping:36a1f9244ea7641a90987c82f33c25c0c13712ee8f48207b2a0825f8a4e4e26a\|mapping:bb768f0b1e1643298f4df1a381001f6ed68fcc8fff49b371f0235b51dbab9e1e | this example needs to refer to the first two mappings in this table by mapping sameness identifier    |
| CHEBI:28646  | ammeline      | skos:exactMatch | mesh:C000089 | Ammeline     | semapv:MappingInversion      | mapping:36a1f9244ea7641a90987c82f33c25c0c13712ee8f48207b2a0825f8a4e4e26a                                                                           | this example just needs to refer to the first mapping in this table by the mapping sameness identifier |
