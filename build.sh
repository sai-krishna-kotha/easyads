#!/usr/bin/env bash
set -o errexit

# Detect current git branch (Render sets RENDER_GIT_BRANCH)
BRANCH_NAME="${RENDER_GIT_BRANCH:-main}"

echo "Running build for branch: $BRANCH_NAME"

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Only run migrate if NOT on 'maintenance' branch
if [ "$BRANCH_NAME" != "maintenance" ]; then
    echo "Applying database migrations..."
    python manage.py migrate
else
    echo "Skipping database migrations for maintenance branch"
fi