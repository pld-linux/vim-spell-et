%define		dict	et_EE
Summary:	Estonian dictionaries for VIMspell
Name:		vim-spell-et
Version:	1.0
Release:	3
License:	free, see http://www.eki.ee/eki/licence.html
Group:		Applications/Editors/Vim
BuildRequires:	myspell-%{dict}
BuildRequires:	unzip
BuildRequires:	vim >= 4:7.0
Requires:	vim-rt >= 4:7.2.170
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
Estonian dictionaries for VIMspell.

%prep
%setup -qcT
# fails if myspell package installed without doc
cp -a %{_docdir}/myspell-%{dict}-$(rpm -q --qf %{V} myspell-%{dict})/README_et_EE.txt* .
[ *.gz ] && gzip -d *.gz

%build
vim -u NONE -c 'set enc=utf-8' -c 'mkspell! et %{_datadir}/myspell/et_EE' -c q

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
