#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libadwaita
Version  : 1.0.2
Release  : 4
URL      : https://download.gnome.org/sources/libadwaita/1.0/libadwaita-1.0.2.tar.xz
Source0  : https://download.gnome.org/sources/libadwaita/1.0/libadwaita-1.0.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: libadwaita-bin = %{version}-%{release}
Requires: libadwaita-data = %{version}-%{release}
Requires: libadwaita-lib = %{version}-%{release}
Requires: libadwaita-license = %{version}-%{release}
Requires: libadwaita-locales = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : sassc

%description
# Adwaita
Building blocks for modern GNOME applications.
## License
Libadwaita is licensed under the LGPL-2.1+.

%package bin
Summary: bin components for the libadwaita package.
Group: Binaries
Requires: libadwaita-data = %{version}-%{release}
Requires: libadwaita-license = %{version}-%{release}

%description bin
bin components for the libadwaita package.


%package data
Summary: data components for the libadwaita package.
Group: Data

%description data
data components for the libadwaita package.


%package dev
Summary: dev components for the libadwaita package.
Group: Development
Requires: libadwaita-lib = %{version}-%{release}
Requires: libadwaita-bin = %{version}-%{release}
Requires: libadwaita-data = %{version}-%{release}
Provides: libadwaita-devel = %{version}-%{release}
Requires: libadwaita = %{version}-%{release}

%description dev
dev components for the libadwaita package.


%package lib
Summary: lib components for the libadwaita package.
Group: Libraries
Requires: libadwaita-data = %{version}-%{release}
Requires: libadwaita-license = %{version}-%{release}

%description lib
lib components for the libadwaita package.


%package license
Summary: license components for the libadwaita package.
Group: Default

%description license
license components for the libadwaita package.


%package locales
Summary: locales components for the libadwaita package.
Group: Default

%description locales
locales components for the libadwaita package.


%prep
%setup -q -n libadwaita-1.0.2
cd %{_builddir}/libadwaita-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1646093719
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libadwaita
cp %{_builddir}/libadwaita-1.0.2/COPYING %{buildroot}/usr/share/package-licenses/libadwaita/01a6b4bf79aca9b556822601186afab86e8c4fbf
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang libadwaita

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/adwaita-1-demo

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Adw-1.typelib
/usr/share/applications/org.gnome.Adwaita1.Demo.desktop
/usr/share/gir-1.0/*.gir
/usr/share/icons/hicolor/scalable/apps/org.gnome.Adwaita1.Demo.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Adwaita1.Demo-symbolic.svg
/usr/share/metainfo/org.gnome.Adwaita1.Demo.metainfo.xml
/usr/share/vala/vapi/libadwaita-1.deps
/usr/share/vala/vapi/libadwaita-1.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libadwaita-1/adw-action-row.h
/usr/include/libadwaita-1/adw-animation-target.h
/usr/include/libadwaita-1/adw-animation-util.h
/usr/include/libadwaita-1/adw-animation.h
/usr/include/libadwaita-1/adw-application-window.h
/usr/include/libadwaita-1/adw-application.h
/usr/include/libadwaita-1/adw-avatar.h
/usr/include/libadwaita-1/adw-bin.h
/usr/include/libadwaita-1/adw-button-content.h
/usr/include/libadwaita-1/adw-carousel-indicator-dots.h
/usr/include/libadwaita-1/adw-carousel-indicator-lines.h
/usr/include/libadwaita-1/adw-carousel.h
/usr/include/libadwaita-1/adw-clamp-layout.h
/usr/include/libadwaita-1/adw-clamp-scrollable.h
/usr/include/libadwaita-1/adw-clamp.h
/usr/include/libadwaita-1/adw-combo-row.h
/usr/include/libadwaita-1/adw-deprecation-macros.h
/usr/include/libadwaita-1/adw-easing.h
/usr/include/libadwaita-1/adw-enum-list-model.h
/usr/include/libadwaita-1/adw-enums.h
/usr/include/libadwaita-1/adw-expander-row.h
/usr/include/libadwaita-1/adw-flap.h
/usr/include/libadwaita-1/adw-fold-threshold-policy.h
/usr/include/libadwaita-1/adw-header-bar.h
/usr/include/libadwaita-1/adw-leaflet.h
/usr/include/libadwaita-1/adw-main.h
/usr/include/libadwaita-1/adw-navigation-direction.h
/usr/include/libadwaita-1/adw-preferences-group.h
/usr/include/libadwaita-1/adw-preferences-page.h
/usr/include/libadwaita-1/adw-preferences-row.h
/usr/include/libadwaita-1/adw-preferences-window.h
/usr/include/libadwaita-1/adw-split-button.h
/usr/include/libadwaita-1/adw-spring-animation.h
/usr/include/libadwaita-1/adw-spring-params.h
/usr/include/libadwaita-1/adw-squeezer.h
/usr/include/libadwaita-1/adw-status-page.h
/usr/include/libadwaita-1/adw-style-manager.h
/usr/include/libadwaita-1/adw-swipe-tracker.h
/usr/include/libadwaita-1/adw-swipeable.h
/usr/include/libadwaita-1/adw-tab-bar.h
/usr/include/libadwaita-1/adw-tab-view.h
/usr/include/libadwaita-1/adw-timed-animation.h
/usr/include/libadwaita-1/adw-toast-overlay.h
/usr/include/libadwaita-1/adw-toast.h
/usr/include/libadwaita-1/adw-version.h
/usr/include/libadwaita-1/adw-view-stack.h
/usr/include/libadwaita-1/adw-view-switcher-bar.h
/usr/include/libadwaita-1/adw-view-switcher-title.h
/usr/include/libadwaita-1/adw-view-switcher.h
/usr/include/libadwaita-1/adw-window-title.h
/usr/include/libadwaita-1/adw-window.h
/usr/include/libadwaita-1/adwaita.h
/usr/lib64/libadwaita-1.so
/usr/lib64/pkgconfig/libadwaita-1.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libadwaita-1.so.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libadwaita/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files locales -f libadwaita.lang
%defattr(-,root,root,-)

