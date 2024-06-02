<h1 align="center">Web development with python, featuring htmx and tailwindcss</h1>


## Table of Contents

- [Table of Contents](#table-of-contents)
- [🧐 About ](#-about-)
- [Prerequisites](#prerequisites)
- [🔧 Run pytest ](#-run-pytest-)
- [🎈 Guide ](#-guide-)
- [💪 Advanced ](#-advanced-)
- [⛏️ Built Using ](#️-built-using-)
- [🎉 Acknowledgements ](#-acknowledgements-)

## 🧐 About <a name = "about"></a>

You can build a beautiful web application using nothing more than Python, htmx, and TailwindCSS. Create dynamic pages using the power of Jinja templates and server-side rendering to create a Hypertext driven application.

### Prerequisites

The example app was created with **Python 3.12**, but it is likely compatible with earlier versions. However, I would highly recommend using the latest version of Python. The rest of the dependencies are listed in the `requirements.txt` file.

```
fastapi[all]
jinja2
jinja2-fragments
pytailwindcss
pytest
python-multipart
tinydb
```

> **Note**
> The `fastapi[all]` dependency installs some other optional dependencies and features. It also includes `uvicorn`, which is used as the server to run your code. (You could choose to just use `fastapi` and `uvicorn[standard]` separately, if you prefer.)

## 🔧 Run pytest <a name = "run_pytest"></a>

After activating your virtual environment, you can run tests by typing `pytest` on the command line. This makes sure that your application is able to generate the index page.

```
pytest
```

> **Note**
> The application does not include comprehensive testing (yet). As of now, if the tests pass, it means that the application runs and generates a response.


## 🎈 Guide <a name="guide"></a>

If you would like to learn how to build a site from the ground up, consider following the instructions over on the [Simple Site repository](https://github.com/tataraba/simplesite).

The repo includes [documentation](https://github.com/tataraba/simplesite/blob/main/docs/00_Preface.md) on how to get started from scratch, with more information on some of the libraries used in this application, including FastAPI, Jinja2, pytailwindcss, and htmx.

## 💪 Advanced <a name="advanced"></a>

The `advanced-features` branch showcases a few features of TailwindCSS and htmx. If you're learning how to use either of the tools, try to tackle them yourself before looking at the branch for solutions. Some of this will be covered in the workshop.

## ⛏️ Built Using <a name = "built_using"></a>

- [FastAPI](https://fastapi.tiangolo.com)
- [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/)
- [TailwindCSS](https://tailwindcss.com/docs/installation)
- [TinyDB](https://tinydb.readthedocs.io/en/latest/)
- [htmx](https://htmx.org)

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- [@tataraba](https://github.com/tataraba) - Mario Munoz, _Python By Night_
- [@kjaymiller](https://github.com/kjaymiller) - Jay Miller, _Senior Cloud Advocate-Python_, Microsoft
