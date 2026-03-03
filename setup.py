from setuptools import setup, find_packages

setup(
    name="espy",
    version="1.0.0",
    author="Esteve Oliver i Juher",
    description="Paquet per a mètodes numèrics EDO",
    packages=find_packages(),  # Això buscarà la carpeta 'espy'
    install_requires=["numpy"],
    python_requires=">=3.6",
)
