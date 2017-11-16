import numpy as np

from xpdsim.build_sim_db import build_sim_db
from xpdsim.movers import shctl1, cs700
from ophyd.sim import (SynSignalWithRegistry, NumpySeqHandler,
                       SynSignalRO)
from xpdsim.area_det import det_factory, nsls_ii_path, xpd_wavelength

db_path, db = build_sim_db() # default is sqlite
db.reg.register_handler('NPY_SEQ', NumpySeqHandler)
# detector with 5 by 5 image -> for testing functionality
simple_pe1c = det_factory(db.reg)
# detector with full image -> for testing data reduction
xpd_pe1c = det_factory(db.reg, full_img=True,
                       src_path=nsls_ii_path)
# synthetic ring current
ring_current = SynSignalRO(lambda : 300, name='ring_current')
