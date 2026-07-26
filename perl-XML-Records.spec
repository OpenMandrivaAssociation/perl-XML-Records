%define upstream_name 	 XML-Records
Name:		perl-%{upstream_name}
Version:	0.12
Release:	6

Summary:	%{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-Records
Source0:	https://cpan.metacpan.org/authors/id/E/EB/EBOHLMAN/XML-Records-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(XML::TokeParser)
BuildArch:	noarch

%description
%{upstream_name} - module for perl

%prep
%setup -q -n %{upstream_name}-%{version}

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
- rebuild using %0.12 Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.12-10mdv2009.0
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

