"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )
        
        #Change the port number n here:
        n=4
		
        # Initialize topology
        s3 = {} # Core
        s2 = {} # Aggregation
        s1 = {} # Edge
        h = {}  # Host
        for i in range(n*n/2): 
            s1[i] = self.addSwitch('s1-%s' % i)
            s2[i] = self.addSwitch('s2-%s' % i)
        for i in range(n*n/4):
            s3[i] =self.addSwitch('s3-%s' % i)
        for i in range(n*n/2):     
            for j in range (n/2):
                h[i*n/2+j] = self.addHost('h%s' % (i*n/2+j))
                self.addLink(h[i*n/2+j],s1[i])
        for i in range (n):
            for j in range(n/2):
                for k in range (n/2):
                    self.addLink(s1[i*n/2+j],s2[i*n/2+k])
                    self.addLink(s2[i*n/2+j],s3[j*n/2+k])
topos = { 'mytopo': ( lambda: MyTopo() ) }
