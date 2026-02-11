#! /bin/bash

verStr="4.0"

noteStr=$*
if [[ -z $noteStr ]]; then
	noteStr="DESC"
else
	noteStr=`printf "%q" "$noteStr"`
	noteStr=$(printf "%q" "$noteStr" | sed "s/\\\\//g")
fi


dayStr=$(date "+%a")
dateStr=$(date "+%Y-%m-%d")
timeStr=$(date "+%H:%M:%S")

#printf "TS::$dayStr::$dateStr::$timeStr::$verStr::$noteStr::\n"
printf  "# ------------------------------------------------------------\n"
printf "TS::$verStr::$dayStr::$dateStr::$timeStr::"
printf "$noteStr"
printf "::\n"


# --------------------
# Ver 4.0
# --------------------
# Moved the version value to the 2nd token in the string.
# Added a 60 char dash line, followed by the TS:: record.
# ------------------------------------------------------------
# TS::4.0::Thu::2018-04-05::12:56:14::DESC::

# --------------------
# Ver 3.0
# --------------------
# Added new parameter processing that allows special characters in the
# string.
# TS::Fri::2014-09-05::16:09:43::3.0::DESC::

# --------------------
# Ver 2.0
# --------------------
# Did not record the changes.
# TS::Fri::2014-09-05::11:02:36::2.0::DESC::

