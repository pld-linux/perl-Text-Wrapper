%define	pdir	Text
%define	pnam	Wrapper
%include	/usr/lib/rpm/macros.perl
Summary:	Text-Wrapper perl module
Summary(pl):	Modu� perla Text-Wrapper
Name:		perl-Text-Wrapper
Version:	1.000
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-Wrapper - provides simple word wrapping.

%description -l pl
Text-Wrapper udost�pnia proste zawijanie linii.

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
