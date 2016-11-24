INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_DEMOD_8 demod_8)

FIND_PATH(
    DEMOD_8_INCLUDE_DIRS
    NAMES demod_8/api.h
    HINTS $ENV{DEMOD_8_DIR}/include
        ${PC_DEMOD_8_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    DEMOD_8_LIBRARIES
    NAMES gnuradio-demod_8
    HINTS $ENV{DEMOD_8_DIR}/lib
        ${PC_DEMOD_8_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(DEMOD_8 DEFAULT_MSG DEMOD_8_LIBRARIES DEMOD_8_INCLUDE_DIRS)
MARK_AS_ADVANCED(DEMOD_8_LIBRARIES DEMOD_8_INCLUDE_DIRS)

