#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : numpy
Version  : 1.19.4
Release  : 187
URL      : https://files.pythonhosted.org/packages/c5/63/a48648ebc57711348420670bb074998f79828291f68aebfff1642be212ec/numpy-1.19.4.zip
Source0  : https://files.pythonhosted.org/packages/c5/63/a48648ebc57711348420670bb074998f79828291f68aebfff1642be212ec/numpy-1.19.4.zip
Summary  : NumPy is the fundamental package for array computing with Python.
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause MIT Python-2.0
Requires: numpy-bin = %{version}-%{release}
Requires: numpy-license = %{version}-%{release}
Requires: numpy-python = %{version}-%{release}
Requires: numpy-python3 = %{version}-%{release}
Requires: gcc-libs-math
Requires: openblas
BuildRequires : Cython
BuildRequires : Jinja2
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : gfortran
BuildRequires : openblas
BuildRequires : python3-dev
Patch1: avx2-distutils.patch
Patch2: avx2-fortran-distutils.patch
Patch3: timestamp.patch
Patch4: cve-2017-12852.nopatch
Patch5: 0001-AVX-Support-for-static-lib.patch
Patch6: 0001-add-numpy-benchmarks-for-pgo.patch
Patch7: 0001-make-distutils-support-PGO-options.patch

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
Requires: numpy = %{version}-%{release}

%description dev
dev components for the numpy package.


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
Provides: pypi(numpy)

%description python3
python3 components for the numpy package.


%prep
%setup -q -n numpy-1.19.4
cd %{_builddir}/numpy-1.19.4
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607986283
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build  --fcompiler=gnu95

## build_append content
export OPT_GENERATE="-fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic -lgcov"
export OPT_USE="-fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "

# doing PGO profile build
rm -rf build  # make clean
NPY_DISTUTILS_APPEND_FLAGS=1 PGO_OPTS="${OPT_GENERATE}" python3 setup.py build --fcompiler=gnu95

# profile using numpy-benchmarks
export PGO_NUMPY_LIB_PATH=`ls -d $PWD/build/lib.linux-*`
# *.so.avx512 profiling
PYTHONPATH="${PGO_NUMPY_LIB_PATH}" python3 Tools/numpy-benchmarks/benchall.py
# *.so.avx2 profiling
find -name "*.so.avx512" -exec rm {} \;
PYTHONPATH="${PGO_NUMPY_LIB_PATH}" python3 Tools/numpy-benchmarks/benchall.py
# *.so profiling
find -name "*.so.avx2" -exec rm {} \;
PYTHONPATH="${PGO_NUMPY_LIB_PATH}" python3 Tools/numpy-benchmarks/benchall.py

# using PGO to compile
rm -rf build  # make clean
NPY_DISTUTILS_APPEND_FLAGS=1 PGO_OPTS="${OPT_USE}" python3 setup.py build  --fcompiler=gnu95

