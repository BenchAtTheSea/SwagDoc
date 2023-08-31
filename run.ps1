param ($s="https://petstore.swagger.io/v2/swagger.json", $o=$PWD)
docker run -v $o":/app/_output" swagdoc -s $s