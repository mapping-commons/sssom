# Simple Standard for Sharing Ontological Mappings (SSSOM)

![SSSOM banner](images/sssom-banner.png)

The Simple Standard for Sharing Ontological Mappings (SSSOM) is a community-driven standard designed to facilitate the exchange and integration of semantic entity mappings.
As data interoperability becomes increasingly crucial across various domains, SSSOM provides a standardized format to share mappings, enabling researchers and developers to more easily connect and utilize diverse datasets.
By establishing a common framework, SSSOM enhances the consistency, quality, and discoverability of mappings, thereby supporting more effective data integration and analysis.

- **Standardization**: SSSOM provides a unified format for representing semantic, or ontological, mappings, making it easier for different systems and organizations to exchange mapping data consistently.
- **Interoperability**: By using SSSOM, data from diverse sources can be integrated more seamlessly, allowing for improved data analysis and research across various fields, including biology, healthcare, and information technology.

Beyond defining the standard itself, the **SSSOM Core Team** and the SSSOM community also develop reference tools and software libraries for working with the standard.

## SSSOM at a glance: Model and Exchange Format

### Basic model

The [data model](spec-model.md) of SSSOM is centered around two fundamental concepts: mappings and mapping sets.

A **SSSOM mapping** is a statement that there is a correspondence between two semantic entities. It comprises two components:

