%include	/usr/lib/rpm/macros.perl
Summary:	Text-Wrapper perl module
Summary(pl):	Modu³ perla Text-Wrapper
Name:		perl-Text-Wrapper
Version:	1.000
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-Wrapper-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-Wrapper - provides simple word wrapping.

%description -l pl
Text-Wrapper udostêpnia proste zawijanie linii.

%prep
%setup -q -n Text-Wrapper-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Text/Wrapper.pm
%{_mandir}/man3/*
