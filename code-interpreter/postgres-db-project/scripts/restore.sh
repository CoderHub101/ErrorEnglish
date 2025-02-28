#!/bin/bash

# Load configuration
source ../config/db.conf

# Check if backup file is provided
if [ -z "$1" ]; then
    echo "Usage: restore.sh <backup_file>"
    exit 1
fi

BACKUP_FILE=$1

# Check if file exists
if [ ! -f "$BACKUP_FILE" ]; then
    echo "Error: Backup file not found"
    exit 1
fi

# If file is compressed, decompress it
if [[ $BACKUP_FILE == *.gz ]]; then
    gunzip -c $BACKUP_FILE | PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME
else
    PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME < $BACKUP_FILE
fi

echo "Restore completed from: $BACKUP_FILE"