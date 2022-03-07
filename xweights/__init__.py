"""Top-level package for xweights."""

from . import _regions as regions
from ._regions import (get_region,
                       which_regions,
                       which_subregions)

from ._domains import (get_domain,
                       which_domains)
from ._netcdf_cf import adjust_vertices
from ._tabulator import (concat_dataframe,
                         write_to_csv)

from ._weightings import spatial_averager
                    
import nc_time_axis  
from ._io import (Input,
                  adjust_name)

from .xweights import (compute_weighted_means_ds,
                       compute_weighted_means)

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

__author__ = """Ludwig Lierhammer"""
__email__ = 'ludwig.lierhammer@hereon.de'
__version__ = '0.1.0'