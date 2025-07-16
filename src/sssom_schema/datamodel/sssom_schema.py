# Auto generated from sssom_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-08-09T22:25:39
# Schema: sssom
#
# id: https://w3id.org/sssom/schema/
# description: Datamodel for Simple Standard for Sharing Ontological Mappings (SSSOM)
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Date, Double, Ncname, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, NCName, URI, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBOINOWL = CurieNamespace('oboInOwl', 'http://www.geneontology.org/formats/oboInOwl#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SEMAPV = CurieNamespace('semapv', 'https://w3id.org/semapv/vocab/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SSSOM = CurieNamespace('sssom', 'https://w3id.org/sssom/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = SSSOM


# Types
class EntityReference(Uriorcurie):
    """ A reference to an entity involved in the mapping.
 """
    type_class_uri = RDFS["Resource"]
    type_class_curie = "rdfs:Resource"
    type_name = "EntityReference"
    type_model_uri = SSSOM.EntityReference


# Class references
class PrefixPrefixName(NCName):
    pass


@dataclass
class MappingSet(YAMLRoot):
    """
    Represents a set of mappings
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SSSOM["MappingSet"]
    class_class_curie: ClassVar[str] = "sssom:MappingSet"
    class_name: ClassVar[str] = "mapping set"
    class_model_uri: ClassVar[URIRef] = SSSOM.MappingSet

    mapping_set_id: Union[str, URI] = None
    license: Union[str, URI] = None
    curie_map: Optional[Union[Dict[Union[str, PrefixPrefixName], Union[dict, "Prefix"]], List[Union[dict, "Prefix"]]]] = empty_dict()
    mappings: Optional[Union[Union[dict, "Mapping"], List[Union[dict, "Mapping"]]]] = empty_list()
    mapping_set_version: Optional[str] = None
    mapping_set_source: Optional[Union[Union[str, URI], List[Union[str, URI]]]] = empty_list()
    mapping_set_title: Optional[str] = None
    mapping_set_description: Optional[str] = None
    creator_id: Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]] = empty_list()
    creator_label: Optional[Union[str, List[str]]] = empty_list()
    subject_type: Optional[Union[str, "EntityTypeEnum"]] = None
    subject_source: Optional[Union[str, EntityReference]] = None
    subject_source_version: Optional[str] = None
    object_type: Optional[Union[str, "EntityTypeEnum"]] = None
    object_source: Optional[Union[str, EntityReference]] = None
    object_source_version: Optional[str] = None
    mapping_provider: Optional[Union[str, URI]] = None
    mapping_tool: Optional[str] = None
    mapping_tool_version: Optional[str] = None
    mapping_date: Optional[Union[str, XSDDate]] = None
    publication_date: Optional[Union[str, XSDDate]] = None
    subject_match_field: Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]] = empty_list()
    object_match_field: Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]] = empty_list()
    subject_preprocessing: Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]] = empty_list()
    object_preprocessing: Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]] = empty_list()
    see_also: Optional[Union[str, List[str]]] = empty_list()
    issue_tracker: Optional[Union[str, URI]] = None
    other: Optional[str] = None
    comment: Optional[str] = None
    extension_definitions: Optional[Union[Union[dict, "ExtensionDefinition"], List[Union[dict, "ExtensionDefinition"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.mapping_set_id):
            self.MissingRequiredField("mapping_set_id")
        if not isinstance(self.mapping_set_id, URI):
            self.mapping_set_id = URI(self.mapping_set_id)

        if self._is_empty(self.license):
            self.MissingRequiredField("license")
        if not isinstance(self.license, URI):
            self.license = URI(self.license)

        self._normalize_inlined_as_dict(slot_name="curie_map", slot_type=Prefix, key_name="prefix_name", keyed=True)

        if not isinstance(self.mappings, list):
            self.mappings = [self.mappings] if self.mappings is not None else []
        self.mappings = [v if isinstance(v, Mapping) else Mapping(**as_dict(v)) for v in self.mappings]

        if self.mapping_set_version is not None and not isinstance(self.mapping_set_version, str):
            self.mapping_set_version = str(self.mapping_set_version)

        if not isinstance(self.mapping_set_source, list):
            self.mapping_set_source = [self.mapping_set_source] if self.mapping_set_source is not None else []
        self.mapping_set_source = [v if isinstance(v, URI) else URI(v) for v in self.mapping_set_source]

        if self.mapping_set_title is not None and not isinstance(self.mapping_set_title, str):
            self.mapping_set_title = str(self.mapping_set_title)

        if self.mapping_set_description is not None and not isinstance(self.mapping_set_description, str):
            self.mapping_set_description = str(self.mapping_set_description)

        if not isinstance(self.creator_id, list):
            self.creator_id = [self.creator_id] if self.creator_id is not None else []
        self.creator_id = [v if isinstance(v, EntityReference) else EntityReference(v) for v in self.creator_id]

        if not isinstance(self.creator_label, list):
            self.creator_label = [self.creator_label] if self.creator_label is not None else []
        self.creator_label = [v if isinstance(v, str) else str(v) for v in self.creator_label]

        if self.subject_type is not None and not isinstance(self.subject_type, EntityTypeEnum):
            self.subject_type = EntityTypeEnum(self.subject_type)

        if self.subject_source is not None and not isinstance(self.subject_source, EntityReference):
            self.subject_source = EntityReference(self.subject_source)

        if self.subject_source_version is not None and not isinstance(self.subject_source_version, str):
            self.subject_source_version = str(self.subject_source_version)

        if self.object_type is not None and not isinstance(self.object_type, EntityTypeEnum):
            self.object_type = EntityTypeEnum(self.object_type)

        if self.object_source is not None and not isinstance(self.object_source, EntityReference):
            self.object_source = EntityReference(self.object_source)

        if self.object_source_version is not None and not isinstance(self.object_source_version, str):
            self.object_source_version = str(self.object_source_version)

        if self.mapping_provider is not None and not isinstance(self.mapping_provider, URI):
            self.mapping_provider = URI(self.mapping_provider)

        if self.mapping_tool is not None and not isinstance(self.mapping_tool, str):
            self.mapping_tool = str(self.mapping_tool)

        if self.mapping_tool_version is not None and not isinstance(self.mapping_tool_version, str):
            self.mapping_tool_version = str(self.mapping_tool_version)

        if self.mapping_date is not None and not isinstance(self.mapping_date, XSDDate):
            self.mapping_date = XSDDate(self.mapping_date)

        if self.publication_date is not None and not isinstance(self.publication_date, XSDDate):
            self.publication_date = XSDDate(self.publication_date)

        if not isinstance(self.subject_match_field, list):
            self.subject_match_field = [self.subject_match_field] if self.subject_match_field is not None else []
        self.subject_match_field = [v if isinstance(v, EntityReference) else EntityReference(v) for v in self.subject_match_field]

        if not isinstance(self.object_match_field, list):
            self.object_match_field = [self.object_match_field] if self.object_match_field is not None else []
        self.object_match_field = [v if isinstance(v, EntityReference) else EntityReference(v) for v in self.object_match_field]

        if not isinstance(self.subject_preprocessing, list):
            self.subject_preprocessing = [self.subject_preprocessing] if self.subject_preprocessing is not None else []
        self.subject_preprocessing = [v if isinstance(v, EntityReference) else EntityReference(v) for v in self.subject_preprocessing]

        if not isinstance(self.object_preprocessing, list):
            self.object_preprocessing = [self.object_preprocessing] if self.object_preprocessing is not None else []
        self.object_preprocessing = [v if isinstance(v, EntityReference) else EntityReference(v) for v in self.object_preprocessing]

        if not isinstance(self.see_also, list):
            self.see_also = [self.see_also] if self.see_also is not None else []
        self.see_also = [v if isinstance(v, str) else str(v) for v in self.see_also]

        if self.issue_tracker is not None and not isinstance(self.issue_tracker, URI):
            self.issue_tracker = URI(self.issue_tracker)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        self._normalize_inlined_as_dict(slot_name="extension_definitions", slot_type=ExtensionDefinition, key_name="slot_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Mapping(YAMLRoot):
    """
    Represents an individual mapping between a pair of entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL["Axiom"]
    class_class_curie: ClassVar[str] = "owl:Axiom"
    class_name: ClassVar[str] = "mapping"
    class_model_uri: ClassVar[URIRef] = SSSOM.Mapping

    predicate_id: Union[str, EntityReference] = None
    mapping_justification: Union[str, EntityReference] = None
    subject_id: Optional[Union[str, EntityReference]] = None
    subject_label: Optional[str] = None
    subject_category: Optional[str] = None
    predicate_label: Optional[str] = None
    predicate_modifier: Optional[Union[str, "PredicateModifierEnum"]] = None
    object_id: Optional[Union[str, EntityReference]] = None
    object_label: Optional[str] = None
    object_category: Optional[str] = None
    author_id: Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]] = empty_list()
    author_label: Optional[Union[str, List[str]]] = empty_list()
    reviewer_id: Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]] = empty_list()
    reviewer_label: Optional[Union[str, List[str]]] = empty_list()
    creator_id: Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]] = empty_list()
    creator_label: Optional[Union[str, List[str]]] = empty_list()
    license: Optional[Union[str, URI]] = None
    subject_type: Optional[Union[str, "EntityTypeEnum"]] = None
    subject_source: Optional[Union[str, EntityReference]] = None
    subject_source_version: Optional[str] = None
    object_type: Optional[Union[str, "EntityTypeEnum"]] = None
    object_source: Optional[Union[str, EntityReference]] = None
    object_source_version: Optional[str] = None
    mapping_provider: Optional[Union[str, URI]] = None
    mapping_source: Optional[Union[str, EntityReference]] = None
    mapping_cardinality: Optional[Union[str, "MappingCardinalityEnum"]] = None
    mapping_tool: Optional[str] = None
    mapping_tool_version: Optional[str] = None
    mapping_date: Optional[Union[str, XSDDate]] = None
    publication_date: Optional[Union[str, XSDDate]] = None
    confidence: Optional[float] = None
    curation_rule: Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]] = empty_list()
    curation_rule_text: Optional[Union[str, List[str]]] = empty_list()
    subject_match_field: Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]] = empty_list()
    object_match_field: Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]] = empty_list()
    match_string: Optional[Union[str, List[str]]] = empty_list()
    subject_preprocessing: Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]] = empty_list()
    object_preprocessing: Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]] = empty_list()
    similarity_score: Optional[float] = None
    similarity_measure: Optional[str] = None
    see_also: Optional[Union[str, List[str]]] = empty_list()
    issue_tracker_item: Optional[Union[str, EntityReference]] = None
    other: Optional[str] = None
    comment: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.predicate_id):
            self.MissingRequiredField("predicate_id")
        if not isinstance(self.predicate_id, EntityReference):
            self.predicate_id = EntityReference(self.predicate_id)

        if self._is_empty(self.mapping_justification):
            self.MissingRequiredField("mapping_justification")
        if not isinstance(self.mapping_justification, EntityReference):
            self.mapping_justification = EntityReference(self.mapping_justification)

        if self.subject_id is not None and not isinstance(self.subject_id, EntityReference):
            self.subject_id = EntityReference(self.subject_id)

        if self.subject_label is not None and not isinstance(self.subject_label, str):
            self.subject_label = str(self.subject_label)

        if self.subject_category is not None and not isinstance(self.subject_category, str):
            self.subject_category = str(self.subject_category)

        if self.predicate_label is not None and not isinstance(self.predicate_label, str):
            self.predicate_label = str(self.predicate_label)

        if self.predicate_modifier is not None and not isinstance(self.predicate_modifier, PredicateModifierEnum):
            self.predicate_modifier = PredicateModifierEnum(self.predicate_modifier)

        if self.object_id is not None and not isinstance(self.object_id, EntityReference):
            self.object_id = EntityReference(self.object_id)

        if self.object_label is not None and not isinstance(self.object_label, str):
            self.object_label = str(self.object_label)

        if self.object_category is not None and not isinstance(self.object_category, str):
            self.object_category = str(self.object_category)

        if not isinstance(self.author_id, list):
            self.author_id = [self.author_id] if self.author_id is not None else []
        self.author_id = [v if isinstance(v, EntityReference) else EntityReference(v) for v in self.author_id]

        if not isinstance(self.author_label, list):
            self.author_label = [self.author_label] if self.author_label is not None else []
        self.author_label = [v if isinstance(v, str) else str(v) for v in self.author_label]

        if not isinstance(self.reviewer_id, list):
            self.reviewer_id = [self.reviewer_id] if self.reviewer_id is not None else []
        self.reviewer_id = [v if isinstance(v, EntityReference) else EntityReference(v) for v in self.reviewer_id]

        if not isinstance(self.reviewer_label, list):
            self.reviewer_label = [self.reviewer_label] if self.reviewer_label is not None else []
        self.reviewer_label = [v if isinstance(v, str) else str(v) for v in self.reviewer_label]

        if not isinstance(self.creator_id, list):
            self.creator_id = [self.creator_id] if self.creator_id is not None else []
        self.creator_id = [v if isinstance(v, EntityReference) else EntityReference(v) for v in self.creator_id]

        if not isinstance(self.creator_label, list):
            self.creator_label = [self.creator_label] if self.creator_label is not None else []
        self.creator_label = [v if isinstance(v, str) else str(v) for v in self.creator_label]

        if self.license is not None and not isinstance(self.license, URI):
            self.license = URI(self.license)

        if self.subject_type is not None and not isinstance(self.subject_type, EntityTypeEnum):
            self.subject_type = EntityTypeEnum(self.subject_type)

        if self.subject_source is not None and not isinstance(self.subject_source, EntityReference):
            self.subject_source = EntityReference(self.subject_source)

        if self.subject_source_version is not None and not isinstance(self.subject_source_version, str):
            self.subject_source_version = str(self.subject_source_version)

        if self.object_type is not None and not isinstance(self.object_type, EntityTypeEnum):
            self.object_type = EntityTypeEnum(self.object_type)

        if self.object_source is not None and not isinstance(self.object_source, EntityReference):
            self.object_source = EntityReference(self.object_source)

        if self.object_source_version is not None and not isinstance(self.object_source_version, str):
            self.object_source_version = str(self.object_source_version)

        if self.mapping_provider is not None and not isinstance(self.mapping_provider, URI):
            self.mapping_provider = URI(self.mapping_provider)

        if self.mapping_source is not None and not isinstance(self.mapping_source, EntityReference):
            self.mapping_source = EntityReference(self.mapping_source)

        if self.mapping_cardinality is not None and not isinstance(self.mapping_cardinality, MappingCardinalityEnum):
            self.mapping_cardinality = MappingCardinalityEnum(self.mapping_cardinality)

        if self.mapping_tool is not None and not isinstance(self.mapping_tool, str):
            self.mapping_tool = str(self.mapping_tool)

        if self.mapping_tool_version is not None and not isinstance(self.mapping_tool_version, str):
            self.mapping_tool_version = str(self.mapping_tool_version)

        if self.mapping_date is not None and not isinstance(self.mapping_date, XSDDate):
            self.mapping_date = XSDDate(self.mapping_date)

        if self.publication_date is not None and not isinstance(self.publication_date, XSDDate):
            self.publication_date = XSDDate(self.publication_date)

        if self.confidence is not None and not isinstance(self.confidence, float):
            self.confidence = float(self.confidence)

        if not isinstance(self.curation_rule, list):
            self.curation_rule = [self.curation_rule] if self.curation_rule is not None else []
        self.curation_rule = [v if isinstance(v, EntityReference) else EntityReference(v) for v in self.curation_rule]

        if not isinstance(self.curation_rule_text, list):
            self.curation_rule_text = [self.curation_rule_text] if self.curation_rule_text is not None else []
        self.curation_rule_text = [v if isinstance(v, str) else str(v) for v in self.curation_rule_text]

        if not isinstance(self.subject_match_field, list):
            self.subject_match_field = [self.subject_match_field] if self.subject_match_field is not None else []
        self.subject_match_field = [v if isinstance(v, EntityReference) else EntityReference(v) for v in self.subject_match_field]

        if not isinstance(self.object_match_field, list):
            self.object_match_field = [self.object_match_field] if self.object_match_field is not None else []
        self.object_match_field = [v if isinstance(v, EntityReference) else EntityReference(v) for v in self.object_match_field]

        if not isinstance(self.match_string, list):
            self.match_string = [self.match_string] if self.match_string is not None else []
        self.match_string = [v if isinstance(v, str) else str(v) for v in self.match_string]

        if not isinstance(self.subject_preprocessing, list):
            self.subject_preprocessing = [self.subject_preprocessing] if self.subject_preprocessing is not None else []
        self.subject_preprocessing = [v if isinstance(v, EntityReference) else EntityReference(v) for v in self.subject_preprocessing]

        if not isinstance(self.object_preprocessing, list):
            self.object_preprocessing = [self.object_preprocessing] if self.object_preprocessing is not None else []
        self.object_preprocessing = [v if isinstance(v, EntityReference) else EntityReference(v) for v in self.object_preprocessing]

        if self.similarity_score is not None and not isinstance(self.similarity_score, float):
            self.similarity_score = float(self.similarity_score)

        if self.similarity_measure is not None and not isinstance(self.similarity_measure, str):
            self.similarity_measure = str(self.similarity_measure)

        if not isinstance(self.see_also, list):
            self.see_also = [self.see_also] if self.see_also is not None else []
        self.see_also = [v if isinstance(v, str) else str(v) for v in self.see_also]

        if self.issue_tracker_item is not None and not isinstance(self.issue_tracker_item, EntityReference):
            self.issue_tracker_item = EntityReference(self.issue_tracker_item)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        super().__post_init__(**kwargs)


