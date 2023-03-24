""" 

Use this script to generate README files for scripts and the initial one for the project.
Initially setup to only run script README generation, will need to be altered to run project documentation.

For the project documentation it will look through the ref/inputs.csv to generate the documentation using those variables. 
Modify ref/inputs.csv and ref/logo.png files to create the project documentation (logo is square by default).
After initial run modify README.md in project folder with any special updates.

For script documentation it will parse through all scripts inputted and create a comprehensive readme document using the standardized script format.
Alter the 'scripts' Global Variable in the ref/readme_config.yaml file in order to input the files desired documentation for.
Make sure to follow comment standards listed in file, file can be altered after creation but will be overwritten if script is run again.

Contact: Andrea Gergel
Date: 2/3/2023
Status: In progress

"""

## Library Imports
import yaml
import os
import re
from typing import List
import pandas as pd

## Global Variables
with open("./ref/readme_config.yaml") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    scripts = config["scripts"]
    output = config["output"]

    run_script = config["run_script"] # Set to True if running script documentation
    run_project = config["run_project"] # Set to True if running project documentation

    test = config["test"] # Set to True if running in github-general-template

## Functions
def create_script_readme(scriptpaths: List[str], rpath="readme.md"):
    """ Function to create readme using filepaths to script documents. Only scripts in list of scriptpaths get added.
    Date: 2/3/2023
    Args:
        scriptpaths - list of paths of scripts wanted in documentation
        rpath - optional, filepath to where the information should land
    """
    # Create and open the rpath file to write documentation in (will overwrite)
    rdoc = open(rpath,'w')

    rdoc.writelines("# Script Annotation\n")
    rdoc.writelines("This script was automatically generated using the 'create-readme.py' script. If any fields are incorrect please make sure the comment patterns below are used in the script.\n")

    rdoc.writelines("\nScript files are commented as follows:\n\n\
    \"\"\"file-summary-text\n\
        Contact: contact-text\n\
        Date: date-text\n\
        Status: status-text\n\
        \"\"\"\n")

    rdoc.writelines("\nFunctions in script are commented as follows:\n\n\
    \"\"\"function-summary-text\n\
        Date: date-text\n\
        Args:\n\
            arg-bullets\n\
        Return:\n\
            return-bullets\n\
        \"\"\"\n")

    for filename in scriptpaths:
        with open(filename) as file:
            rdoc.writelines("\n## " + os.path.basename(filename) + "\n")
            f = file.read()
            
            functions = re.findall('def ([^"]*)\(', f)
            function_strings = re.findall('"""([^"]*)"""', f)
            
            rdoc.writelines("**Date**: " + re.findall('Date:([^"]*)Status:', function_strings[0])[0].replace("\n","").strip() + "\n\n")
            rdoc.writelines("**Status:** " + re.findall('Status:([^"]*)', function_strings[0])[0].replace("\n","").strip() + "\n\n")
            rdoc.writelines(function_strings[0].split("Contact:")[0].replace("\n","").strip() + "\n")

            rdoc.writelines("\n**Library**:")
            for i in f.split("import ")[1:]:
                rdoc.writelines("\n* " + i.split(" ")[0].split("\n")[0])

            rdoc.writelines("\n")

            for num in range(0,len(functions)):
                rdoc.writelines("\n### " + functions[num].strip() + "\n")
                rdoc.writelines("\nSummary: " + function_strings[num+1].split("Date:")[0].replace("\n","").strip() + "\n")
                rdoc.writelines("\nDate: " + re.findall('Date:([^"]*)Args:', function_strings[num+1])[0].replace("\n","").strip() + "\n")
                if "Args:" in function_strings[num+1] or "eturn:" in function_strings[num+1]:
                    rdoc.writelines("\nArguments: \n")
                    for i in ["* " + str.strip() if "eturn:" not in str else "\nReturn" for str in re.findall('Args:([^"]*)', function_strings[num+1])[0].strip().replace("        ","").replace("     ","").split("\n")]:
                        rdoc.writelines(i + "\n")
    
    rdoc.close()

def create_project_readme(sample = "ref/sample.md", input = "ref/inputs.csv"):
    """ Function to create project readme from inputs.csv and template. Modify inputs csv to make changes
    Date: 2/3/2023
    Args:
        sample - optional, filepath to the template
        input - optional, filepath to inputs csv
    """
    # Read in the file
    with open(sample, 'r') as file:
        filedata = file.read()

        # Replace the target string
        inputs = pd.read_csv(input)
        for i in range(0,len(inputs)):
            filedata = filedata.replace("["+inputs["Variable"][i]+"]", inputs["Text"][i])

        # Replace project name variable with actual project name
        filedata = filedata.replace("[Repo Name]", os.path.basename(os.getcwd()))
        
        output = "./README.md"
        if test:
            output = "ref/test.md"

        # Write the file out again
        with open(output, 'w') as file:
            file.write(filedata)

# Script Run
if run_project:
    create_project_readme("ref/sample.md", "ref/inputs.csv")
if run_script:
    create_script_readme(scripts, output)
