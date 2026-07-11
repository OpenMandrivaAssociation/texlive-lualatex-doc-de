%global tl_name lualatex-doc-de
%global tl_revision 30474

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Guide to LuaLaTeX (German translation)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/luatex/lualatex-doc-de
License:	fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-doc-de.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-doc-de.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The document is a German translation of the map/guide to the world of
LuaLaTeX. Coverage supports both new users and package developers. Apart
from the introductory material, the document gathers information from
several sources, and offers links to others.

