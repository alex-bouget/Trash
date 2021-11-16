for /f "delims=" %%a in ('type asset_cr.txt') do echo %%a
for /f "delims=" %%b in ('type asset_pl.txt') do echo %%b
pause>nul