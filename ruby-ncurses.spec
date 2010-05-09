%define rname ncurses
%define name  ruby-%{rname}
%define oname %{rname}-ruby

%define version 1.2.2
%define release %mkrel 2

Summary: Ruby interface for the ncurses text library
Name: %name
Version: %version
Release: %release
License: LGPLv2+
Group: Development/Ruby
URL: http://ncurses-ruby.berlios.de/
Source0: http://download.berlios.de/ncurses-ruby/%{oname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ruby-devel ncurses-devel 
Provides: %{oname}


%description
Ruby interface for the ncurses text library.

%prep
%setup -q -n %{oname}-%{version}

%build
ruby extconf.rb
make

%clean
rm -rf %buildroot

%install
rm -rf %buildroot
make install DESTDIR=%buildroot

%files
%defattr(-,root,root)
%doc VERSION TODO THANKS README Changes  
%ruby_sitelibdir/*.rb
%ruby_sitearchdir/*.so


