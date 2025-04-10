#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : libadwaita
Version  : 1.7.0
Release  : 42
URL      : https://download.gnome.org/sources/libadwaita/1.7/libadwaita-1.7.0.tar.xz
Source0  : https://download.gnome.org/sources/libadwaita/1.7/libadwaita-1.7.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: libadwaita-bin = %{version}-%{release}
Requires: libadwaita-data = %{version}-%{release}
Requires: libadwaita-lib = %{version}-%{release}
Requires: libadwaita-license = %{version}-%{release}
Requires: libadwaita-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(appstream)
BuildRequires : pkgconfig(gtk4)
BuildRequires : sassc
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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


%package staticdev
Summary: staticdev components for the libadwaita package.
Group: Default
Requires: libadwaita-dev = %{version}-%{release}

%description staticdev
staticdev components for the libadwaita package.


%prep
%setup -q -n libadwaita-1.7.0
cd %{_builddir}/libadwaita-1.7.0
pushd ..
cp -a libadwaita-1.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742858723
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
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :
cd ../buildavx2;
meson test -C builddir --print-errorlogs || : || :

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
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/libadwaita
cp %{_builddir}/libadwaita-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libadwaita/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang libadwaita
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/adwaita-1-demo
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
/usr/include/libadwaita-1/adw-about-dialog.h
/usr/include/libadwaita-1/adw-about-window.h
/usr/include/libadwaita-1/adw-accent-color.h
/usr/include/libadwaita-1/adw-action-row.h
/usr/include/libadwaita-1/adw-alert-dialog.h
/usr/include/libadwaita-1/adw-animation-target.h
/usr/include/libadwaita-1/adw-animation-util.h
/usr/include/libadwaita-1/adw-animation.h
/usr/include/libadwaita-1/adw-application-window.h
/usr/include/libadwaita-1/adw-application.h
/usr/include/libadwaita-1/adw-avatar.h
/usr/include/libadwaita-1/adw-banner.h
/usr/include/libadwaita-1/adw-bin.h
/usr/include/libadwaita-1/adw-bottom-sheet.h
/usr/include/libadwaita-1/adw-breakpoint-bin.h
/usr/include/libadwaita-1/adw-breakpoint.h
/usr/include/libadwaita-1/adw-button-content.h
/usr/include/libadwaita-1/adw-button-row.h
/usr/include/libadwaita-1/adw-carousel-indicator-dots.h
/usr/include/libadwaita-1/adw-carousel-indicator-lines.h
/usr/include/libadwaita-1/adw-carousel.h
/usr/include/libadwaita-1/adw-clamp-layout.h
/usr/include/libadwaita-1/adw-clamp-scrollable.h
/usr/include/libadwaita-1/adw-clamp.h
/usr/include/libadwaita-1/adw-combo-row.h
/usr/include/libadwaita-1/adw-dialog.h
/usr/include/libadwaita-1/adw-easing.h
/usr/include/libadwaita-1/adw-entry-row.h
/usr/include/libadwaita-1/adw-enum-list-model.h
/usr/include/libadwaita-1/adw-enums.h
/usr/include/libadwaita-1/adw-expander-row.h
/usr/include/libadwaita-1/adw-flap.h
/usr/include/libadwaita-1/adw-fold-threshold-policy.h
/usr/include/libadwaita-1/adw-header-bar.h
/usr/include/libadwaita-1/adw-inline-view-switcher.h
/usr/include/libadwaita-1/adw-layout-slot.h
/usr/include/libadwaita-1/adw-layout.h
/usr/include/libadwaita-1/adw-leaflet.h
/usr/include/libadwaita-1/adw-length-unit.h
/usr/include/libadwaita-1/adw-main.h
/usr/include/libadwaita-1/adw-message-dialog.h
/usr/include/libadwaita-1/adw-multi-layout-view.h
/usr/include/libadwaita-1/adw-navigation-direction.h
/usr/include/libadwaita-1/adw-navigation-split-view.h
/usr/include/libadwaita-1/adw-navigation-view.h
/usr/include/libadwaita-1/adw-overlay-split-view.h
/usr/include/libadwaita-1/adw-password-entry-row.h
/usr/include/libadwaita-1/adw-preferences-dialog.h
/usr/include/libadwaita-1/adw-preferences-group.h
/usr/include/libadwaita-1/adw-preferences-page.h
/usr/include/libadwaita-1/adw-preferences-row.h
/usr/include/libadwaita-1/adw-preferences-window.h
/usr/include/libadwaita-1/adw-spin-row.h
/usr/include/libadwaita-1/adw-spinner-paintable.h
/usr/include/libadwaita-1/adw-spinner.h
/usr/include/libadwaita-1/adw-split-button.h
/usr/include/libadwaita-1/adw-spring-animation.h
/usr/include/libadwaita-1/adw-spring-params.h
/usr/include/libadwaita-1/adw-squeezer.h
/usr/include/libadwaita-1/adw-status-page.h
/usr/include/libadwaita-1/adw-style-manager.h
/usr/include/libadwaita-1/adw-swipe-tracker.h
/usr/include/libadwaita-1/adw-swipeable.h
/usr/include/libadwaita-1/adw-switch-row.h
/usr/include/libadwaita-1/adw-tab-bar.h
/usr/include/libadwaita-1/adw-tab-button.h
/usr/include/libadwaita-1/adw-tab-overview.h
/usr/include/libadwaita-1/adw-tab-view.h
/usr/include/libadwaita-1/adw-timed-animation.h
/usr/include/libadwaita-1/adw-toast-overlay.h
/usr/include/libadwaita-1/adw-toast.h
/usr/include/libadwaita-1/adw-toggle-group.h
/usr/include/libadwaita-1/adw-toolbar-view.h
/usr/include/libadwaita-1/adw-version.h
/usr/include/libadwaita-1/adw-view-stack.h
/usr/include/libadwaita-1/adw-view-switcher-bar.h
/usr/include/libadwaita-1/adw-view-switcher-title.h
/usr/include/libadwaita-1/adw-view-switcher.h
/usr/include/libadwaita-1/adw-window-title.h
/usr/include/libadwaita-1/adw-window.h
/usr/include/libadwaita-1/adw-wrap-box.h
/usr/include/libadwaita-1/adw-wrap-layout.h
/usr/include/libadwaita-1/adwaita.h
/usr/lib64/libadwaita-1.so
/usr/lib64/pkgconfig/libadwaita-1.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libadwaita-1.so.0
/usr/lib64/libadwaita-1.so.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libadwaita/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libadwaita-1-internal.a

%files locales -f libadwaita.lang
%defattr(-,root,root,-)

