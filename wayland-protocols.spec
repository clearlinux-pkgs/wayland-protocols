#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v24
# autospec commit: a88ffdc
#
# Source0 file verified with key 0xA6EEEC9E0136164A (jadahl@gmail.com)
#
Name     : wayland-protocols
Version  : 1.43
Release  : 50
URL      : https://gitlab.freedesktop.org/wayland/wayland-protocols/-/releases/1.43/downloads/wayland-protocols-1.43.tar.xz
Source0  : https://gitlab.freedesktop.org/wayland/wayland-protocols/-/releases/1.43/downloads/wayland-protocols-1.43.tar.xz
Source1  : https://gitlab.freedesktop.org/wayland/wayland-protocols/-/releases/1.43/downloads/wayland-protocols-1.43.tar.xz.sig
Source2  : A6EEEC9E0136164A.pkey
Summary  : Wayland protocol files
Group    : Development/Tools
License  : MIT
Requires: wayland-protocols-data = %{version}-%{release}
Requires: wayland-protocols-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gnupg
BuildRequires : wayland-dev
BuildRequires : wayland-dev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Xwayland keyboard grabbing protocol
Maintainers:
Olivier Fourdan <ofourdan@redhat.com> (@ofourdan)

%package data
Summary: data components for the wayland-protocols package.
Group: Data

%description data
data components for the wayland-protocols package.


%package dev
Summary: dev components for the wayland-protocols package.
Group: Development
Requires: wayland-protocols-data = %{version}-%{release}
Provides: wayland-protocols-devel = %{version}-%{release}
Requires: wayland-protocols = %{version}-%{release}

%description dev
dev components for the wayland-protocols package.


%package dev32
Summary: dev32 components for the wayland-protocols package.
Group: Default
Requires: wayland-protocols-data = %{version}-%{release}
Requires: wayland-protocols-dev = %{version}-%{release}

%description dev32
dev32 components for the wayland-protocols package.


%package license
Summary: license components for the wayland-protocols package.
Group: Default

