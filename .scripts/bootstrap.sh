#!/usr/bin/env bash

# TODO bash subroutine for verifying these tools exist

pre-commit install --install-hooks --overwrite
pre-commit install --hook-type commit-msg
pre-commit install --hook-type prepare-commit-msg
pre-commit run --all-files
