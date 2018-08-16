if [ $# -lt 1 ];then
    echo "Usage: $0 [container name] (AWS_ECR_URL)"
    exit 1
fi
    
CONTAINER_NAME=$1
if [ $# -gt 1 ];then
    AWS_ECR_URL="$2"
else
    AWS_ECR_URL="fakeaccountnumber.dkr.ecr.us-west-2.amazonaws.com"
fi

echo $CONTAINER_NAME
echo $AWS_ECR_URL

docker build -t ${CONTAINER_NAME} .
docker tag ${CONTAINER_NAME}:latest ${AWS_ECR_URL}/${CONTAINER_NAME}:latest
echo "Push with docker push ${AWS_ECR_URL}/${CONTAINER_NAME}:latest"
#docker push ${AWS_ECR_URL}/${CONTAINER_NAME}:latest
