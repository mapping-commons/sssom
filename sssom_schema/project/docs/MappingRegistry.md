
# Class: mapping registry


A registry for managing mapping sets. It holds a set of mapping set references, and can import other registries.

URI: [sssom:MappingRegistry](https://w3id.org/sssom/MappingRegistry)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MappingSetReference],[MappingSetReference]<mapping_set_references%200..*-++[MappingRegistry&#124;mapping_registry_id:EntityReference;imports:uri%20*;documentation:uri%20%3F;homepage:uri%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[MappingSetReference],[MappingSetReference]<mapping_set_references%200..*-++[MappingRegistry&#124;mapping_registry_id:EntityReference;imports:uri%20*;documentation:uri%20%3F;homepage:uri%20%3F])

## Attributes


### Own

 * [mapping_registry_id](mapping_registry_id.md)  <sub>1..1</sub>
     * Description: The unique identifier of a mapping registry.
     * Range: [EntityReference](types/EntityReference.md)
 * [imports](imports.md)  <sub>0..\*</sub>
     * Description: A list of registries that should be imported into this one.
     * Range: [Uri](types/Uri.md)
 * [mapping_set_references](mapping_set_references.md)  <sub>0..\*</sub>
     * Description: A list of mapping set references.
     * Range: [MappingSetReference](MappingSetReference.md)
 * [documentation](documentation.md)  <sub>0..1</sub>
     * Description: A URL to the documentation of this mapping commons.
     * Range: [Uri](types/Uri.md)
 * [homepage](homepage.md)  <sub>0..1</sub>
     * Description: A URL to a homepage of this mapping commons.
     * Range: [Uri](types/Uri.md)
