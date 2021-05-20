#!/usr/bin/env bash
# I know it's bad but there is no other way to keep docstring working with this decorator
SCRIPT_PATH=`dirname "$0"`
python -m robot.libdoc ${SCRIPT_PATH}/../ArchiveLibrary/ ${SCRIPT_PATH}/../index.html