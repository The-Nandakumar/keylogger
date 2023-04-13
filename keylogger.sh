#!/bin/bash

while true; do
	read -rsn1 input
	if [[ $input = [a-zA-Z] ]]; then
		echo -n $input >> keys.txt
	fi
done