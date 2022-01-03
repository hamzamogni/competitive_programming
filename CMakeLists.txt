cmake_minimum_required(VERSION 3.17)
project(stuff)

set(CMAKE_CXX_STANDARD 14)

add_executable(stuff
        main.cpp
        dna_subset/dna_subset.cpp dna_subset/dna_subset.h
        sum_of_left_leaves/sumOfLeftLeaves.cpp sum_of_left_leaves/sumOfLeftLeaves.h
        missing_number/missingNumber.cpp missing_number/missingNumber.h
        add_two_numbers/add_two_numbers.cpp add_two_numbers/add_two_numbers.h
        palindrome_number/palindromeNumber.h palindrome_number/palindromeNumber.cpp

)
