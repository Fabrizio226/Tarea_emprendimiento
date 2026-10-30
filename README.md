# Lumenia

## Publicar en GitHub Pages

El workflow de GitHub Actions genera el sitio estático y lo publica cuando se actualiza el repositorio. En GitHub, abre **Settings → Pages** y selecciona **GitHub Actions** como origen de publicación. También puedes iniciar el workflow manualmente desde la pestaña **Actions**.

Si prefieres publicar desde una rama (**Deploy from a branch**, raíz `/`), genera y sube también las páginas estáticas a la raíz del repositorio antes de publicar; así GitHub Pages encontrará `index.html` en lugar de mostrar el README. El comando de generación predeterminado las deja en esa ubicación.

La exportación incluye las páginas públicas y sus recursos estáticos. No incluye `formularios.db` ni la página de registros en el sitio publicado. Si el repositorio será público, comprueba además que los archivos versionados no contengan datos personales: el contenido del repositorio puede descargarse aunque no forme parte de Pages.

### Limitación de las solicitudes

GitHub Pages solo aloja archivos estáticos: no ejecuta Flask ni SQLite. Por eso, los formularios publicados informan que no se envían ni se guardan. Para habilitar reservas y cancelaciones, hay que conectar un backend alojado por separado. La aplicación Flask original sigue disponible para ejecutarse localmente.

Para generar las páginas en la raíz del repositorio:

```powershell
python scripts\build_pages.py
```

Para generar la carpeta de publicación que usa el workflow:

```powershell
python scripts\build_pages.py --output _site
```

## Publicar en Render

El archivo `render.yaml` configura un **Static Site** y copia los HTML y recursos a `_site` sin instalar paquetes ni ejecutar Python. Si ya existe el servicio, en **Settings → Build & Deploy** configura el Build Command con el comando de `render.yaml` y el Publish Directory como `_site`; los cambios en `render.yaml` se aplican automáticamente al crear o actualizar un Blueprint.

La configuración publica `_site` y no ejecuta la aplicación Flask ni SQLite. El `Pipfile` se quitó de la raíz para evitar que Render intente instalar Flask/Pipenv al detectar el proyecto. Para ejecutar la aplicación Flask localmente, instala Flask con `python -m pip install flask`.
