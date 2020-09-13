import schemdraw
import schemdraw.elements as elm
from schemdraw.segments import *


class MosfetN(elm.Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        factor = 0.5
        self.segments.append(Segment([[0, 1], [0, -1]]))
        self.segments.append(Segment([[-0.25, 0.5], [-0.25, -0.5]]))
        self.segments.append(Segment([[-0.5, 0], [-0.25, 0]])) # gate terminal
        self.segments.append(Segment([[0, 0.75], [0.5, 0.75]]))
        self.segments.append(Segment([[0.5, 0.75], [0.5, 1]])) # drain terminal
        self.segments.append(SegmentArrow([0, -0.75], [0.5, -0.75]))
        self.segments.append(Segment([[0.5, -0.75], [0.5, -1]])) # source terminal
        self.anchors['gate'] = [-0.5, 0]
        self.anchors['drain'] = [0.5, 1]
        self.anchors['source'] = [0.5, -1]

class MosfetP(elm.Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        factor = 0.5
        self.segments.append(Segment([[0, 1], [0, -1]]))
        self.segments.append(Segment([[-0.25, 0.5], [-0.25, -0.5]]))
        self.segments.append(Segment([[-0.5, 0], [-0.25, 0]])) # gate terminal
        self.segments.append(SegmentArrow([0.5, 0.75], [0, 0.75]))
        self.segments.append(Segment([[0.5, 0.75], [0.5, 1]])) # source terminal
        self.segments.append(Segment([[0, -0.75], [0.5, -0.75]]))
        self.segments.append(Segment([[0.5, -0.75], [0.5, -1]])) # drain terminal
        self.anchors['gate'] = [-0.5, 0]
        self.anchors['drain'] = [0.5, -1]
        self.anchors['source'] = [0.5, 1]

class Schematic():
    def __init__(self):
        self.redraw()
    
    def redraw(self, elelmentName=None):
        self.d = schemdraw.Drawing()
        VoltageSource = self.d.add(elm.Vdd(label='V$_{DD}$'))
        
        # the right side branch
        self.d.add(elm.Line(l=7)) # the right side Vdd
        self.d.add(elm.Arrow(d='down',l=1, botlabel='I$_{bias}$'))
        if(elelmentName == 'M5'):
            M5b = self.d.add(MosfetP(d='right', anchor='source', color='red', rgtlabel='M5b'))  # M5b
        else:
            M5b = self.d.add(MosfetP(d='right', anchor='source', rgtlabel='M5b')) # M5b
        self.d.add(elm.Line(d='down', at=M5b.drain, l=1))
        if(elelmentName == 'M4'):
            M4b = self.d.add(MosfetP(d='right', anchor='source', color='red', rgtlabel='M4b'))  # M4b
        else:
            M4b = self.d.add(MosfetP(d='right', anchor='source', rgtlabel='M4b')) # M4b
        self.d.add(elm.Dot(open=True, at=M4b.gate, lftlabel='V$_{cascp}$'))
        M4bDotM3b = self.d.add(elm.LineDot(d='down', at=M4b.drain, l=1))
        self.d.add(elm.Line(d='down', l=1))
        if(elelmentName == 'M3'):
            M3b = self.d.add(MosfetN(d='right', anchor='drain', color='red', rgtlabel='M3b'))
        else:
            M3b = self.d.add(MosfetN(d='right', anchor='drain', rgtlabel='M3b'))
        self.d.add(elm.Dot(open=True, at=M3b.gate, lftlabel='V$_{cascn}$'))
        M3bDotM2b = self.d.add(elm.LineDot(d='down', at=M3b.source, l=1))
        self.d.add(elm.Line(d='down', l=1))
        if(elelmentName == 'M2'):
            M2b = self.d.add(MosfetN(d='right', anchor='drain', color='red', rgtlabel='M2b'))
        else:
            M2b = self.d.add(MosfetN(d='right', anchor='drain', rgtlabel='M2b'))
        self.d.add(elm.Line(d='down', at=M2b.source, l=1))
        self.d.add(elm.Ground())
        
        # the left side branch
        self.d.add(elm.Line(d='left',l=7,at=VoltageSource.end)) # the left side Vdd
        self.d.add(elm.Arrow(d='down',l=1, toplabel='I$_{bias}$'))
        if(elelmentName == 'M5'):
            M5a = self.d.add(MosfetP(d='right', reverse=True, anchor='source', color='red', lftlabel='M5a'))  # M5a
        else:
            M5a = self.d.add(MosfetP(d='right',reverse=True, anchor='source', lftlabel='M5a')) # M5a
        self.d.add(elm.Line(d='down', at=M5a.drain, l=1))
        if(elelmentName == 'M4'):
            M4a = self.d.add(MosfetP(d='right', reverse=True, anchor='source', color='red', lftlabel='M4a'))  # M4a
        else:
            M4a = self.d.add(MosfetP(d='right',reverse=True, anchor='source', lftlabel='M4a')) # M4a
        self.d.add(elm.Dot(open=True, at=M4a.gate, rgtlabel='V$_{cascp}$'))
        M4aDotM3a = self.d.add(elm.LineDot(d='down', at=M4a.drain, l=1))
        self.d.add(elm.Line(d='down', l=1))
        if(elelmentName == 'M3'):
            M3a = self.d.add(MosfetN(d='right', reverse=True, anchor='drain', color='red', lftlabel='M3a')) # M3a
        else:
            M3a = self.d.add(MosfetN(d='right',reverse=True, anchor='drain', lftlabel='M3a')) # M3a
        self.d.add(elm.Dot(open=True, at=M3a.gate, rgtlabel='V$_{cascn}$'))
        M3aDotM2a = self.d.add(elm.LineDot(d='down', at=M3a.source, l=1))
        self.d.add(elm.Line(d='down', l=1))
        if(elelmentName == 'M2'):
            M2a = self.d.add(MosfetN(d='right', reverse=True, anchor='drain', color='red', lftlabel='M2a')) # M2a
        else:
            M2a = self.d.add(MosfetN(d='right',reverse=True, anchor='drain', lftlabel='M2a')) # M2a
        self.d.add(elm.Line(d='down', at=M2a.source, l=1))
        self.d.add(elm.Ground())
        
        # the middle branch
        self.d.add(elm.Arrow(d='down', at=VoltageSource.end, botlabel='2I$_{bias}$'))
        if(elelmentName == 'M6'):
            M6 = self.d.add(MosfetP(d='right', anchor='source', color='red', rgtlabel='M6')) # M6
        else:
            M6 = self.d.add(MosfetP(d='right', anchor='source', rgtlabel='M6')) # M6
        Vcmfb = self.d.add(elm.Dot(open=True, at=M6.gate, lftlabel='V$_{cmfb}$'))
        M6DotDrain = self.d.add(elm.LineDot(d='down', at=M6.drain, l=1))
        # right of the middle branch
        self.d.add(elm.Line(d='right', l=2))
        self.d.add(elm.Arrow(d='down', l=1, botlabel='I$_{bias}$'))
        if(elelmentName == 'M1'):
            M1b = self.d.add(MosfetP(d='right', reverse=True, anchor='source', color='red', lftlabel='M1b')) # M1b
        else:
            M1b = self.d.add(MosfetP(d='right', reverse=True, anchor='source', lftlabel='M1b')) # M1b
        self.d.add(elm.Line(d='down', xy=M1b.drain, toy=M3bDotM2b.end))
        self.d.add(elm.Line(to=M3bDotM2b.end))
        self.d.add(elm.Dot(xy=M1b.gate, open=True, rgtlabel='V$_{in-}$'))

        # left of the middle branch
        self.d.add(elm.Line(d='left', xy=M6DotDrain.end, l=2))
        self.d.add(elm.Arrow(d='down', l=1, toplabel='I$_{bias}$'))
        if(elelmentName == 'M1'):
            M1a = self.d.add(MosfetP(d='right', anchor='source', color='red', rgtlabel='M1a')) # M1a
        else:
            M1a = self.d.add(MosfetP(d='right', anchor='source', rgtlabel='M1a')) # M1a
        self.d.add(elm.Line(d='down', xy=M1a.drain, toy=M3aDotM2a.end))
        self.d.add(elm.Line(to=M3aDotM2a.end))
        self.d.add(elm.Dot(xy=M1a.gate, open=True, lftlabel='V$_{in+}$'))
        
        # connections
        self.d.add(elm.Line(xy=M2b.gate, tox=M6DotDrain.end))
        Vbiasn = self.d.add(elm.Dot)
        self.d.add(elm.Line(to=M2a.gate))
        self.d.add(elm.LineDot(d='up', l=1, xy=Vbiasn.start, label='V$_{biasn}$'))
        
        self.d.add(elm.Line(xy=M5a.gate, d='right', l=2))
        Vbiasp = self.d.add(elm.Dot)
        self.d.add(elm.Line(to=M5b.gate))
        self.d.add(elm.LineDot(d='up', l=1, xy=Vbiasp.start, label='V$_{biasp}$'))
        
        # output voltage
        self.d.add(elm.LineDot(d='right', at=M4bDotM3b.end, rgtlabel='V$_{out+}$'))
        self.d.add(elm.LineDot(d='left', at=M4aDotM3a.end, lftlabel='V$_{out-}$'))

        self.figure = self.d.draw(show=False)


