# Auto generated from sssom.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-09-27 20:38
# Schema: sssom
#
# id: http://w3id.org/sssom/schema/
# description: Datamodel for Simple Standard for Sharing Ontology Mappings (SSSOM)
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Date, Double, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ORPHANET = CurieNamespace('Orphanet', 'http://www.orpha.net/ORDO/Orphanet_')
DC = CurieNamespace('dc', 'http://purl.org/dc/terms/')
DCE = CurieNamespace('dce', 'http://purl.org/dc/elements/1.1/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NEURONAME = CurieNamespace('neuroname', 'http://braininfo.rprc.washington.edu/centraldirectory.aspx?ID=')
OBOINOWL = CurieNamespace('oboInOwl', 'http://www.geneontology.org/formats/oboInOwl#')
OIO = CurieNamespace('oio', 'http://www.geneontology.org/formats/oboInOwl#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SSSOM = CurieNamespace('sssom', 'http://w3id.org/sssom/')
DEFAULT_ = SSSOM


# Types

# Class references



@dataclass
class MappingSet(YAMLRoot):
    """
    Represents a set of mappings
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SSSOM.MappingSet
    class_class_curie: ClassVar[str] = "sssom:MappingSet"
    class_name: ClassVar[str] = "mapping set"
    class_model_uri: ClassVar[URIRef] = SSSOM.MappingSet

    mapping_set_id: Union[str, URIorCURIE] = None
    license: Union[str, URIorCURIE] = None
    mappings: Optional[Union[Union[dict, "Mapping"], List[Union[dict, "Mapping"]]]] = empty_list()
    mapping_set_version: Optional[str] = None
    mapping_set_source: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    mapping_set_description: Optional[str] = None
    creator_id: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    creator_label: Optional[Union[str, List[str]]] = empty_list()
    subject_source: Optional[Union[str, URIorCURIE]] = None
    subject_source_version: Optional[Union[str, URIorCURIE]] = None
    object_source: Optional[Union[str, URIorCURIE]] = None
    object_source_version: Optional[str] = None
    mapping_provider: Optional[Union[str, URIorCURIE]] = None
    mapping_tool: Optional[str] = None
    mapping_date: Optional[Union[str, XSDDate]] = None
    subject_match_field: Optional[Union[Union[str, "MatchFieldEnum"], List[Union[str, "MatchFieldEnum"]]]] = empty_list()
    object_match_field: Optional[Union[Union[str, "MatchFieldEnum"], List[Union[str, "MatchFieldEnum"]]]] = empty_list()
    subject_preprocessing: Optional[Union[Union[str, "PreprocessingMethodEnum"], List[Union[str, "PreprocessingMethodEnum"]]]] = empty_list()
    object_preprocessing: Optional[Union[Union[str, "PreprocessingMethodEnum"], List[Union[str, "PreprocessingMethodEnum"]]]] = empty_list()
    match_term_type: Optional[Union[str, "MatchTermTypeEnum"]] = None
    see_also: Optional[Union[str, List[str]]] = empty_list()
    other: Optional[str] = None
    comment: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.mapping_set_id):
            self.MissingRequiredField("mapping_set_id")
        if not isinstance(self.mapping_set_id, URIorCURIE):
            self.mapping_set_id = URIorCURIE(self.mapping_set_id)

        if self._is_empty(self.license):
            self.MissingRequiredField("license")
        if not isinstance(self.license, URIorCURIE):
            self.license = URIorCURIE(self.license)

        self._normalize_inlined_as_dict(slot_name="mappings", slot_type=Mapping, key_name="subject_id", keyed=False)

        if self.mapping_set_version is not None and not isinstance(self.mapping_set_version, str):
            self.mapping_set_version = str(self.mapping_set_version)

        if not isinstance(self.mapping_set_source, list):
            self.mapping_set_source = [self.mapping_set_source] if self.mapping_set_source is not None else []
        self.mapping_set_source = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.mapping_set_source]

        if self.mapping_set_description is not None and not isinstance(self.mapping_set_description, str):
            self.mapping_set_description = str(self.mapping_set_description)

        if not isinstance(self.creator_id, list):
            self.creator_id = [self.creator_id] if self.creator_id is not None else []
        self.creator_id = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.creator_id]

        if not isinstance(self.creator_label, list):
            self.creator_label = [self.creator_label] if self.creator_label is not None else []
        self.creator_label = [v if isinstance(v, str) else str(v) for v in self.creator_label]

        if self.subject_source is not None and not isinstance(self.subject_source, URIorCURIE):
            self.subject_source = URIorCURIE(self.subject_source)

        if self.subject_source_version is not None and not isinstance(self.subject_source_version, URIorCURIE):
            self.subject_source_version = URIorCURIE(self.subject_source_version)

        if self.object_source is not None and not isinstance(self.object_source, URIorCURIE):
            self.object_source = URIorCURIE(self.object_source)

        if self.object_source_version is not None and not isinstance(self.object_source_version, str):
            self.object_source_version = str(self.object_source_version)

        if self.mapping_provider is not None and not isinstance(self.mapping_provider, URIorCURIE):
            self.mapping_provider = URIorCURIE(self.mapping_provider)

        if self.mapping_tool is not None and not isinstance(self.mapping_tool, str):
            self.mapping_tool = str(self.mapping_tool)

        if self.mapping_date is not None and not isinstance(self.mapping_date, XSDDate):
            self.mapping_date = XSDDate(self.mapping_date)

        if not isinstance(self.subject_match_field, list):
            self.subject_match_field = [self.subject_match_field] if self.subject_match_field is not None else []
        self.subject_match_field = [v if isinstance(v, MatchFieldEnum) else MatchFieldEnum(v) for v in self.subject_match_field]

        if not isinstance(self.object_match_field, list):
            self.object_match_field = [self.object_match_field] if self.object_match_field is not None else []
        self.object_match_field = [v if isinstance(v, MatchFieldEnum) else MatchFieldEnum(v) for v in self.object_match_field]

        if not isinstance(self.subject_preprocessing, list):
            self.subject_preprocessing = [self.subject_preprocessing] if self.subject_preprocessing is not None else []
        self.subject_preprocessing = [v if isinstance(v, PreprocessingMethodEnum) else PreprocessingMethodEnum(v) for v in self.subject_preprocessing]

        if not isinstance(self.object_preprocessing, list):
            self.object_preprocessing = [self.object_preprocessing] if self.object_preprocessing is not None else []
        self.object_preprocessing = [v if isinstance(v, PreprocessingMethodEnum) else PreprocessingMethodEnum(v) for v in self.object_preprocessing]

        if self.match_term_type is not None and not isinstance(self.match_term_type, MatchTermTypeEnum):
            self.match_term_type = MatchTermTypeEnum(self.match_term_type)

        if not isinstance(self.see_also, list):
            self.see_also = [self.see_also] if self.see_also is not None else []
        self.see_also = [v if isinstance(v, str) else str(v) for v in self.see_also]

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        super().__post_init__(**kwargs)


@dataclass
class Mapping(YAMLRoot):
    """
    Represents an individual mapping between a pair of entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Axiom
    class_class_curie: ClassVar[str] = "owl:Axiom"
    class_name: ClassVar[str] = "mapping"
    class_model_uri: ClassVar[URIRef] = SSSOM.Mapping

    subject_id: Union[str, URIorCURIE] = None
    predicate_id: Union[str, URIorCURIE] = None
    object_id: Union[str, URIorCURIE] = None
    match_type: Union[Union[str, "MatchTypeEnum"], List[Union[str, "MatchTypeEnum"]]] = None
    subject_label: Optional[str] = None
    subject_category: Optional[str] = None
    predicate_label: Optional[str] = None
    object_label: Optional[str] = None
    object_category: Optional[str] = None
    author_id: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    author_label: Optional[Union[str, List[str]]] = empty_list()
    reviewer_id: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    reviewer_label: Optional[Union[str, List[str]]] = empty_list()
    creator_id: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    creator_label: Optional[Union[str, List[str]]] = empty_list()
    license: Optional[Union[str, URIorCURIE]] = None
    subject_source: Optional[Union[str, URIorCURIE]] = None
    subject_source_version: Optional[Union[str, URIorCURIE]] = None
    object_source: Optional[Union[str, URIorCURIE]] = None
    object_source_version: Optional[str] = None
    mapping_provider: Optional[Union[str, URIorCURIE]] = None
    mapping_cardinality: Optional[Union[str, "MappingCardinalityEnum"]] = None
    mapping_tool: Optional[str] = None
    mapping_tool_version: Optional[str] = None
    mapping_date: Optional[Union[str, XSDDate]] = None
    confidence: Optional[float] = None
    subject_match_field: Optional[Union[Union[str, "MatchFieldEnum"], List[Union[str, "MatchFieldEnum"]]]] = empty_list()
    object_match_field: Optional[Union[Union[str, "MatchFieldEnum"], List[Union[str, "MatchFieldEnum"]]]] = empty_list()
    match_string: Optional[Union[str, List[str]]] = empty_list()
    subject_preprocessing: Optional[Union[Union[str, "PreprocessingMethodEnum"], List[Union[str, "PreprocessingMethodEnum"]]]] = empty_list()
    object_preprocessing: Optional[Union[Union[str, "PreprocessingMethodEnum"], List[Union[str, "PreprocessingMethodEnum"]]]] = empty_list()
    match_term_type: Optional[Union[str, "MatchTermTypeEnum"]] = None
    semantic_similarity_score: Optional[float] = None
    semantic_similarity_measure: Optional[Union[str, URIorCURIE]] = None
    see_also: Optional[Union[str, List[str]]] = empty_list()
    other: Optional[str] = None
    comment: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject_id):
            self.MissingRequiredField("subject_id")
        if not isinstance(self.subject_id, URIorCURIE):
            self.subject_id = URIorCURIE(self.subject_id)

        if self._is_empty(self.predicate_id):
            self.MissingRequiredField("predicate_id")
        if not isinstance(self.predicate_id, URIorCURIE):
            self.predicate_id = URIorCURIE(self.predicate_id)

        if self._is_empty(self.object_id):
            self.MissingRequiredField("object_id")
        if not isinstance(self.object_id, URIorCURIE):
            self.object_id = URIorCURIE(self.object_id)

        if self._is_empty(self.match_type):
            self.MissingRequiredField("match_type")
        if not isinstance(self.match_type, list):
            self.match_type = [self.match_type] if self.match_type is not None else []
        self.match_type = [v if isinstance(v, MatchTypeEnum) else MatchTypeEnum(v) for v in self.match_type]

        if self.subject_label is not None and not isinstance(self.subject_label, str):
            self.subject_label = str(self.subject_label)

        if self.subject_category is not None and not isinstance(self.subject_category, str):
            self.subject_category = str(self.subject_category)

        if self.predicate_label is not None and not isinstance(self.predicate_label, str):
            self.predicate_label = str(self.predicate_label)

        if self.object_label is not None and not isinstance(self.object_label, str):
            self.object_label = str(self.object_label)

        if self.object_category is not None and not isinstance(self.object_category, str):
            self.object_category = str(self.object_category)

        if not isinstance(self.author_id, list):
            self.author_id = [self.author_id] if self.author_id is not None else []
        self.author_id = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.author_id]

        if not isinstance(self.author_label, list):
            self.author_label = [self.author_label] if self.author_label is not None else []
        self.author_label = [v if isinstance(v, str) else str(v) for v in self.author_label]

        if not isinstance(self.reviewer_id, list):
            self.reviewer_id = [self.reviewer_id] if self.reviewer_id is not None else []
        self.reviewer_id = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.reviewer_id]

        if not isinstance(self.reviewer_label, list):
            self.reviewer_label = [self.reviewer_label] if self.reviewer_label is not None else []
        self.reviewer_label = [v if isinstance(v, str) else str(v) for v in self.reviewer_label]

        if not isinstance(self.creator_id, list):
            self.creator_id = [self.creator_id] if self.creator_id is not None else []
        self.creator_id = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.creator_id]

        if not isinstance(self.creator_label, list):
            self.creator_label = [self.creator_label] if self.creator_label is not None else []
        self.creator_label = [v if isinstance(v, str) else str(v) for v in self.creator_label]

        if self.license is not None and not isinstance(self.license, URIorCURIE):
            self.license = URIorCURIE(self.license)

        if self.subject_source is not None and not isinstance(self.subject_source, URIorCURIE):
            self.subject_source = URIorCURIE(self.subject_source)

        if self.subject_source_version is not None and not isinstance(self.subject_source_version, URIorCURIE):
            self.subject_source_version = URIorCURIE(self.subject_source_version)

        if self.object_source is not None and not isinstance(self.object_source, URIorCURIE):
            self.object_source = URIorCURIE(self.object_source)

        if self.object_source_version is not None and not isinstance(self.object_source_version, str):
            self.object_source_version = str(self.object_source_version)

        if self.mapping_provider is not None and not isinstance(self.mapping_provider, URIorCURIE):
            self.mapping_provider = URIorCURIE(self.mapping_provider)

        if self.mapping_cardinality is not None and not isinstance(self.mapping_cardinality, MappingCardinalityEnum):
            self.mapping_cardinality = MappingCardinalityEnum(self.mapping_cardinality)

        if self.mapping_tool is not None and not isinstance(self.mapping_tool, str):
            self.mapping_tool = str(self.mapping_tool)

        if self.mapping_tool_version is not None and not isinstance(self.mapping_tool_version, str):
            self.mapping_tool_version = str(self.mapping_tool_version)

        if self.mapping_date is not None and not isinstance(self.mapping_date, XSDDate):
            self.mapping_date = XSDDate(self.mapping_date)

        if self.confidence is not None and not isinstance(self.confidence, float):
            self.confidence = float(self.confidence)

        if not isinstance(self.subject_match_field, list):
            self.subject_match_field = [self.subject_match_field] if self.subject_match_field is not None else []
        self.subject_match_field = [v if isinstance(v, MatchFieldEnum) else MatchFieldEnum(v) for v in self.subject_match_field]

        if not isinstance(self.object_match_field, list):
            self.object_match_field = [self.object_match_field] if self.object_match_field is not None else []
        self.object_match_field = [v if isinstance(v, MatchFieldEnum) else MatchFieldEnum(v) for v in self.object_match_field]

        if not isinstance(self.match_string, list):
            self.match_string = [self.match_string] if self.match_string is not None else []
        self.match_string = [v if isinstance(v, str) else str(v) for v in self.match_string]

        if not isinstance(self.subject_preprocessing, list):
            self.subject_preprocessing = [self.subject_preprocessing] if self.subject_preprocessing is not None else []
        self.subject_preprocessing = [v if isinstance(v, PreprocessingMethodEnum) else PreprocessingMethodEnum(v) for v in self.subject_preprocessing]

        if not isinstance(self.object_preprocessing, list):
            self.object_preprocessing = [self.object_preprocessing] if self.object_preprocessing is not None else []
        self.object_preprocessing = [v if isinstance(v, PreprocessingMethodEnum) else PreprocessingMethodEnum(v) for v in self.object_preprocessing]

        if self.match_term_type is not None and not isinstance(self.match_term_type, MatchTermTypeEnum):
            self.match_term_type = MatchTermTypeEnum(self.match_term_type)

        if self.semantic_similarity_score is not None and not isinstance(self.semantic_similarity_score, float):
            self.semantic_similarity_score = float(self.semantic_similarity_score)

        if self.semantic_similarity_measure is not None and not isinstance(self.semantic_similarity_measure, URIorCURIE):
            self.semantic_similarity_measure = URIorCURIE(self.semantic_similarity_measure)

        if not isinstance(self.see_also, list):
            self.see_also = [self.see_also] if self.see_also is not None else []
        self.see_also = [v if isinstance(v, str) else str(v) for v in self.see_also]

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        super().__post_init__(**kwargs)


