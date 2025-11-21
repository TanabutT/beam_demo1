# Dataflow flex template: beam_export

## Before you begin

Make sure you have followed the
[Dataflow setup instructions](../../README.md).

## Create a Cloud Storage bucket

```sh
export BUCKET="terra-mhesi-dp-poc-gcs-bronze-01/simplecsv/"
gsutil mb gs://$BUCKET
gcloud storage folders create gs://terra-mhesi-dp-poc-gcs-bronze-01/simplecsv/

```
## create docker file

## create an Artifact Registry repository

```sh
export REGION="asia-southeast1"
export REPOSITORY="simplecsv"

gcloud artifacts repositories create $REPOSITORY \
    --repository-format=docker \
    --location=$REGION
```

## upload docker image to Artifact Registry
```sh
export PROJECT="poc-piloturl-nonprod"
export REGION="asia-southeast1"
export REPOSITORY="simplecsv"
export IMAGE_NAME="simplecsv-py"
export TAG="latest"
export IMAGE_URI="$REGION-docker.pkg.dev/$PROJECT/$REPOSITORY/$IMAGE_NAME:$TAG"

gcloud builds submit . --tag $IMAGE_URI
```


## Build the template

```sh
export PROJECT="poc-piloturl-nonprod"
export BUCKET="terra-mhesi-dp-poc-gcs-bronze-01/simplecsv"

    gcloud dataflow flex-template build gs://$BUCKET/simplecsv_py.json \
        --image-gcr-path "$REGION-docker.pkg.dev/$PROJECT/$REPOSITORY/simplecsv-py:latest" \
        --sdk-language "PYTHON" \
        --flex-template-base-image "PYTHON3" \
        --py-path "." \
        --metadata-file "metadata.json" \
        --env "FLEX_TEMPLATE_PYTHON_PY_FILE=simplecsv.py" \
        --env "FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE=requirements.txt"
```

## Run the template

```sh
export PROJECT="poc-piloturl-nonprod"
export BUCKET="terra-mhesi-dp-poc-gcs-bronze-01/simplecsv"
export CSV_OUTPUT_PATH="gs://${BUCKET}/output-csv"
export PARQUET_OUTPUT_PATH="gs://${BUCKET}/output-parquet"
export TEMP_LOCATION="gs://${BUCKET}/temp"

gcloud dataflow flex-template run "simplecsv-`date +%Y%m%d-%H%M%S`" \
    --template-file-gcs-location "gs://$BUCKET/simplecsv_py.json" \
    --region $REGION \
    --parameters output_csv_path=\"${CSV_OUTPUT_PATH}\" \
    --parameters output_parquet_path=\"${PARQUET_OUTPUT_PATH}\" \
    --staging-location "gs://$BUCKET/staging" \
    --temp-location=${TEMP_LOCATION} \
    --launcher-machine-type=n2-standard-2 \
    --worker-machine-type=n2-standard-2 \
    --project ${PROJECT}
```

## What's next?

For more information about building and running flex templates, see
📝 [Use Flex Templates](https://cloud.google.com/dataflow/docs/guides/templates/using-flex-templates).
