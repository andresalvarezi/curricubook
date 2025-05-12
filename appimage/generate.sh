#!/bin/bash
cd ../curricubook
uv run python-appimage build app -p 3.12 ../appimage/recipe
mv curricubook-x86_64.AppImage ../appimage
