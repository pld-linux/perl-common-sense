#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	common
%define	pnam	sense
Summary:	common::sense - save a tree AND a kitten, use common::sense!
Summary(pl.UTF-8):	common::sense - zdroworozsądkowe ustawienia domyślne dla programów w Perlu
Name:		perl-common-sense
Version:	3.6
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/ML/MLEHMANN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9332e9fe85b0bce8c287a0429d164809
URL:		http://search.cpan.org/dist/common-sense/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
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
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%dir %{perl_vendorlib}/common
%{perl_vendorlib}/common/sense.pm
%{_mandir}/man3/common::sense.3pm*
