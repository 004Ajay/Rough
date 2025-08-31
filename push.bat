@echo off
set /p commitmsg=Enter commit message: 

echo.
echo Adding all files...
git add .

echo.
echo Committing with message: "%commitmsg%"
git commit -m "%commitmsg%"

echo.
echo Pushing to origin main...
git push origin main

echo.
echo Done!
pause
