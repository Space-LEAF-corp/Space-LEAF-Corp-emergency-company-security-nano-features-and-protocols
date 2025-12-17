WHITELIST = {
    "bridge_mode": ["sync_timing", "low_energy_stim", "verify_integrity"],
    "trauma_stabilize": ["enter_safe_mode", "cue_help_seeking", "tighten_caps"],
    "calibration_check": ["baseline_sensors", "revalidate_power", "await_dual_reauth"]
}

def is_command_allowed(scope: str, command: str) -> bool:
    return scope in WHITELIST and command in WHITELIST[scope]
