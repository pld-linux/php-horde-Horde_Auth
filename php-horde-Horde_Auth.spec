%define		status		stable
%define		pearname	Horde_Auth
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde Authentication API
Name:		php-horde-Horde_Auth
Version:	1.4.9
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	9ff8e925a46a203046173eea82480055
URL:		https://github.com/horde/horde/tree/master/framework/Auth/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(hash)
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-ctype
Suggests:	php-ftp
Suggests:	php-horde-Horde_Db
Suggests:	php-horde-Horde_History
Suggests:	php-horde-Horde_Http
Suggests:	php-horde-Horde_Imap_Client
Suggests:	php-horde-Horde_Imsp
Suggests:	php-horde-Horde_Kolab_Session
Suggests:	php-horde-Horde_Ldap
Suggests:	php-horde-Horde_Lock
Suggests:	php-pecl-pam
Suggests:	php-pecl-sasl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Db.*) pear(Horde/Imap/Client.*) pear(Horde/Kolab/Session.*) pear(Horde/Ldap.*) pear(Horde/Imsp.*) pear(Horde/Http.*) pear(pam.*) pear(sasl.*)

%description
The Horde_Auth package provides a common interface into the various
backends for the Horde authentication system.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Auth.php
%{php_pear_dir}/Horde/Auth
%{php_pear_dir}/data/Horde_Auth