1. The **core mapping** (or **raw mapping**), which is a triple `<subject, predicate, object>` that represents the correspondence itself between a subject entity, for example a class in an ontology, and an object entity, for example an identifier in some database, via a semantic mapping predicate, for example `skos:exactMatch`.
2. **Metadata** that provide supplementary pieces of information about the core mapping. This notably includes information about the *provenance* of the statement (for example, who authored the statement), the *confidence* with which the mappings holds, and its *justification* (a reason that supports the fidelity of the mapping between the subject and the object, such as _expert review_, or _exact lexical matching_ on the entities' primary names).

A **SSSOM mapping set** is a collection of SSSOM mappings. Mapping sets can also be associated with metadata, such as license statements, or a description.

### The SSSOM/TSV format

The main format proposed by the SSSOM standard to exchange mapping sets is the [SSSOM/TSV format](spec-formats-tsv.md). Here is a basic example of a file in that format:

```
#curie_map:
#  FOODON: http://purl.obolibrary.org/obo/FOODON_
#  KF_FOOD: https://kewl-foodie.inc/food/
#  orcid: https://orcid.org/
#mapping_set_id: https://w3id.org/sssom/tutorial/example1.sssom.tsv
#mapping_set_description: Manually curated alignment of KEWL FOODIE INC internal food and nutrition database with Food Ontology (FOODON). Intended to be used for ontological analysis and grouping of KEWL FOODIE INC related data.
#license: https://creativecommons.org/licenses/by/4.0/
#mapping_date: 2022-05-02
subject_id	subject_label	predicate_id	object_id	object_label	mapping_justification	author_id	confidence	comment
KF_FOOD:F001	apple	skos:exactMatch	FOODON:00002473	apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	0.95	"We could map to FOODON:03310788 instead to cover sliced apples, but only ""whole"" apple types exist."
KF_FOOD:F002	gala	skos:exactMatch	FOODON:00003348	Gala apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	1	
KF_FOOD:F003	pink	skos:exactMatch	FOODON:00004186	Pink apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	0.9	"We could map to FOODON:00004187 instead which more specifically refers to ""raw"" Pink apples. Decided against to be consistent with other mapping choices."
KF_FOOD:F004	braeburn	skos:broadMatch	FOODON:00002473	apple (whole)	semapv:ManualMappingCuration	orcid:0000-0002-7356-1779	1	
```

### Quick links

**General**

- [GitHub page](https://github.com/mapping-commons/sssom)
- [Detailed description](introduction.md)
- [Formal specification](spec-intro.md)

**Publications**

- [A Simple Standard for Sharing Ontological Mappings (SSSOM)](https://doi.org/10.1093/database/baac035) (initial publication in _Database_)
- [A Simple Standard for Ontological Mappings 2022: Updates of data model and outlook](https://zenodo.org/record/7672104) (paper and presentation at the Ontology Matching Workshop 2022)
- [A Simple Standard for Ontological Mappings 2023: Updates on data model, collaborations and tooling](https://zenodo.org/record/8202395) (paper and presentation at the Ontology Matching Workshop 2023)
- [Other presentations](presentations.md)

**Related software**

- [sssom-py](https://mapping-commons.github.io/sssom-py/) (reference implementation of the standard, a toolkit and API for processing mappings, written in Python)
- [SSSOM-Java](https://incenp.org/dvlpt/sssom-java/) (an implementation of the SSSOM standard for the Java language)

## The SSSOM Core Team

### Contact

The preferred way to contact the SSSOM team is through the [issue tracker](https://github.com/mapping-commons/issues) (for problems with SSSOM) or the [GitHub discussion forums](https://github.com/mapping-commons/sssom/discussions) (for general questions).

You can find any of the members of the SSSOM core team [on GitHub](https://github.com/orgs/mapping-commons/teams/sssom-core). Their GitHub profiles usually also provide email addresses.

You can also reach us in the [OBO Foundry Slack](https://obo-communitygroup.slack.com/archives/C01DP18L5GW), in the `#sssom` channel.

### Steering committee

The Steering committee is a self-appointed group of SSSOM contributors, whose aim is to drive the evolution of the standard and coordinate community contributions.

* [Nicolas Matentzoglu](https://orcid.org/0000-0002-7356-1779) (Semanticly, Independent Consultant; [@matentzn](https://github.com/matentzn))
* [Damien Goutte-Gattat](https://orcid.org/0000-0002-6095-8718) (Flybase)
* [Harshad Hegde](https://orcid.org/0000-0002-2411-565X) (LBNL)
* [Chris Mungall](https://orcid.org/0000-0002-6601-2165) (LBNL)
* [Melissa Haendel](https://orcid.org/0000-0001-9114-8737) (UNC)

### Documentation/specification editors

* [Anita Caron](https://orcid.org/0000-0002-6523-4866) (EMBL-EBI)
* [Charlie Hoyt](https://orcid.org/0000-0003-4423-4370) (Harvard Medical School; [@cthoyt](https://github.com/cthoyt))
* [David Osumi-Sutherland](https://orcid.org/0000-0002-7073-9172) (EMBL-EBI)
* [Emily Hartley](https://orcid.org/0000-0001-5839-2535) (Critical Path Institute)
* [Ernesto Jimenez-Ruiz](https://orcid.org/0000-0002-9083-4599) (City, University of London)
* [Harry Caufield](https://orcid.org/0000-0001-5705-7831) (LBNL)
* [Henriette Harmse](https://orcid.org/0000-0001-7251-9504) (EMBL-EBI)
* [James McLaughlin](https://orcid.org/0000-0002-8361-2795) (EMBL-EBI)
* [John Graybeal](https://orcid.org/0000-0001-6875-5360) (Independent Consultant)
* [Sierra Moxon](https://orcid.org/0000-0002-8719-7760) (LBNL)
* [Simon Jupp](https://orcid.org/0000-0002-0643-3144) (SciBite)
* [Thomas Liener](https://orcid.org/0000-0003-3257-9937) (Independent Consultant)
* [Tiffany Callahan](https://orcid.org/0000-0002-8169-9049) ([@callahantiff](https://github.com/callahantiff))
* [William Duncan](https://orcid.org/0000-0001-9625-1899) (University of Florida)

### Contributors

* [Alasdair Gray](https://orcid.org/0000-0002-5711-4872)
* [Alex Wagner](https://orcid.org/0000-0002-2502-8961)
* [Amelia L. Hoyt](https://orcid.org/0000-0003-1307-2508)
* [Andrew Williams](https://orcid.org/0000-0002-0692-412X)
* [Anne Thessen](https://orcid.org/0000-0002-2908-3327)
* [Benjamin M. Gyori](https://orcid.org/0000-0001-9439-5346)
* [Bill Baumgartner](https://orcid.org/0000-0001-6717-5313)
* [Cassia Trojahn](https://orcid.org/0000-0002-0096-2766)
* [Clement Jonquet](https://orcid.org/0000-0002-2404-1582)
* [Christopher Chute](https://orcid.org/0000-0001-5437-2545)
* [Chris T. Evelo](https://orcid.org/0000-0002-5301-3142)
* [Damion Dooley](https://orcid.org/0000-0002-8844-9165)
* [Davera Gabriel](https://orcid.org/0000-0001-9041-4597)
* [Harold Solbrig](https://www.wikidata.org/wiki/Q44607574)
* [HyeongSik Kim](https://orcid.org/0000-0002-3002-9838)
* [Ian Harrow](https://orcid.org/0000-0003-0109-0522)
* [Ian Braun](https://orcid.org/0000-0002-2389-9288)
* [James Malone](https://orcid.org/0000-0002-1615-2899)
* [James Overton](https://orcid.org/0000-0001-5139-5557)
* [James P. Balhoff](https://orcid.org/0000-0002-8688-6599)
* [James Stevenson](https://orcid.org/0000-0002-2568-6163)
* [Javier Millán Acosta](https://orcid.org/0000-0002-4166-7093)
* [Jiao Dahzi](https://orcid.org/0000-0001-5052-3836)
* [Joe Flack](https://orcid.org/0000-0002-2906-7319)
* [Jooho Lee](https://orcid.org/0000-0002-2955-3405)
* [Julie McMurry](https://orcid.org/0000-0002-9353-5498)
* [Kori Kuzma](https://orcid.org/0000-0002-9954-7449)
* [Kristin Kostka](https://orcid.org/0000-0003-2595-8736)
* [Lauren Chan](https://orcid.org/0000-0002-7463-6306)
* [Melissa Haendel](https://orcid.org/0000-0001-9114-8737)
* [Monica Munoz-Torres](https://orcid.org/0000-0001-8430-6039)
* [Nicole Vasilevsky](https://orcid.org/0000-0001-5208-3432)
* [Nomi Harris](https://orcid.org/0000-0001-6315-3707)
* [Núria Queralt-Rosinach](https://orcid.org/0000-0003-0169-8159)
* [Sabrina Toro](https://orcid.org/0000-0002-4142-7153)
* [Sebastian Koehler](https://orcid.org/0000-0002-5316-1399)
* [Shahim Essaid](https://orcid.org/0000-0003-2338-2550)
* [Sophie Aubin](https://orcid.org/0000-0003-4805-8220)
* [Sue Bello](https://orcid.org/0000-0003-4606-0597)
* [Sujay Patil](https://orcid.org/0000-0001-6142-1106)
* [Sven Hertling](https://orcid.org/0000-0003-0333-5888)
* [Tim Putman](https://orcid.org/0000-0002-4291-0737)
* [Vinicius de Souza](https://orcid.org/0000-0002-4971-0439)

## Acknowledgements

- See [Funding](funding.md) for details on direct contributions.
- We thank the [Link Model Language (LinkML) project](https://github.com/linkml) and team for their great framework and the LinkML team for their support developing the schema.