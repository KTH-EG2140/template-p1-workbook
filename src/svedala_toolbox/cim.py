"""CIM-XML: EQ join and SSH snapshot parsing. Built in Lab 6."""
from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_zone_map(eq_path: str | Path, csv_dir: str | Path) -> dict[str, str]:
    """ConformLoad mRID -> zone, via EQ names joined to the course CSVs.

    TODO (Lab 6): EQ gives rdf:ID -> IdentifiedObject.name; loads.csv gives
    name -> bus; buses.csv gives bus -> zone. Trap: the buses.csv column called
    "zone" holds the SUBSTATION name - the ZON_* zone is SubGeographicalRegion_name,
    the column Lab 1's loader used. Log unmapped loads; document your policy for them.
    """
    raise NotImplementedError("Lab 6, task 1")


def parse_ssh(source: str | Path | bytes, zone_map: dict[str, str]):
    """One SSH snapshot -> (timestamp, {zone: MW}).

    TODO (Lab 6): read Model.scenarioTime and every ConformLoad's
    EnergyConsumer.p; aggregate per zone using zone_map.
    """
    raise NotImplementedError("Lab 6, task 2")


def assemble_series(ssh_zip: str | Path, zone_map: dict[str, str]) -> pd.DataFrame:
    """A zip of SSH snapshots -> wide hourly DataFrame (UTC index, zone columns).

    TODO (Lab 6): loop parse_ssh over the archive, sort, sanity-check length.
    """
    raise NotImplementedError("Lab 6, task 3")