%description license
license components for the wayland-protocols package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) A6EEEC9E0136164A' gpg.status
%setup -q -n wayland-protocols-1.43
cd %{_builddir}/wayland-protocols-1.43
pushd ..
cp -a wayland-protocols-1.43 build32
popd
pushd ..
cp -a wayland-protocols-1.43 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1744121263
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
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs
cd ../build32;
meson test -C builddir --print-errorlogs || :
cd ../buildavx2;
meson test -C builddir --print-errorlogs || :

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
mkdir -p %{buildroot}/usr/share/package-licenses/wayland-protocols
cp %{_builddir}/wayland-protocols-%{version}/COPYING %{buildroot}/usr/share/package-licenses/wayland-protocols/9d823228bce4c6977989fdd7b58026cd62fc55e0 || :
pushd ../build32/
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/wayland-protocols/stable/linux-dmabuf/linux-dmabuf-v1.xml
/usr/share/wayland-protocols/stable/presentation-time/presentation-time.xml
/usr/share/wayland-protocols/stable/tablet/tablet-v2.xml
/usr/share/wayland-protocols/stable/viewporter/viewporter.xml
/usr/share/wayland-protocols/stable/xdg-shell/xdg-shell.xml
/usr/share/wayland-protocols/staging/alpha-modifier/alpha-modifier-v1.xml
/usr/share/wayland-protocols/staging/color-management/color-management-v1.xml
/usr/share/wayland-protocols/staging/commit-timing/commit-timing-v1.xml
/usr/share/wayland-protocols/staging/content-type/content-type-v1.xml
/usr/share/wayland-protocols/staging/cursor-shape/cursor-shape-v1.xml
/usr/share/wayland-protocols/staging/drm-lease/drm-lease-v1.xml
/usr/share/wayland-protocols/staging/ext-data-control/ext-data-control-v1.xml
/usr/share/wayland-protocols/staging/ext-foreign-toplevel-list/ext-foreign-toplevel-list-v1.xml
/usr/share/wayland-protocols/staging/ext-idle-notify/ext-idle-notify-v1.xml
/usr/share/wayland-protocols/staging/ext-image-capture-source/ext-image-capture-source-v1.xml
/usr/share/wayland-protocols/staging/ext-image-copy-capture/ext-image-copy-capture-v1.xml
/usr/share/wayland-protocols/staging/ext-session-lock/ext-session-lock-v1.xml
/usr/share/wayland-protocols/staging/ext-transient-seat/ext-transient-seat-v1.xml
/usr/share/wayland-protocols/staging/ext-workspace/ext-workspace-v1.xml
/usr/share/wayland-protocols/staging/fifo/fifo-v1.xml
/usr/share/wayland-protocols/staging/fractional-scale/fractional-scale-v1.xml
/usr/share/wayland-protocols/staging/linux-drm-syncobj/linux-drm-syncobj-v1.xml
/usr/share/wayland-protocols/staging/security-context/security-context-v1.xml
/usr/share/wayland-protocols/staging/single-pixel-buffer/single-pixel-buffer-v1.xml
/usr/share/wayland-protocols/staging/tearing-control/tearing-control-v1.xml
/usr/share/wayland-protocols/staging/xdg-activation/xdg-activation-v1.xml
/usr/share/wayland-protocols/staging/xdg-dialog/xdg-dialog-v1.xml
/usr/share/wayland-protocols/staging/xdg-system-bell/xdg-system-bell-v1.xml
/usr/share/wayland-protocols/staging/xdg-toplevel-drag/xdg-toplevel-drag-v1.xml
/usr/share/wayland-protocols/staging/xdg-toplevel-icon/xdg-toplevel-icon-v1.xml
/usr/share/wayland-protocols/staging/xdg-toplevel-tag/xdg-toplevel-tag-v1.xml
/usr/share/wayland-protocols/staging/xwayland-shell/xwayland-shell-v1.xml
/usr/share/wayland-protocols/unstable/fullscreen-shell/fullscreen-shell-unstable-v1.xml
/usr/share/wayland-protocols/unstable/idle-inhibit/idle-inhibit-unstable-v1.xml
/usr/share/wayland-protocols/unstable/input-method/input-method-unstable-v1.xml
/usr/share/wayland-protocols/unstable/input-timestamps/input-timestamps-unstable-v1.xml
/usr/share/wayland-protocols/unstable/keyboard-shortcuts-inhibit/keyboard-shortcuts-inhibit-unstable-v1.xml
/usr/share/wayland-protocols/unstable/linux-dmabuf/linux-dmabuf-unstable-v1.xml
/usr/share/wayland-protocols/unstable/linux-explicit-synchronization/linux-explicit-synchronization-unstable-v1.xml
/usr/share/wayland-protocols/unstable/pointer-constraints/pointer-constraints-unstable-v1.xml
/usr/share/wayland-protocols/unstable/pointer-gestures/pointer-gestures-unstable-v1.xml
/usr/share/wayland-protocols/unstable/primary-selection/primary-selection-unstable-v1.xml
/usr/share/wayland-protocols/unstable/relative-pointer/relative-pointer-unstable-v1.xml
/usr/share/wayland-protocols/unstable/tablet/tablet-unstable-v1.xml
/usr/share/wayland-protocols/unstable/tablet/tablet-unstable-v2.xml
/usr/share/wayland-protocols/unstable/text-input/text-input-unstable-v1.xml
/usr/share/wayland-protocols/unstable/text-input/text-input-unstable-v3.xml
/usr/share/wayland-protocols/unstable/xdg-decoration/xdg-decoration-unstable-v1.xml
/usr/share/wayland-protocols/unstable/xdg-foreign/xdg-foreign-unstable-v1.xml
/usr/share/wayland-protocols/unstable/xdg-foreign/xdg-foreign-unstable-v2.xml
/usr/share/wayland-protocols/unstable/xdg-output/xdg-output-unstable-v1.xml
/usr/share/wayland-protocols/unstable/xdg-shell/xdg-shell-unstable-v5.xml
/usr/share/wayland-protocols/unstable/xdg-shell/xdg-shell-unstable-v6.xml
/usr/share/wayland-protocols/unstable/xwayland-keyboard-grab/xwayland-keyboard-grab-unstable-v1.xml

