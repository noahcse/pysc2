#!/usr/bin/python
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests that mock environment has same shape outputs as true environment."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl.testing import absltest

from pysc2.env import mock_sc2_env
from pysc2.env import sc2_env


class TestCompareEnvironments(absltest.TestCase):

  @classmethod
  def setUpClass(cls):
    players = [
        sc2_env.Agent(race=sc2_env.Race.terran),
        sc2_env.Bot(
            race=sc2_env.Race.protoss, difficulty=sc2_env.Difficulty.very_easy),
    ]
    kwargs = {
        'map_name': 'Flat64',
        'players': players,
        'feature_screen_height': 64,
        'feature_screen_width': 32,
        'feature_minimap_height': 16,
        'feature_minimap_width': 8,
        'rgb_screen_height': 63,
        'rgb_screen_width': 31,
        'rgb_minimap_height': 15,
        'rgb_minimap_width': 7,
        'action_space': sc2_env.ActionSpace.FEATURES,
    }
    cls._env = sc2_env.SC2Env(**kwargs)
    cls._mock_env = mock_sc2_env.SC2TestEnv(**kwargs)

  @classmethod
  def tearDownClass(cls):
    cls._env.close()
    cls._mock_env.close()

  def test_observation_spec(self):
    self.assertEqual(self._env.observation_spec(),
                     self._mock_env.observation_spec())

  def test_action_spec(self):
    self.assertEqual(self._env.action_spec(), self._mock_env.action_spec())


if __name__ == '__main__':
  absltest.main()
