%define		subver	beta3
%define		rel		0.1
Summary:	Replacement to Red Hat's logrotate
Name:		rottlog
Version:	0.70
Release:	0.%{subver}.%{rel}
License:	GPL v2
Group:		Applications/System
URL:		http://www.gnu.org/software/rottlog/
Source0:	http://download.savannah.gnu.org/releases/rottlog/%{name}-%{version}%{subver}.tar.gz
# Source0-md5:	500670496f05b9c51d35644bb9376757
Patch0:		%{name}-bashism.patch
Patch1:		%{name}-DESTDIR.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Rottlog is a replacement to Red Hat's logrotate. It has similar
syntax, but more powerful features to cut and store logs.

%prep
%setup -q -n %{name}-%{version}%{subver}
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	LOG_OWN=$(id -un) \
	LOG_GROUP=$(id -gn) \
	DESTDIR=$RPM_BUILD_ROOT

chmod u+rwX $RPM_BUILD_ROOT%{_sysconfdir}/rottlog

rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/rottlog/sample_*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS  README README.Log2Rot README.outdated TODO
%doc rc/sample_*
%dir %{_sysconfdir}/rottlog
%attr(755,root,root) %{_sbindir}/rottlog
%attr(755,root,root) %{_sbindir}/virottcustom
%attr(755,root,root) %{_sbindir}/virottday
%attr(755,root,root) %{_sbindir}/virottmonth
%attr(755,root,root) %{_sbindir}/virottrc
%attr(755,root,root) %{_sbindir}/virottweek
%{_infodir}/*.info*
%{_mandir}/man5/rottlogconf.5*
%{_mandir}/man5/rottlogex.5*
%{_mandir}/man5/rottlogrc.5*
%{_mandir}/man8/rottlog.8*
