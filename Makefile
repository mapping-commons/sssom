all: ssom.owl

ssom.owl: sssom_vocab.owl sssom_metadata.owl
	robot merge -i sssom_vocab.owl -i sssom_metadata.owl \
	annotate --ontology-iri "http://purl.org/sssom/sssom.owl" -o $@

sssom_%.owl: sssom_%.tsv
	robot template --template $< \
  --prefix "SSSOM: http://purl.org/sssom/" \
	--prefix "sssom: http://purl.org/sssom/meta/" \
  --output $@
