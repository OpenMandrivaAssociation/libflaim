# This tarball is a subversion checkout for Flaim 5.0
# Available from https://forgesvn1.novell.com/svn/flaim/trunk/
%define major 5
%define minor 2
# SONAME is %{major}.%{minor} here
%define libname %mklibname flaim %{major}.%{minor}
%define devname %mklibname flaim -d

Summary:	Embeddable cross-platform database engine
Name:		libflaim
Version:	4.9.1052
Release:	4
License:	GPLv2+
Group:		System/Libraries
Url:		https://forge.novell.com/modules/xfmod/project/?flaim
Source0:	http://forgeftp.novell.com/flaim/development/flaim/downloads/source/%{name}-%{version}.tar
Patch0:		fortify-source.patch
Patch1:		%{name}-4.9.1052-optflags.patch
Patch2:		%{name}-4.9.1052-fix-format-errors.patch
BuildRequires:	pkgconfig(ncurses)

%description
FLAIM is an embeddable cross-platform database engine that provides a
rich, powerful, easy-to-use feature set. It is the database engine used
by Novell eDirectory. It has proven to be highly scalable, reliable,
and robust. It is available on a wide variety of 32 bit and 64 bit
platforms.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Embeddable cross-platform database engine
Group:		System/Libraries

%description -n %{libname}
FLAIM is an embeddable cross-platform database engine that provides a
rich, powerful, easy-to-use feature set. It is the database engine used
by Novell eDirectory. It has proven to be highly scalable, reliable,
and robust. It is available on a wide variety of 32 bit and 64 bit
platforms.

%files -n %{libname}
%doc flaim/COPYING flaim/COPYRIGHT
%{_libdir}/libflaim.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	libflaim library headers
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This is the libraries, include files and other resources you can use
to incorporate libdvdread into applications.

%files -n %{devname}
%{_libdir}/libflaim.so
%{_libdir}/pkgconfig/libflaim.pc
%{_includedir}/flaim.h
%{_includedir}/flaimtk.h

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
cd flaim/
make CXXFLAGS="%{optflags} -Wno-error" lib_dir_name=%{_lib} verbose libs

%install
cd flaim/
%make rpm_build_root=%{buildroot} lib_dir_name=%{_lib} install
rm -f %{buildroot}%{_libdir}/libflaim.a

