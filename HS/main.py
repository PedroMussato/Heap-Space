from tkinter import Button, Entry, Frame, Label, Tk
from datetime import datetime

VERSION = 8
LOGFILE = "./transactions/log.txt"
VALUE = "2048"


def log(value):
    global LOGFILE
    with open(LOGFILE, "a+") as logfile:
        logfile.write(f"{datetime.now()}\n{value}\n")


def pro(version, value):
    log(f"Version {version}, was selected!")
    if version == 8:
        runPath ="../bin/RunCB.bat"
        runTxt = f"""@ECHO OFF
REM #############################  RunCB.bat  ##################################
REM # You can use this batch to run the backup client application              #
REM ############################################################################

REM ####################  Start: User Defined Section  #########################

REM ------------------------------  SETTING_HOME  ------------------------------
REM | Directory to your setting home. Default to                               |
REM | "C:\\Users\\USER\\.obm" when not set.                                       |
REM | e.g. SET SETTING_HOME="C:\\Users\\John\\.obm"                               |
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
SET JAVA_HOME=%APP_HOME%\\jvm
SET JAVA_EXE=%JAVA_HOME%\\bin\\bJW.exe
SET JAVA_LIB_PATH=-Djava.library.path=%APP_HOME%\\bin
SET PATH=%JAVA_HOME%\\bin;%PATH%

IF "%PROCESSOR_ARCHITECTURE%"=="x86" (
  SET "DEP_LIB_PATH=X86"
  SET JAVA_OPTS=-Xms128m -Xmx{value}m -XX:MaxDirectMemorySize=512m -Dsun.java2d.noddraw -Dsun.nio.PageAlignDirectMemory=true
) ELSE (
  SET "DEP_LIB_PATH=X64"
  SET JAVA_OPTS=-Xms128m -Xmx{value}m -XX:MaxDirectMemorySize=1024m -Dsun.java2d.noddraw -Dsun.nio.PageAlignDirectMemory=true
)

SET PATH=%APP_HOME%\\bin\\%DEP_LIB_PATH%;%JAVA_HOME%\\bin;%PATH%
SET CLASSPATH=%APP_HOME%\bin;%APP_HOME%\\bin\\cb.jar
SET JAVA_LIB_PATH=%JAVA_LIB_PATH%;%APP_HOME%\\bin\\%DEP_LIB_PATH%

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
@ECHO ON"""
        run32Path = "no32bit"
        run32Txt = "no32bit"
        configPath ="../config.ini"
        configTxt = f"""app.system.ui.vm.opt.xms=128
app.system.ui.vm.opt.xmx={value}
app.system.conf.vm.opt.maxdirectmemorysize=1024
app.system.conf.language=en
app.system.product.name=obm
app.system.common.format.datetime.hourinday=true
app.system.ui.backupsetlist.order=creationtime
"""
        log(f"Creating the files with the value of {value}MB")
        return runPath, runTxt, configPath, configTxt, run32Path, run32Txt
    elif version == 7:
        runPath = "../bin/RunCB.bat"
        runTxt = f"""@ECHO OFF
        REM #############################  RunCB.bat  ##################################
        REM # You can use this batch to run the backup client application              #
        REM ############################################################################

        REM ####################  Start: User Defined Section  #########################

        REM ------------------------------  SETTING_HOME  ------------------------------
        REM | Directory to your setting home. Default to                               |
        REM | "C:\\Users\\USER\\.obm" when not set.                                       |
        REM | e.g. SET SETTING_HOME="C:\\Users\\John\\.obm"                               |
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
        SET JAVA_HOME=%APP_HOME%\\jvm
        SET JAVA_EXE=%JAVA_HOME%\\bin\\bJW.exe
        SET JAVA_LIB_PATH=-Djava.library.path=%APP_HOME%\\bin
        SET PATH=%JAVA_HOME%\\bin;%PATH%

        IF "%PROCESSOR_ARCHITECTURE%"=="x86" (
          SET "DEP_LIB_PATH=X86"
          SET JAVA_OPTS=-Xms128m -Xmx{value}m -XX:MaxDirectMemorySize=512m -Dsun.java2d.noddraw -Dsun.nio.PageAlignDirectMemory=true
        ) ELSE (
          SET "DEP_LIB_PATH=X64"
          SET JAVA_OPTS=-Xms128m -Xmx{value}m -XX:MaxDirectMemorySize=1024m -Dsun.java2d.noddraw -Dsun.nio.PageAlignDirectMemory=true
        )

        SET PATH=%APP_HOME%\\bin\\%DEP_LIB_PATH%;%JAVA_HOME%\\bin;%PATH%
        SET CLASSPATH=%APP_HOME%\bin;%APP_HOME%\\bin\\cb.jar
        SET JAVA_LIB_PATH=%JAVA_LIB_PATH%;%APP_HOME%\\bin\\%DEP_LIB_PATH%

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
        @ECHO ON"""
        run32Path = "no32bit"
        run32Txt = "no32bit"
        configPath = "../config.ini"
        configTxt = f"""app.system.ui.vm.opt.xms=128
        app.system.ui.vm.opt.xmx={value}
        app.system.conf.vm.opt.maxdirectmemorysize=1024
        app.system.conf.language=en
        app.system.product.name=obm
        app.system.common.format.datetime.hourinday=true
        app.system.ui.backupsetlist.order=creationtime
        """
        log(f"Creating the files with the value of {value}MB")
        return runPath, runTxt, configPath, configTxt, run32Path, run32Txt
    elif version == 6:
        runPath ="../bin/RunOBC.bat"
        run32Path = "../bin/RunOBC32.bat"
        runTxt = f"""@ECHO OFF
REM #############################  RunOBC.bat  #################################
REM # You can use this batch to run the backup client application              #
REM ############################################################################

REM ####################  Start: User Defined Section  #########################

REM ------------------------------  SETTING_HOME  ------------------------------
REM | Directory to your setting home. Default to                               |
REM | "C:\\Documents and Settings\\USER\\.obm" when not set.                      |
REM | e.g. SET SETTING_HOME="C:\\Documents and Settings\\John\\.obm"              |
REM ----------------------------------------------------------------------------
SET SETTING_HOME=""

REM -------------------------------  DEBUG_MODE  -------------------------------
REM | Enable/Disable debug mode                                                |
REM | e.g. SET DEBUG_MODE="--debug"                                            |
REM |  or  SET DEBUG_MODE=""                                                   |
REM ----------------------------------------------------------------------------
SET DEBUG_MODE=""

REM ####################  END: User Defined Section  ###########################

SET APP_HOME=..
SET JAVA_HOME=%APP_HOME%\\jvm
SET JAVA_EXE=%JAVA_HOME%\\bin\\java.exe
SET JAVA_OPTS=-Xms128m -Xmx{value}m -Dsun.java2d.noddraw 
SET JAVA_LIB_PATH=-Djava.library.path=%APP_HOME%\\bin
SET PATH=%JAVA_HOME%\\bin;%PATH%
SET CLASSPATH=%APP_HOME%\\bin;%APP_HOME%\\bin\\obc.jar;%APP_HOME%\\bin\\obc-lib.jar

SET "DEP_LIB_PATH=X64"
IF "%PROCESSOR_ARCHITECTURE%"=="x86" (
  SET "DEP_LIB_PATH=X86"
)
SET PATH=%CD%\\%APP_HOME%\\bin\\%DEP_LIB_PATH%;%PATH%

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
%JAVA_EXE% %JAVA_LIB_PATH% -cp %CLASSPATH% %JAVA_OPTS% obc %DEBUG_MODE% %APP_HOME% %SETTING_HOME%
PAUSE"""
        run32Txt = f"""@ECHO OFF
REM #############################  RunOBC.bat  #################################
REM # You can use this batch to run the backup client application              #
REM ############################################################################

REM ####################  Start: User Defined Section  #########################

REM ------------------------------  SETTING_HOME  ------------------------------
REM | Directory to your setting home. Default to                               |
REM | "C:\\Documents and Settings\\USER\\.obm" when not set.                      |
REM | e.g. SET SETTING_HOME="C:\\Documents and Settings\\John\\.obm"              |
REM ----------------------------------------------------------------------------
SET SETTING_HOME=""

REM -------------------------------  DEBUG_MODE  -------------------------------
REM | Enable/Disable debug mode                                                |
REM | e.g. SET DEBUG_MODE="--debug"                                            |
REM |  or  SET DEBUG_MODE=""                                                   |
REM ----------------------------------------------------------------------------
SET DEBUG_MODE=""

REM ####################  END: User Defined Section  ###########################

SET APP_HOME=..
SET JAVA_HOME=%APP_HOME%\\jvm32
SET JAVA_EXE=%JAVA_HOME%\\bin\\java.exe
SET JAVA_OPTS=-Xms128m -Xmx{value}m -Dsun.java2d.noddraw 
SET JAVA_LIB_PATH=-Djava.library.path=%APP_HOME%\\bin
SET PATH=%JAVA_HOME%\\bin;%PATH%
SET CLASSPATH=%APP_HOME%\\bin;%APP_HOME%\\bin\\obc.jar;%APP_HOME%\\bin\\obc-lib.jar

SET "DEP_LIB_PATH=X86"
SET PATH=%CD%\\%APP_HOME%\\bin\\%DEP_LIB_PATH%;%PATH%

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
%JAVA_EXE% %JAVA_LIB_PATH% -cp %CLASSPATH% %JAVA_OPTS% obc %DEBUG_MODE% %APP_HOME% %SETTING_HOME%
PAUSE"""
        configPath = "../config.ini"
        configTxt = f"""app.system.ui.vm.opt.xms=128
app.system.ui.vm.opt.xmx={value}
app.system.conf.language=en
app.system.product.name=obm
app.system.common.format.datetime.hourinday=true
"""
        log(f"Creating the files with the value of {value}MB")
        return runPath, runTxt, configPath, configTxt, run32Path, run32Txt


