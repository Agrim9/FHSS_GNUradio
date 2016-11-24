INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_DEMOD_64 demod_64)

FIND_PATH(
    DEMOD_64_INCLUDE_DIRS
    NAMES demod_64/api.h
    HINTS $ENV{DEMOD_64_DIR}/include
        ${PC_DEMOD_64_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    DEMOD_64_LIBRARIES
    NAMES gnuradio-demod_64
    HINTS $ENV{DEMOD_64_DIR}/lib
        ${PC_DEMOD_64_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(DEMOD_64 DEFAULT_MSG DEMOD_64_LIBRARIES DEMOD_64_INCLUDE_DIRS)
MARK_AS_ADVANCED(DEMOD_64_LIBRARIES DEMOD_64_INCLUDE_DIRS)

