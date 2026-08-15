import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent / "src"))


def pytest_configure(config):
    """Register the TRIPWIRE class.

    `wealthTensor-45`. A tripwire is not a guard: it fires on the machine-checkable
    ANTECEDENT of a re-read and says *a human must read this*, where a guard fires on a
    violation and says *this is wrong*. `CONSTRAINT-INVENTORY-001` §3.4 defines the class
    and why an unrecognisable constraint gets one.

    The class is marked in three places on purpose, because a suite that cannot tell a
    tripwire from a guard will eventually have one deleted as a false alarm:

    * the file name — `tests/test_tripwire_*.py`;
    * this marker — `pytest -m tripwire` lists them, `-m "not tripwire"` excludes them;
    * the inventory — a `TRIPWIRE` grade in the `machine` column, which is **not**
      coverage. Only FOR and BINDS mean a constraint is guarded.

    `tests/test_tripwire_class_is_registered.py` binds the three together, so the class
    cannot dissolve one layer at a time.
    """
    config.addinivalue_line(
        "markers",
        "tripwire: fires on the antecedent of a re-read, not on a violation. A red means "
        "GO AND READ the named section against its registration — it is not a failure. "
        "See CONSTRAINT-INVENTORY-001 §3.4.",
    )
