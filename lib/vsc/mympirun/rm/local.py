#
# Copyright 2009-2012 Ghent University
# Copyright 2009-2012 Stijn De Weirdt
#
# This file is part of VSC-tools,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/VSC-tools
#
# VSC-tools is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# VSC-tools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with VSC-tools. If not, see <http://www.gnu.org/licenses/>.
#

"""
Local scheduler : no scheduler, act on single node
"""

from vsc.mympirun.rm.sched import Sched
import time
import random

class Local(Sched):
    """
    Local class for local debugging (ie no scheduler settings)
    - will use the amount of cores found on localhost.
    """
    _sched_for = ['local']
    SCHED_ENVIRON_ID = 'LOCAL_JOBID'
    SCHED_ENVIRON_ID_AUTOGENERATE_JOBID = True

    HYDRA_LAUNCHER = ['local']

    def get_node_list(self):
        """Get the hostnames for the localnode
            MPIRUN_LOCALHOSTNAME is from multiple inheritance with MPI class
        """

        localhostname = getattr(self, 'MPIRUN_LOCALHOSTNAME', 'localhost')
        self.nodes = [localhostname] * len(self.cpus)
        self.nrnodes = len(self.nodes)  # same as len(self.cpus)

        self.log.debug("get_node_list: set %s nodes: %s" % (self.nrnodes, self.nodes))

