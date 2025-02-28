Name:		texlive-turnthepage
Version:	29803
Release:	2
Summary:	Provide "turn page" instructions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/turnthepage
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/turnthepage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/turnthepage.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
