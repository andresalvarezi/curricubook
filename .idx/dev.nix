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