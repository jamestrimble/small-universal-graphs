#!/bin/bash

cat ../exhaustive_tests.txt | grep -v 'graph 5' | grep -v 'tree 7' | while read a b c; do
    echo $a $b $c
#    ./check.sh $a $b $c | tee results/$a-$b-$c.txt
    diff results/$a-$b-$c.txt ../results/$a-$b-$c.txt
done
