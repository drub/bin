#!/Users/thedrub/anaconda3/bin/python

# ----------------------------------------------------------------------
# Libraries
# ----------------------------------------------------------------------
import sys
import os
from os.path import exists
import subprocess

# ----------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------
debug = True
debug = False
#debug = True
ENV_VAR_NAME = "JOURNALPATH"


PROG_CONFIG = \
    {"name"          : os.path.basename(sys.argv[0]), \
     "maj_ver"        : "1", \
     "min_ver"        : "3", \
    }
PROG_CONFIG["ver"] = PROG_CONFIG["maj_ver"] + "." + PROG_CONFIG["min_ver"]


# ----------------------------------------
def Get_Input_Files(environmentVar):
# ----------------------------------------

    funcName = sys._getframe().f_code.co_name
    if debug :
        print(f"++++ {funcName} ++++++++++++++++++++")

    if environmentVar in os.environ:
        # The ENV variable exists. Return the file list.
        if debug :
            print("++ Name: " + environmentVar)
            print("Contents: " + os.environ[environmentVar])
        return os.environ[environmentVar]
    else:
        print("Error: ")
        exit()

# ----------------------------------------
def Print_File_Names(fList):
# ----------------------------------------

    funcName = sys._getframe().f_code.co_name
    if debug :
        print(f"++++ {funcName} ++++++++++++++++++++")

    counter = 0
    for file in fList :
    
        description = GetFileDescription(file)
        # Space pad the counter
        # Suppress newline
        print("[{: >2d}]{}".format(counter, description), end="")
        print("       {}".format(file))
        counter += 1

# ----------------------------------------
def ProgUsage(fList) :
# ----------------------------------------
    funcName = sys._getframe().f_code.co_name
    progName = PROG_CONFIG['name']

    if debug :
        print(f"++++ {funcName} ++++++++++++++++++++")
        print(f"++ progName .......... {progName}")

    print(f"Name")
    print(f"    {progName} - Edit one of the journal files")
    print(f"")
    print(f"Synopsis")
    print(f"    {progName}: j [h] | [-h] | [<journal number>]")
    print(f"    <journal number> is one of the files listed below.")
    print(f"")
    print(f"Description")
    print(f"    A utility that helps access one of the journal files.")
    print(f"    The files are listed in an environment variable: {ENV_VAR_NAME}")
    print(f"")
    print(f"    Journal files:")

    Print_File_Names(fList)
    print(f"")
    #print(f"{PROG_CONFIG["ver"]}")
#PROG_CONFIG["ver"] = PROG_CONFIG["maj_ver"] + "." + PROG_CONFIG["min_ver"]

# ----------------------------------------
def GetFileDescription(file) :
# ----------------------------------------
    funcName = sys._getframe().f_code.co_name
    if debug :
        print(f"++++ {funcName} ++++++++++++++++++++")

    if exists(file) :
        fileDescriptor = open(file, 'r')
        line = fileDescriptor.readline()
    else :
        return(" ERROR: File does not exist.\n")

    elementList =  line.split("::")
    elementLen = len(elementList)

    if debug :
        print ("++ elementList ....... " + str(elementList))
        print ("++ Item Count ........ " + str(elementLen))
        print("++ First token ....... " + str(elementList[0]))

    if elementLen < 2 :
        if debug :
            print ("++ elementList empty ")
            print ("++ Description ....... " + str(description))
        description = " ++ First line does not look like a description. Could be blank.\n"
    else :
        description = elementList[1]

    if elementList[0] != 'Description' :
        description = " ERROR: Malformed first line. First token should be \"Description\".\n"

    return(description)

