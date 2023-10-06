import os
import zipfile
import requests
import json
import argparse
import logging
DEFAULT_OUTPUT_FOLDER = "_output"
DEFAULT_SWAGGER_JSON_URL = "https://petstore.swagger.io/v2/swagger.json"

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
                    help='whether to generate a pdf or not', default=False)

args = parser.parse_args()

swagger_conf_url = args.swagger_conf_url
output_folder = args.output_folder
generate_pdf = args.generate_pdf

swagger_conf_url, output_folder = _check_args(swagger_conf_url, output_folder)

swagger_conf = requests.get(swagger_conf_url)

python_dict=json.loads(swagger_conf.text)

body = {
    "lang": "html2",
    "spec": python_dict,
    "type": "CLIENT"
}

file = requests.post("https://generator3.swagger.io/api/generate", json=body)
with open("some.zip", 'wb') as f:
        f.write(file.content) 

with zipfile.ZipFile('some.zip') as zf:
    zf.extract('index.html', output_folder)
    
html_path = os.path.join(output_folder, "index.html")

if generate_pdf:

    output_pdf = os.path.join(output_folder, "docs.pdf")

    # from pyhtml2pdf import converter
    # converter.convert(f'file:///{html_path}', output_pdf)

    import pdfkit
    pdfkit.from_file(html_path, output_pdf, verbose=True, options={"enable-local-file-access": True}, configuration=pdfkit.configuration(wkhtmltopdf="execs/wkhtmltopdf.exe"))
