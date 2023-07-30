# Simple Standard for Sharing Ontological Mappings (SSSOM)

## How to make a new release
* Automated:
  * On the main code page, click on Releases (right hand column)
  * Click on the `Draft a new release` button
  * Click the `Choose a tag` button, create a new tag: `X.X.X`
  * Click on the `Generate a new release` button
  * Make sure only the `Select as the latest release` checkbox is checked.
  * Click `Publish release` button
* Manual:
  * `make build`
  * `make pypi`

This triggers a GitHub Action workflow that releases the new version of SSSOM to PyPi.

## Documentation deployment
This can be done in two ways:
* Automated: Every time a pull request is merged into the `main` branch, a github action is triggered to deploy documentation automatically.
* Manually: The make command to deploy documentation is `make deploy`.