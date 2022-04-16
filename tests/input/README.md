# Tests input directory
This file contains samples of your schema. Samples can written in yaml, json, rdf or any other language that 
the [https://linkml.github.io/linkml-runtime]() importers and exporters support.

`test_examples.py` will iterate over this directory, loading each test and:
1) For each runtime generator (yaml, json, rdf, ...) will emit the output in that language
2) Will compare the output to its expected value in the `output` directory and will alert you if something
has changed
3) If something HAS changed, will update the output accordingly.

[ ] Add a manifest setup https://linkml.github.io/linkml-template-config-model, so we can specify whether
we expect the tests to pass or fail and, if they fail, why.
