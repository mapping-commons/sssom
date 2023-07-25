# Guide to using Mapping Justifications

The goal of this document is to provide the user with a few pointers into the art of mapping justification construction. As of Summer 2023, the SSSOM justification system is still evolving, and will likely benefit from yoru input. Where informative metadata properties or values are missing from the [SSSOM datamodel](https://mapping-commons.github.io/sssom/) or [SEMAPV](https://mapping-commons.github.io/semantic-mapping-vocabulary/), request them on the [SSSOM](https://github.com/mapping-commons/sssom/issues) or [SEMAPV issue tracker](https://github.com/mapping-commons/semantic-mapping-vocabulary/issues) respectively.

## Table of contents

1. [lexical matching](#lexical-matching)
1. [semantic similarity threshold-based matching](#semantic-matching)
1. [mapping review](#mapping-review)
1. Other justifications
    1. background knowledge-based matching
    1. composite matching
    1. instance-based matching
    1. lexical similarity threshold-based matching
    1. logical reasoning
    1. manual mapping curation
    1. mapping chaining-based matching
    1. mapping inversion-based matching
    1. semantic similarity threshold-based matching
    1. structural matching
    1. unspecified matching


<a id="lexical-matching"></a>

## Lexical matching

There are two kinds of lexical matching justifications we try to distinguish:

- [semapv:LexicalMatching](https://w3id.org/semapv/vocab/LexicalMatching): The match is exact (potentially after pre-processing)
- [semapv:LexicalSimilarityThresholdMatching](https://w3id.org/semapv/vocab/LexicalSimilarityThresholdMatching): The match is fuzzy (for example, Levenshtein distance). Note: embedding similarity, even if constructed purely of a word embedding, is considered a form of _semantic_ similarity.

#### Level 1: Track the fact that the match was based on a lexical process

Whenever a mapping was established by a lexical matching process, track at least that fact:

- [mapping_justification](https://mapping-commons.github.io/sssom/mapping_justification/)`: `[semapv:LexicalMatching](https://w3id.org/semapv/vocab/CompositeMatching). This indicates that the mapping was determined through some form of exact lexical matching.

#### Level 2: Track the specific datamodel fields involved in the matching process

Regardless of which specific lexical matching justification you are working on, it is often useful to document the source field of the values used to aquire the match. For example:

- [subject_match_field](https://mapping-commons.github.io/sssom/subject_match_field/)`: rdfs:label` indicates that the value of the `rdfs:label` property on the subject entity was used to establish the match.
- [object_match_field](https://mapping-commons.github.io/sssom/object_match_field/)`: skos:prefLabel` indicates that the value of the `skos:prefLabel` property on the object entity was used to establish the match.
- [match_string](https://mapping-commons.github.io/sssom/match_string/)`: somestring` the exact string that was used to establish the match. This is especially useful if preprocessing methods are applied, see below (Level 3).

#### Level 3: Pre-processing

There are many pre-processing techniques for text in the NLP literature, such as lower-casing or lemmatisation. To judge the fidelity of a match, it is often useful to document the exact techniques used.

- [subject_preprocessing](https://mapping-commons.github.io/sssom/match_string/)`: semapv:BlankNormalisation` indicates that before determining the match, blank characters (spaces etc) where standardised in some way. There are plenty of preprocessing techniques already recorded in [SEMAPV](https://mapping-commons.github.io/semantic-mapping-vocabulary/), including semapv:BlankNormalisation, semapv:CaseNormalization, semapv:DiacriticsSuppression, semapv:DigitSuppression, semapv:Lemmatization, semapv:LinkStripping, semapv:PunctuationElemination, semapv:RegexRemoval, semapv:RegexReplacement, semapv:Stemming, semapv:StopWordRemoval, semapv:TermExtraction, semapv:Tokenization, but feel free to add more.

However, there is one aspect that makes this process quite difficult to implement: Most matchers will blindly apply a set of normalisation techniques prior to processing, but not document which exact technique **had an effect**. It is obviously less useful to say: we applied all these 20 techniques, if only one of them was actually effectual (i.e. caused the string to change).

If there is no (easy) way to keep track of which technique was effectual for any given match, we believe that it is still better to document all techniques, but doing so on `mapping set` level rather than for each individual mappings (to keep the mapping sets smaller).

<a id="semantic-matching"></a>

## Semantic similarity threshold-based matching

The basic idea behind "Semantic similarity threshold-based matching" is that a process that is "semantics aware" (in the loose sense, either by being cognisant about the graph structure, the logical structure, or a contextual textual knowledge such as an embedded Wikipedia article) enabled computing a score between the subject and object entity that to some degree reflects the "similarity" between the two entities. There are many examples of this:

1. The (graph-)structure around the subject and object entities are projected into a common embedding space, and the similarity between the subject and object entities are expressed as cosine similarity between the two embeddings.
1. The jaccard similarity between a set of properties of the subject and object entities is calculated.
1. The Resnik score is calculated between the subject and object entities.

**Important note on applicability of SSSOM for semantic similarity profiles**: SSSOM is not used for documenting semantic similarity profiles, i.e. cross-tables where some set of terms are compared with another set of terms and the semantic similarity is recorded as a score. SSSOM is used to document mappings, and only if a mapping decision is influenced by a semantic similarity based approach, especially in conjunction with as specific thresshold, SSSOM is applicable. For pure semantic similarity tables use [OAK Semantic Similarity](https://incatools.github.io/ontology-access-kit/datamodels/similarity/index.html).

**Semantic vs lexical similarity?**: Semantic similarity is different from lexical similarity intuitively because the context (the graph structure, the background information) is taken into account and provides an (often crude) model of the actual entity, rather than of the word describing it. However, the distinctions can become a bit hazy. Imagine learning a graph embedding on a graph without edges, or a word embedding purely on a single label - there is definitely a grey zone where lexical similarity finishes and semantic similarity begins. In practice though, it should be mostly clear.

## Level 1: Documenting semantic similarity matches

The suggested metadata for semantic similarity threshold based matching approach is:

- [semantic_similarity_measure](https://mapping-commons.github.io/sssom/semantic_similarity_measure/)
- [semantic_similarity_score](https://mapping-commons.github.io/sssom/semantic_similarity_score/)
- ((authors note: Maybe we need a [value for similarity threshold](https://github.com/mapping-commons/sssom/issues/296)?))

<a id="mapping-review"></a>

## Mapping review

[semapv:MappingReview](https://w3id.org/semapv/vocab/MappingReview) is a process conducted by a (usually human) agent to determine the validity of a specific given mapping. It differs from [semapv:ManualMappingCuration](https://w3id.org/semapv/vocab/ManualMappingCuration) in that it does not involve looking for alternative mappings or indeed, necessarily determining if a mapping is the best possible mapping. It should be considered cheaper, less trustworthy evidence compared to [semapv:ManualMappingCuration](https://w3id.org/semapv/vocab/ManualMappingCuration).

There are two kinds of mapping reviews in SSSOM:

- Review as an independent justification: [semapv:MappingReview](https://w3id.org/semapv/vocab/MappingReview) is an independent process that determines the validity of a mapping.
- Review _of_ an existing justification: Instead of evaluating an entire mapping, you can record the fact that someone has looked at a specific justification and deemed it acceptable. In this case, simply record the reviewers identify using the [reviewer_id](https://mapping-commons.github.io/sssom/reviewer_id/) or [reviewer_label](https://mapping-commons.github.io/sssom/reviewer_label/) fields.

