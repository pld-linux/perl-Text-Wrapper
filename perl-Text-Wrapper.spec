%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Wrapper
Summary:	Text::Wrapper perl module
Summary(pl):	Modu³ perla Text::Wrapper
Name:		perl-Text-Wrapper
Version:	1.000
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Wrapper - provides simple word wrapping.

%description -l pl
Text::Wrapper udostêpnia proste zawijanie linii.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Text/Wrapper.pm
%{_mandir}/man3/*
