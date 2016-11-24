INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_MOD_8 mod_8)

FIND_PATH(
    MOD_8_INCLUDE_DIRS
    NAMES mod_8/api.h
    HINTS $ENV{MOD_8_DIR}/include
        ${PC_MOD_8_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    MOD_8_LIBRARIES
    NAMES gnuradio-mod_8
    HINTS $ENV{MOD_8_DIR}/lib
        ${PC_MOD_8_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(MOD_8 DEFAULT_MSG MOD_8_LIBRARIES MOD_8_INCLUDE_DIRS)
MARK_AS_ADVANCED(MOD_8_LIBRARIES MOD_8_INCLUDE_DIRS)

