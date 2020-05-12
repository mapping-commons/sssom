all: sssom_vocab.owl

sssom_vocab.owl: sssom_vocab.tsv
	robot template --template $< \
  --prefix "SSSOM: http://purl.org/sssom/" \
  --ontology-iri "http://purl.org/sssom/sssom.owl" \
  --output $@