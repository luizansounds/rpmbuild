Name:       lu-blue  
Version:        1
Release:        1
Summary:        i neeeeeeed

License:        GPL3
URL:            https://github.com/Luiza1011/lu-dotfiles/tree/main
Source0:        lu-blue-1.tar.gz
%description
gibbbbbbbb

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp lu-blue-1 $RPM_BUILD_ROOT/%{_bindir}
chmod 775 lu-blue-1

%files
%{_bindir}/lu-blue-1

%changelog
* Wed Aug 30 2023 lblue-install
- 
