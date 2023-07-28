#!/bin/bash

CPU="500m"
# Set the file path
FILE="pod.yaml"

# Check if the file exists
if [ ! -f "$FILE" ]; then
    echo "File not found: $FILE"
    exit 1
fi
# print kind
# print kind
yq '.kind' "$FILE"

# print metadata.namespace
yq '.metadata.namespace // "default"' "$FILE"



# Parse file into JSON
json=$(yq -j '.' $FILE)

# Get the length of the containers array
length=$(echo $json | jq '.spec.containers | length')

# Loop through each container
for (( i=0; i<$length; i++ ))
do
  # Print container name
  echo $json | jq -r ".spec.containers[$i].name"
  
  # Update and print container resource requests
  json=$(echo $json | jq ".spec.containers[$i].resources.requests.cpu = \"$CPU\"")
  json=$(echo $json | jq ".spec.containers[$i].resources.requests.memory = \"$MEMORY\"")
  
  # Update and print container resource requests
  json=$(echo $json | jq ".spec.containers[$i].resources.limits.cpu = \"$CPU\"")
  json=$(echo $json | jq ".spec.containers[$i].resources.limits.memory = \"$MEMORY\"")
done

# Convert JSON back into YAML
yq -y '.' <<< "$json" > $FILE
