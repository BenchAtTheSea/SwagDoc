import os
import zipfile
import requests
import json
import argparse
import logging
from dotenv import load_dotenv
load_dotenv(".env")


DEFAULT_OUTPUT_FOLDER = os.environ.get("DEFAULT_OUTPUT_FOLDER")
DEFAULT_SWAGGER_JSON_URL = os.environ.get("DEFAULT_SWAGGER_JSON_URL")
GENERATE_PDF = os.environ.get("GENERATE_PDF") == "True"
SWAGGER_EDITOR_ENDPOINT = os.environ.get("SWAGGER_EDITOR_ENDPOINT")
TEMP_ZIP_NAME = os.environ.get("TEMP_ZIP_NAME")
HTML_FILE_NAME = os.environ.get("HTML_FILE_NAME")
PDF_FILE_NAME = os.environ.get("PDF_FILE_NAME")
WKHTMLTOPDF_PATH = os.environ.get("WKHTMLTOPDF_PATH")

def _check_args(swagger:str, output_folder:str):
    if not swagger:
        logging.info("no swagger json endpoint was provided.")
        logging.info (f"Using demo mode targetting \"{DEFAULT_SWAGGER_JSON_URL}\"")
        logging.info ("To provide your desired swagger endpoint pass it as -o <swagger_json_url>")
        swagger = "DEFAULT_SWAGGER_JSON_URL"

    if not os.path.isabs(output_folder):
        logging.warning("Provided output folder path is not absolute, support for relative path is not implemented yet.")
        logging.info(f"Using default ouput folder \"{DEFAULT_OUTPUT_FOLDER}\"")
        output_folder = DEFAULT_OUTPUT_FOLDER
    return swagger, output_folder
        

parser = argparse.ArgumentParser(description='Generates html and pdf format docs for a provided swagger instance')
parser.add_argument('--swagger_conf_url', "-s",metavar='S', type=str,
                    help='link to swagger json configuration', default=DEFAULT_SWAGGER_JSON_URL)
parser.add_argument('--output_folder', "-o",metavar='S', type=str,
                    help='the folder where the docs will be saved', default=DEFAULT_OUTPUT_FOLDER)
parser.add_argument('--generate_pdf', "-pdf",metavar='S', type=bool,
                    help='whether to generate a pdf or not', default=GENERATE_PDF)

args = parser.parse_args()

swagger_conf_url = args.swagger_conf_url
output_folder = args.output_folder
generate_pdf = args.generate_pdf

swagger_conf_url, output_folder = _check_args(swagger_conf_url, output_folder)

swagger_conf = requests.get(swagger_conf_url)

python_dict=json.loads(swagger_conf.text)

body = {
    "lang": "html2", # this can in fact support many different format, currently locked to html2 for semplicity
    "spec": python_dict,
    "type": "CLIENT"
}

file = requests.post(SWAGGER_EDITOR_ENDPOINT, json=body)
with open(TEMP_ZIP_NAME, 'wb') as f:
        f.write(file.content) 

with zipfile.ZipFile(TEMP_ZIP_NAME, "r") as zf:
    zf.getinfo("index.html").filename = HTML_FILE_NAME
    zf.extract("index.html", output_folder)

os.remove(TEMP_ZIP_NAME)
    
html_path = os.path.join(output_folder, HTML_FILE_NAME)

if generate_pdf:

    output_pdf = os.path.join(output_folder, PDF_FILE_NAME)

    import pdfkit
    if WKHTMLTOPDF_PATH:
        pdfkit.from_file(html_path, output_pdf, verbose=True, options={"enable-local-file-access": True}, configuration=pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH))
    else:
         pdfkit.from_file(html_path, output_pdf, verbose=True, options={"enable-local-file-access": True})
