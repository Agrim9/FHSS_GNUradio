INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_FHSS FHSS)

FIND_PATH(
    FHSS_INCLUDE_DIRS
    NAMES FHSS/api.h
    HINTS $ENV{FHSS_DIR}/include
        ${PC_FHSS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    FHSS_LIBRARIES
    NAMES gnuradio-FHSS
    HINTS $ENV{FHSS_DIR}/lib
        ${PC_FHSS_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(FHSS DEFAULT_MSG FHSS_LIBRARIES FHSS_INCLUDE_DIRS)
MARK_AS_ADVANCED(FHSS_LIBRARIES FHSS_INCLUDE_DIRS)

