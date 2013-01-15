%define	name	gtkglext
%define	version	1.2.0
%define	release	%mkrel 11

%define	major	0
%define	api_version 1.0

%define	libname %mklibname %{name} %{api_version} %{major}
%define	libnamedev %mklibname %{name} -d

Summary:	OpenGL extension to GTK 2.0 or later
Name:		%{name}
Version:	%{version}
Release: 	%{release}
License:	LGPL
Group:		System/Libraries
Source0:	http://prdownloads.sourceforge.net/gtkglext/%{name}-%{version}.tar.bz2
Patch0:		gtkglext-support-pango.diff
Patch1:		gtkglext-1.2.0-newer-gtk.patch
Patch2:		gtkglext-automake-1.13.patch
URL:		http://gtkglext.sourceforge.net/
BuildRequires:	pkgconfig
BuildRequires:	mesaglu-devel
BuildRequires:	gtk2-devel
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	pango-devel
BuildRequires:	chrpath
BuildRequires:	pkgconfig(pangox)

%description
GtkGLExt is an OpenGL extension to GTK 2.0 or later.
GtkGLExt provides the GDK objects to support OpenGL rendering in GTK,
and GtkWidget API add-ons to make GTK+ widgets OpenGL-capable.
As opposed to Jane Loff's GtkGLArea , it does not provide any OpenGL widget,
but an interface to use OpenGL on *ANY* GTK+ widget. 

%package -n	%{libname}
Summary:	OpenGL extension to GTK 2.0 or later
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{_lib}gtkglext-1.0_0 < %{version}-%{release}

%description -n	%{libname}
GtkGLExt is an OpenGL extension to GTK 2.0 or later.
GtkGLExt provides the GDK objects to support OpenGL rendering in GTK,
and GtkWidget API add-ons to make GTK+ widgets OpenGL-capable.
As opposed to Jane Loff's GtkGLArea , it does not provide any OpenGL widget,
but an interface to use OpenGL on *ANY* GTK+ widget. 

%package -n	%{libnamedev}
Summary:	OpenGL extension to GTK 2.0 or later
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Provides:	lib%{name}-%{api_version}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes:	%{_lib}gtkglext-1.0_0-devel < %{version}-%{release}

%description -n %{libnamedev}
Libraries and includes files you can use for GtkGLExt development.

%prep
%setup -q
%patch0 -p0
%patch1 -p1 -b .gtk
%patch2 -p1 -b .am113~

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files -n %{libnamedev}
%defattr(-,root,root)
%doc AUTHORS ChangeLog TODO README
%doc %{_datadir}/gtk-doc/html/gtkglext
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/*
%{_libdir}/%{name}*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4




%changelog
* Sun May 15 2011 Funda Wang <fwang@mandriva.org> 1.2.0-11mdv2011.0
+ Revision: 674882
- update gtk patch from fedora
- new devel package policy
- fix patch (bug#63304)

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-9
+ Revision: 664952
- mass rebuild

* Fri Dec 03 2010 Funda Wang <fwang@mandriva.org> 1.2.0-8mdv2011.0
+ Revision: 605774
- fix build
- build with latest gtk

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.2.0-6mdv2010.0
+ Revision: 425078
- rebuild

* Fri Nov 07 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-5mdv2009.1
+ Revision: 300800
- rebuilt against new libxcb

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-4mdv2009.0
+ Revision: 221115
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-3mdv2008.1
+ Revision: 170879
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.2.0-2mdv2008.1
+ Revision: 126430
- kill re-definition of %%buildroot on Pixel's request


* Mon Feb 26 2007 Emmanuel Andry <eandry@mandriva.org> 1.2.0-2mdv2007.0
+ Revision: 126153
- buildrequires libgdk_pixbuf2.0-devel
- buildrequires gdk-pixbuf2-devel
- add sourceforge patch for pango support
- Import gtkglext

* Thu Aug 24 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.2.0-1mdv2007.0
- 1.2.0
- %%mkrel
- cleanups
- drop P0 (merged upstream)
- fix summary-ended-with-dot

* Wed May 04 2005 Pascal Terjan <pterjan@mandriva.org> 1.0.6-3mdk
- 
- From Guillaume Rousse
 - use %%configure macro
 - spec cleanup
 - rpmbuildupdate aware

* Mon Jul 26 2004 Pascal Terjan <pterjan@mandrake.org> 1.0.6-2mdk
- DIRM

* Thu Mar 11 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0.6-1mdk
- 1.0.6

