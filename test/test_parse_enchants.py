import lib40k

import os.path
from unittest import TestCase

# This is a bit of a hack, and it depends on the data directory and these
# test cases *not* being moved around.
def compute_data_dir():
  this = os.path.abspath(__file__)
  test_dir,_ = os.path.split(this)
  data_dir = os.path.join(test_dir,'data')
  return data_dir
DATA_DIR = compute_data_dir()

class TestParseEnchants(TestCase):
  # Shortcut
  def _parse(self):
    with open(os.path.join(DATA_DIR,'small_enchant.cfg')) as f:
      shortcuts,enchants = lib40k.parse_enchants(f)
    return shortcuts,enchants

  def test_end_to_end(self):
    shortcuts,enchants = self._parse()

  def test_count(self):
    shortcuts,enchants = self._parse()
    self.assertEqual(len(enchants), 36)

