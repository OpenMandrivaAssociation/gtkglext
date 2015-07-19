%define	api	1.0
%define	major	0
%define	libname %mklibname gtkglext-x11 %{api} %{major}
%define	libgdk	%mklibname gdkglext-x11 %{api} %{major}
%define	devname %mklibname %{name} -d

Summary:	OpenGL extension to GTK 2.0 or later
Name:		gtkglext
Version:	1.2.0
Release: 	24
License:	LGPLv2
Group:		System/Libraries
Url:		http://gtkglext.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/gtkglext/%{name}-%{version}.tar.bz2
Patch0:		gtkglext-support-pango.diff
Patch1:		gtkglext-1.2.0-newer-gtk.patch
Patch2:		gtkglext-automake-1.13.patch

BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(pango)
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

%package -n	%{libgdk}
Summary:	OpenGL extension to GTK 2.0 or later
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Conflicts:	%{_lib}gtkglext-1.0_0 < %{version}-%{release}
Conflicts:	%{_lib}gtkglext1.0_0 < 1.2.0-16

%description -n	%{libgdk}
This package contains a shared library for %{name}.

%package -n	%{devname}
Summary:	OpenGL extension to GTK 2.0 or later
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libgdk} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes:	%{_lib}gtkglext-1.0_0-devel < %{version}-%{release}

%description -n %{devname}
Libraries and includes files you can use for GtkGLExt development.

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libgtkglext-x11-%{api}.so.%{major}*

%files -n %{libgdk}
%{_libdir}/libgdkglext-x11-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog TODO README
%doc %{_datadir}/gtk-doc/html/gtkglext
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/%{name}*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4

