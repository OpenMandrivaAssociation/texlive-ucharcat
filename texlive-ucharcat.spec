Name:		texlive-ucharcat
Version:	38907
Release:	2
Summary:	Implementation of the (new in 2015) XeTeX \Ucharcat command in lua, for LuaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ucharcat
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucharcat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucharcat.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucharcat.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package implements the \Ucharcat command for LuaLaTeX.
\Ucharcat is a new primitive in XeTeX, an extension of the
existing \Uchar command, that allows the specification of the
catcode as well as character code of the character token being
constructed.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/ucharcat
%{_texmfdistdir}/tex/latex/ucharcat
%doc %{_texmfdistdir}/doc/latex/ucharcat

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
