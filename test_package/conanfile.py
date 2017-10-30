from conans import ConanFile, CMake, tools
import os
import shutil

class OpenVolumeMeshTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators="cmake"
    
    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self.conanfile_directory, build_dir=".")
        cmake.build()
        
    def test(self):
        self.run(".%spackage_test" % os.sep)            
    
        
        
    
