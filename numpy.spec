#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : numpy
Version  : 1.17.4
Release  : 161
URL      : https://files.pythonhosted.org/packages/ff/59/d3f6d46aa1fd220d020bdd61e76ca51f6548c6ad6d24ddb614f4037cf49d/numpy-1.17.4.zip
Source0  : https://files.pythonhosted.org/packages/ff/59/d3f6d46aa1fd220d020bdd61e76ca51f6548c6ad6d24ddb614f4037cf49d/numpy-1.17.4.zip
Summary  : NumPy is the fundamental package for array computing with Python.
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause MIT Python-2.0
Requires: numpy-bin = %{version}-%{release}
Requires: numpy-license = %{version}-%{release}
Requires: numpy-python = %{version}-%{release}
Requires: numpy-python3 = %{version}-%{release}
Requires: Cython
Requires: gcc-libs-math
Requires: nose
Requires: openblas
BuildRequires : Cython
BuildRequires : Jinja2
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : gfortran
BuildRequires : nose
BuildRequires : openblas
BuildRequires : python3-dev
Patch1: avx2-distutils.patch
Patch2: avx2-fortran-distutils.patch
Patch3: timestamp.patch
Patch4: cve-2017-12852.nopatch
Patch5: 0001-AVX-implementation-with-intrinsic-for-small_correlat_v1.patch

%description
cdoc
====
This is a simple Doxygen project for building NumPy C code documentation,
with docstrings extracted from the C sources themselves.

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

%description python3
python3 components for the numpy package.


%prep
%setup -q -n numpy-1.17.4
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573491092
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fcf-protection=full -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fcf-protection=full -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fcf-protection=full -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fcf-protection=full -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build  --fcompiler=gnu95

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/numpy
cp %{_builddir}/numpy-1.17.4/doc/scipy-sphinx-theme/LICENSE.txt %{buildroot}/usr/share/package-licenses/numpy/fd2e79f66abba5b94347c2df9ca6cf3584b0c517
cp %{_builddir}/numpy-1.17.4/doc/source/license.rst %{buildroot}/usr/share/package-licenses/numpy/341dccd98f25cfc90429aa52a5639159a574a0bf
cp %{_builddir}/numpy-1.17.4/doc/sphinxext/LICENSE.txt %{buildroot}/usr/share/package-licenses/numpy/df4f727b25238b8a4be050714fe3f1cb06b17f75
cp %{_builddir}/numpy-1.17.4/numpy/linalg/lapack_lite/LICENSE.txt %{buildroot}/usr/share/package-licenses/numpy/3ddf920aa10c8c6ea0c87d218af74651ea7d16d3
cp %{_builddir}/numpy-1.17.4/numpy/ma/LICENSE %{buildroot}/usr/share/package-licenses/numpy/85f84e10061f078b2cfaa62239c3a4bde1355f34
cp %{_builddir}/numpy-1.17.4/numpy/random/src/mt19937/LICENSE.md %{buildroot}/usr/share/package-licenses/numpy/50faca55f553c4ecd9f20c020176ca65324d3604
cp %{_builddir}/numpy-1.17.4/numpy/random/src/pcg64/LICENSE.md %{buildroot}/usr/share/package-licenses/numpy/752f3cb872e3c7a6e096746e3648acaf2e065c96
cp %{_builddir}/numpy-1.17.4/numpy/random/src/philox/LICENSE.md %{buildroot}/usr/share/package-licenses/numpy/c107ade2df71a8954740468bbaa8b15e0ef4cb8b
cp %{_builddir}/numpy-1.17.4/numpy/random/src/sfc64/LICENSE.md %{buildroot}/usr/share/package-licenses/numpy/1e0aa0638753b29e98ff682cff77d40ee4700250
cp %{_builddir}/numpy-1.17.4/tools/npy_tempita/license.txt %{buildroot}/usr/share/package-licenses/numpy/f853f54fdd704c7d99fc6eb5c8e895f3a7764f08
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
/usr/bin/f2py3.7

%files dev
%defattr(-,root,root,-)
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
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/random/bitgen.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/ufuncobject.h
/usr/lib/python3.7/site-packages/numpy/core/include/numpy/utils.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/numpy/1e0aa0638753b29e98ff682cff77d40ee4700250
/usr/share/package-licenses/numpy/341dccd98f25cfc90429aa52a5639159a574a0bf
/usr/share/package-licenses/numpy/3ddf920aa10c8c6ea0c87d218af74651ea7d16d3
/usr/share/package-licenses/numpy/50faca55f553c4ecd9f20c020176ca65324d3604
/usr/share/package-licenses/numpy/752f3cb872e3c7a6e096746e3648acaf2e065c96
/usr/share/package-licenses/numpy/85f84e10061f078b2cfaa62239c3a4bde1355f34
/usr/share/package-licenses/numpy/c107ade2df71a8954740468bbaa8b15e0ef4cb8b
/usr/share/package-licenses/numpy/df4f727b25238b8a4be050714fe3f1cb06b17f75
/usr/share/package-licenses/numpy/f853f54fdd704c7d99fc6eb5c8e895f3a7764f08
/usr/share/package-licenses/numpy/fd2e79f66abba5b94347c2df9ca6cf3584b0c517

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
