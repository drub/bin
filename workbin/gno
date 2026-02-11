#! /bin/bash

# ----------------------------------------
# Constants
# ----------------------------------------
readonly verStr="1.1"
readonly uninitialized="UNINITIALIZED"

# ----------------------------------------------------------------------
# MAIN Main main
# ----------------------------------------------------------------------

#echo "0 ........................ $0"	#debug
#echo "1 ........................ $1"	#debug
#echo "clientStr ................ $clientStr"	#debug

if [[ -z $1 ]]; then
	inputStr=GUIDANCE
else
	inputStr=$*   #! Remainder of the command line
	#echo "0 ........................ $0"	#debug
	#echo "1 ........................ $1"	#debug
	#echo "verStr ................... $verStr"	#debug
	#echo "inputStr ................. $inputStr"	#debug

fi

dayStr=$(date "+%a")
dateStr=$(date "+%Y-%m-%d")
timeStr=$(date "+%H.%M.%S")

	#echo "<remainder> .............. $*"	#debug

printf "%s\n" "GNO::$verStr::$dateStr::$inputStr::"

# ----------------------------------------------------------------------
# END End end
# ----------------------------------------------------------------------
  exit  #! So the rest of the file is not executed
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


----------------------------------------
 Description
----------------------------------------
Create a record for Guidance Not Observed (GNO)
- Guidance is frequently offered. Record when guidance is not observed.
  Best if the item is something regularly not observed. No need to nitpick.

----------------------------------------


----------------------------------------
 History
----------------------------------------

----------------------------------------
v1.1 - Add a trailing field to the record.
       That is the "other", or "notes" field. It is free form.
GNO::1.1::2018-07-18::GUIDANCE::

----------------------------------------
v1.0 - Initial version
       Record when guidance is not observed.
----------------------------------------
GNO::1.0::2018-07-11::GUIDANCE

