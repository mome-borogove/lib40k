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

class TestParseInventory(TestCase):
  # Shortcut
  def _parse(self):
    with open(os.path.join(DATA_DIR,'small_inventory.cfg')) as f:
      relic,archeo,puritan,radical = lib40k.parse_inventory(f)
    return relic,archeo,puritan,radical

  def test_end_to_end(self):
    relic,archeo,puritan,radical = self._parse()

  def test_count(self):
    relic,archeo,puritan,radical = self._parse()
    self.assertEqual(len(relic), 3)
    self.assertEqual(len(archeo), 31)
    self.assertEqual(len(puritan), 19)
    self.assertEqual(len(radical), 15)

