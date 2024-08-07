## Getting started

- First, create a virtual environment of your choice (anaconda, venv, pyenv, poetry etc.). If you need assistance with virtual environments, [here's a guide](https://berkeleybop.github.io/best_practice/python_environments) to help you setup pyenv and use poetry with it.
- Install the [cruft](https://github.com/cruft/cruft) package. Cruft enables keeping projects up-to-date with future updates made to this original template.

    ```
    pip install cruft
    ```
    
- Create a project using the [mapping-commons-cookiecutter](https://github.com/mapping-commons/mapping-commons-cookiecutter) template.

    ```
    cruft create https://github.com/mapping-commons/mapping-commons-cookiecutter
    ```

This kickstarts an interactive session where you declare the following:

- `project_name`: Name of the project. [defaults to: my-commons-name]
- `github_org`: Name of the github org the project belongs to. [defaults to: my-org]
- `project_description`: Description of the project [defaults to: 'This is the project description.']
- `full_name`: Name of the author [defaults to: 'My Name']
- `email`: Author's email [defaults to: 'my-name@my-org.org']
- `yo`: Choose from [1]: Yes, [2]: No [**TEST OPTION FOR NOW**]
- `license`: Choose from [1]: Yes, [2]: No [**TEST OPTION FOR NOW**]

## What does this do?

The following files and directories are autogenerated in the project:

### TODO

## Version control
### GitHub

1. Go to [https://github.com/new] and follow the instructions, being sure to
   NOT add a README or .gitignore file (this cookiecutter template will take
   care of this for you)

2. Add the remote to your local git repository

   ```bash
   git remote add origin https://github.com/my-user-or-organization/my-commons-name.git
   git branch -M main
   git push -u origin main
   ```

### GitLab

#### TODO

## Future updates to the project's boilerplate code

In order to be up-to-date with the template, first check if there is a mismatch between the project's boilerplate code and the template by running:

```
cruft check
```

This indicates if there is a difference between the current project's boilerplate code and the latest version of the project template. If the project is up-to-date with the template:

```
SUCCESS: Good work! Project's cruft is up to date and as clean as possible :).
```

Otherwise, it will indicate that the project's boilerplate code is not up-to-date by the following:

```
FAILURE: Project's cruft is out of date! Run `cruft update` to clean this mess up.
```


For viewing the difference, run `cruft diff`. This shows the difference between the project's boilerplate code and the template's latest version.

After running `cruft update`, the project's boilerplate code will be updated to the latest version of the template.
