NR == 1 {
    print "p edge", NF, 0
}

{
    for (i=1; i<NR; i++) {
        if ($i == 1) {
            print "e", i, NR;
        }
    }
}
