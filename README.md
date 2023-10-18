# SwagDoc
A simple python interface to generate offline html and pdf documentation for swagger interfaces.

## Initial setup base Python

1. Make sure to have [python3](https://www.python.org/downloads/) installed.
2. Install the requirements running 
    > pip install -r requirements.txt

3. If you need your docs in pdf, set WKHTMLTOPDF_PATH in .env to your local binaries path, 
4. Set your configuration in .env, this is not strictly required, as you can pass ovveride it by providing arguments when running swagdock, but could save you some time

## Environment configuration
Create a new file named ".env", you can copy or rename "template.env".
Set the following variables as per your needs.

Ideally you can use defaults and only set the url to your swagger instance json configuration and everything should work.

| Entry | Description | Default |
| --- | --- | --- |
| DEFAULT_OUTPUT_FOLDER | path to folder that will contain the outputs |  "_output"|
| DEFAULT_SWAGGER_JSON_URL | url to swagger json configuration to generate docs on |  "https://petstore.swagger.io/v2/swagger.json"|
| GENERATE_PDF | flag to generate docs in pdf format |  "True"|
| SWAGGER_EDITOR_ENDPOINT | api endpoint for html docs generation |  "https://generator3.swagger.io/api/generate"|
| TEMP_ZIP_NAME | name/path of the downloaded zip file from  |  "_temp.zip"|
| HTML_FILE_NAME | name of the html docs file to generate |  "index2.html"|
| PDF_FILE_NAME | name of the pdf docs file to generate |  "docs.pdf"|
| WKHTMLTOPDF_PATH | path to local installation of wkhtmltopdf, leave empty on linux |  "execs\wkhtmltopdf.exe"|

## In line params

You can also override these environment configurations by prompting them when launching swagdoc

| in line parameter | short in line | overrides | Description |
| --- | --- | --- | --- |
| "--swagger_conf_url" | -s | DEFAULT_SWAGGER_JSON_URL | url to swagger json configuration to generate docs on |
| "--output_folder" | -o | DEFAULT_OUTPUT_FOLDER | absolute path to folder that will contain the outputs |
| "--generate_pdf" | -pdf | GENERATE_PDF | flag to generate docs in pdf format |

## Quick Reference

> python swagdoc.py --swagger_conf_url <swagger_json_url>

> python swagdoc.py -s <swagger_json_url>

> python swagdoc.py --output_folder <abs_path>

> python swagdoc.py -o <abs_path>

> python swagdoc.py --generate_pdf

> python swagdoc.py -pdf

## Known Issues

### PDF generation

Pdf generation relies on [wkhtmltopdf](https://github.com/wkhtmltopdf/packaging/releases/download) binaries to run.
Working version for windows is already provided inside execs folder, for Linux and MacOS you'll need to install it.
Theoretically with both Linux and MacOS it should not be needed to set .env WKHTMLTOPDF_PATH.
Please open an issue if you are having problems with this.

#### Linux

> apt-get install wkhtmltopdf

#### MaxOS

> brew install Caskroom/cask/wkhtmltopdf









# Old instructions

## How to use it
You can directly run the swagdoc.py script using python or use docker

## Install and run with Python
You need to install [wkhtmltopdf](https://wkhtmltopdf.org/) first

## wkhtmltopdf on windows
Download the installer from this [link](https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.msvc2015-win64.exe) and follow the wizard.
After the installation is complete you'll need  to add the installation path to your Environment variables:
1.  On the Windows taskbar, right-click the  Windows  icon and select  System.
2. In the Settings window, under Related Settings, click Advanced system settings.
3. On the Advanced tab, click Environment Variables.
4. Click  New  to create a new environment variable. Click  Edit  to modify an existing environment variable.
5. Your path will probably look like this *C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe*
6. After creating or modifying the environment variable, click  Apply  and then  OK  to have the change take effect.

### wkhtmltpdf on linux
Run this command:

> apt-get update && apt-get install -y wkhtmltopdf 

##### Remember to install the requirements.txt

> pip install -r requirements.txt

### Run the python script
> python swagdoc.py -s <link_to_swagger_json_configuration> -o <absolute_path_to_output_folder>

## Install and run with docker

## Build the image
> docker build -t swagdoc <path_to_repo>

### Run the docker
Once you built the image you can use run.sh on linux or run.ps1 on windows.
> run.xx -s <link_to_swagger_json_configuration> -o <absolute_path_to_output_folder>


