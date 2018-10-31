# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-osci
# catalog-date 2008-10-08 15:45:53 +0200
# catalog-license lppl
# catalog-version 2.82
Name:		texlive-pst-osci
Version:	2.82
Release:	11
Summary:	Oscgons with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-osci
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-osci.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-osci.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
pst-osci is a PSTricks package enables you to produce
oscilloscope "screen shots". Three channels can be used to
represent the most common signals (damped or not): namely
sinusoidal, rectangular, triangular, dog's tooth (left and
right oriented). The third channel allows you to add, to
subtract or to multiply the two other signals. Lissajous
diagrams (XY-mode) can also be obtained.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-osci/pst-osci.tex
%{_texmfdistdir}/tex/latex/pst-osci/pst-osci.sty
%doc %{_texmfdistdir}/doc/generic/pst-osci/Changes
%doc %{_texmfdistdir}/doc/generic/pst-osci/README
%doc %{_texmfdistdir}/doc/generic/pst-osci/oscilloscope.pdf
%doc %{_texmfdistdir}/doc/generic/pst-osci/oscilloscope.tex
%doc %{_texmfdistdir}/doc/generic/pst-osci/pst-osci-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-osci/pst-osci-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.82-2
+ Revision: 755392
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.82-1
+ Revision: 719376
- texlive-pst-osci
- texlive-pst-osci
- texlive-pst-osci
- texlive-pst-osci

