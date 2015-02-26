## -*- encoding: utf-8 -*-
# This file was *autogenerated* from the file Uni1.sagetex.sage
from sage.all_cmdline import *   # import sage library
_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_8 = Integer(8); _sage_const_21p0 = RealNumber('21.0'); _sage_const_18 = Integer(18); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_14 = Integer(14); _sage_const_19 = Integer(19); _sage_const_21 = Integer(21); _sage_const_20 = Integer(20); _sage_const_0p2 = RealNumber('0.2')## This file (Uni1.sagetex.sage) was *autogenerated* from Uni1.tex with sagetex.sty version 2012/01/16 v2.3.3-69dcb0eb93de.
import sagetex
_st_ = sagetex.SageTeXProcessor('Uni1', version='2012/01/16 v2.3.3-69dcb0eb93de', version_check=True)
_st_.blockbegin()
try:
 from sympy import *
 m,g,c,k,t=symbols('m,g,c,k,t')
 v=m/c*g+k*exp(-c/m*t)
 simplify(v.diff(t)+c/m*v)
except:
 _st_.goboom(_sage_const_8 )
_st_.blockend()
try:
 _st_.inline(_sage_const_0 , latex(simplify(v.diff(t)+c/m*v)))
except:
 _st_.goboom(_sage_const_10 )
_st_.blockbegin()
try:
 v=symbols('v',cls=Function)
 EqCaida=Eq(v(t).diff(t)+c/m*v(t),g)
 Vel=dsolve(EqCaida,v(t))
except:
 _st_.goboom(_sage_const_17 )
_st_.blockend()
try:
 _st_.inline(_sage_const_1 , latex(Vel))
except:
 _st_.goboom(_sage_const_19 )
_st_.blockbegin()
try:
 x=symbols('x')
 y=Function('y')(x)
 MiEcua=Eq(y.diff(x),y/x)
 f=dsolve(MiEcua,y)
except:
 _st_.goboom(_sage_const_20 )
_st_.blockend()
_st_.blockbegin()
try:
 from sympy import *
 x,y=symbols('x,y')
 Rango=range(_sage_const_21 )
 L=[tan(pi*k/_sage_const_21p0 ) for k in Rango]
 p=plot(L[_sage_const_0 ]*x,(x,-_sage_const_2 ,_sage_const_2 ),show=False,xlim=(-_sage_const_2 ,_sage_const_2 ),\
 ylim=(-_sage_const_2 ,_sage_const_2 ),aspect_ratio=(_sage_const_1 ,_sage_const_1 ))
 for pend in L[_sage_const_1 :]:
     p1=plot(pend*x,(x,-_sage_const_2 ,_sage_const_2 ),show=False,\
 xlim=(-_sage_const_2 ,_sage_const_2 ),ylim=(-_sage_const_2 ,_sage_const_2 ),aspect_ratio=(_sage_const_1 ,_sage_const_1 ))
     p.append(p1[_sage_const_0 ])
 for r in range(_sage_const_1 ,_sage_const_10 ):
     p1=plot_implicit(Eq(x**_sage_const_2  + y**_sage_const_2 , _sage_const_0p2 *r),\
 show=False,aspect_ratio=(_sage_const_1 ,_sage_const_1 ),xlim=(-_sage_const_2 ,_sage_const_2 ),ylim=(-_sage_const_2 ,_sage_const_2 ))
     p.append(p1[_sage_const_0 ])
except:
 _st_.goboom(_sage_const_18 )
_st_.blockend()
_st_.blockbegin()
try:
 x=symbols('x')
 y=Function('y')(x)
 MiEcua=Eq(y.diff(x),y/x)
 tipo=classify_ode(MiEcua,y)
except:
 _st_.goboom(_sage_const_10 )
_st_.blockend()
_st_.blockbegin()
try:
 x,c=symbols('x,c')
 y=Function('y')(x)
 MiEcua=Eq(y.diff(x),sqrt((c-y)/y))
 f=dsolve(MiEcua,y,hint='separable')
except:
 _st_.goboom(_sage_const_7 )
_st_.blockend()
try:
 _st_.inline(_sage_const_2 , latex(f))
except:
 _st_.goboom(_sage_const_14 )
_st_.endofdoc()
