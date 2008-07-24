%define module  Term-Report
%define name    perl-%{module}
%define version 1.18
%define release %mkrel 9

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Easy way to create dynamic 'reports' from within scripts
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Term/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description 
Term::Report can be used to generate nicely formatted dynamic output. It can
also use Term::StatusBar to show progress and Number::Format so numbers show up
more readable. All output is sent to STDOUT by default.

The current release may not be compatible with previous code. Many changes were
made with regards to how output could be formatted.

%prep
%setup -q -n %{module}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Term*
%{_mandir}/*/*

