#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : numpy
Version  : 1.14.5
Release  : 120
URL      : http://pypi.debian.net/numpy/numpy-1.14.5.zip
Source0  : http://pypi.debian.net/numpy/numpy-1.14.5.zip
Summary  : NumPy: array processing for numbers, strings, records, and objects.
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause BSD-3-Clause-Clear Python-2.0
Requires: numpy-bin
Requires: numpy-python3
Requires: numpy-license
Requires: numpy-python
Requires: Jinja2
Requires: Sphinx
Requires: gcc-libs-math
Requires: openblas
BuildRequires : Cython
BuildRequires : Jinja2
BuildRequires : Sphinx
BuildRequires : gfortran
BuildRequires : openblas
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-core
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
Patch1: build.patch
Patch2: avx2-distutils.patch
Patch3: avx2-fortran-distutils.patch
Patch4: timestamp.patch
Patch5: cve-2017-12852.nopatch
Patch6: use-avx2-instructions.patch
Patch7: use-avx512f-for-numpy-SIMD-instructions.patch

%description
efficiently manipulate large multi-dimensional arrays of arbitrary
        records without sacrificing too much speed for small multi-dimensional
        arrays.  NumPy is built on the Numeric code base and adds features
        introduced by numarray as well as an extended C-API and the ability to
        create arrays of arbitrary type which also makes NumPy suitable for
        interfacing with general-purpose data-base applications.
        
        There are also basic facilities for discrete fourier transform,
        basic linear algebra and random number generation.
        
        All numpy wheels distributed from pypi are BSD licensed.
        
        Windows wheels are linked against the ATLAS BLAS / LAPACK library, restricted
        to SSE2 instructions, so may not give optimal linear algebra performance for

%package bin
Summary: bin components for the numpy package.
Group: Binaries
Requires: numpy-license

%description bin
bin components for the numpy package.


%package dev
Summary: dev components for the numpy package.
Group: Development
Requires: numpy-bin
Provides: numpy-devel

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
Requires: numpy-python3

%description python
python components for the numpy package.


%package python3
Summary: python3 components for the numpy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the numpy package.


%prep
%setup -q -n numpy-1.14.5
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530326700
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
python2 setup.py build -b py2 --fcompiler=gnu95
python3 setup.py build -b py3 --fcompiler=gnu95

%install
export SOURCE_DATE_EPOCH=1530326700
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/numpy
cp LICENSE.txt %{buildroot}/usr/share/doc/numpy/LICENSE.txt
cp doc/sphinxext/LICENSE.txt %{buildroot}/usr/share/doc/numpy/doc_sphinxext_LICENSE.txt
cp doc/source/license.rst %{buildroot}/usr/share/doc/numpy/doc_source_license.rst
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
/usr/bin/f2py3

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

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/numpy/LICENSE.txt
/usr/share/doc/numpy/doc_source_license.rst
/usr/share/doc/numpy/doc_sphinxext_LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
