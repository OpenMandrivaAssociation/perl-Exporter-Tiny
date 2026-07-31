%define upstream_name    Exporter-Tiny
# Avoid nasty build dependency loop
%define dont_gprintify 1

Name:       perl-%{upstream_name}
Version:    1.006003
Release:    1

Summary:    Shortcut for Exporter::Tiny
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/pod/Exporter::Tiny
Source0:    http://www.cpan.org/modules/by-module/Exporter/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires: perl-devel
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Warnings)
BuildRequires: perl(Test::Fatal)

BuildArch: noarch

%description
Exporter::Tiny supports many of Sub::Exporter's external-facing features
including renaming imported functions with the '-as', '-prefix' and
'-suffix' options; explicit destinations with the 'into' option; and
alternative installers with the 'installler' option. But it's written in
only about 40% as many lines of code and with zero non-core dependencies.

Its internal-facing interface is closer to Exporter.pm, with configuration
done through the '@EXPORT', '@EXPORT_OK' and 
#'%EXPORT_TAGS' package (is being seen asunexpanded macro in linting, sflo)
variables.

Exporter::Tiny performs most of its internal duties (including resolution
of tag names to sub names, resolution of sub names to coderefs, and
installation of coderefs into the target package) as method calls, which
means they can be overridden to provide interesting behaviour.

%prep
%setup -qn %{upstream_name}-%{version} -n Exporter-Tiny-1.006003

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.json META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

