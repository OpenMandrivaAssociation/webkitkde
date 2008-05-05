%define         svn   799548

Name:           webkitkde
#TODO: Find a better summary
Summary:        QtWebKit's kpart
Version:        0.0
Release:        %mkrel 0.%{svn}.1
Url:            http://websvn.kde.org/trunk/playground/libs/webkitkde/
License:        LGPL v2+
Group:          Networking/WWW
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Buildrequires:  kde4-macros
Source0:        %{name}-%{version}.%{svn}.tar.bz2


%description
%name is a QtWebKit's kpart

%files
%defattr(-,root,root)
%_kde_appsdir/webkitpart/webkitpart.rc
%_kde_datadir/kde4/services/webkitpart.desktop
%_kde_libdir/kde4/webkitkdepart.so

#--------------------------------------------------------------------
%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt

%description  devel
This package contains header files needed if you wish to build applications
based on %name

%files devel
%defattr(-,root,root)
%_kde_libdir/libwebkitkde.so
%dir %_kde_includedir/KDE/WebKitKde
%_kde_includedir/KDE/WebKitKde/WebKitPart
%_kde_includedir/KDE/WebKitKde/WebView
%dir %_kde_includedir/webkitkde

%_kde_includedir/webkitkde/webkitkde_export.h
%_kde_includedir/webkitkde/webkitpart.h
%_kde_includedir/webkitkde/webkitview.h
%_kde_appsdir/cmake/modules/FindWebKitKde.cmake

#-----------------------------------------------------------------------------

%define libwebkitkde_major 1
%define libwebkitkde %mklibname webkitkde %{libwebkitkde_major}

%package -n %libwebkitkde
Summary: KDE 4 library
Group: System/Libraries

%description -n %libwebkitkde
KDE 4 library.

%post -n %libwebkitkde -p /sbin/ldconfig
%postun -n %libwebkitkde -p /sbin/ldconfig

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
cd build
make DESTDIR=%buildroot install

%clean
%{__rm} -rf "%{buildroot}"
