#!/bin/bash
#13-04-2023

while true; do
	read -rsn1 input
	if [[ $input = [a-zA-Z] ]]; then
		echo -n $input >> keys.txt
	fi
done
