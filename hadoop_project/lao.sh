#!/bin/bash
# Task 1. Script that uploads the file lao.txt to the
# /holbies/input directory
hdfs dfs -copyFromLocal lao.txt /holbies/input
# hdfs dfs -mv lao.txt /holbies/input
