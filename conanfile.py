
from conans import ConanFile, CMake, tools
import os

class OpenvolumemeshConan(ConanFile):
    name = "OpenVolumeMesh"
    version = "2.0.0"
    license = "LGPL-3.0"
    url = "https://github.com/weatherhead99/OpenVolumeMesh-conan"
    description = "A Generic and Versatile Index-Based Data Structure for Polytopal Meshes"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://www.graphics.rwth-aachen.de:9000/OpenVolumeMesh/OpenVolumeMesh.git")
        self.run("cd OpenVolumeMesh && git checkout v%s" % self.version)

    def build(self):
        cmake = CMake(self)
        os.mkdir("./build")
        os.chdir("build")
        self.run('cmake ../OpenVolumeMesh %s' % cmake.command_line)
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        inc_srcdir = "OpenVolumeMesh/src/OpenVolumeMesh/"
        self.copy("*.hh",dst="include/OpenVolumeMesh",src=inc_srcdir)
        self.copy("*T.cc",dst="include/OpenVolumeMesh",src=inc_srcdir)
                
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs=["include"]
        self.cpp_info.libdirs=["lib"]
        if not self.options.shared:
            self.cpp_info.libs=["libOpenVolumeMeshStatic.a"]
        else:
            self.cpp_info.libs=["libOpenVolumeMesh.so"]