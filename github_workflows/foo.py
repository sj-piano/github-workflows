import pkgutil


#module_list = sorted(["%s==%s" % (i.key, i.version) for i in pip.get_installed_distributions()])
module_list = pkgutil.iter_modules()

for module in module_list:
    print(module)