## build_append end
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/numpy
cp %{_builddir}/numpy-1.19.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/numpy/f4622fbbfc7476c5302104204cf8f8ce5308531b
cp %{_builddir}/numpy-1.19.4/doc/scipy-sphinx-theme/LICENSE.txt %{buildroot}/usr/share/package-licenses/numpy/fd2e79f66abba5b94347c2df9ca6cf3584b0c517
cp %{_builddir}/numpy-1.19.4/doc/source/license.rst %{buildroot}/usr/share/package-licenses/numpy/341dccd98f25cfc90429aa52a5639159a574a0bf
cp %{_builddir}/numpy-1.19.4/doc/sphinxext/LICENSE.txt %{buildroot}/usr/share/package-licenses/numpy/df4f727b25238b8a4be050714fe3f1cb06b17f75
cp %{_builddir}/numpy-1.19.4/numpy/linalg/lapack_lite/LICENSE.txt %{buildroot}/usr/share/package-licenses/numpy/3ddf920aa10c8c6ea0c87d218af74651ea7d16d3
cp %{_builddir}/numpy-1.19.4/numpy/ma/LICENSE %{buildroot}/usr/share/package-licenses/numpy/85f84e10061f078b2cfaa62239c3a4bde1355f34
cp %{_builddir}/numpy-1.19.4/numpy/random/LICENSE.md %{buildroot}/usr/share/package-licenses/numpy/64796c34e3592909154742074f735b89171a4418
cp %{_builddir}/numpy-1.19.4/numpy/random/src/distributions/LICENSE.md %{buildroot}/usr/share/package-licenses/numpy/df1c41ca8a294222a81f70a142832d6566fbd889
cp %{_builddir}/numpy-1.19.4/numpy/random/src/mt19937/LICENSE.md %{buildroot}/usr/share/package-licenses/numpy/50faca55f553c4ecd9f20c020176ca65324d3604
cp %{_builddir}/numpy-1.19.4/numpy/random/src/pcg64/LICENSE.md %{buildroot}/usr/share/package-licenses/numpy/752f3cb872e3c7a6e096746e3648acaf2e065c96
cp %{_builddir}/numpy-1.19.4/numpy/random/src/philox/LICENSE.md %{buildroot}/usr/share/package-licenses/numpy/c107ade2df71a8954740468bbaa8b15e0ef4cb8b
cp %{_builddir}/numpy-1.19.4/numpy/random/src/sfc64/LICENSE.md %{buildroot}/usr/share/package-licenses/numpy/1e0aa0638753b29e98ff682cff77d40ee4700250
cp %{_builddir}/numpy-1.19.4/tools/npy_tempita/license.txt %{buildroot}/usr/share/package-licenses/numpy/f853f54fdd704c7d99fc6eb5c8e895f3a7764f08
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/f2py
/usr/bin/f2py3
/usr/bin/f2py3.9

%files dev
%defattr(-,root,root,-)
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/__multiarray_api.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/__ufunc_api.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/_neighborhood_iterator_imp.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/_numpyconfig.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/arrayobject.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/arrayscalars.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/halffloat.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/ndarrayobject.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/ndarraytypes.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/noprefix.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/npy_3kcompat.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/npy_common.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/npy_cpu.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/npy_endian.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/npy_interrupt.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/npy_math.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/npy_no_deprecated_api.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/npy_os.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/numpyconfig.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/old_defines.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/oldnumeric.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/random/bitgen.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/random/distributions.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/ufuncobject.h
/usr/lib/python3.9/site-packages/numpy/core/include/numpy/utils.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/numpy/1e0aa0638753b29e98ff682cff77d40ee4700250
/usr/share/package-licenses/numpy/341dccd98f25cfc90429aa52a5639159a574a0bf
/usr/share/package-licenses/numpy/3ddf920aa10c8c6ea0c87d218af74651ea7d16d3
/usr/share/package-licenses/numpy/50faca55f553c4ecd9f20c020176ca65324d3604
/usr/share/package-licenses/numpy/64796c34e3592909154742074f735b89171a4418
/usr/share/package-licenses/numpy/752f3cb872e3c7a6e096746e3648acaf2e065c96
/usr/share/package-licenses/numpy/85f84e10061f078b2cfaa62239c3a4bde1355f34
/usr/share/package-licenses/numpy/c107ade2df71a8954740468bbaa8b15e0ef4cb8b
/usr/share/package-licenses/numpy/df1c41ca8a294222a81f70a142832d6566fbd889
/usr/share/package-licenses/numpy/df4f727b25238b8a4be050714fe3f1cb06b17f75
/usr/share/package-licenses/numpy/f4622fbbfc7476c5302104204cf8f8ce5308531b
/usr/share/package-licenses/numpy/f853f54fdd704c7d99fc6eb5c8e895f3a7764f08
/usr/share/package-licenses/numpy/fd2e79f66abba5b94347c2df9ca6cf3584b0c517

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
