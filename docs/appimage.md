# Creating AppImage file for easy distribution

We will use the python-appimage library (https://github.com/niess/python-appimage)

1) Install python-appimage library with uv
```python
uv add python-appimage
```

2) Generate the data needed for AppImage packaging. See examples in github: https://github.com/niess/python-appimage/tree/master/applications

3) Generate AppImage from sources
```python
uv run python-appimage build app -p 3.10 /path/to/recipe/folder
```


