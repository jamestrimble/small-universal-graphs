/Graph/ {
    linenumber = 1;
    next;
}

linenumber == 1 {
    n = $1
    m = $2
    print "p edge", n, m
    linenumber += 1;
    next;
}

linenumber > 1 {
    for (i=1; i<NF; i+=2) {
        print "e", ($i + 1), ($(i+1) + 1)
    }
    linenumber += 1;
}
