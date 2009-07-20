Summary:	Estonian dictionaries for VIMspell
Name:		vim-spell-et
Version:	1.0
Release:	1
License:    free, see http://www.eki.ee/eki/licence.html
Group:		Applications/Editors/Vim
Source0:	ftp://ftp.linux.ee/pub/openoffice/contrib/dictionaries/et_EE.zip
# Source0-md5:	2a1e97d61132c537aa03df4d0fee9b89
URL:		http://www.sjp.pl/slownik/ort/
BuildRequires:	unzip
BuildRequires:	vim >= 4:7.0
Requires:	vim-rt >= 4:7.0.017-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
Estonian dictionaries for VIMspell.

%prep
%setup -q -c

%build
vim -u NONE -c 'set enc=utf-8' -c 'mkspell! et et_EE' -c q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/spell
cp -a *.spl $RPM_BUILD_ROOT%{_vimdatadir}/spell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README_et_EE.txt
%{_vimdatadir}/spell/et.*.spl
