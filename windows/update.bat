@echo off

echo Update bot..

git stash
git pull
git stash pop

echo Done
pause
