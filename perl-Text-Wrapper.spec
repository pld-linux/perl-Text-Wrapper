#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Wrapper
Summary:	Text::Wrapper - simple word wrapping routine
Summary(pl):	Text::Wrapper - proste zawijanie linii
Name:		perl-Text-Wrapper
Version:	1.000
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9f78b13b4c32c61e6aac5cefd75989dd
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Wrapper Perl Module provides simple word wrapping.  It breaks
long lines, but does not alter spacing or remove existing line breaks. 
If you're looking for more sophisticated text formatting, try the
Text::Format module.

%description -l pl
Modu³ Perla Text::Wrapper udostêpnia proste zawijanie wierszy. £amie
d³ugie wiersz, ale nie zmienia odstêpów ani nie usuwa istniej±cych
znaków nowego wiersza. Bardziej wyszukane formatowanie tekstu jest
mo¿liwe przy zastosowaniu modu³u Text::Format.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Text/Wrapper.pm
%{_mandir}/man3/*
