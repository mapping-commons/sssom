# Confidence

SSSOM enables annotating confidence in several ways for individual
mappings records and for mapping sets.

1. The creator of a mapping can specify their confidence in t


A value of 1.0 means full confidence and a value of 0.0 means that the
creator is completely unsure whether the mapping is correct or not.

In order to express that a subject-predicate-object triple is incorrect,
assign the `Not` value in the `predicate_modifier` column. If the
`Not` value is present, then a confidence of 1.0 means that the creator of
the mapping is fully confidence that the subject-predicate-object triple
is not true. A value of 0.0 still means that the creator is unsure whether
the mapping is correct or incorrect.