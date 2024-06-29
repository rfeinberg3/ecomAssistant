#!/bin/bash

# Try to pull the latest changes; if it fails, clone the repository
git -C ColBERT/ pull || git clone https://github.com/stanford-futuredata/ColBERT.git ColBERT