@dataclass
class MappingRegistry(YAMLRoot):
    """
    A registry for managing mapping sets. It holds a set of mapping set references, and can import other registries.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SSSOM["MappingRegistry"]
    class_class_curie: ClassVar[str] = "sssom:MappingRegistry"
    class_name: ClassVar[str] = "mapping registry"
    class_model_uri: ClassVar[URIRef] = SSSOM.MappingRegistry

    mapping_registry_id: Union[str, EntityReference] = None
    mapping_registry_title: Optional[str] = None
    mapping_registry_description: Optional[str] = None
    imports: Optional[Union[Union[str, URI], List[Union[str, URI]]]] = empty_list()
    mapping_set_references: Optional[Union[Union[dict, "MappingSetReference"], List[Union[dict, "MappingSetReference"]]]] = empty_list()
    documentation: Optional[Union[str, URI]] = None
    homepage: Optional[Union[str, URI]] = None
    issue_tracker: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.mapping_registry_id):
            self.MissingRequiredField("mapping_registry_id")
        if not isinstance(self.mapping_registry_id, EntityReference):
            self.mapping_registry_id = EntityReference(self.mapping_registry_id)

        if self.mapping_registry_title is not None and not isinstance(self.mapping_registry_title, str):
            self.mapping_registry_title = str(self.mapping_registry_title)

        if self.mapping_registry_description is not None and not isinstance(self.mapping_registry_description, str):
            self.mapping_registry_description = str(self.mapping_registry_description)

        if not isinstance(self.imports, list):
            self.imports = [self.imports] if self.imports is not None else []
        self.imports = [v if isinstance(v, URI) else URI(v) for v in self.imports]

        self._normalize_inlined_as_dict(slot_name="mapping_set_references", slot_type=MappingSetReference, key_name="mapping_set_id", keyed=False)

        if self.documentation is not None and not isinstance(self.documentation, URI):
            self.documentation = URI(self.documentation)

        if self.homepage is not None and not isinstance(self.homepage, URI):
            self.homepage = URI(self.homepage)

        if self.issue_tracker is not None and not isinstance(self.issue_tracker, URI):
            self.issue_tracker = URI(self.issue_tracker)

        super().__post_init__(**kwargs)


@dataclass
class MappingSetReference(YAMLRoot):
    """
    A reference to a mapping set. It allows to augment mapping set metadata from the perspective of the registry, for
    example, providing confidence, or a local filename or a grouping.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SSSOM["MappingSetReference"]
    class_class_curie: ClassVar[str] = "sssom:MappingSetReference"
    class_name: ClassVar[str] = "mapping set reference"
    class_model_uri: ClassVar[URIRef] = SSSOM.MappingSetReference

    mapping_set_id: Union[str, URI] = None
    mirror_from: Optional[Union[str, URI]] = None
    registry_confidence: Optional[float] = None
    mapping_set_group: Optional[str] = None
    last_updated: Optional[Union[str, XSDDate]] = None
    local_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.mapping_set_id):
            self.MissingRequiredField("mapping_set_id")
        if not isinstance(self.mapping_set_id, URI):
            self.mapping_set_id = URI(self.mapping_set_id)

        if self.mirror_from is not None and not isinstance(self.mirror_from, URI):
            self.mirror_from = URI(self.mirror_from)

        if self.registry_confidence is not None and not isinstance(self.registry_confidence, float):
            self.registry_confidence = float(self.registry_confidence)

        if self.mapping_set_group is not None and not isinstance(self.mapping_set_group, str):
            self.mapping_set_group = str(self.mapping_set_group)

        if self.last_updated is not None and not isinstance(self.last_updated, XSDDate):
            self.last_updated = XSDDate(self.last_updated)

        if self.local_name is not None and not isinstance(self.local_name, str):
            self.local_name = str(self.local_name)

        super().__post_init__(**kwargs)


