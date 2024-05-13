Name:           python3-hid
Version:        1000.{{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        hidapi bindings in ctypes
License:        MIT
URL:            https://github.com/KyleGospo/python3-hid

Source:         {{{ git_dir_pack }}}
BuildArch:      noarch
	
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
Requires:       hidapi

%description
Python hidapi bindings in ctypes (aka pyhidapi)

# Disable debug packages
%define debug_package %{nil}

%prep
{{{ git_dir_setup_macro }}}

%build
%{python3} setup.py build

%install
%{python3} setup.py install --skip-build -O1 --root="%{buildroot}"

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/hid-*.egg-info/
%{python3_sitelib}/hid/

%changelog
{{{ git_dir_changelog }}}
