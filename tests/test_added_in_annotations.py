import unittest
from jsonasobj2 import as_dict

from linkml_runtime.utils.schemaview import SchemaView, load_schema_wrap

CURRENT_VERSION = "1.1"


class TestAddedInAnnotationTestCase(unittest.TestCase):
    """Checks that all newly added slots are annotated as such."""

    def test_new_slots(self):
        # For all the classes we care about, we list the pre-existing
        # slots in the last version before the current one.
        # That list should be updated after every release corresponding
        # to a new version of the spec (e.g. after the 1.1 release, add
        # all the 1.1 slots).
        baseslots = {
            "mapping set": [
                "curie_map",
                "mappings",
                "mapping_set_id",
                "mapping_set_version",
                "mapping_set_source",
                "mapping_set_title",
                "mapping_set_description",
                "creator_id",
                "creator_label",
                "license",
                "subject_type",
                "subject_source",
                "subject_source_version",
                "object_type",
                "object_source",
                "object_source_version",
                "mapping_provider",
                "mapping_tool",
                "mapping_tool_version",
                "mapping_date",
                "publication_date",
                "subject_match_field",
                "object_match_field",
                "subject_preprocessing",
                "object_preprocessing",
                "see_also",
                "issue_tracker",
                "other",
                "comment",
                "extension_definitions",
            ],
            "mapping": [
                "subject_id",
                "subject_label",
                "subject_category",
                "predicate_id",
                "predicate_label",
                "predicate_modifier",
                "object_id",
                "object_label",
                "object_category",
                "mapping_justification",
                "author_id",
                "author_label",
                "reviewer_id",
                "reviewer_label",
                "creator_id",
                "creator_label",
                "license",
                "subject_type",
                "subject_source",
                "subject_source_version",
                "object_type",
                "object_source",
                "object_source_version",
                "mapping_provider",
                "mapping_source",
                "mapping_cardinality",
                "mapping_tool",
                "mapping_tool_version",
                "mapping_date",
                "publication_date",
                "confidence",
                "curation_rule",
                "curation_rule_text",
                "subject_match_field",
                "object_match_field",
                "match_string",
                "subject_preprocessing",
                "object_preprocessing",
                "similarity_score",
                "similarity_measure",
                "see_also",
                "issue_tracker_item",
                "other",
                "comment",
            ],
        }
        unannotated = []
        annotated_with_wrong_version = []

        sv = SchemaView(load_schema_wrap("src/sssom_schema/schema/sssom_schema.yaml"))
        for class_name, class_view in sv.all_classes().items():
            baseslots_for_class = baseslots.get(class_name)
            if baseslots_for_class is None:
                continue

            for slot_name in class_view.slots:
                if slot_name in baseslots_for_class:
                    # This is a pre-existing slot, move along
                    continue

                # New slot, check for added_in annotation
                slot_view = sv.induced_slot(slot_name, class_name)
                added_in = as_dict(slot_view.annotations).get("added_in", None)
                if added_in is None:
                    unannotated.append(
                        f"Slot {slot_name} in class {class_name} is not annotated"
                    )
                else:
                    version = added_in.get("value")
                    if version != CURRENT_VERSION:
                        annotated_with_wrong_version.append(
                            f"Slot {slot_name} in class {class_name} is annotated with a wrong version ({version})"
                        )

        self.assertListEqual([], unannotated)
        self.assertListEqual([], annotated_with_wrong_version)


if __name__ == "__main__":
    unittest.main()
