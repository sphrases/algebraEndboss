#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
    
varName = 'Jack London'
varPath = sys.argv[1]

with con:    

    cur = con.cursor()
        
    cur.execute("UPDATE Writers SET Path = %s WHERE Name = %s", 
        (varPath, varName))        
    
    print "Number of rows updated:",  cur.rowcount
