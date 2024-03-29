Summary:	OpenSync file plugin
Summary(pl.UTF-8):	Wtyczka file do OpenSync
Name:		libopensync-plugin-file
Version:	0.39
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	4e4aeb1012b504c005c7f235b1bd0e60
URL:		http://www.opensync.org/
BuildRequires:	cmake
BuildRequires:	fam-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libopensync-devel >= 1:%{version}
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and
distribution independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains file plugin for OpenSync framework.

%description -l pl.UTF-8
OpenSync to niezależny od platformy i dystrybucji szkielet do
synchronizacji danych.

Składa się z różnych wtyczek, których można używać do łączenia z
urządzeniami, potężnego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera wtyczkę file (do synchronizacji plików) dla
szkieletu OpenSync.

%prep
%setup -q

%build
mkdir build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/opensync/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS INSTALL
%attr(755,root,root) %{_libdir}/libopensync1/plugins/file-sync.so
%attr(755,root,root) %{_libdir}/libopensync1/formats/file.so
%attr(755,root,root) %{_libdir}/libopensync1/formats/plain.so
%{_datadir}/libopensync1/defaults/file-sync
