import pip


def generate_reg_txt():
    packages = [dist.project_name for dist in pip.get_installed_distributions()]
    with open("req.txt", 'w') as f:
        for package in packages:
            f.write(package+"\n")


if __name__ == "__main__":
    generate_reg_txt()
