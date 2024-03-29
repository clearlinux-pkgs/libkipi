#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: da8b975
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkipi
Version  : 23.08.5
Release  : 65
URL      : https://download.kde.org/stable/release-service/23.08.5/src/libkipi-23.08.5.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.5/src/libkipi-23.08.5.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.5/src/libkipi-23.08.5.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: libkipi-data = %{version}-%{release}
Requires: libkipi-lib = %{version}-%{release}
Requires: libkipi-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libjpeg-turbo-dev
BuildRequires : libkexiv2-dev
BuildRequires : libpng-dev
BuildRequires : tiff-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
KIPI Library (KDE Image Program Interface)
-- AUTHORS ------------------------------------------------------------

%package data
Summary: data components for the libkipi package.
Group: Data

%description data
data components for the libkipi package.


%package dev
Summary: dev components for the libkipi package.
Group: Development
Requires: libkipi-lib = %{version}-%{release}
Requires: libkipi-data = %{version}-%{release}
Provides: libkipi-devel = %{version}-%{release}
Requires: libkipi = %{version}-%{release}

%description dev
dev components for the libkipi package.


%package lib
Summary: lib components for the libkipi package.
Group: Libraries
Requires: libkipi-data = %{version}-%{release}
Requires: libkipi-license = %{version}-%{release}

%description lib
lib components for the libkipi package.


%package license
Summary: license components for the libkipi package.
Group: Default

%description license
license components for the libkipi package.


%prep
%setup -q -n libkipi-23.08.5
cd %{_builddir}/libkipi-23.08.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1708374880
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DBUILD_TESTING=OFF
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DBUILD_TESTING=OFF
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1708374880
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkipi
cp %{_builddir}/libkipi-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libkipi/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libkipi-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkipi/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/128x128/apps/kipi.png
/usr/share/icons/hicolor/16x16/apps/kipi.png
/usr/share/icons/hicolor/22x22/apps/kipi.png
/usr/share/icons/hicolor/32x32/apps/kipi.png
/usr/share/icons/hicolor/48x48/apps/kipi.png
/usr/share/kservicetypes5/kipiplugin.desktop
/usr/share/qlogging-categories5/kipi.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KIPI/KIPI/ConfigWidget
/usr/include/KF5/KIPI/KIPI/ImageCollection
/usr/include/KF5/KIPI/KIPI/ImageCollectionSelector
/usr/include/KF5/KIPI/KIPI/ImageCollectionShared
/usr/include/KF5/KIPI/KIPI/ImageInfo
/usr/include/KF5/KIPI/KIPI/ImageInfoShared
/usr/include/KF5/KIPI/KIPI/Interface
/usr/include/KF5/KIPI/KIPI/Plugin
/usr/include/KF5/KIPI/KIPI/PluginLoader
/usr/include/KF5/KIPI/KIPI/UploadWidget
/usr/include/KF5/KIPI/kipi/configwidget.h
/usr/include/KF5/KIPI/kipi/imagecollection.h
/usr/include/KF5/KIPI/kipi/imagecollectionselector.h
/usr/include/KF5/KIPI/kipi/imagecollectionshared.h
/usr/include/KF5/KIPI/kipi/imageinfo.h
/usr/include/KF5/KIPI/kipi/imageinfoshared.h
/usr/include/KF5/KIPI/kipi/interface.h
/usr/include/KF5/KIPI/kipi/libkipi_config.h
/usr/include/KF5/KIPI/kipi/libkipi_export.h
/usr/include/KF5/KIPI/kipi/plugin.h
/usr/include/KF5/KIPI/kipi/pluginloader.h
/usr/include/KF5/KIPI/kipi/uploadwidget.h
/usr/include/KF5/KIPI/libkipi_version.h
/usr/lib64/cmake/KF5Kipi/KF5KipiConfig.cmake
/usr/lib64/cmake/KF5Kipi/KF5KipiConfigVersion.cmake
/usr/lib64/cmake/KF5Kipi/KF5KipiTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Kipi/KF5KipiTargets.cmake
/usr/lib64/libKF5Kipi.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5Kipi.so.5.2.0
/usr/lib64/libKF5Kipi.so.32.0.0
/usr/lib64/libKF5Kipi.so.5.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkipi/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/libkipi/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
