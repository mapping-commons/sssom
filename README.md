[![DOI](https://zenodo.org/badge/13996/mapping-commons/sssom.svg)](https://zenodo.org/badge/latestdoi/13996/mapping-commons/sssom)

# A Simple Standard for Sharing Ontology Mappings (SSSOM)

SSSOM is a Simple Standard for Sharing Ontology Mappings, providing 

1. a TSV-based representation for ontology term mappings
1. a comprehensive set of standard metadata elements to describe mappings and 
1. a standard translation between the TSV and the Web Ontology Language (OWL). 

The SSSOM TSV format in particular is geared towards the needs of the wider bioinformatics community as a way to safely exchange mappings in an easily readable yet semantically well-specified manner. Consider this example of a simple mapping file:

| subject_id	| predicate_id	| object_id	| match_type	| subject_label	| object_label |
| --- | --- | --- | --- | --- | --- |
| HP:0009124	| skos:exactMatch	| MP:0000003	| Lexical	| Abnormal adipose tissue morphology	| abnormal adipose tissue morphology |
| HP:0008551	| skos:exactMatch	| MP:0000018	| Lexical	| Microtia	| small ears |
| HP:0000411	| skos:exactMatch	| MP:0000021	| Lexical	| Protruding ear	| prominent ears |

SSSOM specifies all its metadata elements:

- subject_id
- predicate_id
- object_id
- match_type
- subject_label
- object_label

including clear definitions, examples of use and controlled vocabulary where necessary, along with 30 other optional metadata elements to provide additional provenance.

SSSOM further provides a standard way to 
- augment the TSV file with mapping set - level metadata, such as creator_id, mapping_date or license and
- translate a SSSOM compliant TSV files into _OWL reified axioms_. This will allow the easy loading, and merging of SSSOM mapping tables into existing ontologies using standard tools such as ROBOT (under development).

Note that SSSOM is currently under development and subject to change. Please leave us a comment on the [issue tracker](https://github.com/OBOFoundry/SSSOM/issues) if you want to be involved. The full specification can be found [here](https://w3id.org/sssom/spec).

## Citation

If you have found SSSOM to be helpful in your work, please consider citing:

Matentzoglu, N., *et al.* (2021). [A Simple Standard for Sharing Ontological Mappings (SSSOM)](http://arxiv.org/abs/2112.07051). *arXiv*, 2112.07051. 

```bibtex
@article{matentzoglu2021sssom,
    archivePrefix = {arXiv},
    arxivId = {2112.07051},
    author = {Matentzoglu, Nicolas and Balhoff, James P. and Bello, Susan M. and Bizon, Chris and Brush, Matthew and Callahan, Tiffany J. and Chute, Christopher G and Duncan, William D. and Evelo, Chris T. and Gabriel, Davera and Graybeal, John and Gray, Alasdair and Gyori, Benjamin M. and Haendel, Melissa and Harmse, Henriette and Harris, Nomi L. and Harrow, Ian and Hegde, Harshad and Hoyt, Amelia L. and Hoyt, Charles T. and Jiao, Dazhi and Jim{\'{e}}nez-Ruiz, Ernesto and Jupp, Simon and Kim, Hyeongsik and Koehler, Sebastian and Liener, Thomas and Long, Qinqin and Malone, James and McLaughlin, James A. and McMurry, Julie A. and Moxon, Sierra and Munoz-Torres, Monica C. and Osumi-Sutherland, David and Overton, James A. and Peters, Bjoern and Putman, Tim and Queralt-Rosinach, N{\'{u}}ria and Shefchek, Kent and Solbrig, Harold and Thessen, Anne and Tudorache, Tania and Vasilevsky, Nicole and Wagner, Alex H. and Mungall, Christopher J.},
    eprint = {2112.07051},
    month = {dec},
    title = {{A Simple Standard for Sharing Ontological Mappings (SSSOM)}},
    url = {http://arxiv.org/abs/2112.07051},
    year = {2021}
}
```
