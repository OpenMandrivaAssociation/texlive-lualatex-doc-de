# revision 30474
# category Package
# catalog-ctan /info/luatex/lualatex-doc-de
# catalog-date 2013-05-14 17:57:54 +0200
# catalog-license fdl
# catalog-version 1.0
Name:		texlive-lualatex-doc-de
Version:	1.0
Release:	4
Summary:	Guide to LuaLaTeX (German translation)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/luatex/lualatex-doc-de
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-doc-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-doc-de.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
