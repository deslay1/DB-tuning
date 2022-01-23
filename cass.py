from cassandra.cluster import Cluster
import os

cluster = Cluster()
session = cluster.connect()

session.execute("USE ycsb")
# os.system("sleep 5s")
session.execute("DROP TABLE ycsb.usertable")
