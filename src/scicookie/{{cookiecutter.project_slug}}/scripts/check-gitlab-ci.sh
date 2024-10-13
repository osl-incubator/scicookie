#!/bin/bash

# Replace with the actual GitLab project ID and GitLab API URL
PROJECT_ID="{{ cookiecutter.git_username }}%2F{{ cookiecutter.project_slug }}"
GITLAB_API_URL="https://gitlab.com/api/v4/projects/$PROJECT_ID/ci/lint"

# Read the content of the .gitlab-ci.yml file and format it with jq
GITLAB_CI_CONTENT=$(jq --raw-input --slurp < .gitlab-ci.yml)

# Print the content for debugging
echo "Contenido de .gitlab-ci.yml:"
echo "$GITLAB_CI_CONTENT"

# Send the formatted content to the GitLab CI Lint API using curl
RESPONSE=$(curl --silent --header "Content-Type: application/json" 
    --data "{"content": $GITLAB_CI_CONTENT}" 
    "$GITLAB_API_URL")

# Print the response for debugging
echo "Respuesta de la API:"
echo "$RESPONSE"

# Extract the 'valid' field from the API response using jq
VALID=$(echo "$RESPONSE" | jq -r '.valid')

# Check if the 'valid' field is true
if [[ "$VALID" == "true" ]]; then
    echo "The .gitlab-ci.yml file is valid."
else
    echo "The .gitlab-ci.yml file is invalid. Details:"
    echo "$RESPONSE" | jq -r '.errors[]'
fi
