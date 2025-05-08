cmake_minimum_required(VERSION 3.10)
project(BankAccount)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include directories
include_directories(${CMAKE_SOURCE_DIR}/include)

# Main executable
add_executable(bank_account
        src/main.cpp
        src/Account.cpp
)

# Shared library for Python testing
add_library(account_shared SHARED
        src/Account.cpp
)

# Set output name for the shared library
set_target_properties(account_shared PROPERTIES
        OUTPUT_NAME "account"
        PREFIX ""
        SUFFIX ".so"
)

# Find Python executable
find_program(PYTHON_EXECUTABLE python)
if(NOT PYTHON_EXECUTABLE)
    message(FATAL_ERROR "Python not found. Please install Python.")
endif()

# Custom target to run pytest
add_custom_target(run_pytest
        COMMAND ${PYTHON_EXECUTABLE} -m pytest ${CMAKE_SOURCE_DIR}/tests/test_account.py -v
        DEPENDS account_shared
        WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
        COMMENT "Running Python tests with pytest"
)

# Make pytest run after building the main target
add_dependencies(bank_account run_pytest)

# Enable testing for ctest (optional, for manual test runs)
enable_testing()
add_test(
        NAME PythonTests
        COMMAND ${PYTHON_EXECUTABLE} -m pytest ${CMAKE_SOURCE_DIR}/tests/test_account.py -v
)