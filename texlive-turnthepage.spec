%global tl_name turnthepage
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0a
Release:	%{tl_revision}.1
Summary:	Provide turn page instructions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/turnthepage
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/turnthepage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/turnthepage.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package prints a 'turn' instruction at the bottom of odd-numbered
pages (except the last). This is a common convention for examination
papers and the like.

