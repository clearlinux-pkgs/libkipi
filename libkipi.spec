#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : libkipi
Version  : 18.08.0
Release  : 1
URL      : https://download.kde.org/stable/applications/18.08.0/src/libkipi-18.08.0.tar.xz
Source0  : https://download.kde.org/stable/applications/18.08.0/src/libkipi-18.08.0.tar.xz
Source99 : https://download.kde.org/stable/applications/18.08.0/src/libkipi-18.08.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.1
Requires: libkipi-lib
Requires: libkipi-license
Requires: libkipi-data
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libjpeg-turbo-dev
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
Requires: libkipi-lib
Requires: libkipi-data
Provides: libkipi-devel

%description dev
dev components for the libkipi package.


%package lib
Summary: lib components for the libkipi package.
Group: Libraries
Requires: libkipi-data
Requires: libkipi-license

%description lib
lib components for the libkipi package.


%package license
Summary: license components for the libkipi package.
Group: Default

%description license
license components for the libkipi package.


%prep
%setup -q -n libkipi-18.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535236473
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535236473
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libkipi
cp COPYING %{buildroot}/usr/share/doc/libkipi/COPYING
cp COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/doc/libkipi/COPYING-CMAKE-SCRIPTS
cp COPYING.LIB %{buildroot}/usr/share/doc/libkipi/COPYING.LIB
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
/usr/share/kservices5/kipiplugin_kxmlhelloworld.desktop
/usr/share/kservicetypes5/kipiplugin.desktop
/usr/share/kxmlgui5/kipi/kipiplugin_kxmlhelloworldui.rc

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
/usr/lib64/qt5/plugins/kipiplugin_kxmlhelloworld.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/libkipi/COPYING
/usr/share/doc/libkipi/COPYING-CMAKE-SCRIPTS
/usr/share/doc/libkipi/COPYING.LIB
