
#! /bin/bash

# ----------------------------------------
# Constants
# ----------------------------------------
readonly origIFS=$IFS
readonly progVer="5.0"
readonly progName=$(basename $0)
readonly uninitialized="UNINITIALIZED"
readonly allRecords="FALSE"
readonly fileSearchList="\
${HOME}/cloud_storage/Dropbox (cPrime Inc.)/for David Bacon/cPrime.txt\
:${HOME}/Sync/Work/Agile/agile.txt\
"

# ----------------------------------------
# ToDo
# ----------------------------------------
# - Search multiple files in a list,using the $PATH syntax
# - Add these to the search list
#   /Users/thedrub/cloud_storage/Dropbox\ \(Personal\)/doc/journal.txt
#   /Users/thedrub/Sync/Work/Agile/agile.txt"

# ----------------------------------------
# Globals
# ----------------------------------------
debug="FALSE"
debug="TRUE"
recordCount=0


if [ "$debug" == "TRUE" ]; then
  printf "%s\n"  "++ 0 ........................ .$0."
  printf "%s\n"  "++ 1 ........................ .$1."
  printf "%s\n"  "++ \$* ...................... .$*."
  printf "%s\n"  "++ progName ................. .$progName."
  printf "%s\n"  "++ File search list ......... .$fileSearchList."
fi


# ----------------------------------------
  function ProgUsage () {
# ----------------------------------------
  printf "%s"  "
Syntax:
$progName search_name [ file_name  ]
  contact -h

Where
  search_name is a string used for the search
  file_name is a file to search.

Defaults
  A file list is stored in a variable in the script.

Version: $progVer"

}	# function


# ----------------------------------------
  function Dummy () {
# ----------------------------------------
local fileName=$1
local stringToFind=$2
local fileBaseName=$(basename $fileName)


}


# ----------------------------------------
  function SearchFile () {
# ----------------------------------------
local fileName=$1
local stringToFind=$2
local fileBaseName=$(basename $fileName)

        #set -xv #debug
debug="TRUE"    #debug
    if [ "$debug" == "TRUE" ]; then
        printf "%s" "
**    function ........... SearchFile
**    parm 1 ............. .${1}.
**    parm 2 ............. .${2}.
**    fileName ........... .${fileName}.
**    fileBaseName ....... .${fileBaseName}.
**    stringToFind ....... .${stringToFind}.
"
    fi
    exit #debug

# Parse CONREC version 3.0 record format
    IFS=":"
        #set -xv #debug
    grep "CONREC::" ${fileName} | grep -i ${stringToFind} | \
    while read recordType junk recordVer junk recordDate junk firstStr junk lastStr junk emailStr junk phoneStr junk orgStr junk roleStr junk remainingStr 
    do
        recordCount=$((recordCount+1))  # Increment recordCount

        if [ "$debug" == "TRUE" ]; then
            echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
            echo "++ recordType ......... .$recordType."
            echo "++ recordVer .......... .$recordVer."
            echo "++ Date ............... .$recordDate."
            echo "++ recordVer .......... .$recordVer."
            echo "++ firstStr ........... .$firstStr."
            echo "++ lastStr ............ .$lastStr."
            echo "++ emailStr ........... .$emailStr."
            echo "++ phoneStr ........... .$phoneStr."
            echo "++ orgStr ............. .$orgStr."
            echo "++ roleStr ............ .$roleStr."
            echo "++ remainingStr ....... .$remainingStr.".
        fi

        if [[ $recordCount == 1 ]]; then

            printf "%s\n" " ---------------------------------------- $progName  v$progVer -----"
            printf "%s\n" " ---------------------------------------- $fileBaseName"
        fi

        echo "   Name ........ $firstStr $lastStr"
        echo "   Phone ....... $phoneStr"
        echo "   email ....... $emailStr"

        if [[ ! -z $remainingStr ]]; then
            echo "     Note ...... $remainingStr"
        fi

        echo "     Org ....... $orgStr"
        echo "     Created ... $recordDate                Record Ver: $recordVer"

        printf "%s\n" " ------------------------------------------------------------"
        printf "%s" "\n"
    done
}