# Enumerations
class MappingCardinalityEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MappingCardinalityEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1:1",
                PermissibleValue(text="1:1",
                                 description="One-to-one mapping") )
        setattr(cls, "1:n",
                PermissibleValue(text="1:n",
                                 description="One-to-many mapping") )
        setattr(cls, "n:1",
                PermissibleValue(text="n:1",
                                 description="Many-to-one mapping") )
        setattr(cls, "1:0",
                PermissibleValue(text="1:0",
                                 description="One-to-none mapping") )
        setattr(cls, "0:1",
                PermissibleValue(text="0:1",
                                 description="None-to-one mapping") )
        setattr(cls, "n:n",
                PermissibleValue(text="n:n",
                                 description="Many-to-many mapping") )

class MatchTypeEnum(EnumDefinitionImpl):

    Lexical = PermissibleValue(text="Lexical",
                                     description="Lexical match")
    Logical = PermissibleValue(text="Logical",
                                     description="Logical match")
    HumanCurated = PermissibleValue(text="HumanCurated",
                                               description="Match based on human expert opinion")
    Complex = PermissibleValue(text="Complex",
                                     description="Match based on a variety of different strategies")
    Unspecified = PermissibleValue(text="Unspecified",
                                             description="Unknown match type")
    SemanticSimilarity = PermissibleValue(text="SemanticSimilarity",
                                                           description="Match based on close semantic similarity")

    _defn = EnumDefinition(
        name="MatchTypeEnum",
    )

