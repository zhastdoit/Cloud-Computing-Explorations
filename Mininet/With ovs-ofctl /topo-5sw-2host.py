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

        # Add hosts and switches
        H1 = self.addHost( 'h1' )
        H2 = self.addHost( 'h2' )

        S1 = self.addSwitch( 's1' )
        S2 = self.addSwitch( 's2' )
        S3 = self.addSwitch( 's3' )
        S4 = self.addSwitch( 's4' )
        S5 = self.addSwitch( 's5' )
        # Add links
        self.addLink( H1, S1)
        self.addLink( S5, H2)
        self.addLink( S1, S2)
        self.addLink( S1, S3)
        self.addLink( S2, S3)
        self.addLink( S2, S5)
        self.addLink( S3, S4)
        self.addLink( S4, S5)


topos = { 'mytopo': ( lambda: MyTopo() ) }
