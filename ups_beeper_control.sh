#!/bin/bash -e
# https://moshib.in/2019/02/08/disable-ups-beeper-synology.html
if [ "$1" == "curtime" ]
then
	echo "Using current time to set UPS beeper status"
	H=$(date "+%k")
	if (( "$H" >= 9 )) 
	then
		goal="enable"
	else
		goal="disable"
	fi
else
	goal=$1
fi

if [ "$goal" == "enable" ] || [ "$goal" == "disable" ]
then
	echo "$goal beeper..."
	python /root/upscmd.py beeper.${goal}
	echo "Waiting 5 seconds for UPS to update state..."
	sleep 5
	if [[ "$(upsc ups ups.beeper.status)" == "${goal}d" ]]
	then
		echo "Beeper ${goal}d."
	else
		echo "Unable to $goal beeper. Status = $(upsc ups ups.beeper.status)."
		exit 1
	fi
else
	echo "Unknown / unsupported argument: $1"
fi