class MatchTermTypeEnum(EnumDefinitionImpl):

    TermMatch = PermissibleValue(text="TermMatch",
                                         description="A match between two terms")
    ConceptMatch = PermissibleValue(text="ConceptMatch",
                                               description="A match between two SKOS concepts")
    ClassMatch = PermissibleValue(text="ClassMatch",
                                           description="A match between two OWL/RDFS classes")
    ObjectPropertyMatch = PermissibleValue(text="ObjectPropertyMatch",
                                                             description="A match between two OWL object properties")
    IndividualMatch = PermissibleValue(text="IndividualMatch",
                                                     description="A match between two OWL Individuals")
    DataPropertyMatch = PermissibleValue(text="DataPropertyMatch",
                                                         description="A match between two OWL object properties")

    _defn = EnumDefinition(
        name="MatchTermTypeEnum",
    )

class PreprocessingMethodEnum(EnumDefinitionImpl):

    Stemming = PermissibleValue(text="Stemming")
    TaxonRestrictionRemoval = PermissibleValue(text="TaxonRestrictionRemoval")

    _defn = EnumDefinition(
        name="PreprocessingMethodEnum",
    )

class MatchFieldEnum(EnumDefinitionImpl):

    ExactSynonym = PermissibleValue(text="ExactSynonym")
    Label = PermissibleValue(text="Label")
    RelatedSynonym = PermissibleValue(text="RelatedSynonym")
    CloseSyonym = PermissibleValue(text="CloseSyonym")
    BroadSynonym = PermissibleValue(text="BroadSynonym")
    NarrowSynonm = PermissibleValue(text="NarrowSynonm")
    Definition = PermissibleValue(text="Definition")

    _defn = EnumDefinition(
        name="MatchFieldEnum",
    )

# Slots

