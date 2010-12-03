%define         svn  1079772

Name:           webkitkde
#TODO: Find a better summary
Summary:        QtWebKit's kpart
Version:        0.0
Release:        %mkrel 0.%{svn}.2
Url:            http://websvn.kde.org/trunk/playground/libs/webkitkde
License:        LGPLv2+
Group:          Networking/WWW
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Buildrequires:  kdelibs4-devel >= 2:4.2.69
Source0:        %{name}-%{version}.%{svn}.tar.bz2

%description
%name is a QtWebKit's kpart

%files
%defattr(-,root,root)
%_kde_appsdir/kwebkitpart
%_kde_datadir/kde4/services/kwebkitpart.desktop
%_kde_libdir/kde4/*
%_kde_iconsdir/*/*/*/*

#-----------------------------------------------------------------------------

%define libkwebkit_major 1
%define libkwebkit %mklibname kwebkit %{libkwebkit_major}

%package -n %libkwebkit
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkwebkit
KDE 4 library.

%files -n %libkwebkit
%defattr(-,root,root)
%_kde_libdir/libkwebkit.so.%{libkwebkit_major}*

#-----------------------------------------------------------------------------
%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: %libkwebkit = %version-%release

%description  devel
This package contains header files needed if you wish to build applications
based on %name

%files devel
%defattr(-,root,root)
%_kde_libdir/libkwebkit.so
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
