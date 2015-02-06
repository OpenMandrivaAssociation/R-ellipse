%global packname  ellipse
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Epoch:            1
Version:          0.3.8
Release:          2
Summary:          Functions for drawing ellipses and ellipse-like confidence regions
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/ellipse_0.3-8.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-graphics
Requires:         R-stats 
BuildRequires:    R-devel
BuildRequires:    Rmath-devel
BuildRequires:    texlive-collection-latex
BuildRequires:    R-graphics
BuildRequires:    R-stats
BuildRequires:    pkgconfig(lapack)
%rename R-cran-ellipse

%description
This package contains various routines for drawing ellipses and
ellipse-like confidence regions, implementing the plots described in
Murdoch and Chow (1996), A graphical display of large correlation
matrices, The American Statistician 50, 178-180. There are also routines
implementing the profile plots described in Bates and Watts (1988),
Nonlinear Regression Analysis and its Applications.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:0.3_5-1
+ Revision: 775045
- Update to latest version
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:0.3_4-1
+ Revision: 774848
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.5-3mdv2011.0
+ Revision: 616448
- the mass rebuild of 2010.0 packages

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 0.3.5-2mdv2010.0
+ Revision: 433081
- rebuild

* Wed Jun 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.5-1mdv2009.0
+ Revision: 228933
- import R-cran-ellipse


