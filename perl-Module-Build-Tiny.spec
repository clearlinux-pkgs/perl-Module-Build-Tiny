#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Module-Build-Tiny
Version  : 0.051
Release  : 35
URL      : https://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-Tiny-0.051.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-Tiny-0.051.tar.gz
Summary  : 'A tiny replacement for Module::Build'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Module-Build-Tiny-license = %{version}-%{release}
Requires: perl-Module-Build-Tiny-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Module-Build-Tiny,
version 0.051:
A tiny replacement for Module::Build

%package dev
Summary: dev components for the perl-Module-Build-Tiny package.
Group: Development
Provides: perl-Module-Build-Tiny-devel = %{version}-%{release}
Requires: perl-Module-Build-Tiny = %{version}-%{release}

%description dev
dev components for the perl-Module-Build-Tiny package.


%package license
Summary: license components for the perl-Module-Build-Tiny package.
Group: Default

%description license
license components for the perl-Module-Build-Tiny package.


%package perl
Summary: perl components for the perl-Module-Build-Tiny package.
Group: Default
Requires: perl-Module-Build-Tiny = %{version}-%{release}

%description perl
perl components for the perl-Module-Build-Tiny package.


%prep
%setup -q -n Module-Build-Tiny-0.051
cd %{_builddir}/Module-Build-Tiny-0.051

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Module-Build-Tiny
cp %{_builddir}/Module-Build-Tiny-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Module-Build-Tiny/83ea5587776238d07e8f5f3f26a5b92192cf9536 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Module::Build::Tiny.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Module-Build-Tiny/83ea5587776238d07e8f5f3f26a5b92192cf9536

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
