from um import count

def test_normal():
    assert count("hello um whats um, up")==2
    assert count("hello um um hi um um  my name is um Shrey")==5

def test_case():
    assert count ("hi Shrey Um how UM, u doing uM lately")==3

def test_start_end():
    assert count ("um hi um hello um")==3

def test_word():
    assert count("cucumbers are very yummy")==0