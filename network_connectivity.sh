#!/bin/bash

echo "Select number for ping test"
echo "1. google.com"
echo "2. yahoo.com"
echo "3. jabil.com"

read input

file_name="$(date +%F)_$(date +%T).log"
touch $file_name

if [ $input == 1 ]
then
  ping -n 1 google.com >> $file_name
  if [ $? -eq 0 ]
  then
    echo "ping sucess"
    mv $file_name "pass_$file_name"
  else
    echo "ping fail"
    mv $file_name "fail_$file_name"
  fi
elif [ $input == 2 ]
then
  ping -n 1 yahoo.com >> $file_name
  if [ $? -eq 0 ]
  then
    echo "ping sucess"
    mv $file_name "pass_$file_name"
  else
    echo "ping fail"
    mv $file_name "fail_$file_name"
  fi
elif [ $input == 3 ]
then
  ping -n 1 jabil.com >> $file_name
  if [ $? -eq 0 ]
  then
    echo "ping sucess"
    mv $file_name "pass_$file_name" 
  else
    echo "ping fail"
    mv $file_name "fail_$file_name"
  fi
fi


