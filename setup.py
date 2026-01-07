from setuptools import find_packages,setup




def get_requirements(file_path:str):
   
   hypen_e="-e ."
   requirements=[]

   with open(file_path) as f:
      requirements=[r.replace("\n","")  for r in f.readlines()]


      if hypen_e in requirements :

         requirements.remove(hypen_e)

   
   return requirements
      




setup(
    name="MLOPS-project",
    version="0.0.1",
    author="Anurag",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)