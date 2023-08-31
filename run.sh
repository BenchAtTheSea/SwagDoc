while getopts "s:o:" opt
do
    case "$opt" in
        s ) parameterA="$OPTARG" ;;
        o ) parameterB="$OPTARG" ;;
    esac
done

if [ -z ${parameterB} ]
then
    parameterB=\%cd\%
fi

if [ -z ${parameterA} ]
then
    parameterA="https://petstore.swagger.io/v2/swagger.json"
fi
echo $parameterB

docker run -v $parameterB:/app/_output swagdoc \-s $parameterA
