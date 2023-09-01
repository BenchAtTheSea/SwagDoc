import os
import zipfile
import requests
import json

import argparse

parser = argparse.ArgumentParser(description='Generates html and pdf format docs for a provided swagger instance')
parser.add_argument('--swagger_conf_url', "-s",metavar='S', type=str,
                    help='link to swagger json configuration')
parser.add_argument('--output_folder', "-o",metavar='S', type=str,
                    help='the folder where the docs will be saved', default="_output")

args = parser.parse_args()

swagger_conf_url = args.swagger_conf_url or "https://petstore.swagger.io/v2/swagger.json"# or "http://localhost:5000/swagger/v1/swagger.json"
output_folder = args.output_folder

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

output_pdf = os.path.join(output_folder, "docs.pdf")

# from pyhtml2pdf import converter
# converter.convert(f'file:///{html_path}', output_pdf)

import pdfkit
pdfkit.from_file(html_path, output_pdf, verbose=True, options={"enable-local-file-access": True}, pdfkit.configuration(wkhtmltopdf="path_to_exe"))
