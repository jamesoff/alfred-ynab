import alp

path = alp.args()[0]
if path == "auto":
    path = ""

s = alp.Settings()
s.set(**{"budget_path": path})

if path == "":
    print "YNAB budget path set to automatic"
else:
    print "YNAB budget path set to %s" % path
