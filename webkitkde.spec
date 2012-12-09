%define         svn  1079772

Name:           webkitkde
#TODO: Find a better summary
Summary:        QtWebKit's kpart
Version:        0.0
Release:        %mkrel 0.%{svn}.3
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


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0-0.1079772.3mdv2011.0
+ Revision: 670803
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0-0.1079772.2mdv2011.0
+ Revision: 608157
- rebuild

* Mon Jan 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.0-0.1079772.1mdv2010.1
+ Revision: 495710
- New snapshot

* Fri Nov 20 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.0-0.1050148.3mdv2010.1
+ Revision: 467604
- Exclude more files that conflicts with kdelibs4-devel

* Tue Nov 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.0-0.1050148.2mdv2010.1
+ Revision: 466806
- exclude the good lib

* Tue Nov 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.0-0.1050148.1mdv2010.1
+ Revision: 466789
- Update to latest svn snapshot
  Exclude libwebkitkde.so because is on kdelibs4 too ( this is temporary hack because all will go on kdelibs soon )

* Sat Nov 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.0-0.1046057.1mdv2010.1
+ Revision: 462191
- new snapshot

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream release 4.3.0.

* Tue May 26 2009 Funda Wang <fwang@mandriva.org> 0.0-0.972995.1mdv2010.0
+ Revision: 379841
- New snapshot to build with latest kdelibs4

* Sun Jan 18 2009 Funda Wang <fwang@mandriva.org> 0.0-0.912736.1mdv2009.1
+ Revision: 330856
- New snapshot

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Rebuild against new kde4

* Thu Jul 10 2008 Helio Chissini de Castro <helio@mandriva.com> 0.0-0.826469.3mdv2009.0
+ Revision: 233199
- Update for current svn snapshot
- Update svn release
- Fix 2008.1 build

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri May 23 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.0-0.799548.3mdv2009.0
+ Revision: 210207
- own %%_kde_appsdir/webkitpart
- Remove workaround not needed anymore

* Tue May 06 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.0-0.799548.2mdv2009.0
+ Revision: 202008
- Fix Requires

* Tue May 06 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.0-0.799548.1mdv2009.0
+ Revision: 201969
- workaround buildrequires
- add kde4-macros as buildrequires
- Fix Group and description
- import webkitkde


