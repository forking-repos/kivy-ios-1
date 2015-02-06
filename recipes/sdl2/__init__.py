
from toolchain import Recipe, shprint
from os.path import join, exists
import sh
import shutil


class LibSDL2Recipe(Recipe):
    version = "2.0.3"
    url = "https://www.libsdl.org/release/SDL2-{version}.tar.gz"
    library = "Xcode-iOS/SDL/build/Release-{arch.sdk}/libSDL2.a"
    include_dir = "include"

    def build_arch(self, arch):
        shprint(sh.xcodebuild,
                "ONLY_ACTIVE_ARCH=NO",
                "ARCHS={}".format(arch.arch),
                "-sdk", arch.sdk,
                "-project", "Xcode-iOS/SDL/SDL.xcodeproj",
                "-target", "libSDL",
                "-configuration", "Release")


recipe = LibSDL2Recipe()

