from tkinter import Button, Entry, Frame, Label, Tk
from datetime import datetime

run = "../bin/RunCB.bat"


def write(a = "2048"):
    max_xmx = a
    V8_RunCB_bat = (f"""@ECHO OFF
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
  SET JAVA_OPTS=-Xms128m -Xmx{max_xmx}m -XX:MaxDirectMemorySize=512m -Dsun.java2d.noddraw -Dsun.nio.PageAlignDirectMemory=true
) ELSE (
  SET "DEP_LIB_PATH=X64"
  SET JAVA_OPTS=-Xms128m -Xmx{max_xmx}m -XX:MaxDirectMemorySize=1024m -Dsun.java2d.noddraw -Dsun.nio.PageAlignDirectMemory=true
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
@ECHO ON""")
    if run == "../bin/RunCB.bat":
        with open(run, "w") as c:
            c.write(V8_RunCB_bat)
            print("writing file")
    elif run == "../bin/RunOBC.bat":
        print("zzz")



STATIC=768

def runFile(v):
    global run
    if (v == 6):
        run = "../bin/RunOBC.bat"
        print("def pro6")
    elif (v == 7):
        run = "../bin/RunCB.bat"
        print("def pro7")
    elif (v == 8):
        run = "../bin/RunCB.bat"
        print("def pro8")

def save():
    global run, entry, max_xmx86, max_xmx64
    try:
        print(f"tring save with {entry.get()} value")
        with open(run, "r") as file:
            a = file.read()
        with open(f"transactions/log.txt", "a+") as b:
            b.write(f"{datetime.now()}\n" + a)
    except:
        print("failed")
    else:
        print("successfull")
        write(entry.get())


def reset():
    global run, entry, max_xmx86, max_xmx64
    max_xmx86 = "768"
    max_xmx64 = "2048"
    try:
        with open(run, "r") as file:
            a = file.read()
            with open(f"/transactions/{datetime.now()} - Run__%file", "w+") as b:
                b.write(a)
    except:
        pass
    else:
        if run == "../bin/RunCB.bat":
            with open(run, "w") as c:
                c.write(V8_RunCB_bat)
        elif run == "../bin/RunOBC.bat":
            pass

root = Tk()

Label(root, text="Product version:").grid(row=0, column=0)

prod_frame = Frame(root)
btn_prod6 = Button(prod_frame, text="6", command=lambda: runFile(6)).grid(row=0, column=0)
btn_prod7 = Button(prod_frame, text="7", command=lambda: runFile(7)).grid(row=0, column=1)
btn_prod8 = Button(prod_frame, text="8", command=lambda: runFile(8)).grid(row=0, column=2)

prod_frame.grid(row=0, column=1)

Label(root, text="Set to (MB):").grid(row=1, column=0)

entry = Entry(root)
entry.grid(row=1, column=1)

btn_reset = Button(root, text="Save!", command=save)
btn_reset.grid(row=2, column=1)
btn_save = Button(root, text="Reset", command=reset)
btn_save.grid(row=2, column=0)

root.mainloop()
