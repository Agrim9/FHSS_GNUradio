INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_MOD_64 mod_64)

FIND_PATH(
    MOD_64_INCLUDE_DIRS
    NAMES mod_64/api.h
    HINTS $ENV{MOD_64_DIR}/include
        ${PC_MOD_64_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    MOD_64_LIBRARIES
    NAMES gnuradio-mod_64
    HINTS $ENV{MOD_64_DIR}/lib
        ${PC_MOD_64_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(MOD_64 DEFAULT_MSG MOD_64_LIBRARIES MOD_64_INCLUDE_DIRS)
MARK_AS_ADVANCED(MOD_64_LIBRARIES MOD_64_INCLUDE_DIRS)

