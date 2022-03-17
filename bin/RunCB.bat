@ECHO OFF
REM #############################  RunCB.bat  ##################################
REM # You can use this batch to run the backup client application              #
REM ############################################################################

REM ####################  Start: User Defined Section  #########################

REM ------------------------------  SETTING_HOME  ------------------------------
REM | Directory to your setting home. Default to                               |
REM | "C:\Users\USER\.obm" when not set.                                       |
REM | e.g. SET SETTING_HOME="C:\Users\John\.obm"                               |
REM ----------------------------------------------------------------------------
SET SETTING_HOME=""

REM -------------------------------  DEBUG_MODE  -------------------------------
REM | Enable/Disable debug mode                                                |
REM | e.g. SET DEBUG_MODE="--debug"                                            |
REM |  or  SET DEBUG_MODE=""                                                   |
REM ----------------------------------------------------------------------------
SET DEBUG_MODE=""

REM ####################  END: User Defined Section  ###########################

SET EXE_DIR=%CD%
SET APP_HOME=..
SET JAVA_HOME=%APP_HOME%\jvm
SET JAVA_EXE=%JAVA_HOME%\bin\bJW.exe
SET JAVA_LIB_PATH=-Djava.library.path=%APP_HOME%\bin
SET PATH=%JAVA_HOME%\bin;%PATH%

IF "%PROCESSOR_ARCHITECTURE%"=="x86" (
  SET "DEP_LIB_PATH=X86"
  SET JAVA_OPTS=-Xms128m -Xmx2048m -XX:MaxDirectMemorySize=512m -Dsun.java2d.noddraw -Dsun.nio.PageAlignDirectMemory=true
) ELSE (
  SET "DEP_LIB_PATH=X64"
  SET JAVA_OPTS=-Xms128m -Xmx2048m -XX:MaxDirectMemorySize=1024m -Dsun.java2d.noddraw -Dsun.nio.PageAlignDirectMemory=true
)

SET PATH=%APP_HOME%\bin\%DEP_LIB_PATH%;%JAVA_HOME%\bin;%PATH%
SET CLASSPATH=%APP_HOME%in;%APP_HOME%\bin\cb.jar
SET JAVA_LIB_PATH=%JAVA_LIB_PATH%;%APP_HOME%\bin\%DEP_LIB_PATH%

REM #############################################################################
ECHO - 
ECHO APP_HOME=%APP_HOME%
ECHO SETTING_HOME=%SETTING_HOME%
ECHO JAVA_HOME=%JAVA_HOME%
ECHO JAVA_EXE=%JAVA_EXE%
ECHO JAVA_OPTS=%JAVA_OPTS%
ECHO JAVA_LIB_PATH=%JAVA_LIB_PATH%
ECHO PATH=%PATH%
ECHO CLASSPATH=%CLASSPATH%
ECHO - 

@ECHO ON
%JAVA_EXE% %JAVA_LIB_PATH% -cp %CLASSPATH% %JAVA_OPTS% Gui %DEBUG_MODE% %APP_HOME% %SETTING_HOME%
@ECHO OFF
CD "%EXE_DIR%"
IF "%APP_HOME%"==".." PAUSE
@ECHO ON