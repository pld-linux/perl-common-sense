# $Revision:
#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	common
%define	pnam	sense
Summary:	common::sense - save a tree AND a kitten, use common::sense!
Summary(pl.UTF-8):	common::sense - dostarcza zdroworozsądkowe ustawienia domyślne
Name:		perl-common-sense
Version:	3.0
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	43e50e48f465f616b82837a09101a566
URL:		http://search.cpan.org/dist/Devel-FindRef/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements some sane defaults for Perl programs, as
defined by two typical (or not so typical - use your common sense)
specimens of Perl coders.

%description -l pl.UTF-8
Moduł ten implementuje pewne zdroworozsądkowe ustawienia domyślne dla
programów perlowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/common
%{perl_vendorlib}/common/sense.pm
%{_mandir}/man3/common::sense.3pm*
