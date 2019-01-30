#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : numpy
Version  : 1.16.0
Release  : 142
URL      : https://files.pythonhosted.org/packages/04/b6/d7faa70a3e3eac39f943cc6a6a64ce378259677de516bd899dd9eb8f9b32/numpy-1.16.0.zip
Source0  : https://files.pythonhosted.org/packages/04/b6/d7faa70a3e3eac39f943cc6a6a64ce378259677de516bd899dd9eb8f9b32/numpy-1.16.0.zip
Summary  : NumPy is the fundamental package for array computing with Python.
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause MIT Python-2.0
Requires: numpy-bin = %{version}-%{release}
Requires: numpy-license = %{version}-%{release}
Requires: numpy-python = %{version}-%{release}
Requires: numpy-python3 = %{version}-%{release}
Requires: gcc-libs-math
Requires: matplotlib
Requires: nose
Requires: numpy
Requires: openblas
Requires: pytest-timeout
Requires: pytest-xdist
BuildRequires : Cython
BuildRequires : Jinja2
BuildRequires : Sphinx
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3
BuildRequires : gfortran
BuildRequires : openblas
BuildRequires : python-core
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools-legacypython
Patch1: build.patch
Patch2: avx2-distutils.patch
Patch3: avx2-fortran-distutils.patch
Patch4: timestamp.patch
Patch5: cve-2017-12852.nopatch
Patch6: CVE-2019-6446.patch

%description
- a powerful N-dimensional array object
        - sophisticated (broadcasting) functions
        - tools for integrating C/C++ and Fortran code
        - useful linear algebra, Fourier transform, and random number capabilities
        - and much more
        
        Besides its obvious scientific uses, NumPy can also be used as an efficient
        multi-dimensional container of generic data. Arbitrary data-types can be
        defined. This allows NumPy to seamlessly and speedily integrate with a wide
        variety of databases.
        
        All NumPy wheels distributed on PyPI are BSD licensed.

%package bin
Summary: bin components for the numpy package.
Group: Binaries
Requires: numpy-license = %{version}-%{release}

%description bin
bin components for the numpy package.


%package dev
Summary: dev components for the numpy package.
Group: Development
Requires: numpy-bin = %{version}-%{release}
Provides: numpy-devel = %{version}-%{release}

%description dev
dev components for the numpy package.


%package extras
Summary: extras components for the numpy package.
Group: Default

%description extras
extras components for the numpy package.


%package legacypython
Summary: legacypython components for the numpy package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the numpy package.


%package license
Summary: license components for the numpy package.
Group: Default

%description license
license components for the numpy package.


%package python
Summary: python components for the numpy package.
Group: Default
Requires: numpy-python3 = %{version}-%{release}

%description python
python components for the numpy package.


%package python3
Summary: python3 components for the numpy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the numpy package.


%prep
%setup -q -n numpy-1.16.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548891339
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
python2 setup.py build -b py2 --fcompiler=gnu95
python3 setup.py build -b py3 --fcompiler=gnu95

%install
export SOURCE_DATE_EPOCH=1548891339
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/numpy
cp doc/scipy-sphinx-theme/LICENSE.txt %{buildroot}/usr/share/package-licenses/numpy/doc_scipy-sphinx-theme_LICENSE.txt
cp doc/source/license.rst %{buildroot}/usr/share/package-licenses/numpy/doc_source_license.rst
cp doc/sphinxext/LICENSE.txt %{buildroot}/usr/share/package-licenses/numpy/doc_sphinxext_LICENSE.txt
cp tools/npy_tempita/license.txt %{buildroot}/usr/share/package-licenses/numpy/tools_npy_tempita_license.txt
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/f2py2
%exclude /usr/bin/f2py2.7
/usr/bin/f2py
/usr/bin/f2py3
/usr/bin/f2py3.7

%files dev
%defattr(-,root,root,-)
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/__multiarray_api.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/__ufunc_api.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/_neighborhood_iterator_imp.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/_numpyconfig.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/arrayobject.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/arrayscalars.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/halffloat.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/ndarrayobject.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/ndarraytypes.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/noprefix.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/npy_3kcompat.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/npy_common.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/npy_cpu.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/npy_endian.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/npy_interrupt.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/npy_math.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/npy_no_deprecated_api.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/npy_os.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/numpyconfig.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/old_defines.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/oldnumeric.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/ufuncobject.h
/usr/lib/python2.7/site-packages/numpy/core/include/numpy/utils.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/__multiarray_api.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/__ufunc_api.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/_neighborhood_iterator_imp.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/_numpyconfig.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/arrayscalars.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/halffloat.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/noprefix.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/npy_3kcompat.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/npy_common.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/npy_cpu.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/npy_endian.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/npy_interrupt.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/npy_math.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/npy_no_deprecated_api.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/npy_os.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/numpyconfig.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/old_defines.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/oldnumeric.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/ufuncobject.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/utils.h

%files extras
%defattr(-,root,root,-)
/usr/bin/f2py2
/usr/bin/f2py2.7

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/numpy/doc_scipy-sphinx-theme_LICENSE.txt
/usr/share/package-licenses/numpy/doc_source_license.rst
/usr/share/package-licenses/numpy/doc_sphinxext_LICENSE.txt
/usr/share/package-licenses/numpy/tools_npy_tempita_license.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
