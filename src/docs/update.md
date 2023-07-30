## Final process

1. Finish your edits and merge them into master
2. Rebuild the LinkML model using the [“build” action](https://github.com/mapping-commons/sssom/blob/master/.github/workflows/build.yml)
3. Create a [GitHub release](https://github.com/mapping-commons/sssom/releases)
    - This will automatically trigger a PyPI release using [this action](https://github.com/mapping-commons/sssom/blob/master/.github/workflows/pypi-publish.yaml), of the sssom_schema module
    - The context file is packaged and delivered to projects that depend on `sssom-schema`.
4. Updating sssom-py
    1. After the pypi release is completed,  update sssom-schema dependency using `poetry update sssom-schema`.  The new context is available and accessible via `pkg_resources`.
    1. Release `sssom-py` using the same method as `sssom-schema` above.