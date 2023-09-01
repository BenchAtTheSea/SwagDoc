# Silent Contributors
https://github.com/sara-ghiglione
https://github.com/Alessandro-Lica

# SwagDoc
A simple python interface to generate offline html and pdf documentation for swagger interfaces.

# How to use it
You can directly run the swagdoc.py script using python or use docker

# Install and run with Python
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

## wkhtmltpdf on linux
Run this command:

> apt-get update && apt-get install -y wkhtmltopdf 

#### Remember to install the requirements.txt

> pip install -r requirements.txt

## Run the python script
> python swagdoc.py -s <link_to_swagger_json_configuration> -o <absolute_path_to_output_folder>

# Install and run with docker

## Build the image
> docker build -t swagdoc <path_to_repo>

## Run the docker
Once you built the image you can use run.sh on linux or run.ps1 on windows.
> run.xx -s <link_to_swagger_json_configuration> -o <absolute_path_to_output_folder>


