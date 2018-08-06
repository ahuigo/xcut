from subprocess import getoutput as sh

class TestClass:
    def test_main(self):
        cmd = "echo 'Lucy,Artist,16' | python xcut -f 1,3 -od '\t' -t index "
        out = sh(cmd)
        assert "1	3" in out
        assert "Lucy	16" in out

        cmd = "echo 'name=Lucy||job=Artist||age=16' | python xcut -f age -d '||' -od ',' -t kv"
        out = sh(cmd)
        assert "16" in out

        cmd = '''echo 'Lucy,"98,99",23' | python xcut -f scores,name --titles name,scores,age --from-csv --to-csv'''
        assert '"98,99",Lucy' in sh(cmd)
