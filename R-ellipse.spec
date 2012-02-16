%global packname  ellipse
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Epoch:            1
Version:          0.3_4
Release:          1
Summary:          Functions for drawing ellipses and ellipse-like confidence regions
Group:            Sciences/Mathematics
License:          This library was written by D. J. Murdoch and E. D. Chow. This software is licensed under the GPL terms. It is free software and comes with ABSOLUTELY NO WARRANTY.
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/Archive/%{packname}/%{packname}_0.3-4.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-graphics R-stats 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-graphics R-stats
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