%files dev
%defattr(-,root,root,-)
/usr/include/wayland-protocols/alpha-modifier-v1-enum.h
/usr/include/wayland-protocols/color-management-v1-enum.h
/usr/include/wayland-protocols/commit-timing-v1-enum.h
/usr/include/wayland-protocols/content-type-v1-enum.h
/usr/include/wayland-protocols/cursor-shape-v1-enum.h
/usr/include/wayland-protocols/drm-lease-v1-enum.h
/usr/include/wayland-protocols/ext-data-control-v1-enum.h
/usr/include/wayland-protocols/ext-foreign-toplevel-list-v1-enum.h
/usr/include/wayland-protocols/ext-idle-notify-v1-enum.h
/usr/include/wayland-protocols/ext-image-capture-source-v1-enum.h
/usr/include/wayland-protocols/ext-image-copy-capture-v1-enum.h
/usr/include/wayland-protocols/ext-session-lock-v1-enum.h
/usr/include/wayland-protocols/ext-transient-seat-v1-enum.h
/usr/include/wayland-protocols/ext-workspace-v1-enum.h
/usr/include/wayland-protocols/fifo-v1-enum.h
/usr/include/wayland-protocols/fractional-scale-v1-enum.h
/usr/include/wayland-protocols/fullscreen-shell-unstable-v1-enum.h
/usr/include/wayland-protocols/idle-inhibit-unstable-v1-enum.h
/usr/include/wayland-protocols/input-method-unstable-v1-enum.h
/usr/include/wayland-protocols/input-timestamps-unstable-v1-enum.h
/usr/include/wayland-protocols/keyboard-shortcuts-inhibit-unstable-v1-enum.h
/usr/include/wayland-protocols/linux-dmabuf-unstable-v1-enum.h
/usr/include/wayland-protocols/linux-dmabuf-v1-enum.h
/usr/include/wayland-protocols/linux-drm-syncobj-v1-enum.h
/usr/include/wayland-protocols/linux-explicit-synchronization-unstable-v1-enum.h
/usr/include/wayland-protocols/pointer-constraints-unstable-v1-enum.h
/usr/include/wayland-protocols/pointer-gestures-unstable-v1-enum.h
/usr/include/wayland-protocols/presentation-time-enum.h
/usr/include/wayland-protocols/primary-selection-unstable-v1-enum.h
/usr/include/wayland-protocols/relative-pointer-unstable-v1-enum.h
/usr/include/wayland-protocols/security-context-v1-enum.h
/usr/include/wayland-protocols/single-pixel-buffer-v1-enum.h
/usr/include/wayland-protocols/tablet-unstable-v1-enum.h
/usr/include/wayland-protocols/tablet-unstable-v2-enum.h
/usr/include/wayland-protocols/tablet-v2-enum.h
/usr/include/wayland-protocols/tearing-control-v1-enum.h
/usr/include/wayland-protocols/text-input-unstable-v1-enum.h
/usr/include/wayland-protocols/text-input-unstable-v3-enum.h
/usr/include/wayland-protocols/viewporter-enum.h
/usr/include/wayland-protocols/xdg-activation-v1-enum.h
/usr/include/wayland-protocols/xdg-decoration-unstable-v1-enum.h
/usr/include/wayland-protocols/xdg-dialog-v1-enum.h
/usr/include/wayland-protocols/xdg-foreign-unstable-v1-enum.h
/usr/include/wayland-protocols/xdg-foreign-unstable-v2-enum.h
/usr/include/wayland-protocols/xdg-output-unstable-v1-enum.h
/usr/include/wayland-protocols/xdg-shell-enum.h
/usr/include/wayland-protocols/xdg-shell-unstable-v5-enum.h
/usr/include/wayland-protocols/xdg-shell-unstable-v6-enum.h
/usr/include/wayland-protocols/xdg-system-bell-v1-enum.h
/usr/include/wayland-protocols/xdg-toplevel-drag-v1-enum.h
/usr/include/wayland-protocols/xdg-toplevel-icon-v1-enum.h
/usr/include/wayland-protocols/xdg-toplevel-tag-v1-enum.h
/usr/include/wayland-protocols/xwayland-keyboard-grab-unstable-v1-enum.h
/usr/include/wayland-protocols/xwayland-shell-v1-enum.h
/usr/share/pkgconfig/wayland-protocols.pc

%files dev32
%defattr(-,root,root,-)
/usr/share/pkgconfig/32wayland-protocols.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/wayland-protocols/9d823228bce4c6977989fdd7b58026cd62fc55e0
