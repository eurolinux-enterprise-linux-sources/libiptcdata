%if 0%{?rhel} <= 5
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name: libiptcdata
Version: 1.0.4
Release: 11%{?dist}
Summary: IPTC tag library

Group: Development/Libraries
License: LGPLv2+
URL: http://libiptcdata.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gettext
BuildRequires: libtool
BuildRequires: gtk-doc

%description
libiptcdata is a library for parsing, editing, and saving IPTC data
stored inside images.  IPTC is a standard for encoding metadata such
as captions, titles, locations, etc. in the headers of an image file.
libiptcdata also includes a command-line utility for modifying the
metadata.

%package devel
Summary: Headers and libraries for libiptcdata application development
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
The libiptcdata-devel package contains the libraries and include files
that you can use to develop libiptcdata applications.

%package python
Summary: Python bindings for libiptcdata
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
BuildRequires: python-devel

%description python
The libiptcdata-python package contains a Python module that allows Python
applications to use the libiptcdata API for reading and writing IPTC
metadata in images.

%prep
%setup -q

%build
%configure --enable-gtk-doc --enable-python --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} INSTALL="%{__install} -c -p" install
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.la
rm -f $RPM_BUILD_ROOT%{python_sitearch}/iptcdata.la
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/*
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libiptcdata
%{_datadir}/gtk-doc/html/libiptcdata

%files python
%defattr(-,root,root)
%doc python/README
%doc python/examples/*
%{python_sitearch}/*.so

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.0.4-11
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0.4-10
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec  4 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.0.4-6
- Mark translations with %%lang.

* Wed Nov 16 2011 David Moore <david.moore@gmail.com> 1.0.4-5
- Removed 'Requires: gtk-doc', updated python sitearch.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 05 2009 David Moore <dcm@acm.org> 1.0.4-1
- New upstream version

* Sun Apr 12 2009 David Moore <dcm@acm.org> 1.0.3-3
- Added 'BuildRequires: gtk-doc'

* Sun Apr 12 2009 David Moore <dcm@acm.org> 1.0.3-2
- Added 'Requires: gtk-doc' and 'BuildRequires: libtool' and gettext

* Sun Apr 12 2009 David Moore <dcm@acm.org> 1.0.3-1
- New upstream version
- Added translation to file list

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.2-4
- Rebuild for Python 2.6

* Thu May 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.2-3
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.2-2
- Autorebuild for GCC 4.3

* Tue May 15 2007 David Moore <dcm@acm.org> 1.0.2-1
- New upstream version

* Fri Mar 23 2007 David Moore <dcm@acm.org> 1.0.1-1
- New upstream version

* Thu Mar 22 2007 David Moore <dcm@acm.org> 1.0.0-2
- Fixed URL, removed INSTALL file, fixed python path and timestamps

* Wed Mar 21 2007 David Moore <dcm@acm.org> 1.0.0-1
- Updated spec file to better match Fedora guidelines

* Sun Jan 28 2007 David Moore <dcm@acm.org>
- Added libiptcdata-python package

* Wed Apr 12 2006 David Moore <dcm@acm.org>
- Removed *.mo from spec file since there are no translations yet

* Mon Feb 28 2005 David Moore <dcm@acm.org>
- Initial version
