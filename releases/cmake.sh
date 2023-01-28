#!/bin/bash
read -p "Create programming in currently path: " PROJECT

mkdir $PROJECT \
	$PROJECT/include \
	$PROJECT/source	\
	$PROJECT/resource \
	$PROJECT/build \
	$PROJECT/document \
	$PROJECT/third_party

touch $PROJECT/main.c \
	$PROJECT/README.MD \
	$PROJECT/LICENSE \
	$PROJECT/CMakeLists.txt \
	$PROJECT/include/CMakeLists.txt \
	$PROJECT/source/CMakeLists.txt \
	$PROJECT/resource/CMakeLists.txt \
	$PROJECT/third_party/CMakeLists.txt

CMAKELISTS=$PROJECT/CMakeLists.txt
cat>$CMAKELISTS<<EOF
# HOST CMakeLists.txt
cmake_minimum_required(VERSION 3.16)
include(CMakePrintHelpers)
include(CheckCCompilerFlag)
project($PROJECT VERSION 1.0)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_C_STANDARD 99)
add_subdirectory(include)
add_executable($PROJECT main.c)
target_link_libraries($PROJECT INTERFACE include)
check_c_compiler_flag(-std=gnu99 FLAG_STD_C99)
if(FLAG_STD_C99)
	message("-- The Completion has been done")
	message("-- The Completion has been done - Success")
else()
	message("-- The Completion hasn't been done")
	message("-- The Completion hasn't been done - Fail")
endif()
cmake_print_variables(CMAKE_C_COMPILER)
EOF

CMAKELISTS_INC=$PROJECT/include/CMakeLists.txt
cat>$CMAKELISTS_INC<<EOF
cmake_minimum_required(VERSION 3.16)
project(include)
add_library(include INTERFACE)
target_link_libraries(include INTERFACE ${PROJECT_SOURCE_DIR})
EOF

PATH=$(pwd)
echo "Currently path: $PATH/$PROJECT"
