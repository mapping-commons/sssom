# Matching Tools: Implementation Guide for SSSOM

*Summary**: The goal of this document is to advice matching tool developers how to implement SSSOM-style matching justifications as part of their output. For example, if a mapping was determined (or is supported by) a lexical matching process, we can document that, alongside metadata that further describes the details about that process.

As of 17.07.2023, this guide is a _work in progress_. If you are a tool developer interested to implement these recommendations, feel free to reach out on https://github.com/mapping-commons/sssom/issues for support and feel empowered to help us improve this guide!

## Basics

1. A (semantic) mapping in the sense of this guide is a tuple `<s, p, o, |j|>` that describes the correspondence of a subject `s` to an object `o` via a mapping predicate `p`. `|j|` is a non-empty set of mapping justifications that provide evidence towards the validity of the correspondence.
1. As stated above, but re-stated for clarity: **every mapping can be associated with 1 or more justifications**.
1. Carefully consider if a piece of metadata should be applied on [mapping](https://mapping-commons.github.io/sssom/Mapping/) or [mapping set](https://mapping-commons.github.io/sssom/MappingSet/) level. As a rule of thumb, if a piece of metadata applies to absolutely all mappings in the target set, then consider adding it as metadata to the mapping set, to safe space.
1. Justifications in the sense of this guide comprise a *category* (documented in the [mapping_justification](https://mapping-commons.github.io/sssom/mapping_justification/) field), which is represented as a specific matching activity such as "lexical matching", "logical matching", "manual mapping curation", etc, a confidence value that represents the amount of confidence the justification contributes to the perceived truthfulness of a mapping, and additional metadata that provide additional provenance.
1. The basic vocabulary for the justification category is the [Semantic Mapping Vocabulary](https://github.com/mapping-commons/semantic-mapping-vocabulary). Feel free to use the [issue tracker](https://github.com/mapping-commons/semantic-mapping-vocabulary/issues) to request new categories to be added. There is a fast turnaround.
1. The goal of providing mapping justifications is to enable cross-purpose re-use of mappings, sharing of mappings and [mapping reconciliation](glossary.md). Mapping justifications make individual mapping decisions transparent.
1. Adding justifications is always valueable, even if **not all detailed metadata is provided**.
1. Many justifications are combinations of other justifications. For example, we may decide that a match is justified if (a) there is a lexical match and (b) the surrounding graph-structure is isomorphic or (c) the entities involved share the same properties. In this case, we should add individual justifications for each individual justification. The [confidence](https://mapping-commons.github.io/sssom/confidence/) value expresses how **confident the specific justification makes you feel about the truthfulness of the mapping**. If a joint probability is calculated from multiple justifications, add a separate justification for that, e.g. [semapv:CompositeMatching](https://w3id.org/semapv/vocab/CompositeMatching).
1. In the SSSOM TSV formats, every row corresponds to a justification, not a mapping. So the same mapping with three justifications will result in three rows in the SSSOM TSV file.

## Background

Before reading on, please skim through the [technical documentation of SSSOM](index.md) to get a sense of what kind of properties exist, and read our primer on [mapping justifications](mapping-justifications.md) first, which explains how to design a number of frequently used mapping justifications.

As the collection of justifications can impact the performance of he matching process (at least for huge matching tasks), it is adviseable that the process can be switched off by the CLI.

For most matching processes, we first construct a candidate mapping set from a combination of sources, for example:

1. Mappings provided by user as input to the matching process
1. Lexical exact matching
1. Lexical fuzzy matching (traditional and word embeddings)

As a second step, we use often complex combinations of techniques to refine and expand the candidate mapping set:

1. Structural matching (graph-based approaches etc)
1. Semantic matching
   1. Logical matching (for example by deconstructing complex terms into composites and then using logical reasoning).
   1. Similarity based matching, including graph-embedding similarity (machine learning), old-school semantic similarity measures like Resnik or even Jaccard (over some part of the ontology/schema structure)

As a rule of thumb, the more complex the rules by which a match is determined, the harder it is to provide a useful justification. To put it slighly differently: the more complex a justification, the less useful it is if the goal is to make matching decisions **transparent for human users**. A good example of this are decisions based on embedding (e.g. graph, node) similarity: while it is often useful to understand that a match has been determined by a threshold (e.g. >=0.9) of cosine similarity of a node embedding, it is less important to communicate exactly how the embedding space was constructed.

This insight guides our implementation in two ways:

1. We start by focusing on the "easy" cases with clear mapping justifications (like the lexical ones used to construct the _candidate mapping set_), and incrementally work our way up towards harder ones.
1. We have a default justification for "complex" cases which we have not covered yet. This is necessary not only because it may be hard to construct complex justifications from within a matching tool, but also because SSSOM simply does not have a way to express the justification yet (in this case, request clarification on the [SSSOM issue tracker](https://github.com/mapping-commons/sssom/issues)).

## Step-by-step guide for implementation

This step by step guide is roughly according to our own thinking of what should be done first, second, and so on.

1. Add an option to your matching tool to output legal SSSOM TSV (recommended format now), for example `--export-sssom` or similar.
1. OPTIONAL: Add an option to your matching tool to accept legal SSSOM TSV as user input as an alternative to Alignment API (recommended format now).
1. Always provide basic provenance in the SSSOM output:
   - [mapping_tool](https://mapping-commons.github.io/sssom/mapping_tool/): The canonical reference to your tool, ideally a persistent identifier.
   - [mapping_tool_version](https://mapping-commons.github.io/sssom/mapping_tool_version/): The version of the tool used to compute the mapping set.
   - [mapping_set_id](https://mapping-commons.github.io/sssom/mapping_set_id/): A (often randomly generated) mapping set identifier.
   - [mapping_date](https://mapping-commons.github.io/sssom/mapping_date/): The date the mapping was generated.
   - OPTIONAL: if available, add [subject_source](https://mapping-commons.github.io/sssom/subject_source/), [object_source](https://mapping-commons.github.io/sssom/object_source/) and [subject_source_version](https://mapping-commons.github.io/sssom/subject_source_version/), [object_source_version](https://mapping-commons.github.io/sssom/object_source_version/).
1. Document some basic entity metadata, this can help reading the mapping set:
   - [subject_label](https://mapping-commons.github.io/sssom/subject_label/), [object_label](https://mapping-commons.github.io/sssom/object_label/): If available, add the label of the subject, and object id.
1. Add basic justification support
    1. Track lexical matching-based mapping decisions. A good chunk of candidate mappings will be computed by some form of lexical matching. See [here](mapping-justifications.md#lexical-matching) for details.
    1. If something more complex than a simple lexical matching has happened, try to find an appropriate one in [SEMAPV](https://mapping-commons.github.io/semantic-mapping-vocabulary/). If none exists, or its too much work to create one, use as a fall-through:
       - [semapv:CompositeMatching](https://w3id.org/semapv/vocab/CompositeMatching) in the case that the match was established through a combination of approaches, but you don't want to provide justifications for each individual one.
       - [semapv:UnspecifiedMatching](https://w3id.org/semapv/vocab/UnspecifiedMatching) in the case you dont know why the match happened.
    1. All justifications should come with a [confidence](https://mapping-commons.github.io/sssom/confidence/) value that expresses how **confident the specific justification makes you feel about the truthfulness of the mapping**.
1. Track if a mapping was provided (as input) by a user. Ideally, if the input to the matching process is SSSOM, simply adopt all of the mapping justifications provided by the user. If the provided mapping has no metadata, add a suitable [mapping_provider](https://mapping-commons.github.io/sssom/mapping_provider/) value (e.g. `MYTOOL:USER`, to indicate  that the mapping was provided by the user).
1. Add advanced justification support. Add all metadata explained in [mapping justifications](mapping-justifications.md). Where suitable fields or values are missing from the [SSSOM datamodel](https://mapping-commons.github.io/sssom/) or [SEMAPV](https://mapping-commons.github.io/semantic-mapping-vocabulary/), request them on the [SSSOM](https://github.com/mapping-commons/sssom/issues) or [SEMAPV issue tracker](https://github.com/mapping-commons/semantic-mapping-vocabulary/issues) respectively. There is likely a lot of interesting details to be added, so dont be shy to request/suggest!
1. If you reject a user provided mapping, it makes sense to include that in a negative mapping set in SSSOM. You could provide [predicate_modifier](https://mapping-commons.github.io/sssom/predicate_modifier/)`= NOT` to ensure the file is not interpreted wrongly.
1. HIGHLY OPTIONAL: In some few cases, it may be interesting to inform the user that not all mappings are 1:1. In this case, it could be advisable to use the `mapping_cardinality` field.
1. OPTIONAL: If relevant you can add the [subject_type](https://mapping-commons.github.io/sssom/subject_type/) and [object_type](https://mapping-commons.github.io/sssom/object_type/) fields to your output, if known. This can be interesting in some cases with mixed content (being able to separate `owl:Class` related mappings from those about `owl:ObjectProperty`).
1. You can always use the [comment](https://mapping-commons.github.io/sssom/comment/) or [other](https://mapping-commons.github.io/sssom/other/)* fields to deposit additional useful metadata that can later be turned into structured content.

## Examples

- [MGI Mouse-Human mappings](https://github.com/mapping-commons/mh_mapping_initiative/blob/master/mappings/mp_hp_mgi_all.sssom.tsv)
- [SSSOM examples](https://github.com/mapping-commons/sssom/tree/master/examples/embedded)
