import argparse
from src.nano.scaffold_sim import NanoScaffoldSim
from src.nano.photonic_nodes_sim import PhotonicNodesSim
from src.redteam.chaos_crucible import chaos_crucible
from src.soldier.blue_team_ocean_cruise import emotional_update
from src.diagnostics.chemistry_sim import chemistry_update
from src.diagnostics.mechanics_sim import mechanics_update
from src.diagnostics.mental_state_sim import mental_state_update
from src.diagnostics.sleep_monitor_sim import sleep_status_update

def run_zero_ground():
    scaffold = NanoScaffoldSim()
    photonic = PhotonicNodesSim()
    crucible = chaos_crucible(scaffold, photonic)

    diag = {
        "chemistry": chemistry_update(),
        "mechanics": mechanics_update(),
        "mental": mental_state_update(),
        "sleep": sleep_status_update()
    }
    blue = emotional_update(stress_proxy=0.7, fatigue_proxy=0.5)

    return {"crucible": crucible, "diagnostics": diag, "blue_team": blue}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", choices=["zero-ground"], default="zero-ground")
    args = parser.parse_args()
    if args.scenario == "zero-ground":
        print(run_zero_ground())
