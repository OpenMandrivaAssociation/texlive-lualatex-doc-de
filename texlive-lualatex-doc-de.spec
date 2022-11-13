Name:		texlive-lualatex-doc-de
Version:	30474
Release:	1
Summary:	Guide to LuaLaTeX (German translation)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/luatex/lualatex-doc-de
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-doc-de.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-doc-de.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The document is a German translation of the map/guide to the
world of LuaLaTeX. Coverage supports both new users and package
developers. Apart from the introductory material, the document
gathers information from several sources, and offers links to
others.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lualatex-doc-de/lualatex-doc-DE.pdf
%doc %{_texmfdistdir}/doc/latex/lualatex-doc-de/lualatex-doc-DE.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
