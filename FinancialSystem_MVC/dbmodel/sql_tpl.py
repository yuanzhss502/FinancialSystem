#!/usr/bin/python
# -*- coding: <encoding name> -*-

SQL_TPL = {

    'activecount': '''
                select fdate, fgamename, SUM(fcount) as activecount from gameactive where fdate >= '%(sdata)s' and fdate <= '%(edata)s' GROUP by fdate, fgamename, fcount limit 10
    
    
              '''
    
    'gameuserage': '''
                select fdate, fgametime, fage from analysis.gameuserage where  fdate >= '%(sdata)s' and fdate <= '%(edata)s' GROUP by fdate, fgametime, fage limit 10
    
    '''

}