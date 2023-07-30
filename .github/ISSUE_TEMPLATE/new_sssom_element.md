---
title: "[New metadata element]: "
name: Add new SSSOM metadata element
about: New metadata element suggestion for SSSOM
assignees: matentzn 
labels: 'new metadata element request'
---

**Element id (e.g. creator_id, mapping_tool_version):**
(Must be lower case and contain only letters and underscores.)

```
element_id_example
```

**Value data type (e.g. URI, URL, text, xsd:boolean):**

```
xsd:string
```

**Description**
(Provide a human-readable description that clarifies the intended use of the metadata element.)

Example description.

**Complete example to a SSSOM file with this element**
(This example can be given as a markdown table or a linked SSSOM file, feel free to edit the markdown table below)

```
# curie_map:
#   HP: http://purl.obolibrary.org/obo/FBbt_
#   MP: http://purl.obolibrary.org/obo/UBERON_
#   owl: http://www.w3.org/2002/07/owl#
#   rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
#   rdfs: http://www.w3.org/2000/01/rdf-schema#
#   semapv: https://w3id.org/semapv/vocab/
#   skos: http://www.w3.org/2004/02/skos/core#
#   sssom: https://w3id.org/sssom/
# license: https://w3id.org/sssom/license/unspecified
# mapping_set_id: https://w3id.org/sssom/mappings/ac9e1878-73f4-4767-8402-a6c40e1b0835
```

| subject_id	| predicate_id	  | object_id	  | mapping_justification   | element_id_example	| 
| ----------- | --------------- | ----------- | ----------------------- | ------------------- |
| HP:0009124	| skos:exactMatch	| MP:0000003	| semapv:LexicalMatching	| YOUR EXAMPLE VALUE	| 
| HP:0008551	| skos:exactMatch	| MP:0000018	| semapv:LexicalMatching	| YOUR EXAMPLE VALUE	|
