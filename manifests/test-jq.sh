#!/bin/bash

CPU_REQUESTS="500m"
MEMORY_REQUESTS="200Mi"
CPU_LIMITS="1Gi"
MEMORY_LIMITS="500Mi"

# Set the file path
FILE="pod.yaml"

# Check if the file exists
if [ ! -f "$FILE" ]; then
    echo "File not found: $FILE"
    exit 1
fi
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
  json=$(echo $json | jq ".spec.containers[$i].resources.requests.cpu = \"$CPU_REQUESTS\"")
  json=$(echo $json | jq ".spec.containers[$i].resources.requests.memory = \"$MEMORY_REQUESTS\"")
  
  # Update and print container resource limits
  json=$(echo $json | jq ".spec.containers[$i].resources.limits.cpu = \"$CPU_LIMITS\"")
  json=$(echo $json | jq ".spec.containers[$i].resources.limits.memory = \"$MEMORY_LIMITS\"")
done

# Convert JSON back into YAML
yq -y '.' <<< "$json" > $FILE