@dataclass
class Prefix(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SSSOM["Prefix"]
    class_class_curie: ClassVar[str] = "sssom:Prefix"
    class_name: ClassVar[str] = "prefix"
    class_model_uri: ClassVar[URIRef] = SSSOM.Prefix

    prefix_name: Union[str, PrefixPrefixName] = None
    prefix_url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.prefix_name):
            self.MissingRequiredField("prefix_name")
        if not isinstance(self.prefix_name, PrefixPrefixName):
            self.prefix_name = PrefixPrefixName(self.prefix_name)

        if self.prefix_url is not None and not isinstance(self.prefix_url, URI):
            self.prefix_url = URI(self.prefix_url)

        super().__post_init__(**kwargs)


@dataclass
class ExtensionDefinition(YAMLRoot):
    """
    A definition of an extension (non-standard) slot.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SSSOM["ExtensionDefinition"]
    class_class_curie: ClassVar[str] = "sssom:ExtensionDefinition"
    class_name: ClassVar[str] = "extension definition"
    class_model_uri: ClassVar[URIRef] = SSSOM.ExtensionDefinition

    slot_name: Union[str, NCName] = None
    property: Optional[Union[str, URIorCURIE]] = None
    type_hint: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.slot_name):
            self.MissingRequiredField("slot_name")
        if not isinstance(self.slot_name, NCName):
            self.slot_name = NCName(self.slot_name)

        if self.property is not None and not isinstance(self.property, URIorCURIE):
            self.property = URIorCURIE(self.property)

        if self.type_hint is not None and not isinstance(self.type_hint, URIorCURIE):
            self.type_hint = URIorCURIE(self.type_hint)

        super().__post_init__(**kwargs)


@dataclass
class Propagatable(YAMLRoot):
    """
    Metamodel extension class to describe slots whose value can be propagated down from the MappingSet class to the
    Mapping class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SSSOM["Propagatable"]
    class_class_curie: ClassVar[str] = "sssom:Propagatable"
    class_name: ClassVar[str] = "Propagatable"
    class_model_uri: ClassVar[URIRef] = SSSOM.Propagatable

    propagated: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.propagated is not None and not isinstance(self.propagated, Bool):
            self.propagated = Bool(self.propagated)

        super().__post_init__(**kwargs)


