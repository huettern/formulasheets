#!/bin/bash

eval "$(ssh-agent -s)"
chmod 600 /tmp/deploy_rsa
ssh-add /tmp/deploy_rsa
git remote add target git@github.com:noah95/formulasheets.git
git checkout -b build
git add -f */*.pdf
git status
git commit -am "Build"
git push target build --force
