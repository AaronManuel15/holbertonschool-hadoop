#!/bin/bash
# Task 1. Script that uploads the file lao.txt to the
# /holbies/input directory
hdfs dfs -copyFromLocal lao.txt /holbies/input

# Can use the following to create a file if there isn't one locally
# hdfs dfs -touch lao.txt /holbies/input
