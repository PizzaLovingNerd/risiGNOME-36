%global extuuid		risiGNOME@risi.io
%global extdir		%{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global gitname		risiGNOME-36
%global giturl		https://github.com/pizzalovingnerd/%{gitname}
%global srcdir		%{_builddir}/%{gitname}-main

Name:		gnome-shell-extension-risi-gnome
Version:	1.0.1
Release:	10%{?dist}
Summary:	Some of risiOS GNOME changes

License:	GPLv2+
URL:		https://github.com/pizzalovingnerd/%{gitname}
Source0:	https://github.com/pizzalovingnerd/%{gitname}/archive/refs/heads/main.tar.gz


BuildArch:	noarch
BuildRequires:  glib2
Requires:	gnome-shell-extension-common
Requires:   adw-gtk-theme
Requires: adwcolor

%description
This is where we are going to put changes we want to make for the GNOME desktop.

%prep
%autosetup -n risiGNOME-36-main
rm gnome-shell-extension-risi-gnome.spec

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions
cp -ar %{srcdir} %{buildroot}%{extdir}

%files
%{extdir}

%changelog
* Thu Feb 24 2022 PizzaLovingNerd
- Spec file built
