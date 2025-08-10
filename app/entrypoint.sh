#!/bin/bash
set -e

if [ "$RUN_ONCE" = "true" ]; then
  python /app/etl.py --once
  exit 0
fi

CRON_SCHEDULE="${CRON_SCHEDULE:-0 * * * *}"
echo "$CRON_SCHEDULE root /usr/local/bin/python /app/etl.py >> /var/log/etl.log 2>&1" > /etc/cron.d/etl-cron
chmod 0644 /etc/cron.d/etl-cron
crontab /etc/cron.d/etl-cron
touch /var/log/etl.log
cron && tail -F /var/log/etl.log
