project(test_OpenVolumeMesh)
cmake_minimum_required(VERSION 3.2)
set(CMAKE_CXX_STANDARD 11)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_define_targets()


add_executable(package_test test.cpp)
target_link_libraries(package_test CONAN_PKG::OpenVolumeMesh)


