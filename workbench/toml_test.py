import toml

# Read a TOML file
with open('workbench/elioc.toml') as f:
    config = toml.load(f)
print(config)