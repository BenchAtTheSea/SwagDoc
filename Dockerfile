#Deriving the latest base image
FROM python:latest


#Labels as key value pair
LABEL Maintainer="https://github.com/BenchAtTheSea"

# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /app

#to COPY the remote file at working directory in container
COPY swagdoc.py ./
# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.
RUN apt-get update && apt-get install -y wkhtmltopdf 
RUN pip install pdfkit
RUN pip install requests
# CMD [ "python", "./swagdoc.py"]
ENV PATH="/app:$PATH"
ENTRYPOINT ["python","swagdoc.py"]
