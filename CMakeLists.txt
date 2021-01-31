cmake_minimum_required(VERSION 3.17)
project(stuff)

set(CMAKE_CXX_STANDARD 14)

add_executable(stuff
        main.cpp
#        dna_subset/dna_subset.cpp dna_subset/dna_subset.h
        sum_of_left_leaves/sumOfLeftLeaves.cpp sum_of_left_leaves/sumOfLeftLeaves.h)
