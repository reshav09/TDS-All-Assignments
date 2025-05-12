#!/bin/bash

# Create 20 directories named "Question 1" to "Question 20"
for i in {1..20}
do
  dir_name="Question $i"
  mkdir -p "$dir_name"  # -p avoids error if dir already exists
  echo "Created directory: $dir_name"
done

