%define _prefix /usr/ant

Name:		apache-ant
Version:	%{ver}
Release:	2%{?dist}
Summary:	Apache ant
License:	Apache
URL:		http://ant.apache.org
Source: 	http://apache.mogo.be/ant/binaries/apache-ant-%{version}-bin.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch
Requires: java-1.7.0-openjdk

%description
%{summary}
%
%prep
%setup -q -n apache-ant-%{version}


%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_prefix}
cp -r bin etc lib %{buildroot}%{_prefix}
mkdir %{buildroot}/usr/sbin
ln -sf %{_prefix}/bin/ant %{buildroot}/usr/sbin/ant

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}
/usr/sbin/ant

%changelog
* Fri Sep 14 2012 Patrick Wong <patrick.k.wong@rrd.com>
- Some additions so that it is more usable
* Thu Mar 1 2012 Jean-Francois Roche <jfroche@affinitic.be>
- Initial implementation
