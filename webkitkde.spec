%define         svn   826469

Name:           webkitkde
#TODO: Find a better summary
Summary:        QtWebKit's kpart
Version:        0.0
Release:        %mkrel 0.%{svn}.4
Url:            http://websvn.kde.org/trunk/playground/libs/webkitkde/
License:        LGPL v2+
Group:          Networking/WWW
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Buildrequires:  kdelibs4-devel
Source0:        %{name}-%{version}.%{svn}.tar.bz2


%description
%name is a QtWebKit's kpart

%files
%defattr(-,root,root)
%_kde_appsdir/webkitpart
%_kde_datadir/kde4/services/webkitpart.desktop
%_kde_libdir/kde4/webkitkdepart.so
%_kde_iconsdir/*/*/*/*

#--------------------------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: %name

%description  devel
This package contains header files needed if you wish to build applications
based on %name

%files devel
%defattr(-,root,root)
%_kde_libdir/libwebkitkde.so
%_kde_includedir/*
%_kde_appsdir/cmake/modules/FindWebKitKde.cmake

#-----------------------------------------------------------------------------

%define libwebkitkde_major 1
%define libwebkitkde %mklibname webkitkde %{libwebkitkde_major}

%package -n %libwebkitkde
Summary: KDE 4 library
Group: System/Libraries

%description -n %libwebkitkde
KDE 4 library.

%if %mdkversion < 200900
%post -n %libwebkitkde -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libwebkitkde -p /sbin/ldconfig
%endif

%files -n %libwebkitkde
%defattr(-,root,root)
%_kde_libdir/libwebkitkde.so.%{libwebkitkde_major}*

#--------------------------------------------------------------------

%prep
%setup -q -n %name

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%clean
rm -rf %buildroot
