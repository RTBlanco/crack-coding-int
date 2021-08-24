from q_1 import unique_str, is_permutation

def test_unique_str():
  assert unique_str("testing") == False
  assert unique_str("are") == True
  
def test_is_permutation():
  assert is_permutation('eat', 'ate') == True
  assert is_permutation('romo', 'moro' ) == True
  assert is_permutation('cat', 'hat' ) == False
  assert is_permutation('duck', 'ducking' ) == False
