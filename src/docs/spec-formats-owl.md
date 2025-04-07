# The OWL/RDF serialisation format

This section defines a way to serialise SSSOM mappings as _reified OWL axioms_. This has the advantage that any mapping set can be simply merged with an ontology in the usual way, for example using [ROBOT merge](https://robot.obolibrary.org/merge).

The OWL/RDF serialisation rules deal with three types of reified OWL axioms, and a few sub-types:

1. Predicate is an annotation property
2. Predicate is an object property and
   1. Object/Subject are classes
   2. Object/Subject are individuals
3. Predicate is language relational construct of RDFS or OWL (`rdfs:subClassOf`, `owl:equivalentClass`)

## Predicate is an annotation property:

If the predicate corresponds to an annotation property, the mapping `<S,P,O, meta>` gets converted to an OWLAnnotationAssertion axiom: `OWLAnnotationAssertion(P,S,O)`. All mapping level metadata (`meta`) gets converted into OWLAnnotation objects which are materialised as axiom annotations on the mapping annotation assertion, see [OWL 2 Structural Specification](https://www.w3.org/TR/owl2-syntax/#Annotations):

```
AnnotationAssertion(meta P, S, O)
```

Where `meta` is a sequence of OWL Annotations objects like:

```
Annotation(Q1,V1) Annotation(Q2,V2) ... Annotation(Qn,Vn)
```

where `Qi` is a SSSOM metadata slot and `Vi` is an annotation value.

Note that if a SSSOM metadata element value is a list `L` (i.e. can have multiple elements, such as creator and others), individual annotations are created for each of them:

```
Annotation(Q,V) for all V in L.
```

Example:

```
AnnotationAssertion(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:mapping_justification semapv:LexicalMatching) skos:exactMatch <http://purl.obolibrary.org/obo/HP_0009894> <http://purl.obolibrary.org/obo/MP_0000019>)
```

Mapping set level annotations are manifested as Ontology annotation in the usual way, according to the [OWL 2 Structural Specification](https://www.w3.org/TR/owl2-syntax/#Annotations).

## Predicate is an object property

### Case 1: Object and Subject are classes.

The mapping `<S,P,O>` gets translated into an existential restriction:

```
SubclassOf(S, P some O)
```

All metadata slots are added as OWLAnnotation objects and added to SubclassOf axiom as axiom annotations:

```
SubclassOf(meta, S, P some O)
```

Example:

```
SubClassOf(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:mapping_justification semapv:LexicalMatching) <http://example.org/AA> ObjectSomeValuesFrom(<http://example.org/x> <http://example.org/BB>))
```

### Case 2: Object and Subject are individuals

The mapping `<S,P,O>` gets translated into an object property assertion:

```
ObjectPropertyAssertion(P, S, O)
```

All metadata slots are added as OWLAnnotation objects and added to ObjectPropertyAssertion axiom as axiom annotations:

```
ObjectPropertyAssertion(meta, P, S, O)
```

Example:

```
ObjectPropertyAssertion(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:mapping_justification semapv:LexicalMatching) <http://www.example.org/x> <http://www.example.org/a> <http://www.example.org/b>)
```


### Predicate is language relational construct of RDFS or OWL

The mapping `<S,P,O, meta>` gets translated into an annotated axiom using the following table:

| Mapping predicate   | Generated axiom             |
| ------------------- | --------------------------- |
| owl:equivalentClass | EquivalentClass(meta, S, O) |
| rdfs:subClassOf     | SubClassOf(meta, S, O)      |

Example:

```
SubClassOf(Annotation(sssom:creator_id <https://orcid.org/0000-0002-7356-1779>) Annotation(sssom:mapping_justification semapv:LexicalMatching) <http://www.example.org/a> <http://www.example.org/b>)
```
