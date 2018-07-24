from subprocess import getoutput as sh

class TestClass:
    def test_main(self):
        cmd = "echo 'Lucy,Artist,16' | python xcut -f 1,3 -od '\t' -t index "
        out = sh(cmd)
        assert "1	3" in out
        assert "Lucy	16" in out
