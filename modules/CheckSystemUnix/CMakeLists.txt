cmake_minimum_required(VERSION 3.10)

set(TARGET CheckSystemUnix)

project(${TARGET})

create_module(SRCS ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR})

set(SRCS
    ${SRCS}
    CheckSystem.cpp
    filter.cpp
    ${NSCP_DEF_PLUGIN_CPP}
    ${NSCP_FILTER_CPP}
    realtime_thread.cpp
    realtime_data.cpp
    filter_config_object.cpp)

add_definitions(${NSCP_GLOBAL_DEFINES})

if(WIN32)
  set(SRCS
      ${SRCS}
      CheckSystem.h
      filter.hpp
      realtime_thread.hpp
      realtime_data.hpp
      filter_config_object.hpp
      ${NSCP_DEF_PLUGIN_HPP}
      ${NSCP_FILTER_HPP})
endif(WIN32)

add_library(${TARGET} MODULE ${SRCS})
nscp_debug_symbols(${TARGET})

target_link_libraries(
  ${TARGET}
  ${Boost_FILESYSTEM_LIBRARY}
  ${Boost_REGEX_LIBRARY}
  ${Boost_THREAD_LIBRARY}
  ${Boost_PROGRAM_OPTIONS_LIBRARY}
  ${NSCP_DEF_PLUGIN_LIB}
  ${NSCP_FILTER_LIB}
  expression_parser)
include(${BUILD_CMAKE_FOLDER}/module.cmake)
