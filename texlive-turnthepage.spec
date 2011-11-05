# revision 23784
# category Package
# catalog-ctan /macros/latex/contrib/turnthepage
# catalog-date 2011-03-24 23:15:02 +0100
# catalog-license lppl
# catalog-version 1.3a
Name:		texlive-turnthepage
Version:	1.3a
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package prints a 'turn' instruction at the bottom of odd-
numbered pages (except the last). This is a common convention
for examination papers and the like.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
