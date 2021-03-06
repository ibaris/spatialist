import os
import pytest


@pytest.fixture
def travis():
    return 'TRAVIS' in os.environ.keys()


@pytest.fixture
def appveyor():
    return 'APPVEYOR' in os.environ.keys()


@pytest.fixture
def testdir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


@pytest.fixture
def testdata(testdir):
    out = {
        'tif': os.path.join(testdir, 'S1A__IW___A_20150309T173017_VV_grd_mli_geo_norm_db.tif')
    }
    return out
