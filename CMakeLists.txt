cmake_minimum_required(VERSION 3.16)
project(wordscope_native VERSION 1.0.0 LANGUAGES CXX)

add_library(wordscope_native SHARED
    native/src/text_stats.cpp
    native/src/bindings.cpp
)

target_include_directories(wordscope_native
    PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/native/include
)

target_compile_features(wordscope_native PRIVATE cxx_std_17)
set_target_properties(wordscope_native PROPERTIES
    CXX_VISIBILITY_PRESET hidden
    VISIBILITY_INLINES_HIDDEN YES
    OUTPUT_NAME "wordscope_native"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)

if(MSVC)
    target_compile_options(wordscope_native PRIVATE /W4 /permissive-)
else()
    target_compile_options(wordscope_native PRIVATE -Wall -Wextra -Wpedantic)
endif()

foreach(config Debug Release RelWithDebInfo MinSizeRel)
    string(TOUPPER "${config}" config_upper)
    set_target_properties(wordscope_native PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY_${config_upper} "${CMAKE_BINARY_DIR}"
        LIBRARY_OUTPUT_DIRECTORY_${config_upper} "${CMAKE_BINARY_DIR}"
    )
endforeach()
