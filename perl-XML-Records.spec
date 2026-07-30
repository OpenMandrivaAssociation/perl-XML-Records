%define upstream_name 	 XML-Records
%define upstream_version 0.12
Name:		perl-%{upstream_name}
Version:	0.12
Release:	2

Summary:	%{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-Records
Source0:	https://cpan.metacpan.org/authors/id/E/EB/EBOHLMAN/XML-Records-0.12.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(XML::TokeParser)
BuildArch:	noarch

%description
%{upstream_name} - module for perl

%prep
%setup -q -n XML-Records-0.12

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
%makeinstall_std

%files
%doc README MANIFEST Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML


