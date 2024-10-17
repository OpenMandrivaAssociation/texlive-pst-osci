Name:		texlive-pst-osci
Version:	15878
Release:	2
Summary:	Oscgons with PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-osci
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-osci.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-osci.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
