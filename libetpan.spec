Name:           libetpan
Version:        0.47
Release:        1%{?dist}
Summary: Portable, efficient middleware for different kinds of mail access

Group:          System Environment/Libraries
License:        BSD
URL:            http://www.etpan.org/
Source0:        http://dl.sf.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  db4-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  openssl-devel

%description
The purpose of this mail library is to provide a portable, efficient middleware
for different kinds of mail access. When using the drivers interface, the
interface is the same for all kinds of mail access, remote and local mailboxes.

%package        devel
Summary:        Development package for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       openssl-devel
Requires:       cyrus-sasl-devel
Requires:       db4-devel

%description    devel
The %{name}-devel package contains the files needed for development
with %{name}.

%prep
%setup -q

%build
%configure --disable-static --with-gnutls=no
make # %{?_smp_mflags} not parallel clean


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_libdir}/libetpan.la
chmod 755 $RPM_BUILD_ROOT%{_libdir}/libetpan.so.8.1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYRIGHT NEWS TODO
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc doc/API.html doc/README.html doc/DOCUMENTATION
%{_bindir}/libetpan-config
%{_includedir}/libetpan.h
%{_includedir}/libetpan
%{_libdir}/*.so

%changelog
* Thu Oct 19 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.47-1
- version upgrade

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.46-2
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.46-1
- version upgrade

* Wed Sep 13 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.45-2
- FE6 rebuild

* Thu Mar 23 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.45-1
- version upgrade

* Wed Feb 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.42-2
- Rebuild for Fedora Extras 5

* Fri Feb 03 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.42-1
- version upgrade

* Sun Dec 25 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.41-1
- version upgrade

* Thu Nov 17 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.40-1
- version upgrade

* Fri Sep 23 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.39.1-1
- version upgrade

* Sat Aug 13 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.38-4
- add dist tag

* Mon Aug 08 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.38-3
- remove some doc
- build without gnutls

* Sun Jul 31 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.38-2
- add documentation
- add more Requires/BuildRequires
- build with gnutls support

* Sun Jul 31 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.38-1
- Initial Release
