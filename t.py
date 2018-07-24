from subprocess import getoutput as sh
cmd = "echo $'\ta'"
print(sh(cmd))
