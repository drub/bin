#! /bin/bash

noteStr=$*
if [[ -z $noteStr ]]; then
	noteStr="COMPANY"
fi

verStr="1.2"

dayStr=$(date "+%a")
dateStr=$(date "+%Y-%m-%d")
timeStr=$(date "+%H:%M:%S")

printf "App::$dateStr::$timeStr::$verStr::"
printf "$noteStr"
printf "::POSITION::RESUME_VER"
printf "::\n"

#App::2014-08-11::09:29:09::1.0::
#App::2014-08-11::09:36:23::1.1::COMPANY::POSITION::RESUME VER::
#App::2014-08-18::13:21:35::1.2::COMPANY::POSITION::RESUME_VER::