class NoTermFound(YAMLRoot):
    """
    sssom:NoTermFound can be used in place of a subject_id or object_id when the corresponding entity could not be
    found. It SHOULD be used in conjunction with a corresponding subject_source or object_source to signify where the
    term was not found.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SSSOM["NoTermFound"]
    class_class_curie: ClassVar[str] = "sssom:NoTermFound"
    class_name: ClassVar[str] = "NoTermFound"
    class_model_uri: ClassVar[URIRef] = SSSOM.NoTermFound


# Enumerations
class EntityTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EntityTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "owl class",
            PermissibleValue(
                text="owl class",
                meaning=OWL["Class"]))
        setattr(cls, "owl object property",
            PermissibleValue(
                text="owl object property",
                meaning=OWL["ObjectProperty"]))
        setattr(cls, "owl data property",
            PermissibleValue(
                text="owl data property",
                meaning=OWL["DataProperty"]))
        setattr(cls, "owl annotation property",
            PermissibleValue(
                text="owl annotation property",
                meaning=OWL["AnnotationProperty"]))
        setattr(cls, "owl named individual",
            PermissibleValue(
                text="owl named individual",
                meaning=OWL["NamedIndividual"]))
        setattr(cls, "skos concept",
            PermissibleValue(
                text="skos concept",
                meaning=SKOS["Concept"]))
        setattr(cls, "rdfs resource",
            PermissibleValue(
                text="rdfs resource",
                meaning=RDFS["Resource"]))
        setattr(cls, "rdfs class",
            PermissibleValue(
                text="rdfs class",
                meaning=RDFS["Class"]))
        setattr(cls, "rdfs literal",
            PermissibleValue(
                text="rdfs literal",
                description="""This value indicate that the entity being mapped is not a semantic entity with a distinct identifier, but is instead represented entirely by its literal label. This value MUST NOT be used in the predicate_type slot.""",
                meaning=RDFS["Literal"]))
        setattr(cls, "rdfs datatype",
            PermissibleValue(
                text="rdfs datatype",
                meaning=RDFS["Datatype"]))
        setattr(cls, "rdf property",
            PermissibleValue(
                text="rdf property",
                meaning=RDF["Property"]))

class PredicateModifierEnum(EnumDefinitionImpl):

    Not = PermissibleValue(
        text="Not",
        description="""Negating the mapping predicate. The meaning of the triple becomes subject_id is not a predicate_id match to object_id.""")

    _defn = EnumDefinition(
        name="PredicateModifierEnum",
    )

class MappingCardinalityEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MappingCardinalityEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1:1",
            PermissibleValue(
                text="1:1",
                description="One-to-one mapping"))
        setattr(cls, "1:n",
            PermissibleValue(
                text="1:n",
                description="One-to-many mapping"))
        setattr(cls, "n:1",
            PermissibleValue(
                text="n:1",
                description="Many-to-one mapping"))
        setattr(cls, "1:0",
            PermissibleValue(
                text="1:0",
                description="One-to-none mapping"))
        setattr(cls, "0:1",
            PermissibleValue(
                text="0:1",
                description="None-to-one mapping"))
        setattr(cls, "n:n",
            PermissibleValue(
                text="n:n",
                description="Many-to-many mapping"))

# Slots
class slots:
    pass

slots.prefix_name = Slot(uri=SSSOM.prefix_name, name="prefix_name", curie=SSSOM.curie('prefix_name'),
                   model_uri=SSSOM.prefix_name, domain=None, range=URIRef)

slots.prefix_url = Slot(uri=SSSOM.prefix_url, name="prefix_url", curie=SSSOM.curie('prefix_url'),
                   model_uri=SSSOM.prefix_url, domain=None, range=Optional[Union[str, URI]])

slots.curie_map = Slot(uri=SSSOM.curie_map, name="curie_map", curie=SSSOM.curie('curie_map'),
                   model_uri=SSSOM.curie_map, domain=None, range=Optional[Union[Dict[Union[str, PrefixPrefixName], Union[dict, Prefix]], List[Union[dict, Prefix]]]])

slots.mirror_from = Slot(uri=SSSOM.mirror_from, name="mirror_from", curie=SSSOM.curie('mirror_from'),
                   model_uri=SSSOM.mirror_from, domain=None, range=Optional[Union[str, URI]])

slots.registry_confidence = Slot(uri=SSSOM.registry_confidence, name="registry_confidence", curie=SSSOM.curie('registry_confidence'),
                   model_uri=SSSOM.registry_confidence, domain=None, range=Optional[float])

slots.last_updated = Slot(uri=SSSOM.last_updated, name="last_updated", curie=SSSOM.curie('last_updated'),
                   model_uri=SSSOM.last_updated, domain=None, range=Optional[Union[str, XSDDate]])

slots.local_name = Slot(uri=SSSOM.local_name, name="local_name", curie=SSSOM.curie('local_name'),
                   model_uri=SSSOM.local_name, domain=None, range=Optional[str])

slots.mapping_set_references = Slot(uri=SSSOM.mapping_set_references, name="mapping_set_references", curie=SSSOM.curie('mapping_set_references'),
                   model_uri=SSSOM.mapping_set_references, domain=None, range=Optional[Union[Union[dict, MappingSetReference], List[Union[dict, MappingSetReference]]]])

slots.mapping_registry_id = Slot(uri=SSSOM.mapping_registry_id, name="mapping_registry_id", curie=SSSOM.curie('mapping_registry_id'),
                   model_uri=SSSOM.mapping_registry_id, domain=None, range=Union[str, EntityReference])

slots.mapping_registry_title = Slot(uri=SSSOM.mapping_registry_title, name="mapping_registry_title", curie=SSSOM.curie('mapping_registry_title'),
                   model_uri=SSSOM.mapping_registry_title, domain=None, range=Optional[str])

slots.mapping_registry_description = Slot(uri=SSSOM.mapping_registry_description, name="mapping_registry_description", curie=SSSOM.curie('mapping_registry_description'),
                   model_uri=SSSOM.mapping_registry_description, domain=None, range=Optional[str])

slots.imports = Slot(uri=SSSOM.imports, name="imports", curie=SSSOM.curie('imports'),
                   model_uri=SSSOM.imports, domain=None, range=Optional[Union[Union[str, URI], List[Union[str, URI]]]])

slots.documentation = Slot(uri=SSSOM.documentation, name="documentation", curie=SSSOM.curie('documentation'),
                   model_uri=SSSOM.documentation, domain=None, range=Optional[Union[str, URI]])

slots.homepage = Slot(uri=SSSOM.homepage, name="homepage", curie=SSSOM.curie('homepage'),
                   model_uri=SSSOM.homepage, domain=None, range=Optional[Union[str, URI]])

slots.mappings = Slot(uri=SSSOM.mappings, name="mappings", curie=SSSOM.curie('mappings'),
                   model_uri=SSSOM.mappings, domain=None, range=Optional[Union[Union[dict, Mapping], List[Union[dict, Mapping]]]])

slots.subject_id = Slot(uri=OWL.annotatedSource, name="subject_id", curie=OWL.curie('annotatedSource'),
                   model_uri=SSSOM.subject_id, domain=None, range=Optional[Union[str, EntityReference]])

slots.subject_label = Slot(uri=SSSOM.subject_label, name="subject_label", curie=SSSOM.curie('subject_label'),
                   model_uri=SSSOM.subject_label, domain=None, range=Optional[str])

slots.subject_category = Slot(uri=SSSOM.subject_category, name="subject_category", curie=SSSOM.curie('subject_category'),
                   model_uri=SSSOM.subject_category, domain=None, range=Optional[str])

slots.subject_type = Slot(uri=SSSOM.subject_type, name="subject_type", curie=SSSOM.curie('subject_type'),
                   model_uri=SSSOM.subject_type, domain=None, range=Optional[Union[str, "EntityTypeEnum"]])

slots.predicate_id = Slot(uri=OWL.annotatedProperty, name="predicate_id", curie=OWL.curie('annotatedProperty'),
                   model_uri=SSSOM.predicate_id, domain=None, range=Union[str, EntityReference])

slots.predicate_modifier = Slot(uri=SSSOM.predicate_modifier, name="predicate_modifier", curie=SSSOM.curie('predicate_modifier'),
                   model_uri=SSSOM.predicate_modifier, domain=None, range=Optional[Union[str, "PredicateModifierEnum"]])

slots.predicate_label = Slot(uri=SSSOM.predicate_label, name="predicate_label", curie=SSSOM.curie('predicate_label'),
                   model_uri=SSSOM.predicate_label, domain=None, range=Optional[str])

slots.predicate_type = Slot(uri=SSSOM.predicate_type, name="predicate_type", curie=SSSOM.curie('predicate_type'),
                   model_uri=SSSOM.predicate_type, domain=None, range=Optional[Union[str, "EntityTypeEnum"]])

slots.object_id = Slot(uri=OWL.annotatedTarget, name="object_id", curie=OWL.curie('annotatedTarget'),
                   model_uri=SSSOM.object_id, domain=None, range=Optional[Union[str, EntityReference]])

slots.object_label = Slot(uri=SSSOM.object_label, name="object_label", curie=SSSOM.curie('object_label'),
                   model_uri=SSSOM.object_label, domain=None, range=Optional[str])

slots.object_category = Slot(uri=SSSOM.object_category, name="object_category", curie=SSSOM.curie('object_category'),
                   model_uri=SSSOM.object_category, domain=None, range=Optional[str])

slots.mapping_justification = Slot(uri=SSSOM.mapping_justification, name="mapping_justification", curie=SSSOM.curie('mapping_justification'),
                   model_uri=SSSOM.mapping_justification, domain=None, range=Union[str, EntityReference],
                   pattern=re.compile(r'^semapv:(MappingReview|ManualMappingCuration|LogicalReasoning|LexicalMatching|CompositeMatching|UnspecifiedMatching|SemanticSimilarityThresholdMatching|LexicalSimilarityThresholdMatching|MappingChaining)$'))

slots.object_type = Slot(uri=SSSOM.object_type, name="object_type", curie=SSSOM.curie('object_type'),
                   model_uri=SSSOM.object_type, domain=None, range=Optional[Union[str, "EntityTypeEnum"]])

slots.mapping_set_id = Slot(uri=SSSOM.mapping_set_id, name="mapping_set_id", curie=SSSOM.curie('mapping_set_id'),
                   model_uri=SSSOM.mapping_set_id, domain=None, range=Union[str, URI])

slots.mapping_set_version = Slot(uri=OWL.versionInfo, name="mapping_set_version", curie=OWL.curie('versionInfo'),
                   model_uri=SSSOM.mapping_set_version, domain=None, range=Optional[str])

slots.mapping_set_group = Slot(uri=SSSOM.mapping_set_group, name="mapping_set_group", curie=SSSOM.curie('mapping_set_group'),
                   model_uri=SSSOM.mapping_set_group, domain=None, range=Optional[str])

slots.mapping_set_title = Slot(uri=DCTERMS.title, name="mapping_set_title", curie=DCTERMS.curie('title'),
                   model_uri=SSSOM.mapping_set_title, domain=None, range=Optional[str])

slots.mapping_set_description = Slot(uri=DCTERMS.description, name="mapping_set_description", curie=DCTERMS.curie('description'),
                   model_uri=SSSOM.mapping_set_description, domain=None, range=Optional[str])

slots.creator_id = Slot(uri=DCTERMS.creator, name="creator_id", curie=DCTERMS.curie('creator'),
                   model_uri=SSSOM.creator_id, domain=None, range=Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]])

slots.creator_label = Slot(uri=SSSOM.creator_label, name="creator_label", curie=SSSOM.curie('creator_label'),
                   model_uri=SSSOM.creator_label, domain=None, range=Optional[Union[str, List[str]]])

slots.author_id = Slot(uri=PAV.authoredBy, name="author_id", curie=PAV.curie('authoredBy'),
                   model_uri=SSSOM.author_id, domain=None, range=Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]])

slots.author_label = Slot(uri=SSSOM.author_label, name="author_label", curie=SSSOM.curie('author_label'),
                   model_uri=SSSOM.author_label, domain=None, range=Optional[Union[str, List[str]]])

slots.reviewer_id = Slot(uri=SSSOM.reviewer_id, name="reviewer_id", curie=SSSOM.curie('reviewer_id'),
                   model_uri=SSSOM.reviewer_id, domain=None, range=Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]])

slots.reviewer_label = Slot(uri=SSSOM.reviewer_label, name="reviewer_label", curie=SSSOM.curie('reviewer_label'),
                   model_uri=SSSOM.reviewer_label, domain=None, range=Optional[Union[str, List[str]]])

slots.license = Slot(uri=DCTERMS.license, name="license", curie=DCTERMS.curie('license'),
                   model_uri=SSSOM.license, domain=None, range=Optional[Union[str, URI]])

slots.subject_source = Slot(uri=SSSOM.subject_source, name="subject_source", curie=SSSOM.curie('subject_source'),
                   model_uri=SSSOM.subject_source, domain=None, range=Optional[Union[str, EntityReference]])

slots.subject_source_version = Slot(uri=SSSOM.subject_source_version, name="subject_source_version", curie=SSSOM.curie('subject_source_version'),
                   model_uri=SSSOM.subject_source_version, domain=None, range=Optional[str])

slots.object_source = Slot(uri=SSSOM.object_source, name="object_source", curie=SSSOM.curie('object_source'),
                   model_uri=SSSOM.object_source, domain=None, range=Optional[Union[str, EntityReference]])

slots.object_source_version = Slot(uri=SSSOM.object_source_version, name="object_source_version", curie=SSSOM.curie('object_source_version'),
                   model_uri=SSSOM.object_source_version, domain=None, range=Optional[str])

slots.mapping_provider = Slot(uri=SSSOM.mapping_provider, name="mapping_provider", curie=SSSOM.curie('mapping_provider'),
                   model_uri=SSSOM.mapping_provider, domain=None, range=Optional[Union[str, URI]])

slots.mapping_set_source = Slot(uri=PROV.wasDerivedFrom, name="mapping_set_source", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=SSSOM.mapping_set_source, domain=None, range=Optional[Union[Union[str, URI], List[Union[str, URI]]]])

slots.mapping_source = Slot(uri=SSSOM.mapping_source, name="mapping_source", curie=SSSOM.curie('mapping_source'),
                   model_uri=SSSOM.mapping_source, domain=None, range=Optional[Union[str, EntityReference]])

slots.mapping_cardinality = Slot(uri=SSSOM.mapping_cardinality, name="mapping_cardinality", curie=SSSOM.curie('mapping_cardinality'),
                   model_uri=SSSOM.mapping_cardinality, domain=None, range=Optional[Union[str, "MappingCardinalityEnum"]])

slots.mapping_tool = Slot(uri=SSSOM.mapping_tool, name="mapping_tool", curie=SSSOM.curie('mapping_tool'),
                   model_uri=SSSOM.mapping_tool, domain=None, range=Optional[str])

slots.mapping_tool_version = Slot(uri=SSSOM.mapping_tool_version, name="mapping_tool_version", curie=SSSOM.curie('mapping_tool_version'),
                   model_uri=SSSOM.mapping_tool_version, domain=None, range=Optional[str])

slots.mapping_date = Slot(uri=PAV.authoredOn, name="mapping_date", curie=PAV.curie('authoredOn'),
                   model_uri=SSSOM.mapping_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.publication_date = Slot(uri=DCTERMS.created, name="publication_date", curie=DCTERMS.curie('created'),
                   model_uri=SSSOM.publication_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.confidence = Slot(uri=SSSOM.confidence, name="confidence", curie=SSSOM.curie('confidence'),
                   model_uri=SSSOM.confidence, domain=None, range=Optional[float])

slots.subject_match_field = Slot(uri=SSSOM.subject_match_field, name="subject_match_field", curie=SSSOM.curie('subject_match_field'),
                   model_uri=SSSOM.subject_match_field, domain=None, range=Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]])

slots.object_match_field = Slot(uri=SSSOM.object_match_field, name="object_match_field", curie=SSSOM.curie('object_match_field'),
                   model_uri=SSSOM.object_match_field, domain=None, range=Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]])

slots.match_string = Slot(uri=SSSOM.match_string, name="match_string", curie=SSSOM.curie('match_string'),
                   model_uri=SSSOM.match_string, domain=None, range=Optional[Union[str, List[str]]])

slots.subject_preprocessing = Slot(uri=SSSOM.subject_preprocessing, name="subject_preprocessing", curie=SSSOM.curie('subject_preprocessing'),
                   model_uri=SSSOM.subject_preprocessing, domain=None, range=Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]])

slots.object_preprocessing = Slot(uri=SSSOM.object_preprocessing, name="object_preprocessing", curie=SSSOM.curie('object_preprocessing'),
                   model_uri=SSSOM.object_preprocessing, domain=None, range=Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]])

slots.curation_rule = Slot(uri=SSSOM.curation_rule, name="curation_rule", curie=SSSOM.curie('curation_rule'),
                   model_uri=SSSOM.curation_rule, domain=None, range=Optional[Union[Union[str, EntityReference], List[Union[str, EntityReference]]]])

slots.curation_rule_text = Slot(uri=SSSOM.curation_rule_text, name="curation_rule_text", curie=SSSOM.curie('curation_rule_text'),
                   model_uri=SSSOM.curation_rule_text, domain=None, range=Optional[Union[str, List[str]]])

slots.similarity_score = Slot(uri=SSSOM.similarity_score, name="similarity_score", curie=SSSOM.curie('similarity_score'),
                   model_uri=SSSOM.similarity_score, domain=None, range=Optional[float])

slots.similarity_measure = Slot(uri=SSSOM.similarity_measure, name="similarity_measure", curie=SSSOM.curie('similarity_measure'),
                   model_uri=SSSOM.similarity_measure, domain=None, range=Optional[str])

slots.issue_tracker_item = Slot(uri=SSSOM.issue_tracker_item, name="issue_tracker_item", curie=SSSOM.curie('issue_tracker_item'),
                   model_uri=SSSOM.issue_tracker_item, domain=None, range=Optional[Union[str, EntityReference]])

slots.issue_tracker = Slot(uri=SSSOM.issue_tracker, name="issue_tracker", curie=SSSOM.curie('issue_tracker'),
                   model_uri=SSSOM.issue_tracker, domain=None, range=Optional[Union[str, URI]])

slots.see_also = Slot(uri=RDFS.seeAlso, name="see_also", curie=RDFS.curie('seeAlso'),
                   model_uri=SSSOM.see_also, domain=None, range=Optional[Union[str, List[str]]])

slots.other = Slot(uri=SSSOM.other, name="other", curie=SSSOM.curie('other'),
                   model_uri=SSSOM.other, domain=None, range=Optional[str])

slots.comment = Slot(uri=RDFS.comment, name="comment", curie=RDFS.curie('comment'),
                   model_uri=SSSOM.comment, domain=None, range=Optional[str])

slots.extension_definitions = Slot(uri=SSSOM.extension_definitions, name="extension_definitions", curie=SSSOM.curie('extension_definitions'),
                   model_uri=SSSOM.extension_definitions, domain=None, range=Optional[Union[Union[dict, ExtensionDefinition], List[Union[dict, ExtensionDefinition]]]])

slots.extensionDefinition__slot_name = Slot(uri=SSSOM.slot_name, name="extensionDefinition__slot_name", curie=SSSOM.curie('slot_name'),
                   model_uri=SSSOM.extensionDefinition__slot_name, domain=None, range=Union[str, NCName])

slots.extensionDefinition__property = Slot(uri=SSSOM.property, name="extensionDefinition__property", curie=SSSOM.curie('property'),
                   model_uri=SSSOM.extensionDefinition__property, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.extensionDefinition__type_hint = Slot(uri=SSSOM.type_hint, name="extensionDefinition__type_hint", curie=SSSOM.curie('type_hint'),
                   model_uri=SSSOM.extensionDefinition__type_hint, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.propagatable__propagated = Slot(uri=SSSOM.propagated, name="propagatable__propagated", curie=SSSOM.curie('propagated'),
                   model_uri=SSSOM.propagatable__propagated, domain=None, range=Optional[Union[bool, Bool]])

slots.mapping_set_license = Slot(uri=DCTERMS.license, name="mapping set_license", curie=DCTERMS.curie('license'),
                   model_uri=SSSOM.mapping_set_license, domain=MappingSet, range=Union[str, URI])