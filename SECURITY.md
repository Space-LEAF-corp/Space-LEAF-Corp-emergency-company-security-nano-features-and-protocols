# Security Posture

- Zero trust boundary: only two trusted principals (Patient, MedicalRole).
- Dual consent: both must be present for privileged actions.
- Offline default: air-gapped operational mode; proximity-bound sessions.
- Command whitelisting: only pre-verified routines; no arbitrary code execution.
- Immutable audit: write-once logs mirrored to patient-held media.
- Post-quantum crypto: keys never leave secure enclave. Rotating ephemeral medical keys per session.
- Attack surface minimization: no universal radios; optical/wired interfaces with physical interlocks.

Red Team cadence:
- Quarterly chaos crucible with multi-axis fault injection.
- Continuous fuzzing of protocol boundaries.
- Signed builds, deterministic firmware, supply chain verification.
