import main
import io
import sys
import re


def test_main_100_20():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '100 \n 20'
    sys.stdin = io.StringIO(datastr)

    
    sys.stdout = sys.__stdout__
    print('Captured\n', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)
    
    p = re.compile('[\w,\W]*[H,h]ello[\w,\W]*[w, W]orld[\w,\W]*')
    res = p.match(lines[0])
    print(res.group())
    res = re.search('100', lines[0])
    print(res.group())

    assert res != None

    

