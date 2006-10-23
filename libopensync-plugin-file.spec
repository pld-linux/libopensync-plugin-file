Summary:	OpenSync file plugin
Summary(pl):	Wtyczka file do OpenSync
Name:		libopensync-plugin-file
Version:	0.19
Release:	0.1
License:	LGPL
Group:		Libraries
#Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.gz?format=raw
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	dad7ded0c3f5ec089e6efdb4bf5d7b4b
URL:		http://www.opensync.org/
BuildRequires:	libopensync-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and distribution
independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains file plugin for OpenSync framework.

%description -l pl
OpenSync to niezale¿ny od platformy i dystrybucji szkielet do
synchronizacji danych.

Sk³ada siê z ró¿nych wtyczek, których mo¿na u¿ywaæ do ³±czenia z
urz±dzeniami, potê¿nego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera wtyczkê file (do synchronizacji plików) dla
szkieletu OpenSync.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/opensync/plugins/*.so
%{_libdir}/opensync/plugins/*.la
%{_datadir}/opensync/defaults/*
