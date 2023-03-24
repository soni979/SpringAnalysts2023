<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/AMEND-Consulting-LLC/github-general-template">
    <img src="ref/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Github General Template</h3>

  <p align="center">
    This is a template containing scripts and documentation setup to quickly start a Python project.
    <br />
    <a href="https://github.com/AMEND-Consulting-LLC/github-general-template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/AMEND-Consulting-LLC/github-general-template">View Demo</a>
    ·
    <a href="https://github.com/AMEND-Consulting-LLC/github-general-template/issues">Report Bug</a>
    ·
    <a href="https://github.com/AMEND-Consulting-LLC/github-general-template/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#configuration">Configuration</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The template contains scripts showcasing usage of a YAML configuration file and resources for project folder setup, a default git ignore file, data import and export functions, comment structures, and project auto documentation scripts.

To use this template's readme generation script, make sure to follow default comment structures and update files in the `ref` folder including _logo.png_, _input.csv_, _readme_config.yaml_ and _sample.md_ files. Please note that that _sample.md_ file contains variables that will be filled in by the _input.csv_ file. After these files are altered and the scripts are annotated correctly, the `scripts/create_readme.py` can be run to automatically generate README.md files. For more information, view the [Usage Instructions](#usage).

This template is updated according to feedback, if there are any desired changes or ideas please submit them through <a href="https://github.com/AMEND-Consulting-LLC/github-general-template/issues">this page</a>.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [YAML](https://yaml.org/)
* [Oracle](https://www.oracle.com/)
* [ODBC](https://learn.microsoft.com/en-us/sql/odbc/microsoft-open-database-connectivity-odbc)
* [Pickle](https://docs.python.org/3/library/pickle.html)
* [Excel](https://www.microsoft.com/en-us/microsoft-365/excel)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To start modifying this script you will need to get a local copy up and running. Follow these steps to get this onto your machine. If running within template make sure to set the `scripts/create_readme.py` script's test variable to True before running, if run in current state it will overwrite this document with the `sample.md` script. For more information, view the [Usage Instructions](#usage).

### Prerequisites

Follow steps through these links to install [Python](https://www.python.org/downloads/), [Pip](https://pip.pypa.io/en/stable/installation/), and [Github](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). If changes to code are necessary, you will need to install an IDE such as [Visual Studio Code](https://code.visualstudio.com/download) or [Spyder](https://docs.spyder-ide.org/current/installation.html).

### Installation

1. Clone this repo using Git
   ```sh
   git clone gh repo clone AMEND-Consulting-LLC/github-general-template
   ```
2. Install required packages using pip
   ```sh
   pip install -r requirements.txt
   ```
3. Enter your values in `config.yaml`, see below for more information on [config setup](#configuration).
4. Run the keyring commands to input credentials used in the script
    ```sh
    python keyring.set_password("system","username","password")
    ```
5. Execute the `script/test_script.py` file
    ```sh
    python script/test_script.py
    ```
 6. Read the output from the file created

<p align="right">(<a href="#top">back to top</a>)</p>

### Configuration

If your codebase uses the `config.yaml` file you can use the file to create global variables your script can access. This allows for easy manipulation of script for handling problems like multiple access tokens, changing values, filepaths, etc. Multiple YAML files can be used, this project is just setup for a quick simple `config.yaml` file use.

Example of `config.yaml` below:
```yaml
example-parameter: true
example-list:
  item-1: 1
  item-2: "two"
  item-3: 'image/url.com'
example-empty:
  ```

The `scripts/create_readme.py` script uses a separate configuration yaml file that can be found in `ref/readme_config.yaml`. See below for an example of what the variables currently look like:
```yaml
# List of scripts used in the project
scripts:
  - "./script/test_script.py"
  - "./script/data_input.py" 
  - "./script/data_output.py"

# Output for the script annotation (make sure it's a .md file)
output: "./script/README.md"

# Setting scripts to run
run_script: False # Set to True if running script documentation
run_project: True # Set to True if running project documentation

test: False # Set to True if running in github-general-template
  ```

  <p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

The scripts found in this template can be used to quickly load in data from select resources and upload data. It also contains code to automatically create documentation and update it.

### Starting Out
This template can be used for quick project setup,
1) Navigate to [AMEND's main project page](https://github.com/AMEND-Consulting-LLC) and click the green 'New' button.
2) On the _Create New a Repository_ page use the dropdown under "Repository template" and select the option "AMEND-Consulting-LLC/github-general-template". Fill in the desired project name and project description (the description can be editted in the future), ensure that the project is set to Private, and click the green 'Create Repository' button at the bottom of the page.
3) Once the project has been created follow the steps for [installation](#installation) to get the project running on your local machine, replacing this templates name with your new project's name.
4) Now that the scripts have been installed on your machine, perform the following:
   - Replace the `ref/logo.png` file with the a square logo image
   - Modify the text values in the `ref/inputs.csv` file to match your project's information
   - Run the `scripts/create_readme.py` script to create the initial project's readme
5) The project's readme document, which is what shows in the main project page, has now been created. You can either continue manipulating the file directly in the `README.md` file, or edit the `ref/sample.md` document and rerun the `scripts/create_readme.py` script for every change. Please note, the `scripts/create_readme.py` script overwrites the main file when run, so any changes made to it directly would be lost if this is run and the changes were not made to the `ref/sample.md` file.
6) As you create and update the scripts if you follow the comment structure the `scripts/create_readme.py` script can be utilized to make a script annotation file with details for any .py files used. To use this feature do the following:
   - Open the `ref/readme_config.yaml` configuration file and modify the global variables. Note; make sure to have the `run_project` variable marked False if any manual updates were made to the `README.md` file
   - Run the script.

### Creating Variables for Project README
You can make updates to the `ref/sample.md` file and add new variables that will automatically fill according to the `ref/inputs.csv` file.
- Enter variables in desired places in the sample file using brackets surrounding the desired variable name (example `[variable name]`).
- Enter the variable names desired into the inputs file without brackets and their corresponding values.
- Variables can be updated in the inputs file and then the `scripts/create_readme.py` script can be run to automatically generate README files for the project.

### Updating project files
You will need to have an IDE installed in order to modify the python scripts. These steps use the git commands that can be run in command line, however you can use the desktop github application to make updates more easily.
1) Pull down the project using the steps in the [installation](#installation) section. 
2) Create a new branch using this command: `git checkout -b branch-name`
3) Open and modify files where the changes need to be made. 
4) Once the changes are done and the scripts have been tested and work as expected, commit these changes to the branch using this command: `git commit -a -m 'Description of changes'`
   - You can continue working out of this branch until all changes you want to do are done, or move to the next step and redo this process later for additional changes
5) Merge your changes to the `master` branch run the following commands:
    ```sh
    git checkout master
    git merge branch-name
    ```
   - Note that if you made changes to a file at the same time as someone else merge conflicts may happen, these can be dealt with using additional commands
   - For more information on [Git Commands](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

Additional features and documentation can be added using this [page](https://github.com/AMEND-Consulting-LLC/github-general-template/issues) or through contacts.

### Checklist of Features
- [x] Put together library of Data Import Functions
- [x] Put together library of Data Export Functions
- [ ] Add script to generate documentation
    - [x] Creating general project documentation
    - [x] Creating script documentation
    - [ ] Creating requirements.txt
- [x] Modify Readme Script to use YAML file
- [ ] Add links to other resources
- [ ] Add generalized github instructions (i.e. making updates, getting updates, setting up on a new machine)

### Additional Documentation
[Git Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging): For Command Prompt Commands

[GitHub Markdown Language](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax): Used for ReadMe files

See the [open issues](https://github.com/AMEND-Consulting-LLC/github-general-template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

* Andrea Gergel - gergel@AMENDLLC.com

<p align="right">(<a href="#top">back to top</a>)</p>
