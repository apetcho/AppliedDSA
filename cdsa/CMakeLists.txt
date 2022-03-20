cmake_minimum_required(VERSION 3.17)
project(cdsa LANGUAGES C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED TRUE)

add_executable(cdsatuto
    src/main.c
    src/llist.c
    src/llist.h
)
