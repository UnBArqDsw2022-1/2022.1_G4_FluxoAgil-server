import pytest
import asyncio
from typing import Final
from scraper import get_programs, get_valid_curricula


programs_link: Final[dict[str, str]] = {
    "ufpa": "https://sigaa.ufpa.br/sigaa/public/curso/lista.jsf?nivel=G&aba=p-ensino",
    "unb": "https://sig.unb.br/sigaa/public/curso/lista.jsf?nivel=G&aba=p-graduacao"
}


@pytest.mark.parametrize(
    "programs_link_input, expected_programs_count_output", [
        (programs_link["ufpa"], 627),
        (programs_link["unb"], 157),
    ])
def test_get_programs(
    programs_link_input: str,
    expected_programs_count_output: int
):
    programs = asyncio.run(get_programs(programs_link_input))

    assert len(programs) == expected_programs_count_output


curricula_link: Final[dict[str, str]] = {
    "adm": "https://sig.unb.br/sigaa/public/curso/curriculo.jsf?lc=pt_BR&id=414112",
    "cic": "https://sig.unb.br/sigaa/public/curso/curriculo.jsf?lc=pt_BR&id=414599"
}


@pytest.mark.parametrize(
    "link_input, expected_count_output", [
        (curricula_link["adm"], 7),
        (curricula_link["cic"], 8),
    ])
def test_get_valid_curricula(link_input: str, expected_count_output: int):
    curricula = asyncio.run(get_valid_curricula(link_input))

    assert len(curricula) == expected_count_output
