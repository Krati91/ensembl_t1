# ENSEMBL REST WEB SERVICE  

**API SPECIFICATIONS**  
**Name** : `/gene_suggest`  
**Method** : GET  
**Description** : Search for genome display labels from ensemble database  
  
**Required Parameters**
1. **query**  
   Data Type : string  
  **Description** : any valid string from the display labels  
2. **species**  
   Data Type : string  
   Description : any valid species name  
3. **limit**  
   Data Type : integer  
   Description : the number of suggestions to return  
  
<h3>DEPLOYMENT</h3>
1. We chose cloud based deployment. Various PaaS and IaaS providers support Django app deployment eg:- [Heroku](https://devcenter.heroku.com/articles/deploying-python),              [PythonAnywhere](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/), [Amazon Web Services](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html) etc.  
2. For now, the application has been hosted on Heroku with free resources, since it is a POC. Scaling up with the increase in traffic might require upgrading to paid resources.      For more flexibility an IaaS provider is also an option.    
3. To view the working application [click here](https://ensembl.herokuapp.com/gene_suggest?query=brc&species=gorilla_gorilla&limit=10)
