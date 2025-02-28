#!/bin/bash

# Load configuration
source ../config/db.conf

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# Generate timestamp
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/backup_$TIMESTAMP.sql"

# Perform backup
PGPASSWORD=$DB_PASSWORD pg_dump -h $DB_HOST -p $DB_PORT -U $DB_USER $DB_NAME > $BACKUP_FILE

# Compress backup
gzip $BACKUP_FILE

# Clean up old backups
find $BACKUP_DIR -name "backup_*.sql.gz" -mtime +$BACKUP_RETENTION_DAYS -delete

echo "Backup completed: ${BACKUP_FILE}.gz"