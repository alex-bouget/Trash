@echo off
setlocal EnableDelayedExpansion

REM VARIABLES LIBRAIRIE A 0
set ibrary_music_wait_finish=0
set library_gui_agraf=0
set library_dowload_unarchive=0

REM SQUELETTE GENERAL
if /i "%1" == "options" (
	if /i "%2" == "" (
		goto options
	) else (
		if /i "%2" == "music" (
			goto options_music
		)
		if /i "%2" == "gui" (
			goto options_gui
		)
		if /i "%2" == "download" (
			goto options_download
		)
		if /i "%2" == "speech" (
			goto options_speech
		)
		goto end
	)
)
if /i "%1" == "speech" (
	if not "%~2" == "" (
		set "text"="%~2"
	)
	if "%text%" == "" (
		no speech on text variable
		goto end
	)
	goto speech
)
if /i "%1" == "music" (
	if /i "%2" == "stop" (
		goto fin
	)
	if /i "%2" == "" (
		echo set your music
		goto end
	) else (
		if not exist "%2" (
			echo your music not exist
			goto end
		)
	)
	if /i "%3" == "" (
		set library_music_wait_finish=false
		goto music
	) else (
		if /i "%3" == "true" (
			set library_music_wait_finish=true
			goto music
		) else (
			if /i "%3" == "false" (
				set library_music_wait_finish=false
				goto music
			) else (
				echo music wait no recon
				goto end
			)
		)
	)
)
if /i "%1" == "gui" (
	if /i "%2" == "1" (
		set library_gui_agraf=1
	) else (
		if /i "%2" == "2" (
			set library_gui_agraf=2
		) else (
			echo agraf code no recon
			goto end
		)
	)
	if not exist "%~3" (
		echo %3 not found
		goto end
	)
	if /i "%4" == "" (
		echo set gui name
		goto end
	)
	call :gui "%3" %4
	goto end
)
if /i "%1" == "download" (
	if /i "%2" == "" (
		echo no file to download
		goto end
	)
	if /i "%3" == "" (
		set library_dowload_unarchive=false
		goto download
	) else (
		if /i "%3" == "true" (
			if /i "%4" == "" (
				echo no name write
				goto end
			)
			set library_dowload_unarchive=true
			goto download
		) else (
			if /i "%3" == "false" (
				set library_dowload_unarchive=false
				goto download
			) else (
				echo unarchive no recon
				goto end
			)
		)
	)
)

REM SQUELETTE SECONDAIRE
:options
echo -------
echo options
echo -------
echo.
echo [] (eventualy)
echo.
echo options : open settings
echo music [song] (waiting music finish=false)
echo music stop
echo gui [use agraf numero] [file name] [gui name] 
echo download [file to download] (unarchive file=false) (if unarchive file = true please write name of file)
echo speech
goto end
:options_music
echo -----
echo music
echo -----
echo.
echo [1]-music
echo [2]-adress of song (ex: C:/music.wav)
echo (3)-waiting music (normally false)
goto end
:options_gui
echo ---
echo gui
echo ---
echo.
echo [1]-gui
echo [2]-agraf numero (1 or 2)
echo [3]-"adress of file name" (ex: "C:/agraf")
echo [4]-Agraf gui name (ex : #Gui_0)
goto end
:options_download
echo --------
echo download
echo --------
echo.
echo [1]-download
echo [2]-file to download (ex: https://www.google.fr/file.rar)
echo (3)-unarchive file (normally false)
echo [4 if unarchive file=true]-name of archive (ex: file.rar)
goto end
:options_speech
echo ------
echo speech
echo ------
echo.
echo set text=your speech
echo [1]-speech
goto end




:music
echo set song=%2>>load.bat
start library\song
if %library_music_wait_finish% ==false goto end
if %library_music_wait_finish% ==true (
	set EXE=cmdmp3.exe
	:return_music
	cls
	choice /c wn /n /t 2 /d n /m "appuyer sur w pour arreter le sons"
	if %ERRORLEVEL% ==1 goto fin
	FOR /F %%x IN ('tasklist /NH /FI "IMAGENAME eq cmdmp3.exe"') DO IF %%x == cmdmp3.exe goto return_music
	:fin
	taskkill /IM TASKKILL /F /IM cmdmp3.exe
	cls
	goto end
)

:gui
FOR /F "tokens=1,* delims=:" %%A IN ('library\AGRAF%library_gui_agraf% "%~1" %2') DO SET %%A=%%B
goto:eof

:download
library\wget "%2"
if %library_dowload_unarchive% ==true (
	library\7z x "%4"
)
goto end

:speech
set library_num=%random%
if exist temp%library_num%.vbs del temp%library_num%.vbs
echo ' > "temp%library_num%.vbs"
echo set speech = Wscript.CreateObject("SAPI.spVoice") >> "temp%library_num%.vbs"
echo speech.speak "%text%" >> "temp%library_num%.vbs"
temp%library_num%.vbs
del temp%library_num%.vbs
goto end

REM FIN
:end
goto:eof