from pyppeteer import launch
import asyncio
import re


async def get_programs(programs_link: str):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(programs_link)

    programs_elements = await page.querySelectorAll(".listagem tr.linhaPar, .listagem tr.linhaImpar")

    programs = []

    for program_element in programs_elements:
        title_page_function = '(element) => element.querySelector("td").innerText'
        raw_title: str = await page.evaluate(title_page_function, program_element)
        title = raw_title.translate(str.maketrans({chr(10): '', chr(9): ''}))

        program_link_page_function = '(element) => element.querySelector("a").href'
        program_link = await page.evaluate(program_link_page_function, program_element)
        id = re.search("id=([0-9]*)&", program_link).group(1)

        program = {
            "id": id,
            "title": title,
            "program_link": program_link

        }

        programs.append(program)

    return programs


async def get_valid_curricula(curricula_link: str):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(curricula_link)

    valid_curricula_id = []

    curricula_elements = await page.querySelectorAll("table#table_lt tr.linha_par, table#table_lt tr.linha_impar")

    for curricula_element in curricula_elements:
        curriculum_status_page_function = '(element) => element.querySelector("td:nth-of-type(2)").innerText'
        curriculum_status_inner_text = await page.evaluate(curriculum_status_page_function, curricula_element)
        curriculum_status = curriculum_status_inner_text.strip()

        if curriculum_status != "Ativa":
            continue

        curriculum_id_page_function = '(element) => element.querySelector("td:nth-of-type(1)").innerText'
        curriculum_id_inner_text = await page.evaluate(curriculum_id_page_function, curricula_element)
        curriculum_id_pattern = "Detalhes da Estrutura Curricular (.*), Criado"
        curriculum_id = re.search(
            curriculum_id_pattern, curriculum_id_inner_text).group(1)

        valid_curricula_id.append(curriculum_id)

    return valid_curricula_id

unb_programs_url = "https://sig.unb.br/sigaa/public/curso/lista.jsf?nivel=G&aba=p-graduacao"
programs = asyncio.run(get_programs(unb_programs_url))

print(programs)
