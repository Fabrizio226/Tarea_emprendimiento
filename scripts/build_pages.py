from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    "index.html": "index.html",
    "solicitud_hora.html": "agendar-hora.html",
    "cancelar_hora.html": "cancelar-hora.html",
    "preguntas.html": "preguntas.html",
    "horarios.html": "horarios.html",
    "ayuda.html": "ayuda.html",
}
ENDPOINTS = {
    "inicio": "index.html",
    "agendar": "agendar-hora.html",
    "cancelar": "cancelar-hora.html",
    "horarios": "horarios.html",
    "ayuda": "ayuda.html",
    "preguntas": "preguntas.html",
    "guardar": "agendar-hora.html",
}
URL_FOR = re.compile(
    r"\{\{\s*url_for\('([^']+)'\s*(?:,\s*filename='([^']*)')?\)\s*\}\}"
)


def render_static_template(template_name: str) -> str:
    html = (ROOT / "templates" / template_name).read_text(encoding="utf-8")

    def replace_url_for(match: re.Match[str]) -> str:
        endpoint, filename = match.groups()
        if endpoint == "static" and filename is not None:
            return f"static/{filename}"
        if endpoint not in ENDPOINTS:
            raise ValueError(f"Endpoint Flask sin equivalente estático: {endpoint}")
        return ENDPOINTS[endpoint]

    html = URL_FOR.sub(replace_url_for, html)
    html = html.replace("../static/", "static/")
    html = html.replace('action="agendar-hora.html"', "data-static-only")
    html = html.replace(' method="POST"', "")
    html = html.replace(
        '<form class="formulario-cancelar">',
        '<form class="formulario-cancelar" data-static-only>',
    )
    html = re.sub(
        r'\s*<script src="https://cdn\.jsdelivr\.net/npm/@emailjs/browser@4/dist/email\.min\.js"></script>',
        "",
        html,
    )
    html = html.replace(
        '<script src="static/js/solicitud_hora.js"></script>',
        '<script src="static/js/script.js"></script>',
    )
    if "{{" in html or "{%" in html:
        raise ValueError(f"Quedó sintaxis Flask/Jinja en {template_name}")

    html = html.replace(
        "</head>",
        '    <link rel="stylesheet" href="static/css/pages-notice.css">\n'
        "</head>",
        1,
    )
    html = html.replace(
        "</body>",
        '    <script src="static/js/pages-static.js"></script>\n'
        "</body>",
        1,
    )
    return html


def build(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for template_name, output_name in PAGES.items():
        (output_dir / output_name).write_text(
            render_static_template(template_name),
            encoding="utf-8",
        )

    shutil.copytree(ROOT / "static", output_dir / "static", dirs_exist_ok=True)
    (output_dir / ".nojekyll").touch()
    print(f"Sitio estático generado en {output_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Exporta el sitio para GitHub Pages.")
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "_site",
        help="Directorio de salida (predeterminado: _site)",
    )
    args = parser.parse_args()
    build(args.output.resolve())


if __name__ == "__main__":
    main()