# ----------------------------------------
# ----------------------------------------
# main Main MAIN
# ----------------------------------------
# ----------------------------------------


if [[ -z $1 ]]; then
    echo
    echo "ERROR: search_name not supplied."
    echo
    ProgUsage
    printf "\n"
    exit
else
    searchStr=$1 

    # See if a Usage message was requested, the "-h" flag
    if [[ "${searchStr}" = "-h" ]]; then
        ProgUsage
        exit
    fi
fi

IFS=:
for searchFileName in $fileSearchList; do

    if [ -f $searchFileName ]; then
        #set -xv #debug
        #if [ "$debug" == "TRUE" ]; then
            printf "%s" "
++ Main
++ searchFileName .................... $searchFileName
++ searchStr ......................... $searchStr
"
        #set +xv #debug
       #fi
        #SearchFile "$searchFileName" "$searchStr"
        Dummy "$searchFileName" "$searchStr"
        #exit    #debug
    else
        printf "%s" "
ERROR: A file registered for search does not exist
       File: $searchFileName
"
    fi
done
unset IFS



# ----------------------------------------
# ----------------------------------------
  exit	# Without this, the comment section will execute and error out.
# ----------------------------------------
# ----------------------------------------

------------------------------------------------------------
 2018-06-20
 Version 5.0
 Compatible with CONREC version 4.0
------------------------------------------------------------
Major refactor
- Search for the contact in a file list.
- Remove the file_name option

------------------------------------------------------------
 2018-06-07
 Version 4.1
 Compatible with CONREC version 4.0
------------------------------------------------------------
Changed progVersion to 4.1

The records were not being displayed properly.
- Some fields were not being displayed.
- There were errors in the parsing.

Changed variable name for better clarity.
- recordID --> recordVer
- Intended to display the version of the record found.

Updated the debug output for the new variable name.

Updated the user output for the new variable name.

Added recordID to the debug output

Added roleStr to the record parsing
- Was blank in the debug output
- Was included as part of the remainingStr

Added recordCount to count the number of records found.

Added the progName variable.
- Added to debug output
- Added to user output


# ----------------------------------------------------------------------
# 2018-06-19
# Version 5.0
# Compatible with CONREC version 4.0
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 2018-04-20
# Version 4.0
# Compatible with CONREC version 4.0
# ----------------------------------------------------------------------
Note: There was no version 3.0 of this script. Trying to keep the record
script and this script versions in sync. Maybe it's useful?

Ver 4.0 CONREC record changed. Moved ver. Added a role.
- Change the parsing to be consistent with 4.0

 ---------------------------------------- contact  v4.1 -----
   Name ........ Rick Harper
   Phone ....... 781.997.5257
   email ....... RHarper@grgc.com
     Note ...... Boston. Gem recruiter.
     Org ....... Gardner Resources Consulting
     Created ... 2018-06-07                Record Ver: 4.0
 ------------------------------------------------------------

# ----------------------------------------------------------------------
# 2018-04-19
# Version 2.0
# Compatible with CONREC version 3.0
# ----------------------------------------------------------------------
- If the file name is not supplied, use a default search file.
    Default = cPrime.txt in the cPrime directory
- Much more error checking on input parameters
- Write the ProgUsage function, a syntax description
- When there is an entry at the end of the line, treat it as a note. If the
  value is set, ouput it as a "Note" field

"contact dane" produces this output":

 ------------------------------------------------- v2.0 -----
   Name ........ Dane Jessen
   Phone ....... 509.230.2877
   email ....... dane@rainincubator.org
     Note ........ Chief Operations Officer
     Org ......... RAIN Incubator
     Created ..... 2018-04-17                CONREC 3.0
 ------------------------------------------------------------


# ----------------------------------------------------------------------
# 2018-04-17
# Version 1.0
# Compatible with CONREC version 3.0
# ----------------------------------------------------------------------
"contact dane < cPrime.txt" produces this output:

 -------------------------------------------------- 1.0 -----
   Name ........ Dane Jessen
   Phone ....... 509.230.2877
   email ....... dane@rainincubator.org
     Org ......... RAIN Incubator
     Created ..... 2018-04-17                CONREC 3.0
 ------------------------------------------------------------

