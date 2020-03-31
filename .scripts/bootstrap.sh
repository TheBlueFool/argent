#!/usr/bin/env bash

# TODO bash subroutine for verifying these tools exist

pre-commit install --install-hooks --overwrite
pre-commit run --all-files
