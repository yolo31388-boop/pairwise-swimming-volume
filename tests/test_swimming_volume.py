import pytest
import math
from gameplay import swimming_volume as mod

CASES = [
    ("ratio", 'm.submerged_ratio(0, 1, 0) == approx(0.5)'),
    ("buoy", 'm.buoyancy(2, 0.5) == approx(1.0)'),
    ("wave", 'm.wave_height(1, 2, 0) == approx(1.0)'),
    ("near", 'm.camera_near_plane(5) == approx(0.5)'),
    ("shallow", 'm.shallow_blend(0.5, 1) == approx(0.5)'),
    ("current", 'm.apply_current(2) == 2'),
    ("tint", 'm.underwater_tint(1) == approx(0.7)'),
    ("stamina", 'm.stamina_speed(0.5, 4) == approx(2.0)'),
    ("exit", 'm.exit_height(2, 5) == 3'),
    ("sync", 'm.sync_dive(1) == 1'),
    ("lowpass", 'm.lowpass_cutoff(800) == 800'),
    ("key", 'm.swim_key(3, 2) == "3:2"'),
    ("density", 'm.density_ratio(0.5) == 0.5'),
    ("clamp", 'm.clamp_depth(5, 3) == 3'),
    ("under", 'm.is_underwater(-1, 0) is True')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
