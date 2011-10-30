%define	name	gtkglext
%define	version	1.2.0
%define	release	%mkrel 12

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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://gtkglext.sourceforge.net/
BuildRequires:	pkgconfig
BuildRequires:	MesaGLU-devel
BuildRequires:	gtk2-devel
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	pango-devel
BuildRequires:	chrpath

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
%{_libdir}/*.la
%{_includedir}/*
%{_libdir}/%{name}*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4


