
# Class: mapping set reference


A reference to a mapping set. It allows to augment mapping set metadata from the perspective of the registry, for example, providing confidence, or a local filename or a grouping.

URI: [sssom:MappingSetReference](https://w3id.org/sssom/MappingSetReference)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MappingRegistry]++-%20mapping_set_references%200..*>[MappingSetReference&#124;mapping_set_id:uri;mirror_from:uri%20%3F;registry_confidence:double%20%3F;mapping_set_group:string%20%3F;last_updated:date%20%3F;local_name:string%20%3F],[MappingRegistry])](https://yuml.me/diagram/nofunky;dir:TB/class/[MappingRegistry]++-%20mapping_set_references%200..*>[MappingSetReference&#124;mapping_set_id:uri;mirror_from:uri%20%3F;registry_confidence:double%20%3F;mapping_set_group:string%20%3F;last_updated:date%20%3F;local_name:string%20%3F],[MappingRegistry])

## Referenced by Class

 *  **None** *[mapping_set_references](mapping_set_references.md)*  <sub>0..\*</sub>  **[MappingSetReference](MappingSetReference.md)**

## Attributes


### Own

 * [mapping_set_id](mapping_set_id.md)  <sub>1..1</sub>
     * Description: A globally unique identifier for the mapping set (not each individual mapping). Should be IRI, ideally resolvable.
     * Range: [Uri](types/Uri.md)
     * Example: http://purl.obolibrary.org/obo/mondo/mappings/mondo_exactmatch_ncit.sssom.tsv (A persistent URI pointing to the latest version of the Mondo - NCIT mapping in the Mondo namespace.)
 * [mirror_from](mirror_from.md)  <sub>0..1</sub>
     * Description: A URL location from which to obtain a resource, such as a mapping set.
     * Range: [Uri](types/Uri.md)
 * [registry_confidence](registry_confidence.md)  <sub>0..1</sub>
     * Description: This value is set by the registry that indexes the mapping set. It reflects the confidence the registry has in the correctness of the mappings in the mapping set.
     * Range: [Double](types/Double.md)
 * [mapping_set_group](mapping_set_group.md)  <sub>0..1</sub>
     * Description: Set by the owners of the mapping registry. A way to group .
     * Range: [String](types/String.md)
 * [last_updated](last_updated.md)  <sub>0..1</sub>
     * Description: The date this reference was last updated.
     * Range: [Date](types/Date.md)
 * [local_name](local_name.md)  <sub>0..1</sub>
     * Description: The local name assigned to file that corresponds to the downloaded mapping set.
     * Range: [String](types/String.md)