# ----------------------------------------
def ParseUserOptions () :
# ----------------------------------------
    funcName = sys._getframe().f_code.co_name
    if debug :
        print(f"++++ {funcName} ++++++++++++++++++++")

    # If no arguments, set to the default, 0
    if len(sys.argv) == 1 :
        if debug :
            print ("++ No arguments. Set journalNumber, arg1 to 0.")
        # When no argument set the default value, 0
        journalNumber = 0
        arg1 = 0

    # There is an argument. Save in arg1
    elif len(sys.argv) > 1 :
        arg1 = sys.argv[1]

    # Is arg1 a help flag? Output the Usage message and exit
    if arg1 == "h" or arg1 == "-h" :
        ProgUsage(fileList)
        sys.exit(0)

    # arg1 can now be a numeric character or another character. Or multiple
    # characters.
    if debug :
        print(f"++ arg1 type ......... {type(arg1)}")
        print(f"++ fileList type ..... {type(fileList)}")
        #print(f"++ File list: {str(fileList)}")    # Very verbose

    # The number of files contained in the env variable
    journalCount = len(fileList)
    if debug :
        print(f"++ journalCount ...... {journalCount}")

    fileNo = arg1
    if debug :
        print (f"++ fileNo ............ a numeric character")
        print (f"++ fileNo type ....... {type(fileNo)}")
        print (f"++ fileNo ............ {fileNo}")

    # Is the fileNo in range? Char "0" to "9"
    if not ( str(fileNo) >= "0" and str(fileNo) <= "9" ) :
        # The user-supplied is not in a numeric character or characters
        # Or, it is some other character or characters not "h" or "-h"
        print(f"ERROR: Option supplied is not numeric ... {fileNo}")
        sys.exit(1)
    else :
        if debug :
            print (f"++ journalNumber is in range.")

    return(fileNo)

# ----------------------------------------------------------------------
# Main MAIN main
# ----------------------------------------------------------------------

if __name__ == '__main__' :

    envVarContents = Get_Input_Files(ENV_VAR_NAME)
    # Parse the env variable contents
    fileList = envVarContents.split(":")

    targetFileNo = ParseUserOptions()
    targetFile   = fileList[int(targetFileNo)]

    if debug :
        print (f"++ targetFileNo ...... {str(targetFileNo)}")
        print (f"++ targetFile ........ {targetFile}")

    if exists(targetFile) :
        if debug :
            print (f"++++ Main ++++++++++++++++++++")
            print (f"++ targetFile ........ File exists")
            print (f"++ targetFileNo ...... {targetFileNo}")
            print (f"++ File .............. {targetFile}")
            print("++ Start vi ... but we're in debug mode.")
            sys.exit(0)

        subprocess.run(['vim', targetFile])

    else :
        print(f"ERROR: File does not exist.")
        print(f"       A file is named in the environment variable {ENV_VAR_NAME}.")
        print(f"       {targetFile}")
        sys.exit(1)

    sys.exit(0)

'''
# ----------------------------------------------------------------------
# ToDo TODO todo
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# History HISTORY history
# ----------------------------------------------------------------------

--------------------------------------------------
j, Ver 1.3
--------------------------------------------------
- Cleaned up getting the description line out of the journal files, the first line of the file.
- Better error detection and reporting
- Parse the line on ::
- The syntax for the first line is
Description:: <text>

--------------------------------------------------
j, Ver 1.2
--------------------------------------------------
- Added
    if __name__ == '__main__' :
- Updated indenting

--------------------------------------------------
j, Ver 1.1
--------------------------------------------------
- Better struct ProgUsage
- Cleanup

--------------------------------------------------
j, Ver 1.0
--------------------------------------------------
Initial version
- Substantially functionally equivalent to the shell version, "journal".
- A huge improvement. Much easier to implement and maintain.

Name
  Usage: j [h] | [-h] | [<journal Number>]

Where 
  <journal Number> is one of

[ 0] Work journal
       /Users/thedrub/sync_synology/doc/journal/work/journal_work.txt
[ 1] Personal journal
       /Users/thedrub/sync_synology/doc/journal/journal_personal.txt
[ 2] Gratitude
       /Users/thedrub/sync_synology/doc/journal/journal_gratitude.txt
[ 3] Agile topics and events
       /Users/thedrub/sync_synology/Work/Agile/agile.txt
[ 4] Investment activities, calls, notes
       /Users/thedrub/sync_synology/doc/journal/journal_investments.txt
[ 5] Job search, recruiter contact, etc
       /Users/thedrub/sync_synology/home/job-search/job.txt
[ 6] Rotary notes
       /Users/thedrub/sync_synology/doc/journal/journal_rotary.txt
[ 7] PDA, Product Delivery Alchemy
       /Users/thedrub/sync_synology/doc/journal/journal_pda.txt
[ 8] Test file in iCloud. See how it works.
       /Users/thedrub/Library/Mobile Documents/com~apple~CloudDocs/Documents/journal/test.txt
[ 9] Divorce
       /Users/thedrub/sync_synology/doc/journal/journal_divorce.txt


'''
