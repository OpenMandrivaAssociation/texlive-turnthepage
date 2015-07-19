# revision 29803
# category Package
# catalog-ctan /macros/latex/contrib/turnthepage
# catalog-date 2012-08-19 17:38:37 +0200
# catalog-license lppl
# catalog-version 1.3a
Name:		texlive-turnthepage
Version:	1.3a
Release:	11
Summary:	Provide "turn page" instructions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/turnthepage
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/turnthepage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/turnthepage.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package prints a 'turn' instruction at the bottom of odd-
numbered pages (except the last). This is a common convention
for examination papers and the like.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/turnthepage/turnpageetex.sty
%{_texmfdistdir}/tex/latex/turnthepage/turnpagewoetex.sty
%{_texmfdistdir}/tex/latex/turnthepage/turnthepage.sty
%doc %{_texmfdistdir}/doc/latex/turnthepage/Makefile
%doc %{_texmfdistdir}/doc/latex/turnthepage/README
%doc %{_texmfdistdir}/doc/latex/turnthepage/perso.ist
%doc %{_texmfdistdir}/doc/latex/turnthepage/turnthepage-bib.bib
%doc %{_texmfdistdir}/doc/latex/turnthepage/turnthepage.pdf
%doc %{_texmfdistdir}/doc/latex/turnthepage/turnthepage.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
