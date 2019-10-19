from conans import ConanFile, tools
from conans.tools import os_info, SystemPackageTool
import os


class Sol2Conan(ConanFile):
    name = "sol2"
    version = "2.20.6"
    description = "sol is a C++ library binding to Lua. It currently supports all Lua versions 5.1+ (LuaJIT 2.x "\
                  "included). sol aims to be easy to use and easy to add to a project. The library is header-only for "\
                  "easy integration with projects."
    topics = ("conan", "lua")
    url = "https://github.com/jinntechio/conan-sol2"
    homepage = "https://github.com/ThePhD/sol2"
    license = "MIT"
    no_copy_source = True

    _source_subfolder = "source_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "single/sol")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()

    def system_requirements(self):
        pack_name = None
        if os_info.linux_distro == "ubuntu":
            if os_info.os_version > "12":
                pack_name = "lua5.3 liblua5.3-dev"
            else:
                pack_name = "lua5.3 liblua5.3-dev"
        # elif os_info.linux_distro == "fedora" or os_info.linux_distro == "centos":
        #    pack_name = "package_name_in_fedora_and_centos"
        elif os_info.is_macos:
            pack_name = ["lua"]
        # elif os_info.is_freebsd:
        #    pack_name = "package_name_in_freebsd"
        # elif os_info.is_solaris:
        #    pack_name = "package_name_in_solaris"

        if pack_name:
            installer = SystemPackageTool()
            installer.install(pack_name)
