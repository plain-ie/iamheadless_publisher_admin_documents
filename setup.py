from distutils.core import setup


setup(

    # Application name:
    name="iamheadless_publisher_admin_documents",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="Maris Erts",
    author_email="maris@plain.ie",

    # Packages
    packages=["iamheadless_publisher_admin_documents"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="#",

    #
    license="LICENSE",
    description="#",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        # 'https://github.com/plain-ie/iamheadless_file_handling/archive/refs/heads/main.zip',
        # 'https://github.com/plain-ie/iamheadless_publisher_admin/archive/refs/heads/main.zip',
    ],

)
