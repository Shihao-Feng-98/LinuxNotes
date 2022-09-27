cmake_minimum_required(VERSION 3.0) # 指明CMAKE最小版本要求

project(PROJECTNAME) # 定义工程名称

include_directories(${CMAKE_SOURCE_DIR}/include) # 向工程添加多个特定的头文件搜索路径

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall") # g++编译选项

set(CMAKE_BUILD_TYPE Debug) # 编译类型 Debug/Release

add_executable(main_cmake main.cpp src/source1.cpp src/source2.cpp) # 生成可执行文件
