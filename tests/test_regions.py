
import pytest

import xweights as xw

from . import has_cordex, requires_cordex
from . import has_geopandas, requires_geopandas

def test_which_regions():
    assert xw.which_regions()

def test_which_subregions():
    assert xw.which_subregions('states')
    assert xw.which_subregions('counties')
    assert xw.which_subregions('prudence')

def test_get_region():
    states   = xw.get_region('states')
    hamburg  = xw.get_region('states', name='02_Hamburg')
    ngermany =  xw.get_region('states', 
                              name=['01_Schleswig-Holstein','02_Hamburg'],
                              merge='all')
    counties = xw.get_region('counties')
    prudence = xw.get_region('prudence')

def test_get_user_region():
    shpfile   = xw.test_shp[0]
    neusiedel = xw.get_region(shpfile, merge='VA', column='VA')
