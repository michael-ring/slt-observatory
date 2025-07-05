#!/bin/sh
. ./.venv/bin/activate
make ssh_upload
chmod 644 rawimages/*
rsync --archive --verbose --progress rawimages/* root@michael-ring.org:/var/www/slt-observatory.space/images/
