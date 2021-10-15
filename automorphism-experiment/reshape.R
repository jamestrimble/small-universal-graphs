library(tidyverse)

for (type in c("graph", "sample-of-graphs")) {
    autom <- read.delim(paste0("results-of-second-experiment_automorphisms_", type, ".txt"), header=FALSE, col.names=c("calls", "X"), sep=" ")$calls
    degree <- read.delim(paste0("results-of-second-experiment_degree_", type, ".txt"), header=FALSE, col.names=c("calls", "X"), sep=" ")$calls
    almost_random <- read.delim(paste0("results-of-second-experiment_almost-random_", type, ".txt"), header=FALSE, col.names=c("calls", "X"), sep=" ")$calls
    r <- read.delim(paste0("results-of-second-experiment_random_", type, ".txt"), header=FALSE, col.names=c("calls", "X"), sep=" ")$calls

    d <- data.frame(autom, degree, almost_random, r)

    e <- d %>%
        pivot_longer(everything(), names_to = "method", values_to = "calls")

    e$methodnum <- match(e$method, c("autom", "degree", "almost_random", "r"))
    e$jittered_methodnum <- e$methodnum + runif(nrow(e), -.0, .0)
    write.table(e, paste0("results-of-second-experiment_", type, ".tsv"), sep="\t", row.names=FALSE, quote=FALSE)

    f <- e %>%
        group_by(methodnum) %>%
        summarise(mean=mean(calls))
    write.table(f, paste0("results-of-second-experiment-summary_", type, ".tsv"), sep="\t", row.names=FALSE, quote=FALSE)
}
