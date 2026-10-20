from tools.text_utils import slugify


def test_slugify_removes_accents_and_symbols():
    assert slugify("¿Los Teléfonos de Alta Gama son una trampa?") == "los_telefonos_de_alta_gama_son_una_trampa"


def test_slugify_collapses_spaces_and_dashes():
    assert slugify("  Guía  Anti-Pánico  ") == "guia_anti_panico"
