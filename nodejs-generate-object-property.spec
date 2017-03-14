%{?scl:%scl_package nodejs-%{srcname}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global srcname generate-object-property

Name:           %{?scl_prefix}nodejs-%{srcname}
Version:        1.2.0
Release:        3%{?dist}
Summary:        Generate safe JS code that can used to reference a object property
License:        MIT
URL:            https://github.com/mafintosh/generate-object-property
Source0:        https://registry.npmjs.org/%{srcname}/-/%{srcname}-%{version}.tgz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(is-property)
BuildRequires:  %{?scl_prefix}npm(tape)
%endif

%description
%{summary}.

%prep
%setup -q -n package
rm -rf node_modules/

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/%{srcname}

%nodejs_symlink_deps


%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
tape test.js
%endif

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{srcname}

%changelog
* Mon Jan 16 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.0-3
- Rebuild for rhscl

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.2.0-1
- Initial package
