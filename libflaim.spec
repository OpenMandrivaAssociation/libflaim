# This tarball is a subversion checkout for Flaim 5.0
# Available from https://forgesvn1.novell.com/svn/flaim/trunk/
%define major 5.2
%define libname %mklibname flaim %{major}
%define develname %mklibname flaim -d

Name:		libflaim
Version:	4.9.1052
Release:	%mkrel 1
Summary:	Embeddable cross-platform database engine
URL:		http://forge.novell.com/modules/xfmod/project/?flaim
License:	GPLv2
Group:		System/Libraries
Source:		http://forgeftp.novell.com/flaim/development/flaim/downloads/source/%{name}-4.9.1052.tar.gz
Patch0:		fortify-source.patch
Patch1:		%{name}-4.9.1052-optflags.patch
Patch2:		%{name}-4.9.1052-fix-format-errors.patch
BuildRequires:	ncurses-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
FLAIM is an embeddable cross-platform database engine that provides a
rich, powerful, easy-to-use feature set. It is the database engine used
by Novell eDirectory. It has proven to be highly scalable, reliable,
and robust. It is available on a wide variety of 32 bit and 64 bit
platforms.

%package -n	%{libname}
Summary:	Embeddable cross-platform database engine
Group:		System/Libraries

%description -n	%{libname}
FLAIM is an embeddable cross-platform database engine that provides a
rich, powerful, easy-to-use feature set. It is the database engine used
by Novell eDirectory. It has proven to be highly scalable, reliable,
and robust. It is available on a wide variety of 32 bit and 64 bit
platforms.

%package -n	%{develname}
Summary:	libflaim library headers
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:   %{name}-devel = %{version}-%{release}

%description -n	%{develname}
This is the libraries, include files and other resources you can use
to incorporate libdvdread into applications.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
cd flaim/
%make CXXFLAGS="$RPM_OPT_FLAGS -Wno-error" lib_dir_name=%{_lib} verbose libs

%install
rm -rf %{buildroot}
cd flaim/
%make rpm_build_root=%{buildroot} lib_dir_name=%{_lib} install

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc flaim/COPYING flaim/COPYRIGHT
%{_libdir}/libflaim.so.*

%files -n %{develname}
%defattr(-,root,root)
%exclude %{_libdir}/libflaim.a
%{_libdir}/libflaim.so
%{_libdir}/pkgconfig/libflaim.pc
%{_includedir}/flaim.h
%{_includedir}/flaimtk.h

