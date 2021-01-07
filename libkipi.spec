#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : libkipi
Version  : 20.12.1
Release  : 29
URL      : https://download.kde.org/stable/release-service/20.12.1/src/libkipi-20.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.12.1/src/libkipi-20.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.12.1/src/libkipi-20.12.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.1
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
%setup -q -n libkipi-20.12.1
cd %{_builddir}/libkipi-20.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610055003
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DBUILD_TESTING=OFF
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1610055003
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkipi
cp %{_builddir}/libkipi-20.12.1/COPYING %{buildroot}/usr/share/package-licenses/libkipi/075bb44a94e785a073154a32aa32554587f330f2
cp %{_builddir}/libkipi-20.12.1/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libkipi/ff3ed70db4739b3c6747c7f624fe2bad70802987
cp %{_builddir}/libkipi-20.12.1/COPYING.LIB %{buildroot}/usr/share/package-licenses/libkipi/1568befcb09e881d29dd760911ceeb4e2d810884
pushd clr-build
%make_install
popd

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
/usr/include/KF5/libkipi_version.h
/usr/lib64/cmake/KF5Kipi/KF5KipiConfig.cmake
/usr/lib64/cmake/KF5Kipi/KF5KipiConfigVersion.cmake
/usr/lib64/cmake/KF5Kipi/KF5KipiTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Kipi/KF5KipiTargets.cmake
/usr/lib64/libKF5Kipi.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Kipi.so.32.0.0
/usr/lib64/libKF5Kipi.so.5.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkipi/075bb44a94e785a073154a32aa32554587f330f2
/usr/share/package-licenses/libkipi/1568befcb09e881d29dd760911ceeb4e2d810884
/usr/share/package-licenses/libkipi/ff3ed70db4739b3c6747c7f624fe2bad70802987
