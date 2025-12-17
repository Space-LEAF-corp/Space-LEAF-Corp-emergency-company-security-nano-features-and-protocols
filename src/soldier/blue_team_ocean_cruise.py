OCEAN_CUES = [
    "You are steady as the ocean.",
    "Ask your crew for help if you need it.",
    "We hold the line, calmly and together."
]

def emotional_update(stress_proxy: float, fatigue_proxy: float):
    cues = OCEAN_CUES
    return {
        "stress_proxy": stress_proxy,
        "fatigue_proxy": fatigue_proxy,
        "cues": cues,
        "tone": "calm"
    }
