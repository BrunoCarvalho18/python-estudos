import yaml

yaml_file = open("arquivo_yaml.yaml",'r')
yaml_content = yaml.load(yaml_file)


for key, value in yaml_content.items():
    print(f"{key}: {value}")

print(yaml_content['programming_languages'][0])
print(yaml_content['libraries'][0])