%define idmetaversion %(. ./IDMETA; printf $VERSION )
Summary: XQuery Processor
Name: idzorba
Version: %{idmetaversion}
Release: 1.indexdata
BuildRequires: cmake
BuildRequires: gcc gcc-c++ pkgconfig
BuildRequires: wget
BuildRequires: xerces-c-devel
BuildRequires: libcurl-devel
BuildRequires: libxslt-devel
BuildRequires: libuuid-devel
BuildRequires: boost-devel
BuildRequires: libicu-devel
License: Apache
Group: Applications/Internet
Vendor: Index Data ApS <info@indexdata.dk>
Source: idzorba-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Packager: Adam Dickmeiss <adam@indexdata.dk>
URL: http://www.zorba.io/

%description
Zorba - The XQuery Processor developed by the FLWOR Foundation

Requires: libcurl
Requires: xerces-c

%prep
%setup
rm -fr tmp
mkdir tmp; cd tmp
wget http://ftp.indexdata.dk/pub/support/zorba-3.1.d3870d.tar.gz
tar zxf zorba-3.1.d3870d.tar.gz

%build
cd tmp/zorba-3.1
mkdir build
cd build
cmake \
	-Wno-dev \
	-D CMAKE_INSTALL_PREFIX=/opt/idzorba \
	-D ZORBA_SUPPRESS_SWIG:BOOL=ON \
	..
cd ../../..

%install
cd tmp/zorba-3.1/build
rm -fr ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} install
cd ../../..

%clean
rm -fr ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
/opt/idzorba
