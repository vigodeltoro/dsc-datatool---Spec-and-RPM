Name: dsc-datatool		
Version: 0.02 
Release: 1%{?dist}
Summary: Domain Statistics Collector Datatool
Group: Monitoring software		
License: GPL
Source: v%{version}.tar.gz
URL: https://github.com/DNS-OARC/dsc-datatool/archive
BuildRoot: %{_tmppath}/%{name}


Requires: epel-release perl-Module-Find perl-libxml-perl perl-YAML-Tiny perl-common-sense perl-NetAddr-IP perl-IP-Country perl-XML-LibXML-Simple	

%description
DSC Datatool - Tool for converting, exporting, merging and transforming DSC data 

%prep
cd /root/rpmbuild/SOURCES/
tar -xvf v%{version}.tar.gz

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/lib64/perl5

cp /root/rpmbuild/SOURCES/%{name}-%{version}/bin/dsc-datatool $RPM_BUILD_ROOT/usr/local/bin
cp -R /root/rpmbuild/SOURCES/%{name}-%{version}/lib/App $RPM_BUILD_ROOT/usr/lib64/perl5


%clean
rm -rf $RPM_BUILD_ROOT
rm -rf /root/rpmbuild/SOURCES/%{name}-%{version}

%files

%defattr(-,root,root)
%attr(0755,root,root) /usr/local/bin/dsc-datatool
%attr(0755,root,root) /usr/lib64/perl5/App

%changelog
