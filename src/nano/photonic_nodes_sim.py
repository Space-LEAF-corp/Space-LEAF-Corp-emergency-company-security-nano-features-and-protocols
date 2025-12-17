class PhotonicNodesSim:
    def stimulate_low_energy(self, wavelength_nm: int, duty_cycle: float):
        assert 700 <= wavelength_nm <= 950
        assert 0.0 < duty_cycle <= 0.2
        return {"stim_ok": True, "thermal_margin": "conservative"}
