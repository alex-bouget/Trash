@echo off
if not exist cache\DATA.C Call data\cache.bat
Call data\launch\launch.bat
exit