%define upstream_name    Term-Report
%define upstream_version 1.18

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Easy way to create dynamic 'reports' from within scripts
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description 
Term::Report can be used to generate nicely formatted dynamic output. It can
also use Term::StatusBar to show progress and Number::Format so numbers show up
more readable. All output is sent to STDOUT by default.

The current release may not be compatible with previous code. Many changes were
made with regards to how output could be formatted.

%prep
%setup -q -n %{upstream_name}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Term*
%{_mandir}/*/*

%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 1.180.0-2mdv2011.0
+ Revision: 664911
- mass rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.180.0-1mdv2010.0
+ Revision: 405541
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.18-10mdv2009.0
+ Revision: 258508
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.18-9mdv2009.0
+ Revision: 246523
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.18-7mdv2008.1
+ Revision: 136360
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.18-7mdv2008.0
+ Revision: 86965
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.18-6mdv2007.0
- Rebuild

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.18-5mdk
- Fix SPEC according to Perl Policy
    - Source URL

* Fri Dec 16 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.18-4mdk
- spec cleanup
- %%mkrel

* Wed Dec 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.18-3mdk 
- fix buildrequires in a backward compatible way

* Mon Nov 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.18-2mdk 
- fix buildrequires

* Thu Nov 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.18-1mdk 
- first mdk release

