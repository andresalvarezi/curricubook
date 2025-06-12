# Curricubook
Tool to generate fancy work and education documents in several formats, lengths and styles

# What you can do with Curricubook?

With Curricubook you can:
* Organize all your work and education elements in any level of detaul
* Export them as a short resumee or as a full detailed book abouryour whole carreer
* Track your profesional life in an prganized way


# Installation and basic usage

To be done


# Development environment

Curricubook uses Astral uv tool (https://github.com/astral-sh/uv) to organize the project. To develop any new functionality you can:

1) Clone the repo:
```bash
git clone https://github.com/andresalvarezi/curricubook.git
```

2) Install uv if not already installed:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3) Initialize the virtual environment and download all dependencies
```bash
uv sync
```


# Serve the output directory

```bash
python -m http.server 8080 --directory demo/output/html/
```


# Google IDX configuration

After import the GitHub repo:

1) Create .idx/dev.nix file with:

```
{ pkgs, ... }: {

  # Which nixpkgs channel to use.
  channel = "stable-23.11"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
  packages = [
    pkgs.python313
  ];

  # Sets environment variables in the workspace
  env = {
  };

  # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
  idx.extensions = [
  ];

  # Enable previews and customize configuration
  idx.previews = {
    enable = true;
    previews = {
      web = {
        command = [
          "python3"
          "-m"
          "http.server"
          "--directory"
          "/home/user/curricubook/demo/output/html/"
          "$PORT"
        ];
        manager = "web";
      };
    };
  };
}
```
