Summary:	Run a program as another user
Name:		dropto
Version:	0.3.1
Release:	2
License:	GPL v3
Group:		Base/Utilities
Source0:	http://users.ox.ac.uk/~tom/source/dropto/%{name}-%{version}.tar.gz
# Source0-md5:	1c22adbe6c10c91a1037a8d5dd8220f8
URL:		http://users.ox.ac.uk/~tom/dropto/dropto.8
BuildRequires:	asciidoc
BuildRequires:	xmlto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# don't clobber user path with progs that need root
%define		_bindir		%{_sbindir}

%description
Privilege-dropping exec()er in the spirit of setuidgid, but with
supplementary group membership.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README THANKS
%attr(755,root,root) %{_bindir}/dropto
%{_mandir}/man8/dropto.8*