def changeValues(version):
    global VALUE
    log(f"Version {version} was selected.")
    if version > 5 and version < 9:
        value = VALUE
        log("This version is valid")
        runPath, runTxt, configPath, configTxt, run32Path, Run3Txt = pro(version, value)
        with open(runPath, "r") as runOldFile:
            log(f"Reading {runPath} file.")
            readed = runOldFile.read()
            log(f"{readed}")

        with open(runPath, "w") as runFile:
            log(f"Writing {runPath} file.")
            runFile.write(runTxt)

        with open(configPath, "r") as configOldFile:
            log(f"Reading {configPath} file.")
            readed = configOldFile.read()
            log(f"{readed}")

        with open(configPath, "w") as configFile:
            log(f"Writing {configPath} file.")
            configFile.write(configTxt)

        if run32Path != "no32bit":
            with open(run32Path, "r") as runOldFile:
                log(f"Reading {run32Path} file.")
                readed = runOldFile.read()
                log(f"{readed}")

            with open(run32Path, "w") as runFile:
                log(f"Writing {run32Path} file.")
                runFile.write(runTxt)
        return True
    else:
        log(f"version {version} is not avaliable.")
        return False


def save():
    global VERSION, VALUE, entry
    VALUE = entry.get()
    try:
        changeValues(VERSION)
    except Exception:
        log(f"ERROR: {Exception}")
    else:
        log(f"Saved Successfully!")

def reset():
    global VERSION, VAlUE
    VAlUE = 768
    changeValues(VERSION)


def version(value):
    global VERSION
    VERSION = value
    log(f"Version {value} was selected!")


root = Tk()
root.title("HS")
root.resizable(width=0, height=0)
log("Starting")

Label(root, text="Product version:").grid(row=0, column=0)

prod_frame = Frame(root)
btn_prod6 = Button(prod_frame, text="6", command=lambda: version(6)).grid(row=0, column=0)
btn_prod7 = Button(prod_frame, text="7", command=lambda: version(7)).grid(row=0, column=1)
btn_prod8 = Button(prod_frame, text="8", command=lambda: version(8)).grid(row=0, column=2)

prod_frame.grid(row=0, column=1)

Label(root, text="Set to (MB):").grid(row=1, column=0)

entry = Entry(root)
entry.grid(row=1, column=1)

btn_reset = Button(root, text="Reset", command=reset)
btn_reset.grid(row=2, column=0)
btn_save = Button(root, text="Save!", command=save)
btn_save.grid(row=2, column=1)

root.mainloop()
