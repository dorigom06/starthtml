#!/Users/jlee/projects/mypython/starthtml/bin/python
import fire
import os

def build(build_mode, cwd):
    """
    Builds files according to the build_mode after checking for validity.
    """
    print(f'Build mode: {build_mode}')
    html_path = os.path.join(cwd, "index.html")
    css_path = os.path.join(cwd, "style.css")
    js_path = os.path.join(cwd, "app.js")

    for path in [html_path, css_path, js_path]:
        if os.path.exists(path):
            raise OSError 
    
    if build_mode == 1:
        open(html_path, "w").close()
        print(html_path, "created.")
    elif build_mode == 2:
        open(html_path, "w").close()
        open(css_path, "w").close()
        print(html_path, "created.")
        print(css_path, "created.")
    elif build_mode == 3:
        open(html_path, "w").close()
        open(js_path, "w").close()
        print(html_path, "created.")
        print(js_path, "created.")
    elif build_mode == 4:
        open(html_path, "w").close()
        open(css_path, "w").close()
        open(js_path, "w").close()
        print(html_path, "created.")
        print(css_path, "created.")
        print(js_path, "created.")
    else:
        raise ValueError 

def start(project_name=None, build_mode=4):
    """
    Creates the basic files for web development.
    Build modes: 
    1) HTML only;
    2) HTML + CSS;
    3) HTML + JS;
    4) HTML + CSS + JS; (DEFAULT)
    """
    try:
        cwd = os.getcwd()
        if project_name:
            cwd = os.path.join(cwd, project_name)
            os.mkdir(cwd)
        build(build_mode, cwd)
    #except OSError:
    #    print("The file you're trying to create already exists.")
    except ValueError:
        print("""
        The build_mode must be a value between [1,4].
        1) HTML only;
        2) HTML + CSS;
        3) HTML + JS;
        4) HTML + CSS + JS""")
    except FileExistsError:
        print("The project name you've chosen already exists in the current directory.")
    except OSError:
        print("The file(s) you're trying to create already exists. Please delete them before proceeding; this process will overwrite the current file.")
if __name__ == "__main__":
    fire.Fire(start)

