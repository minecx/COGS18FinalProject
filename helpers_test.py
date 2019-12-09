import TimeProcessor as tp

def testStringIsInt():
    assert(tp.stringIsInt("6") == 6)
    assert(tp.stringIsInt("-6") == -6)
    assert(not tp.stringIsInt("wrong"))

def testProcess():
    assert(tp.process("11:00am") == [11, 0, 12, 0])
    assert(tp.process("11:00am-1:00pm") == [11, 0, 13, 0])
    assert(tp.process("11:00am-1:00am") == [11, 0, 1, 0])
