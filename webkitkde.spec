%define         svn   1050148

Name:           webkitkde
#TODO: Find a better summary
Summary:        QtWebKit's kpart
Version:        0.0
Release:        %mkrel 0.%{svn}.1
Url:            http://websvn.kde.org/trunk/playground/libs/webkitkde/
License:        LGPLv2+
Group:          Networking/WWW
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Buildrequires:  kdelibs4-devel >= 2:4.2.69
Source0:        %{name}-%{version}.%{svn}.tar.bz2

%description
%name is a QtWebKit's kpart

%files
%defattr(-,root,root)
%_kde_appsdir/webkitpart
%_kde_datadir/kde4/services/webkitpart.desktop
%_kde_libdir/kde4/webkitkdepart.so
%_kde_iconsdir/*/*/*/*

#-----------------------------------------------------------------------------

%define libwebkitkde_major 1
%define libwebkitkde %mklibname webkitkde %{libwebkitkde_major}

%package -n %libwebkitkde
Summary: KDE 4 library
Group: System/Libraries

%description -n %libwebkitkde
KDE 4 library.

%files -n %libwebkitkde
%defattr(-,root,root)
%_kde_libdir/libwebkitkde.so.%{libwebkitkde_major}*

#-----------------------------------------------------------------------------

%define libkdewebkit_major 1
%define libkdewebkit %mklibname kdewebkit %{libkdewebkit_major}

%package -n %libkdewebkit
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdewebkit
KDE 4 library.

%files -n %libkdewebkit
%defattr(-,root,root)
%_kde_libdir/libkdewebkit.so.%{libkdewebkit_major}*

#-----------------------------------------------------------------------------
%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: %libwebkitkde = %version-%release
Requires: %libkdewebkit = %version-%release

%description  devel
This package contains header files needed if you wish to build applications
based on %name

%files devel
%defattr(-,root,root)
%_kde_libdir/libkdewebkit.so
%exclude %_kde_libdir/libwebkitkde.so
%_kde_includedir/*
%_kde_appsdir/cmake/modules/*.cmake

#-----------------------------------------------------------------------------

%prep
%setup -q -n %name

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot
