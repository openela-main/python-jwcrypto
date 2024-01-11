%if 0%{?fedora} || 0%{?rhel} > 7
# Enable python3 build by default
%bcond_without python3
%else
%bcond_with python3
%endif

%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

%global srcname jwcrypto

Name:           python-%{srcname}
Version:        0.5.0
Release:        1.1%{?dist}
Summary:        Implements JWK, JWS, JWE specifications using python-cryptography

License:        LGPLv3+
URL:            https://github.com/latchset/%{srcname}
Source0:        https://github.com/latchset/%{srcname}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-cryptography >= 1.5
BuildRequires:  python2-pytest
%endif
%if %{with python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-cryptography >= 1.5
BuildRequires:  python%{python3_pkgversion}-pytest
%endif

%description
Implements JWK, JWS, JWE specifications using python-cryptography

%if %{with python2}
%package -n python2-%{srcname}
Summary:        Implements JWK,JWS,JWE specifications using python-cryptography
Requires:       python2-cryptography >= 1.5
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Implements JWK, JWS, JWE specifications using python-cryptography
%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Implements JWK, JWS, JWE specifications using python-cryptography
Requires:       python%{python3_pkgversion}-cryptography >= 1.5
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Implements JWK, JWS, JWE specifications using python-cryptography
%endif


%prep
%setup -q -n %{srcname}-%{version}


%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif


%check
%if %{with python2}
%{__python2} -bb -m pytest %{srcname}/test*.py
%endif
%if %{with python3}
%{__python3} -bb -m pytest %{srcname}/test*.py
%endif


%install
%if %{with python2}
%py2_install
rm -rf %{buildroot}%{_docdir}/%{srcname}
rm -rf %{buildroot}%{python2_sitelib}/%{srcname}/tests{,-cookbook}.py*
%endif
%if %{with python3}
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/tests{,-cookbook}.py*
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/__pycache__/tests{,-cookbook}.*.py*
%endif
rm -rf %{buildroot}/usr/share/doc/jwcrypto

%if %{with python2}
%files -n python2-%{srcname}
%doc README.md
%license LICENSE
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%endif


%changelog
* Fri Jun 17 2022 Christian Heimes <cheimes@redhat.com> - 0.5.0-1.1
- Bump dist to solve version sorting issue, fixes RHBZ#2097800

* Thu Jun 28 2018 Christian Heimes <cheimes@redhat.com> - 0.5.0-1
- New upstream release 0.5.0
- Fixes Coverity scan issue

* Mon Apr 16 2018 Christian Heimes <cheimes@redhat.com> - 0.4.2-5
- Drop Python 2 subpackages from RHEL 8, fixes RHBZ#1567152

* Thu Nov 23 2017 Christian Heimes <cheimes@redhat.com> - 0.4.2-4
- Build Python 3 package on RHEL > 7, fixes RHBZ#1516813

* Wed Aug 02 2017 Christian Heimes <cheimes@redhat.com> - 0.4.2-3
- Run tests with bytes warning

* Tue Aug 01 2017 Christian Heimes <cheimes@redhat.com> - 0.4.2-2
- Modernize spec

* Tue Aug 01 2017 Christian Heimes <cheimes@redhat.com> - 0.4.2-1
- Upstream release 0.4.2
- Resolves: RHBZ #1476150

* Mon Jul 24 2017 Christian Heimes <cheimes@redhat.com> - 0.4.1-1
- Upstream release 0.4.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-2
- Rebuild for Python 3.6

* Wed Aug 31 2016 Simo Sorce <simo@redhat.com> - 0.3.2-1
- Security release 0.3.2
- Resolves: CVE-2016-6298

* Fri Aug 19 2016 Simo Sorce <simo@redhat.com> - 0.3.1-1
- Bugfix release 0.3.1

* Wed Aug 10 2016 Simo Sorce <simo@redhat.com> - 0.3.0-1
- New release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Aug  3 2015 Simo Sorce <simo@redhat.com> - 0.2.1-1
- New release
- Fixes some key generation issues

* Mon Jun 22 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.2.0-5
- Fix macro in changelog
- Remove the last remnants of the test suite

* Wed Jun 17 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.2.0-4
- Ship readme and license with python3 subpackage
- Move tests to %%check

* Wed Jun 17 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.2.0-3
- Fix F21 build error by adding buildrequire python-setuptools
- Move files into python3-jwcrypto subpackage
- Run test suite
- Do not install test suite
- Fix summary and description of python3-jwcrypto

* Tue Jun 16 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.2.0-2
- Enable python3 build

* Tue Jun 16 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.2.0-1
- Initial packaging
