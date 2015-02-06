%define upstream_name 	 XML-Records
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	%{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(XML::TokeParser)
BuildArch:	noarch

%description
%{upstream_name} - module for perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
%makeinstall_std

%files
%doc README MANIFEST Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML


%changelog
* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.0
+ Revision: 408245
- rebuild using %%perl_convert_version

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.12-10mdv2009.0
+ Revision: 258879
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.12-9mdv2009.0
+ Revision: 246779
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.12-7mdv2008.1
+ Revision: 136367
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.12-7mdv2008.0
+ Revision: 23501
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.12-6mdk
- Fix According to perl Policy
	- Source URL
	- URL
	- BuildRequires
- use mkrel

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.12-5mdk
- rebuild
- Own dir

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.12-4mdk
- rebuild for new auto{prov,req}

